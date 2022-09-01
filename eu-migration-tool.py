#414d6591-b136-4408-9a7b-38eff9bfd1e9

import requests
import json
from pprint import pprint

auth_bearer1 = input("Input AG1 token : ")
auth_bearer2 = input("Input AG2 token : ")

def create_a2s_test():
    payload = json.dumps({
    "interval": int(fetch_test_details.tinterval),
    "agents": json.loads(fetch_test_details.tagents),
    "testName": str(fetch_test_details.tname),
    "description": str(fetch_test_details.tdesc),
    "server": str(fetch_test_details.tserver.split(":")[0]),
    "port": int(fetch_test_details.tserver.split(":")[1]),
    "protocol": str(fetch_test_details.tprotocol),
    "probeMode": str(fetch_test_details.tprobemode),
    "alertsEnabled": 1
    })
    headers = {
    'Content-Type': 'application/json',
    'Accept': 'application/json',
    'Authorization': 'Bearer ' + str(auth_bearer2)
    }    
    create_tests_url = "https://api.thousandeyes.com/v6/tests/" + 'agent-to-server' + "/new.json"
    response = requests.request("POST", create_tests_url, headers=headers, data=payload)
    print(response.status_code)

def create_a2a_test():
    payload = json.dumps({
    "interval": int(fetch_test_details.tinterval),
    "agents": json.loads(fetch_test_details.tagents),
    "testName": str(fetch_test_details.tname),
    "description": str(fetch_test_details.tdesc),
    "protocol": str(fetch_test_details.tprotocol),
    "direction": str(fetch_test_details.tdirection),
    "targetAgentId": str(fetch_test_details.ttargetAgentId),
    "alertsEnabled": 1
    })
    headers = {
    'Content-Type': 'application/json',
    'Accept': 'application/json',
    'Authorization': 'Bearer ' + str(auth_bearer2)
    }    
    create_tests_url = "https://api.thousandeyes.com/v6/tests/" + 'agent-to-agent' + "/new.json"
    response = requests.request("POST", create_tests_url, headers=headers, data=payload)
    print(response.status_code)

def create_http_server_test():
    payload = json.dumps({
    "interval": int(fetch_test_details.tinterval),
    "agents": json.loads(fetch_test_details.tagents),
    "testName": str(fetch_test_details.tname),
    "description": str(fetch_test_details.tdesc),
    "url": str(fetch_test_details.turl),
    "protocol": str(fetch_test_details.tprotocol),
    "probeMode": str(fetch_test_details.tprobemode),
    "alertsEnabled": 1
    })
    headers = {
    'Content-Type': 'application/json',
    'Accept': 'application/json',
    'Authorization': 'Bearer ' + str(auth_bearer2)
    }    
    create_tests_url = "https://api.thousandeyes.com/v6/tests/" + 'http-server' + "/new.json"
    response = requests.request("POST", create_tests_url, headers=headers, data=payload)
    print(response.status_code)

def create_pageload_test():
    payload = json.dumps({
    "interval": int(fetch_test_details.tinterval),
    "agents": json.loads(fetch_test_details.tagents),
    "testName": str(fetch_test_details.tname),
    "description": str(fetch_test_details.tdesc),
    "url": str(fetch_test_details.turl),
    "httpInterval":str(fetch_test_details.thttpInterval),
    "protocol": str(fetch_test_details.tprotocol),
    "probeMode": str(fetch_test_details.tprobemode),
    "alertsEnabled": 1
    })
    headers = {
    'Content-Type': 'application/json',
    'Accept': 'application/json',
    'Authorization': 'Bearer ' + str(auth_bearer2)
    }    
    create_tests_url = "https://api.thousandeyes.com/v6/tests/" + 'page-load' + "/new.json"
    response = requests.request("POST", create_tests_url, headers=headers, data=payload)
    print(response.status_code)

def create_dns_server_test():
    payload = json.dumps({
    "interval": int(fetch_test_details.tinterval),
    "agents": json.loads(fetch_test_details.tagents),
    "testName": str(fetch_test_details.tname),
    "description": str(fetch_test_details.tdesc),
    "domain": str(fetch_test_details.tdomain),
    "protocol": str(fetch_test_details.tprotocol),
    "probeMode": str(fetch_test_details.tprobemode),
    "dnsQueryClass": str(fetch_test_details.tdnsQueryClass),
    "dnsServers": fetch_test_details.tdnsServers,
    "alertsEnabled": 1
    })
    headers = {
    'Content-Type': 'application/json',
    'Accept': 'application/json',
    'Authorization': 'Bearer ' + str(auth_bearer2)
    }    
    create_tests_url = "https://api.thousandeyes.com/v6/tests/" + 'dns-server' + "/new.json"
    response = requests.request("POST", create_tests_url, headers=headers, data=payload)
    print(response.status_code)

