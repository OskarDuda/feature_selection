import pyarrow.parquet as pq

def read_parquet(url, file_path):
    full_path = "/".join([url, file_path])
    df = pq.read_pandas(full_path).to_pandas()
    return df
