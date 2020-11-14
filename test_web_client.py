import requests
import json

def getResponseFromCleverbot(message):

    headers = {
      'Content-Type': 'application/json'
    }

    cleverbot_url = "http://localhost:5000/render"
    PARAMS = {'text':message} 

    r = requests.get(url = cleverbot_url, params = PARAMS) 
    data = r.json() 

    # print(data)
    return data['response']


if __name__ == '__main__':
    print(getResponseFromCleverbot("Hi, how are you?"))
