from joblib import load
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

converter_model = "main/models/final_converter.joblib"
final_model = "main/models/final_model.joblib"


def get_predictions(camp: list[list[int]]):
    converter: PolynomialFeatures = load(converter_model)
    model: LinearRegression = load(final_model)
    new_x = converter.fit_transform(camp)
    prediction = model.predict(new_x)
    return {'prediction': prediction.tolist()}
