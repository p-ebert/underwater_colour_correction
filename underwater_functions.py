import numpy as np
import cv2

def check_input(arr):
    """Check the shape of the array
    """
    if arr.shape[-1] != 3:
        raise ValueError("Input array must have a shape == (..., 3)), "
                         f"got {arr.shape}")

    return arr.astype('uint8')

def adjust_gamma(image, gamma=1.0):
    # build a lookup table mapping the pixel values [0, 255]
    # their adjusted gamma values
    invGamma = 1.0 / gamma
    table = np.array([((i / 255.0) ** invGamma) * 255
        for i in np.arange(0, 256)]).astype("uint8")
    # apply gamma correction using the lookup table
    return cv2.LUT(image, table)



# transformation matrix from RGB to XYZ space
Txyz = np.array([[0.5141, 0.3239, 0.1604],
                 [0.2651, 0.6702, 0.0641],
                 [0.0241, 0.1288, 0.8444]])

# transformation matrix from XYZ to LMS space
Tlms = np.array([[0.3897, 0.6890, -0.0787],
                 [-0.2298, 1.1834, 0.0464],
                 [0.0000, 0.0000, 1.0000]])

# PCA transformation matrix to decorrelate axes
Tpca1 = np.array([[1/np.sqrt(3), 0, 0],
                [0, 1/np.sqrt(6), 0],
                [0, 0, 1/np.sqrt(2)]])

Tpca2 = np.array([[1, 1, 1],
                 [1, 1, -2],
                  [1, -1, 0]])

Tpca = Tpca1 @ Tpca2

def RGB2Lab(im):
    """
    converts RGB image into Lab image ( XYZ -> LMS - > log space -> LAB)
    input: image in RGB
    output: image in Lab space
    """
    return np.log(im @ Txyz.T @ Tlms.T)/np.log(10)@ Tpca.T


def ColorCorrec(im):
    """
    corrects the color only on alpha and beta channel : substract channel wise median
    input : image in Lab space
    output: corrected image in Lab space
    """
    imCorrec = im.copy()
    imCorrec [:,:,1] = im[:,:,1] - np.median(im[:,:,1])
    imCorrec [:,:,2] = im[:,:,2] - np.median(im[:,:,2])

    return imCorrec


def Lab2RGB(im):
    """
    converts Lab image into RGB image
    input: image in Lab
    output: image in RGB
    """

    return 10**(im @ np.linalg.inv(Tpca.T))@ np.linalg.inv(Txyz.T @ Tlms.T)


def normalize(im):
    #return im
    return (im - im.min())/(im.max()-im.min())

def normalizeTer(img):
    sum = img[:,:,0] + img[:,:,1] + img[:,:,2]
    img[:,:,0] /= sum
    img[:,:,1] /= sum
    img[:,:,2] /= sum
    return img

def normalizeBis(im):
    for i in range(0,3):
        im[:,:,0] = (im[:,:,0] - im[:,:,0].min())/(im[:,:,0].max()-im[:,:,0].min())

    return im

def constrast_correction_lab(imLabCorrec2, cut_off):
    # converting image into Lab space with opencv
    #imLabCorrec = cv2.cvtColor((imRGBCorrec*255).astype('uint8'), cv2.COLOR_RGB2LAB)
    L_channel = imLabCorrec2[:,:,0]
    I_min, I_max = L_channel.min(),L_channel .max()

    imhisto, bins = np.histogram(L_channel.copy(), bins = 100000)
    imhisto      = imhisto/np.sum(imhisto)
    imhistocum = np.cumsum(imhisto)

    cut_off = 1e-3
    idx_bin_min = len(imhistocum[imhistocum < cut_off])
    idx_bin_max = len(imhistocum) - len(imhistocum[imhistocum > (1-cut_off)])

    thresh_min = bins[idx_bin_min]
    thresh_max = bins[idx_bin_max]

    L_channel[L_channel < thresh_min ] =  thresh_min
    L_channel[L_channel > thresh_max ] =  thresh_max

    I_min, I_max = thresh_min,thresh_max+1
    L_channel =(L_channel - L_channel.min())*(I_max - I_min)/(L_channel.max()-L_channel.min())+ I_min

    # avec open cv2
    #imRGBCorrec2 = cv2.cvtColor(imLabCorrec2, cv2.COLOR_LAB2RGB)
    imLabCorrec2[:,:,0] = L_channel

    return imLabCorrec2
