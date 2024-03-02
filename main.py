# Importing required Packages
import keyring as kr
import polars as pl
from serpapi import GoogleSearch




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
    

def main():

    # Getting token for authentication(using keyring package)
    token = kr.get_password("Auth-Token", "Token")

    # Pulling data from the API
    pull_data_from_api(token)



if __name__ == "__main__":
    main()







