import json
import requests

def _get(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

class Public:
    def __init__(self,Pair):
        self.BaseURL = "https://vip.bitcoin.co.id/api/"
        self.Pair = Pair
    
    def getTicker(self):
        return _get(self.BaseURL + self.Pair + '/ticker')

    def getTrades(self):
        return _get(self.BaseURL + self.Pair + '/trades')

    def getDepth(self):
        return _get(self.BaseURL + self.Pair + '/depth')

