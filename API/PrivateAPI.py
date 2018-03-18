from time import time
import hashlib
import hmac
import requests
from requests.auth import AuthBase
from urllib.parse import urlencode

class APIAuth(AuthBase):
    def __init__(self,key,sign):
        self.key = key
        self.sign = sign
    def __call__(self,r):
        r.headers['Key'] = self.key
        r.headers['Sign'] = self.sign
        return r
def generate_sign(secret,parameter):
    sign = hmac.new(secret.encode(),parameter.encode(),hashlib.sha512).hexdigest()
    return sign

class Private:
    def __init__(self,key,secret):
        self.Key = key
        self.Secret = secret

    def __send(self,method,parameter):
        url = 'https://vip.bitcoin.co.id/tapi'
        parameter['nonce'] = int(time() * 1000)
        parameter['method'] = method
        auth = APIAuth(self.Key,generate_sign(self.Secret,urlencode(parameter)))
        response = requests.post(url, data=parameter, auth=auth)
        return response.json()

    def getInfo(self):
        return self.__send('getInfo',{})
    
    def transHistory(self):
        return self.__send('transHistory',{})

    def tradeHistory(self,pair):
        value = {
            "pair":pair
        }
        return self.__send('tradeHistory',value)

    def openOrders(self,pair = None):
        if pair == None:
            value = {}
        else:
            value = {
                "pair":pair
            }
        return self.__send('openOrders',value)
    
    def orderHistory(self,pair,count=100,source=0):
        value = {
            "pair":pair,
            "count":count,
            "source":source
        }
        return self.__send('orderHistory',value)

    def getOrder(self,order_id,pair='btc_idr'):
        value = {
            "order_id":order_id,
            "pair":pair
        }
        return self.__send('getOrder',value)
    
    def trade(self,pair,type,price,amount,pair_sell="btc"):
        value = {
            "pair":pair,
            "type":type,
            "price":price
        }
        if type=='buy':
            value["idr"] = amount
        else:
            value[pair_sell] = amount
        return self.__send('trade',value)
    
    def cancelOrder(self,order_id,type,pair="btc_idr"):
        value = {
            "pair":pair,
            "order_id":order_id,
            "type":type
        }
        return self.__send('cancelOrder',value)
    
    def withdrawCoin(self):
        pass
