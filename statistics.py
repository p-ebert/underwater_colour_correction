import pandas as pd
import numpy as np
import scipy.stats as stats

df = pd.read_csv("resultats_sondage_n=21.csv")

df.columns

df["Sur quelle image voit-on mieux les couleurs du fond marin?"][df["Sur quelle image voit-on mieux les couleurs du fond marin?"]=="A"] = 1
df["Sur quelle image voit-on mieux les couleurs du fond marin?"][df["Sur quelle image voit-on mieux les couleurs du fond marin?"]=="B"] = 0

df["Sur quelle image voit-on mieux les couleurs du fond marin?.1"][df["Sur quelle image voit-on mieux les couleurs du fond marin?.1"]=="A"] = 1
df["Sur quelle image voit-on mieux les couleurs du fond marin?.1"][df["Sur quelle image voit-on mieux les couleurs du fond marin?.1"]=="B"] = 0

df["Sur quelle image voit-on mieux les couleurs du fond marin?.2"][df["Sur quelle image voit-on mieux les couleurs du fond marin?.2"]=="B"] = 1
df["Sur quelle image voit-on mieux les couleurs du fond marin?.2"][df["Sur quelle image voit-on mieux les couleurs du fond marin?.2"]=="A"] = 0

df["Sur quelle image voit-on mieux les couleurs du fond marin?.3"][df["Sur quelle image voit-on mieux les couleurs du fond marin?.3"]=="A"] = 1
df["Sur quelle image voit-on mieux les couleurs du fond marin?.3"][df["Sur quelle image voit-on mieux les couleurs du fond marin?.3"]=="B"] = 0

df["Sur quelle image voit-on mieux les couleurs du fond marin?.4"][df["Sur quelle image voit-on mieux les couleurs du fond marin?.4"]=="A"] = 0
df["Sur quelle image voit-on mieux les couleurs du fond marin?.4"][df["Sur quelle image voit-on mieux les couleurs du fond marin?.4"]=="B"] = 1

df["Sur quelle image voit-on mieux les couleurs du fond marin?.5"][df["Sur quelle image voit-on mieux les couleurs du fond marin?.5"]=="B"] = 1
df["Sur quelle image voit-on mieux les couleurs du fond marin?.5"][df["Sur quelle image voit-on mieux les couleurs du fond marin?.5"]=="A"] = 0

df["Sur quelle image voit-on mieux les couleurs du fond marin?.6"][df["Sur quelle image voit-on mieux les couleurs du fond marin?.6"]=="A"] = 1
df["Sur quelle image voit-on mieux les couleurs du fond marin?.6"][df["Sur quelle image voit-on mieux les couleurs du fond marin?.6"]=="B"] = 0

section_1 = df[["Sur quelle image voit-on mieux les couleurs du fond marin?{}".format(i) for i in ["",".1",".2",".3",".4",".5",".6"]]]

lab_correc = section_1.sum(axis=1)
no_correc = 7-lab
stats.ttest_rel(lab_correc, no_correc)

df["Quelle image a le meilleur contraste? "][df["Quelle image a le meilleur contraste? "]=="A"] = 1
df["Quelle image a le meilleur contraste? "][df["Quelle image a le meilleur contraste? "]=="B"] = 0

df["Quelle image a le meilleur contraste? .1"][df["Quelle image a le meilleur contraste? .1"]=="A"] = 1
df["Quelle image a le meilleur contraste? .1"][df["Quelle image a le meilleur contraste? .1"]=="B"] = 0

df["Quelle image a le meilleur contraste? .2"][df["Quelle image a le meilleur contraste? .2"]=="A"] = 1
df["Quelle image a le meilleur contraste? .2"][df["Quelle image a le meilleur contraste? .2"]=="B"] = 0

df["Quelle image a le meilleur contraste? .3"][df["Quelle image a le meilleur contraste? .3"]=="A"] = 1
df["Quelle image a le meilleur contraste? .3"][df["Quelle image a le meilleur contraste? .3"]=="B"] = 0

df["Quelle image a le meilleur contraste? .4"][df["Quelle image a le meilleur contraste? .4"]=="A"] = 0
df["Quelle image a le meilleur contraste? .4"][df["Quelle image a le meilleur contraste? .4"]=="B"] = 1

df["Quelle image a le meilleur contraste? .5"][df["Quelle image a le meilleur contraste? .5"]=="A"] = 1
df["Quelle image a le meilleur contraste? .5"][df["Quelle image a le meilleur contraste? .5"]=="B"] = 0

df["Quelle image a le meilleur contraste? .6"][df["Quelle image a le meilleur contraste? .6"]=="A"] = 1
df["Quelle image a le meilleur contraste? .6"][df["Quelle image a le meilleur contraste? .6"]=="B"] = 0

section_2 = df[["Quelle image a le meilleur contraste? {}".format(i) for i in ["",".1",".2",".3",".4",".5",".6"]]]

clahe = section_2.sum(axis=1)

stretching = 7-lab

clahe.mean()
stretching.mean()
clahe.std()
stretching.std()

stats.ttest_rel(clahe, stretching)


df["Quelle image est la plus réaliste? "][df["Quelle image est la plus réaliste? "]=="A"] = 1
df["Quelle image est la plus réaliste? "][df["Quelle image est la plus réaliste? "]=="B"] = 0

df["Quelle image est la plus réaliste? .1"][df["Quelle image est la plus réaliste? .1"]=="A"] = 0
df["Quelle image est la plus réaliste? .1"][df["Quelle image est la plus réaliste? .1"]=="B"] = 1

df["Quelle image est la plus réaliste? .2"][df["Quelle image est la plus réaliste? .2"]=="A"] = 0
df["Quelle image est la plus réaliste? .2"][df["Quelle image est la plus réaliste? .2"]=="B"] = 1

df["Quelle image est la plus réaliste? .3"][df["Quelle image est la plus réaliste? .3"]=="A"] = 1
df["Quelle image est la plus réaliste? .3"][df["Quelle image est la plus réaliste? .3"]=="B"] = 0

df["Quelle image est la plus réaliste? .4"][df["Quelle image est la plus réaliste? .4"]=="A"] = 0
df["Quelle image est la plus réaliste? .4"][df["Quelle image est la plus réaliste? .4"]=="B"] = 1

df["Quelle image est la plus réaliste? .5"][df["Quelle image est la plus réaliste? .5"]=="A"] = 0
df["Quelle image est la plus réaliste? .5"][df["Quelle image est la plus réaliste? .5"]=="B"] = 1

df["Quelle image est la plus réaliste? .6"][df["Quelle image est la plus réaliste? .6"]=="A"] = 0
df["Quelle image est la plus réaliste? .6"][df["Quelle image est la plus réaliste? .6"]=="B"] = 1

section_3 = df[["Quelle image est la plus réaliste? {}".format(i) for i in ["",".1",".2",".3",".4",".5",".6"]]]

lab_correc_CLAHE = section_3.sum(axis=1)

CIELAB_correc_clahe = 7-lab_correc_CLAHE

lab_correc_CLAHE.mean()
CIELAB_correc_clahe.mean()
lab_correc_CLAHE.std()
CIELAB_correc_clahe.std()

stats.ttest_rel(lab_correc_CLAHE, CIELAB_correc_clahe)




section_3
