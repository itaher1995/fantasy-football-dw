"""This script houses functions that aid in the transformation of data into new
datasets."""

import os
import duckdb
import sqlparse

def write_result_of_query_to_parquet(relative_filepath, schema):


    with open(relative_filepath, 'r') as f:
        query = sqlparse.format(f).replace('\n', ' ')
    save_path = os.path.join(
        'data', schema, 
        relative_filepath.replace('sql', 'parquet').split('/')[-1]
    )
    duckdb.sql(query).write_parquet(save_path)