def create_dns_trace_test():
    payload = json.dumps({
    "interval": int(fetch_test_details.tinterval),
    "agents": json.loads(fetch_test_details.tagents),
    "testName": str(fetch_test_details.tname),
    "description": str(fetch_test_details.tdesc),
    "domain": str(fetch_test_details.tdomain),
    "protocol": str(fetch_test_details.tprotocol),
    "dnsQueryClass": str(fetch_test_details.tdnsQueryClass),
    "dnsTransportProtocol": str(fetch_test_details.tdnsTransportProtocol),
    "alertsEnabled": 1
    })
    headers = {
    'Content-Type': 'application/json',
    'Accept': 'application/json',
    'Authorization': 'Bearer ' + str(auth_bearer2)
    }    
    create_tests_url = "https://api.thousandeyes.com/v6/tests/" + 'dns-trace' + "/new.json"
    response = requests.request("POST", create_tests_url, headers=headers, data=payload)
    print(response.status_code)
    
def create_dns_dnssec_test():
    payload = json.dumps({
    "interval": int(fetch_test_details.tinterval),
    "agents": json.loads(fetch_test_details.tagents),
    "testName": str(fetch_test_details.tname),
    "description": str(fetch_test_details.tdesc),
    "domain": str(fetch_test_details.tdomain),
    "protocol": str(fetch_test_details.tprotocol),
    "dnsQueryClass": str(fetch_test_details.tdnsQueryClass),
    "alertsEnabled": 1
    })
    headers = {
    'Content-Type': 'application/json',
    'Accept': 'application/json',
    'Authorization': 'Bearer ' + str(auth_bearer2)
    }    
    create_tests_url = "https://api.thousandeyes.com/v6/tests/" + 'dns-dnssec' + "/new.json"
    response = requests.request("POST", create_tests_url, headers=headers, data=payload)
    print(response.status_code)
    
def create_bgp_test():
    payload = json.dumps({
    "testName": str(fetch_test_details.tname),
    "description": str(fetch_test_details.tdesc),
    "prefix": str(fetch_test_details.tprefix),
    "alertsEnabled": 1
    })
    headers = {
    'Content-Type': 'application/json',
    'Accept': 'application/json',
    'Authorization': 'Bearer ' + str(auth_bearer2)
    }    
    create_tests_url = "https://api.thousandeyes.com/v6/tests/" + 'bgp' + "/new.json"
    response = requests.request("POST", create_tests_url, headers=headers, data=payload)
    print(response.status_code)


