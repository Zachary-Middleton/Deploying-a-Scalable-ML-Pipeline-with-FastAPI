import pandas as pd
import pytest



@pytest.fixture(scope="session")
def data():

    df = pd.read_csv('data/census.csv')
    return df

    pass

def test_age_range(data):
    assert data['age'].min() >= 0, "Found negative age values."
    assert data['age'].max() <= 110, "Found age values that are likely too high."

def is_numeric(series):
    return pd.api.types.is_numeric_dtype(series)

def is_string_object(series):
    return pd.api.types.is_object_dtype(series)

def test_check_columns(data):

    # Use a dictionary to map column names to their verification functions
    required_columns = {
        "age": is_numeric,
        "workclass": is_string_object,
        "fnlgt": is_numeric,
        "education": is_string_object,
        "education-num": is_numeric,
        "marital-status": is_string_object,
        "occupation": is_string_object,
        "relationship": is_string_object,
        "race": is_string_object,
        "sex": is_string_object,
        "capital-gain": is_numeric,
        "capital-loss": is_numeric,
        "hours-per-week": is_numeric,
        "native-country": is_string_object,
        "salary": is_string_object
    }

    # 1. Check if all required columns are present
    assert set(data.columns.values).issuperset(set(required_columns.keys()))

    # 2. Iterate over the dictionary's items to check each column's format
    for col_name, format_verification_funct in required_columns.items():
        assert format_verification_funct(
            data[col_name]), f"Column '{col_name}' failed data format test '{format_verification_funct.__name__}'"


# TODO: implement the third test. Change the function name and input as needed
def test_no_null_values(data):
    """
    Tests that there are no missing (null/NaN) values in the DataFrame.
    """
    # assert that the total number of null values in the entire dataframe is 0
    assert data.isnull().sum().sum() == 0, "Found null values in the dataset."

    pass
