from flask import request
import pandas as pd


def save_to_parquet():
    # Retrieve the dataframe from the request
    data = request.get_json()['data']
    title = request.get_json()['name']
    df = pd.DataFrame(data)

    # Save the dataframe as a Parquet file
    filename = f"{title}.parquet"
    df.to_parquet(filename)

    return "Data saved as Parquet file: {}".format(filename)
