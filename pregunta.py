
import os
import glob
import pandas as pd

# Funcion para crear el train.csv

def create_train():
    folder_train = ["negative", "neutral", "positive"]
    col_1 = []
    col_2 = []
    for folder in folder_train:
        filenames = glob.glob(f"data/train/{folder}" + "/*")
        for filename in filenames:
            col_1.append(pd.read_csv(filename, sep="\t", header=None, names=["phrase"]))
            col_2.append(folder)
    concatenated_col1 = pd.concat(col_1, ignore_index=True, axis=0)
    concatenated_col2 = pd.DataFrame(col_2, columns=["sentiment"])
    df = pd.concat(objs=[concatenated_col1, concatenated_col2], axis=1, join="outer", ignore_index=False, sort=False)
    df.to_csv("train_dataset.csv", sep=",", index=False, header=True)
    return df

# Funcion para crear el test.csv

def create_test():
    folder_test = ["negative", "neutral", "positive"]
    col_1 = []
    col_2 = []
    for folder in folder_test:
        filenames = glob.glob(f"data/test/{folder}" + "/*")
        for filename in filenames:
            col_1.append(pd.read_csv(filename, sep="\t", header=None, names=["phrase"]))
            col_2.append(folder)
    concatenated_col_1 = pd.concat(col_1, ignore_index=True, axis=0)
    concatenated_col_2 = pd.DataFrame(col_2, columns=["sentiment"])
    df = pd.concat(objs=[concatenated_col_1, concatenated_col_2], axis=1, join="outer", ignore_index=False, sort=False)
    df.to_csv("test_dataset.csv", sep=",", index=False, header=True)
    return df


create_test()
create_train()
