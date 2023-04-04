import json
import requests

class ApiClient:
    def __init__(self, jsonpath):
        self.jsonpath = jsonpath
    
    def result(self, url):
        file = self.jsonpath
        with open(file) as json_file:
            api_headers = json.load(json_file)
        return requests.get(url, headers = api_headers)