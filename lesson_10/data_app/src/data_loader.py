import pandas as pd

def load_data(file_path):
    """
    Load data from a CSV file.

    :param file_path: str, the path to the CSV file
    :return: pandas.DataFrame, the loaded data
    """
    try:
        data = pd.read_csv(file_path)
        return data
    except FileNotFoundError:
        print(f"The file {file_path} was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
