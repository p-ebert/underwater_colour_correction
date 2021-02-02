from os import walk
import argparse
import numpy as np
import matplotlib.pyplot as plt
import cv2
import os
import skimage
from skimage import io, color


from underwater_functions import check_input, adjust_gamma, RGB2Lab, ColorCorrec, Lab2RGB, normalize, constrast_correction_lab

parser = argparse.ArgumentParser()

parser.add_argument('--input_dir', default="./input_images/", help="input directory")
parser.add_argument('--output_dir', default="./output_images/", help="output directory")
parser.add_argument('--colour_correction', default="LAB", help="perform colour correction in [LAB, CIELAB, LUV, YCBC] spaces")
parser.add_argument('--lab_constrast_correction', default="CLAHE", help="perform contrast correction with [stretching, CLAHE, equalisation, none] methods")
parser.add_argument('--constrast_cut_off', default=1e-3, help="cut-off level for lab contrast correction")

args = parser.parse_args()

file_list = []

for (dirpath, dirnames, filenames) in walk(args.input_dir):
    file_list.extend(filenames)
    break

for file in file_list:
    im = plt.imread(args.input_dir + file)
    im = check_input(im)

    im = adjust_gamma(im, gamma= 1)

    #im = cv2.resize(dsize = (im.shape[1]//4,im.shape[0]//4), src = im )

    if args.colour_correction == "LAB":
        imLab = RGB2Lab(im)
        imLabCorrec = ColorCorrec(imLab)

        if args.lab_constrast_correction == "stretching":
            imLabCorrec2 = imLabCorrec.copy()
            imLabCorrec = constrast_correction_lab(imLabCorrec2, args.constrast_cut_off)
            imRGBCorrec = Lab2RGB(imLabCorrec)
            imRGBCorrec = normalize(imRGBCorrec)

        if args.lab_constrast_correction == "CLAHE":
            imRGBCorrec = Lab2RGB(imLabCorrec)
            imRGBCorrec = normalize(imRGBCorrec)
            lab = cv2.cvtColor((imRGBCorrec*255).astype('uint8'), cv2.COLOR_RGB2LAB)
            lab_planes = cv2.split(lab)
            clahe = cv2.createCLAHE(clipLimit=1.0,tileGridSize=(8,8))
            lab_planes[0] = clahe.apply(lab_planes[0])
            lab = cv2.merge(lab_planes)
            imRGBCorrec = cv2.cvtColor(lab, cv2.COLOR_LAB2RGB)
            #imRGBCorrec = normalize(imRGBCorrec)

        if args.lab_constrast_correction == "equalisation":
            imRGBCorrec = Lab2RGB(imLabCorrec)
            imRGBCorrec = normalize(imRGBCorrec)
            lab = cv2.cvtColor((imRGBCorrec*255).astype('uint8'), cv2.COLOR_RGB2LAB)
            lab_planes = cv2.split(lab)
            lab_planes[0] = cv2.equalizeHist(lab_planes[0])
            lab = cv2.merge(lab_planes)
            imRGBCorrec = cv2.cvtColor(lab, cv2.COLOR_LAB2RGB)

        if args.lab_constrast_correction == "none":
            imRGBCorrec = Lab2RGB(imLabCorrec)
            imRGBCorrec = normalize(imRGBCorrec)

    elif args.colour_correction == "CIELAB":
        imCIELab = color.rgb2lab(im)
        imCIELabCorrec = ColorCorrec(imCIELab)
        imRGBCorrec = color.lab2rgb(imCIELabCorrec)
        imRGBCorrec = normalize(imRGBCorrec)

    if args.colour_correction == "LUV":
        imLuv = color.rgb2luv(im)
        imLuvCorrec = ColorCorrec(imLuv)
        imRGBCorrec = color.luv2rgb(imLuvCorrec)
        imRGBCorrec = normalize(imRGBCorrec)

    if args.colour_correction == "YCBC":
        imYCbCr = color.rgb2ycbcr(im)
        imYCbCrCorrec = ColorCorrec(imYCbCr)
        imRGBCorrec = color.ycbcr2rgb(imYCbCrCorrec)
        imRGBCorrec = normalize(imRGBCorrec)

    plt.imsave(args.output_dir + file[:-4] +"_" + args.colour_correction + "_" + args.lab_constrast_correction + ".jpg", imRGBCorrec)
