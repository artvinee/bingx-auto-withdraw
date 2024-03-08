import time
import requests
import hmac
import random
from hashlib import sha256

APIURL = "https://open-api.bingx.com"
APIKEY = ""
SECRETKEY = ""
def demo():
    with open('addresses.txt', 'r') as file:
        addresses = file.readlines()
    for address in addresses:
        payload = {}
        path = '/openApi/wallets/v1/capital/withdraw/apply'
        method = "POST"
        paramsMap = {
            "address": address.strip(),
            "addressTag": "None",
            "amount": "0.01",
            "coin": "BNB",
            "network": "BEP20",
            "timestamp": "1709825340278",
            "walletType": "1"
        }
        paramsStr = parseParam(paramsMap)
        print(send_request(method, path, paramsStr, payload))
        time.sleep(random.randint(30, 60))

def get_sign(api_secret, payload):
    signature = hmac.new(api_secret.encode("utf-8"), payload.encode("utf-8"), digestmod=sha256).hexdigest()
    print("sign=" + signature)
    return signature

def send_request(method, path, urlpa, payload):
    url = "%s%s?%s&signature=%s" % (APIURL, path, urlpa, get_sign(SECRETKEY, urlpa))
    print(url)
    headers = {
        'X-BX-APIKEY': APIKEY,
    }
    response = requests.request(method, url, headers=headers, data=payload)
    return response.text

def parseParam(paramsMap):
    sortedKeys = sorted(paramsMap)
    paramsStr = "&".join(["%s=%s" % (x, paramsMap[x]) for x in sortedKeys])
    if paramsStr != "": 
     return paramsStr+"&timestamp="+str(int(time.time() * 1000))
    else:
     return paramsStr+"timestamp="+str(int(time.time() * 1000))

if __name__ == '__main__':
    print("demo:", demo())
