import requests
import json

class GetRequester:

    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        response = response.get(self.url)
        return response

    def load_json(self):
        response_body = self.get_response_body()
        response_json = response_body.json
        return response_json