def fetch_test_details():
    #Fetch list of all tests
    payload = {}
    headers = {
    'Authorization': 'Bearer ' + str(auth_bearer1)
    }
    fetch_tests_url = "https://api.thousandeyes.com/v6/tests.json"
    fetch_tests_response = requests.request("GET", fetch_tests_url, headers=headers, data=payload)
    tests_data = json.loads(fetch_tests_response.text)
    for i in range(0,len(tests_data['test'])):
        #pprint(tests_data['test'][i])
        
        #Agent to Server Tests Migration
        #Fetch test details by type and store in a global variable
        if str(tests_data['test'][i]['type']) == 'agent-to-server':
            fetch_test_details.tname = tests_data['test'][i]['testName']
            fetch_test_details.tdesc = tests_data['test'][i]['description']
            fetch_test_details.tinterval = tests_data['test'][i]['interval']
            fetch_test_details.tserver = tests_data['test'][i]['server']
            fetch_test_details.tprotocol = tests_data['test'][i]['protocol']
            fetch_test_details.tprobemode = tests_data['test'][i]['probeMode']       
            #Fetching agent details for the test
            fetch_test_details.tagents = "["
            fetch_a2s_details_url = "https://api.thousandeyes.com/v6/tests/" + str(tests_data['test'][i]['testId']) + ".json"
            fetch_a2s_details_response = requests.request("GET", fetch_a2s_details_url, headers=headers, data=payload)
            a2s_test_data = json.loads(fetch_a2s_details_response.text)
            for j in range(0,len(a2s_test_data['test'][0]['agents'])):
                if str(a2s_test_data['test'][0]['agents'][j]['agentType']) == 'Cloud':
                    fetch_test_details.tagents = fetch_test_details.tagents + '{"agentId":' + str(a2s_test_data['test'][0]['agents'][j]['agentId']) + '},'
            fetch_test_details.tagents = fetch_test_details.tagents[:-1] + ']'
            create_a2s_test() #UNCOMMENT TO RUN

        #Agent to Agent Tests Migration
        #Fetch test details by type and store in a global variable
        if str(tests_data['test'][i]['type']) == 'agent-to-agent':
            fetch_test_details.tname = tests_data['test'][i]['testName']
            fetch_test_details.tdesc = tests_data['test'][i]['description']
            fetch_test_details.tinterval = tests_data['test'][i]['interval']
            fetch_test_details.tprotocol = tests_data['test'][i]['protocol']
            fetch_test_details.tdirection = tests_data['test'][i]['direction']
            fetch_test_details.ttargetAgentId = tests_data['test'][i]['targetAgentId']       
            #Fetching agent details for the test
            fetch_test_details.tagents = "["
            fetch_a2s_details_url = "https://api.thousandeyes.com/v6/tests/" + str(tests_data['test'][i]['testId']) + ".json"
            fetch_a2s_details_response = requests.request("GET", fetch_a2s_details_url, headers=headers, data=payload)
            a2s_test_data = json.loads(fetch_a2s_details_response.text)
            for j in range(0,len(a2s_test_data['test'][0]['agents'])):
                if str(a2s_test_data['test'][0]['agents'][j]['agentType']) == 'Cloud':
                    fetch_test_details.tagents = fetch_test_details.tagents + '{"agentId":' + str(a2s_test_data['test'][0]['agents'][j]['agentId']) + '},'
            fetch_test_details.tagents = fetch_test_details.tagents[:-1] + ']'
            create_a2a_test() #UNCOMMENT TO RUN
        
        #HTTP Server Tests Migration
        #Fetch test details by type and store in a global variable
        if str(tests_data['test'][i]['type']) == 'http-server':
            fetch_test_details.tname = tests_data['test'][i]['testName']
            fetch_test_details.tdesc = tests_data['test'][i]['description']
            fetch_test_details.tinterval = tests_data['test'][i]['interval']
            fetch_test_details.turl = tests_data['test'][i]['url']
            fetch_test_details.tprotocol = tests_data['test'][i]['protocol']
            fetch_test_details.tprobemode = tests_data['test'][i]['probeMode']       
            #Fetching agent details for the test
            fetch_test_details.tagents = "["
            fetch_a2s_details_url = "https://api.thousandeyes.com/v6/tests/" + str(tests_data['test'][i]['testId']) + ".json"
            fetch_a2s_details_response = requests.request("GET", fetch_a2s_details_url, headers=headers, data=payload)
            a2s_test_data = json.loads(fetch_a2s_details_response.text)
            for j in range(0,len(a2s_test_data['test'][0]['agents'])):
                if str(a2s_test_data['test'][0]['agents'][j]['agentType']) == 'Cloud':
                    fetch_test_details.tagents = fetch_test_details.tagents + '{"agentId":' + str(a2s_test_data['test'][0]['agents'][j]['agentId']) + '},'
            fetch_test_details.tagents = fetch_test_details.tagents[:-1] + ']'
            create_http_server_test() #UNCOMMENT TO RUN
            
        #Page Load Tests Migration
        #Fetch test details by type and store in a global variable
        if str(tests_data['test'][i]['type']) == 'page-load':
            fetch_test_details.tname = tests_data['test'][i]['testName']
            fetch_test_details.tdesc = tests_data['test'][i]['description']
            fetch_test_details.tinterval = tests_data['test'][i]['interval']
            fetch_test_details.thttpInterval = tests_data['test'][i]['httpInterval']            
            fetch_test_details.turl = tests_data['test'][i]['url']
            fetch_test_details.tprotocol = tests_data['test'][i]['protocol']
            fetch_test_details.tprobemode = tests_data['test'][i]['probeMode']       
            #Fetching agent details for the test
            fetch_test_details.tagents = "["
            fetch_a2s_details_url = "https://api.thousandeyes.com/v6/tests/" + str(tests_data['test'][i]['testId']) + ".json"
            fetch_a2s_details_response = requests.request("GET", fetch_a2s_details_url, headers=headers, data=payload)
            a2s_test_data = json.loads(fetch_a2s_details_response.text)
            for j in range(0,len(a2s_test_data['test'][0]['agents'])):
                if str(a2s_test_data['test'][0]['agents'][j]['agentType']) == 'Cloud':
                    fetch_test_details.tagents = fetch_test_details.tagents + '{"agentId":' + str(a2s_test_data['test'][0]['agents'][j]['agentId']) + '},'
            fetch_test_details.tagents = fetch_test_details.tagents[:-1] + ']'
            create_pageload_test() #UNCOMMENT TO RUN
        
        #DNS Server Tests Migration
        #Fetch test details by type and store in a global variable            
        if str(tests_data['test'][i]['type']) == 'dns-server':
            fetch_test_details.tname = tests_data['test'][i]['testName']
            fetch_test_details.tdesc = tests_data['test'][i]['description']
            fetch_test_details.tinterval = tests_data['test'][i]['interval']
            fetch_test_details.tdomain = tests_data['test'][i]['domain']
            fetch_test_details.tprobemode = tests_data['test'][i]['probeMode']
            fetch_test_details.tdnsQueryClass = tests_data['test'][i]['dnsQueryClass']
            fetch_test_details.tdnsServers = tests_data['test'][i]['dnsServers']                  
            #Fetching agent details for the test
            fetch_test_details.tagents = "["
            fetch_a2s_details_url = "https://api.thousandeyes.com/v6/tests/" + str(tests_data['test'][i]['testId']) + ".json"
            fetch_a2s_details_response = requests.request("GET", fetch_a2s_details_url, headers=headers, data=payload)
            a2s_test_data = json.loads(fetch_a2s_details_response.text)
            for j in range(0,len(a2s_test_data['test'][0]['agents'])):
                if str(a2s_test_data['test'][0]['agents'][j]['agentType']) == 'Cloud':
                    fetch_test_details.tagents = fetch_test_details.tagents + '{"agentId":' + str(a2s_test_data['test'][0]['agents'][j]['agentId']) + '},'
            fetch_test_details.tagents = fetch_test_details.tagents[:-1] + ']'
            create_dns_server_test() #UNCOMMENT TO RUN
            
        #DNS Trace Tests Migration
        #Fetch test details by type and store in a global variable            
        if str(tests_data['test'][i]['type']) == 'dns-trace':
            fetch_test_details.tname = tests_data['test'][i]['testName']
            fetch_test_details.tdesc = tests_data['test'][i]['description']
            fetch_test_details.tinterval = tests_data['test'][i]['interval']
            fetch_test_details.tdomain = tests_data['test'][i]['domain']
            fetch_test_details.tdnsQueryClass = tests_data['test'][i]['dnsQueryClass']
            fetch_test_details.tdnsTransportProtocol = tests_data['test'][i]['dnsTransportProtocol']                         
            #Fetching agent details for the test
            fetch_test_details.tagents = "["
            fetch_a2s_details_url = "https://api.thousandeyes.com/v6/tests/" + str(tests_data['test'][i]['testId']) + ".json"
            fetch_a2s_details_response = requests.request("GET", fetch_a2s_details_url, headers=headers, data=payload)
            a2s_test_data = json.loads(fetch_a2s_details_response.text)
            for j in range(0,len(a2s_test_data['test'][0]['agents'])):
                if str(a2s_test_data['test'][0]['agents'][j]['agentType']) == 'Cloud':
                    fetch_test_details.tagents = fetch_test_details.tagents + '{"agentId":' + str(a2s_test_data['test'][0]['agents'][j]['agentId']) + '},'
            fetch_test_details.tagents = fetch_test_details.tagents[:-1] + ']'
            create_dns_trace_test() #UNCOMMENT TO RUN

        #DNSSEC Tests Migration
        #Fetch test details by type and store in a global variable            
        if str(tests_data['test'][i]['type']) == 'dns-dnssec':
            fetch_test_details.tname = tests_data['test'][i]['testName']
            fetch_test_details.tdesc = tests_data['test'][i]['description']
            fetch_test_details.tinterval = tests_data['test'][i]['interval']
            fetch_test_details.tdomain = tests_data['test'][i]['domain']
            fetch_test_details.tdnsQueryClass = tests_data['test'][i]['dnsQueryClass']
            #Fetching agent details for the test
            fetch_test_details.tagents = "["
            fetch_a2s_details_url = "https://api.thousandeyes.com/v6/tests/" + str(tests_data['test'][i]['testId']) + ".json"
            fetch_a2s_details_response = requests.request("GET", fetch_a2s_details_url, headers=headers, data=payload)
            a2s_test_data = json.loads(fetch_a2s_details_response.text)
            for j in range(0,len(a2s_test_data['test'][0]['agents'])):
                if str(a2s_test_data['test'][0]['agents'][j]['agentType']) == 'Cloud':
                    fetch_test_details.tagents = fetch_test_details.tagents + '{"agentId":' + str(a2s_test_data['test'][0]['agents'][j]['agentId']) + '},'
            fetch_test_details.tagents = fetch_test_details.tagents[:-1] + ']'
            create_dns_dnssec_test() #UNCOMMENT TO RUN

        #BGP Tests Migration
        #Fetch test details by type and store in a global variable            
        if str(tests_data['test'][i]['type']) == 'bgp':
            fetch_test_details.tname = tests_data['test'][i]['testName']
            fetch_test_details.tdesc = tests_data['test'][i]['description']
            fetch_test_details.tprefix = tests_data['test'][i]['prefix']
            create_bgp_test() #UNCOMMENT TO RUN


def main():
    fetch_test_details()

if __name__ == "__main__":
    main()
