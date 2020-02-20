import threading
import requests


user_id = str(-187880935)
token = ""

url = "https://api.vk.com/method/messages.send?user_id="+user_id+"&v=5.37&access_token="+token+"&message="



def buy():
    while True:
        requests.get(url+"/buy 1")
  
def sell():
    while True:
        requests.get(url+"/sell")


threading.Thread(target=buy).start()
threading.Thread(target=sell).start()
