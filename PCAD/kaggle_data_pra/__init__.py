import kagglehub
from kagglehub import KaggleDatasetAdapter


def dataset_load(dataset_name="", filename=""):
    df = kagglehub.dataset_load(
        KaggleDatasetAdapter.PANDAS,
        handle=dataset_name,
        path=filename, )
    return df.reset_index(drop=True)


def dataset_names():
    dataset_names = [
        # "neurocipher/heartdisease",
        # "emonsharkar/python-learning-and-exam-performance-dataset",
        "oddrationale/mnist-in-csv"
    ]
    return dataset_names


def filenames():
    filenames = [
        # "Heart_Disease_Prediction.csv",
        # "python_learning_exam_performance.csv",
        "mnist_test.csv"
    ]
    return filenames
