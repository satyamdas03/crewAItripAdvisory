# here search tool will be created which will be used by the agent 

import json
import os

import requests
from lanchain.tools import tool

class SearchTools():
    @tool("Search the internet")
    def search_internet(query):
        """
        useful to search the internet
        about a given topic and return relevant results
        """
        top_result_to_return = 4
        url = "https://google.serper.dev/search"
        payload = json.dumps({"q": query})
        headers = {
            'X-API-KEY' : os.environ['SERPER_API_KEY'],
            'content-type' : 'application/json'
        }
        response = requests.request("POST", url, headers=headers, data=payload)
        #check if there is an organic key
        if 'organic' not in response.json():
            return "Sorry, I couldn't find anything about that, there could be an error with you serper api"
        else:
            results = response.json()['organic']
            