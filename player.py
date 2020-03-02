import requests
import json
import time

api_key = 'Token 530ea0e7002d91818d4bf1044726330f50e557cb'

headers = {
    'Authorization': api_key,
    'Content-Type': 'application/json'
}


class Player:
    def __init__(self, name, startingRoom):
        self.name = name
        self.currentRoom = startingRoom

    def travel(self, direction):
        print("Direction", direction)
        if direction == "n":
            data = {"direction": "n"}
        if direction == "s":
            data = {"direction": "s"}
        if direction == "e":
            data = {"direction": "e"}
        if direction == "w":
            data = {"direction": "w"}
        res = requests.post(
            # 'https://lambda-treasure-hunt.herokuapp.com/api/adv/move/', headers=headers, data=json.dumps(data)
            'http://127.0.0.1:8000/api/adv/move/', headers=headers, data=json.dumps(data)
        )

        nextRoom = json.loads(res.text)
        self.currentRoom = nextRoom
        print(nextRoom, "Here is our new room")

    def init(self):
        res = requests.get(
            # 'https://lambda-treasure-hunt.herokuapp.com/api/adv/init/', headers=headers
            'http://127.0.0.1:8000/api/adv/init/', headers=headers

        )
        nextRoom = json.loads(res.text)
        self.currentRoom = nextRoom

    # def take(self):
    #     if len(self.currentRoom['items']) > 0:
    #         data={"name": "treasure"}
    #         res=requests.post(
    #         'https://lambda-treasure-hunt.herokuapp.com/api/adv/take/', headers=headers, data=json.dumps(data)
    #         )

    # def drop(self):
    #     data={"name": "treasure"}
    #     res=requests.post(
    #     'https://lambda-treasure-hunt.herokuapp.com/api/adv/drop/', headers=headers, data=json.dumps(data)
    #     )
    #     print("-------", res.text, "DROPPING TREASURE")

    # def status(self):
    #     res=requests.post(
    #         'https://lambda-treasure-hunt.herokuapp.com/api/adv/status/', headers=headers
    #         )
    #     print("-------------------------------STATUS-------------------------------------", json.loads(res.text))

    # def sell(self):
    #     data1={"name": "treasure"}
    #     res=requests.post(
    #     'https://lambda-treasure-hunt.herokuapp.com/api/adv/sell/', headers=headers, data=json.dumps(data1)
    #     )
    #     print("-------", res.text, "SELLING MY TREASURE")
    #     time.sleep(5)
    #     data2={"name": "treasure", "confirm": "name changed"}
    #     res=requests.post(
    #     'https://lambda-treasure-hunt.herokuapp.com/api/adv/sell/', headers=headers, data=json.dumps(data2)
    #     )

    # def name_change(self):
    #     data1={"name":"[Cameron]"}
    #     res=requests.post(
    #     'https://lambda-treasure-hunt.herokuapp.com/api/adv/change_name/', headers=headers, data=json.dumps(data1)
    #     )
    #     print("--------", res.text, "NAME CHANGE")
    #     time.sleep(35)
    #     data2={"name":"[Cameron]", "confirm": "name changed"}
    #     res=requests.post(
    #     'https://lambda-treasure-hunt.herokuapp.com/api/adv/change_name/', headers=headers, data=json.dumps(data2)
    #     )
    #     print("--------", res.text, "NAME CHANGE")

    # def examine(self):
    #     data={"name":"Wishing Well"}
    #     res=requests.post(
    #     'https://lambda-treasure-hunt.herokuapp.com/api/adv/examine/', headers=headers, data=json.dumps(data)
    #     )
    #     print("--------", res.text, "WISHING WELL INFO")
