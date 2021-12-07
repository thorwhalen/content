"""Code to access thorwhalen/content data with ease"""

content_url = 'https://raw.githubusercontent.com/thorwhalen/content/main/{}'.format

def get_content_bytes(key, max_age=None):
    """Get bytes of content from `thorwhalen/content`, automatically caching locally.
    
    ```
    # add max_age=1e-6 if you want to update the data with the remote data
    b = get_content_bytes('tables/csv/projects.csv', max_age=None)
    ```
    """
    from graze import graze
    return graze(content_url(key), max_age=max_age)

def get_table(key, max_age=None, **extra_pandas_kwargs):
    """Get pandas dataframe from `thorwhalen/content`, automatically caching locally.
    ```
    # add max_age=1e-6 if you want to update the data with the remote data
    t = get_table('tables/projects.csv', max_age=None)
    ```
    """
    import pandas as pd
    import io
    b = get_content_bytes(key, max_age=max_age)
    if key.endswith('.csv'):
        return pd.read_csv(io.BytesIO(b), **extra_pandas_kwargs)
