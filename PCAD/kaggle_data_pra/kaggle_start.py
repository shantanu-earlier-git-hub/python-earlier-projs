import pandas as pd
from kaggle_data_pra import dataset_load, dataset_names, filenames

if __name__ == '__main__':

    name = dataset_names()[0]
    filename = filenames()[0]

    print(f"dataset name: {name} , filename: {filename}")

    df = dataset_load(dataset_name=name, filename=filename)
    print(df.head(20))
