# Importing required Packages
import keyring as kr
import polars as pl
from serpapi import GoogleSearch
from google.cloud import bigquery
import os

# Env variable to authenticate the current user
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'google-key/proud-device-416516-34036a112ff4.json'

# Creating Bigquery Client to interact with BQ API
client = bigquery.Client()

def pull_data_from_api(token):
    params = {
      "api_key": token,
      "engine": "google_trends",
      "q": "Delhi Metro, Noida Metro, Gurugram Metro",
      "geo": "IN",
      "region": "REGION",
      "data_type": "GEO_MAP",
      "cat": "667"
    }

    search = GoogleSearch(params)
    results = search.get_dict()
    # print(results)


def main():

    # Getting token for authentication(using keyring package)
    # https://www.geeksforgeeks.org/storing-passwords-with-python-keyring/
    token = kr.get_password("Auth-Token", "Token")

    # Pulling data from the API
    # https://serpapi.com/dashboard
    pull_data_from_api(token)



    # Perform a query.
    QUERY = (
        'SELECT * FROM `proud-device-416516.google_trends_ds.test_table`'
    )
    query_job = client.query(QUERY)  # API request
    rows = query_job.result()  # Waits for query to finish
    print(rows)

    for row in rows:
        print(row)



if __name__ == "__main__":
    main()







