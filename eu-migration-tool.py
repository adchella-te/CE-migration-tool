#US - account token - 414d6591-b136-4408-9a7b-38eff9bfd1e9
#EU - account token - 01ab-9393447c-a74d-4941-aef7-a637285f4773


import requests
import json
from pprint import pprint

auth_bearer1 = input("Input AG1 token : ")
auth_bearer2 = input("Input AG2 token : ")

def create_agent_toserver_test():
    payload2 = json.dumps({
    "interval": int(fetch_tests_from_EU.tinterval),
    "agents": [
        {
        "agentId": 3
        }
    ],
    "testName": str(fetch_tests_from_EU.tname),
    "server": str(fetch_tests_from_EU.tserver.split(":")[0]),
    "port": int(fetch_tests_from_EU.tserver.split(":")[1]),
    "protocol": str(fetch_tests_from_EU.tprotocol),
    "probeMode": str(fetch_tests_from_EU.tprobemode),
    "alertsEnabled": 0
    })
    headers2 = {
    'Content-Type': 'application/json',
    'Accept': 'application/json',
    'Authorization': 'Bearer ' + str(auth_bearer2)
    }
    create_tests_url = "https://api.thousandeyes.com/v6/tests/" + str(fetch_tests_from_EU.ttype) + "/new.json"
    response3 = requests.request("POST", create_tests_url, headers=headers2, data=payload2)
    #print(response3.text)

def fetch_tests_from_EU():
    payload = {}
    headers = {
    'Authorization': 'Bearer ' + str(auth_bearer1)
    }

    tests_url = "https://api.thousandeyes.com/v6/tests.json"
    response1 = requests.request("GET", tests_url, headers=headers, data=payload)
    tests_data = json.loads(response1.text)
    print(tests_data['test'][0])
    fetch_tests_from_EU.ttype = tests_data['test'][0]['type']
    fetch_tests_from_EU.tid = tests_data['test'][0]['testId']
    fetch_tests_from_EU.tname = tests_data['test'][0]['testName']
    fetch_tests_from_EU.tinterval = tests_data['test'][0]['interval']

    if str(fetch_tests_from_EU.ttype) == "agent-to-server":
        fetch_tests_from_EU.tserver = tests_data['test'][0]['server']
        fetch_tests_from_EU.tprotocol = tests_data['test'][0]['protocol']
        fetch_tests_from_EU.tprobemode = tests_data['test'][0]['probeMode']
        create_agent_toserver_test()


def main():
    fetch_tests_from_EU()

if __name__ == "__main__":
    main()
