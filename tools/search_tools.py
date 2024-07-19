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
        url = "https://google.serper.dev/search"  ##this application goes and makes google searches using api
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
            string = []
            for result in results[:top_result_to_return]:
                try:
                    string.append('\n'.join([
                        f"Title: {result['title']}", f"Link: {result['link']}",
                        f"Snippet: {result['snippet']}", "\n--------"
                    ]))
                except KeyError:
                    next

            return '\n'.join(string)

## over here we are passing along the payload which is going to be our query, so what we are doing is, we are making a post request to a certain
## .. endpoint, with a certain header, and want to query for certain data.
## .. for the response, and we are going to do some generic validation, that we are getting a response, yes or no.
## .. if we are getting a response, we are pulling out the information that was gathered for us, then we will start building a repository of 
## .. data that was passed back to the cell, we are going to grab the title , link and the snippet of what the search result said