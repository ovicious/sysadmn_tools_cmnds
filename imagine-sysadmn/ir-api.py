import requests
import threading  
import time

def api_1_10():
    while(True):
        res = requests.get("http://45.114.84.83:9001/api/irhomev2",headers={'Authorization': 'Token 5916f988f8fe3d1c6ea6488c473222c01b97d567'})

        if res.status_code is not 200:
            print(str(res.status_code) + ' - ' + str(res.text))
        else:
            print(str(res.status_code) + str(' ok'))
        time.sleep(5)

threading.Thread(target=api_1_10).start()
