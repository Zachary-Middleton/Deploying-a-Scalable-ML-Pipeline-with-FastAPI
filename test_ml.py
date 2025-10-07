import pytest
from sklearn.linear_model import LogisticRegression

from ml.data import process_data
from ml.model import train_model


# TODO: add necessary import

# TODO: implement the first test. Change the function name and input as needed
def test_one():
    """
    # add description for the first test
    """
    # Your code here
    pass


# TODO: implement the second test. Change the function name and input as needed
def test_train_model_type(sample_data):
    """
    Tests if the train_model function returns the expected algorithm type.
    """
    # Process data to get training inputs
    X, y, _, _ = process_data(
        sample_data,
        categorical_features=["workclass", "education"],
        label="salary",
        training=True
    )

    # Train the model
    model = train_model(X, y)

    # Assert that the returned object is a LogisticRegression model
    assert isinstance(model, LogisticRegression)


# TODO: implement the third test. Change the function name and input as needed
def test_three():
    """
    # add description for the third test
    """
    # Your code here
    pass
