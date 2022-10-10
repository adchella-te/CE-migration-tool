import requests
import json
from pprint import pprint

auth_bearer1 = input("Enter Account Token 1: ")
auth_bearer2 = input("Enter Account Token 2: ")

headers = {
    'Content-Type': 'application/json',
    'Accept': 'application/json',
    'Authorization': 'Bearer ' + str(auth_bearer2)
}    

def create_bgp_test():
    global headers
    payload = json.dumps({
    "testName": str(fetch_test_details.tname),
    "description": str(fetch_test_details.tdesc),
    "alertsEnabled": str(fetch_test_details.talertsEnabled),
    "prefix": str(fetch_test_details.tprefix),
    "includeCoveredPrefixes": int(fetch_test_details.tincludeCoveredPrefixes),
    "usePublicBgp": int(fetch_test_details.tusePublicBgp)
    })
    create_tests_url = "https://api.thousandeyes.com/v6/tests/" + 'bgp' + "/new.json"
    response = requests.request("POST", create_tests_url, headers=headers, data=payload)
    if response.status_code != 201:
        print("Error Code : "+ response.status_code + "\nError Message : " + response.text)        

def create_rtp_test():
    global headers
    payload = json.dumps({
    "testName": str(fetch_test_details.tname),
    "description": str(fetch_test_details.tdesc),
    "alertsEnabled": str(fetch_test_details.talertsEnabled),
    "interval": int(fetch_test_details.tinterval),
    "agents": json.loads(fetch_test_details.tagents),
    "targetAgentId": str(fetch_test_details.ttargetAgentId)
    })
    create_tests_url = "https://api.thousandeyes.com/v6/tests/" + 'voice' + "/new.json"
    response = requests.request("POST", create_tests_url, headers=headers, data=payload)
    print(response.status_code)        
    
def create_sip_test():
    global headers
    payload = json.dumps({
    "testName": str(fetch_test_details.tname),
    "description": str(fetch_test_details.tdesc),
    "alertsEnabled": str(fetch_test_details.talertsEnabled),
    "interval": int(fetch_test_details.tinterval),
    "agents": json.loads(fetch_test_details.tagents),
    "targetSipCredentials": {
        "sipRegistrar":  str(fetch_test_details.tsipRegistrar),
            "port": str(fetch_test_details.tport),
            "protocol": str(fetch_test_details.tprotocol)
        }
    })
    create_tests_url = "https://api.thousandeyes.com/v6/tests/" + 'sip-server' + "/new.json"
    response = requests.request("POST", create_tests_url, headers=headers, data=payload)
    print(response.status_code)        

def create_ftp_test():
    global headers
    fetch_test_details.tpassword = input("Enter the password for FTP server - " + fetch_test_details.turl + ": ")
    payload = json.dumps({
    "testName": str(fetch_test_details.tname),
    "description": str(fetch_test_details.tdesc),
    "alertsEnabled": str(fetch_test_details.talertsEnabled),
    "interval": int(fetch_test_details.tinterval),
    "agents": json.loads(fetch_test_details.tagents),
    "url":  str(fetch_test_details.turl),
    "requestType": str(fetch_test_details.trequestType),
    "username": str(fetch_test_details.tusername),
    "password": str(fetch_test_details.tpassword)
    })
    create_tests_url = "https://api.thousandeyes.com/v6/tests/" + 'ftp-server' + "/new.json"
    response = requests.request("POST", create_tests_url, headers=headers, data=payload)
    print(response.status_code)        

def create_transaction_test():
    global headers
    payload = json.dumps({
    "testName": str(fetch_test_details.tname),
    "description": str(fetch_test_details.tdesc),
    "alertsEnabled": str(fetch_test_details.talertsEnabled),
    "interval": int(fetch_test_details.tinterval),
    "agents": json.loads(fetch_test_details.tagents),
    "url":  str(fetch_test_details.turl),
    "transactionScript": str(fetch_test_details.ttransactionScript)
    })
    create_tests_url = "https://api.thousandeyes.com/v6/tests/" + 'web-transactions' + "/new.json"
    response = requests.request("POST", create_tests_url, headers=headers, data=payload)
    print(response.status_code)        

def create_page_test():
    global headers
    payload = json.dumps({
    "testName": str(fetch_test_details.tname),
    "description": str(fetch_test_details.tdesc),
    "alertsEnabled": str(fetch_test_details.talertsEnabled),
    "interval": int(fetch_test_details.tinterval),
    "agents": json.loads(fetch_test_details.tagents),
    "url":  str(fetch_test_details.turl),
    "httpInterval": int(fetch_test_details.thttpInterval)
    })
    create_tests_url = "https://api.thousandeyes.com/v6/tests/" + 'page-load' + "/new.json"
    response = requests.request("POST", create_tests_url, headers=headers, data=payload)
    print(response.status_code)        

def create_http_test():
    global headers
    payload = json.dumps({
    "testName": str(fetch_test_details.tname),
    "description": str(fetch_test_details.tdesc),
    "alertsEnabled": str(fetch_test_details.talertsEnabled),
    "interval": int(fetch_test_details.tinterval),
    "agents": json.loads(fetch_test_details.tagents),
    "url":  str(fetch_test_details.turl)
    })
    create_tests_url = "https://api.thousandeyes.com/v6/tests/" + 'http-server' + "/new.json"
    response = requests.request("POST", create_tests_url, headers=headers, data=payload)
    print(response.status_code)        

def create_dnssec_test():
    global headers
    payload = json.dumps({
    "testName": str(fetch_test_details.tname),
    "description": str(fetch_test_details.tdesc),
    "alertsEnabled": str(fetch_test_details.talertsEnabled),
    "interval": int(fetch_test_details.tinterval),
    "agents": json.loads(fetch_test_details.tagents),
    "domain":  str(fetch_test_details.tdomain)
    })
    create_tests_url = "https://api.thousandeyes.com/v6/tests/" + 'dns-dnssec' + "/new.json"
    response = requests.request("POST", create_tests_url, headers=headers, data=payload)
    print(response.status_code)        
    
def create_dnstrace_test():
    global headers
    payload = json.dumps({
    "testName": str(fetch_test_details.tname),
    "description": str(fetch_test_details.tdesc),
    "alertsEnabled": str(fetch_test_details.talertsEnabled),
    "interval": int(fetch_test_details.tinterval),
    "agents": json.loads(fetch_test_details.tagents),
    "domain":  str(fetch_test_details.tdomain)
    })
    create_tests_url = "https://api.thousandeyes.com/v6/tests/" + 'dns-trace' + "/new.json"
    response = requests.request("POST", create_tests_url, headers=headers, data=payload)
    print(response.status_code)        
    
def create_dnsserv_test():
    global headers
    payload = json.dumps({
    "testName": str(fetch_test_details.tname),
    "description": str(fetch_test_details.tdesc),
    "alertsEnabled": str(fetch_test_details.talertsEnabled),
    "interval": int(fetch_test_details.tinterval),
    "agents": json.loads(fetch_test_details.tagents),
    "domain":  str(fetch_test_details.tdomain),
    "dnsServers": fetch_test_details.tdnsServers
    })
    create_tests_url = "https://api.thousandeyes.com/v6/tests/" + 'dns-server' + "/new.json"
    response = requests.request("POST", create_tests_url, headers=headers, data=payload)
    print(response.status_code)        

def create_a2a_test():
    global headers
    payload = json.dumps({
    "testName": str(fetch_test_details.tname),
    "description": str(fetch_test_details.tdesc),
    "alertsEnabled": str(fetch_test_details.talertsEnabled),
    "interval": int(fetch_test_details.tinterval),
    "agents": json.loads(fetch_test_details.tagents),
    "targetAgentId":  str(fetch_test_details.ttargetAgentId)
    })
    create_tests_url = "https://api.thousandeyes.com/v6/tests/" + 'agent-to-agent' + "/new.json"
    response = requests.request("POST", create_tests_url, headers=headers, data=payload)
    print(response.status_code)        

def create_a2s_test():
    global headers
    payload = json.dumps({
    "testName": str(fetch_test_details.tname),
    "description": str(fetch_test_details.tdesc),
    "alertsEnabled": str(fetch_test_details.talertsEnabled),
    "interval": int(fetch_test_details.tinterval),
    "agents": json.loads(fetch_test_details.tagents),
    "server": str(fetch_test_details.tserver.split(":")[0]),
    "port": fetch_test_details.tport,
    "protocol": str(fetch_test_details.tprotocol),
    "probeMode": str(fetch_test_details.tprobeMode),
    "pathTraceMode": str(fetch_test_details.tpathTraceMode),
    "continuousMode": int(fetch_test_details.tcontinuousMode),
    "networkMeasurements": int(fetch_test_details.tnetworkMeasurements),
    "mtuMeasurements": str(fetch_test_details.tmtuMeasurements),
    "bgpMeasurements": str(fetch_test_details.tbgpMeasurements),
    "pingPayloadSize": int(fetch_test_details.tpingPayloadSize),
    "numPathTraces":int(fetch_test_details.tnumPathTraces), 
    "dscp": str(fetch_test_details.tdscp),
    "dscpId": str(fetch_test_details.tdscpId),
    "ipv6Policy": str(fetch_test_details.tipv6Policy)
    })
    if fetch_test_details.tfixedPacketRate!= 0:
        final_payload = payload[:-1]
        final_payload = final_payload + ', ' + "\"fixedPacketRate\":" + str(fetch_test_details.tfixedPacketRate) + "}"
    else:
        final_payload = payload

    create_tests_url = "https://api.thousandeyes.com/v6/tests/" + 'agent-to-server' + "/new.json"
    response = requests.request("POST", create_tests_url, headers=headers, data=final_payload)
    pprint(final_payload)
    print(response.status_code)        
    
def fetch_test_details():
    payload = {}
    headers = {
    'Authorization': 'Bearer ' + str(auth_bearer1)
    }
    fetch_tests_url = "https://api.thousandeyes.com/v6/tests.json"
    fetch_tests_response = requests.request("GET", fetch_tests_url, headers=headers, data=payload)
    tests_data = json.loads(fetch_tests_response.text)

    for i in range(0,len(tests_data['test'])):
        fetch_test_details.tname = tests_data['test'][i]['testName']
        if('description' in tests_data['test'][i]):
            fetch_test_details.tdesc = tests_data['test'][i]['description']
        else:
            fetch_test_details.tdesc = None
        fetch_test_details.talertsEnabled = tests_data['test'][i]['alertsEnabled']  
               
        if str(tests_data['test'][i]['type']) == 'bgp':
            try:
                #Required
                fetch_test_details.tprefix = tests_data['test'][i]['prefix']
                #Optional
                fetch_test_details.tincludeCoveredPrefixes = tests_data['test'][i]['includeCoveredPrefixes']
                fetch_test_details.tusePublicBgp = tests_data['test'][i]['usePublicBgp']
                create_bgp_test()
            except Exception as e:
                print("Error migrating BGP tests: " +  str(e))
        
        if str(tests_data['test'][i]['type']) == 'voice':
            try:
                #Required    
                fetch_test_details.tinterval = tests_data['test'][i]['interval']
                fetch_test_details.tagents = "["
                fetch_agent_details_url = "https://api.thousandeyes.com/v6/tests/" + str(tests_data['test'][i]['testId']) + ".json"
                fetch_agent_details_response = requests.request("GET", fetch_agent_details_url, headers=headers, data=payload)
                test_data_agents = json.loads(fetch_agent_details_response.text)
                for j in range(0,len(test_data_agents['test'][0]['agents'])):
                    if str(test_data_agents['test'][0]['agents'][j]['agentType']) == 'Cloud':
                        fetch_test_details.tagents = fetch_test_details.tagents + '{"agentId":' + str(test_data_agents['test'][0]['agents'][j]['agentId']) + '},'
                fetch_test_details.tagents = fetch_test_details.tagents[:-1] + ']'
                fetch_test_details.ttargetAgentId = tests_data['test'][i]['targetAgentId']
                #Optional
                create_rtp_test()
            except Exception as e:
                print("Error migrating RTP tests: " +  str(e))
            
        if str(tests_data['test'][i]['type']) == 'sip-server':
            try:
                #Required    
                fetch_test_details.tinterval = tests_data['test'][i]['interval']
                fetch_test_details.tagents = "["
                fetch_agent_details_url = "https://api.thousandeyes.com/v6/tests/" + str(tests_data['test'][i]['testId']) + ".json"
                fetch_agent_details_response = requests.request("GET", fetch_agent_details_url, headers=headers, data=payload)
                test_data_agents = json.loads(fetch_agent_details_response.text)
                for j in range(0,len(test_data_agents['test'][0]['agents'])):
                    if str(test_data_agents['test'][0]['agents'][j]['agentType']) == 'Cloud':
                        fetch_test_details.tagents = fetch_test_details.tagents + '{"agentId":' + str(test_data_agents['test'][0]['agents'][j]['agentId']) + '},'
                fetch_test_details.tagents = fetch_test_details.tagents[:-1] + ']'
                fetch_test_details.tsipRegistrar = tests_data['test'][i]['sipRegistrar']
                fetch_test_details.tport = tests_data['test'][i]['port']
                fetch_test_details.tprotocol = tests_data['test'][i]['protocol']
                #Optional
                create_sip_test()
            except Exception as e:
                print("Error migrating SIP tests: " +  str(e))        

        if str(tests_data['test'][i]['type']) == 'ftp-server':
            try:
                #Required    
                fetch_test_details.tinterval = tests_data['test'][i]['interval']
                fetch_test_details.tagents = "["
                fetch_agent_details_url = "https://api.thousandeyes.com/v6/tests/" + str(tests_data['test'][i]['testId']) + ".json"
                fetch_agent_details_response = requests.request("GET", fetch_agent_details_url, headers=headers, data=payload)
                test_data_agents = json.loads(fetch_agent_details_response.text)
                for j in range(0,len(test_data_agents['test'][0]['agents'])):
                    if str(test_data_agents['test'][0]['agents'][j]['agentType']) == 'Cloud':
                        fetch_test_details.tagents = fetch_test_details.tagents + '{"agentId":' + str(test_data_agents['test'][0]['agents'][j]['agentId']) + '},'
                fetch_test_details.tagents = fetch_test_details.tagents[:-1] + ']'
                fetch_test_details.turl = tests_data['test'][i]['url']
                fetch_test_details.trequestType = tests_data['test'][i]['requestType']
                fetch_test_details.tusername = tests_data['test'][i]['username']
                #Optional
                create_ftp_test()
            except Exception as e:
                print("Error migrating FTP tests: " +  str(e))        

        if str(tests_data['test'][i]['type']) == 'web-transactions':
            try:
                #Required  
                fetch_test_details.tinterval = tests_data['test'][i]['interval']
                fetch_test_details.tagents = "["
                fetch_agent_details_url = "https://api.thousandeyes.com/v6/tests/" + str(tests_data['test'][i]['testId']) + ".json"
                fetch_agent_details_response = requests.request("GET", fetch_agent_details_url, headers=headers, data=payload)
                test_data_agents = json.loads(fetch_agent_details_response.text)
                for j in range(0,len(test_data_agents['test'][0]['agents'])):
                    if str(test_data_agents['test'][0]['agents'][j]['agentType']) == 'Cloud':
                        fetch_test_details.tagents = fetch_test_details.tagents + '{"agentId":' + str(test_data_agents['test'][0]['agents'][j]['agentId']) + '},'
                fetch_test_details.tagents = fetch_test_details.tagents[:-1] + ']'
                fetch_test_details.turl = tests_data['test'][i]['url']
                fetch_test_details.ttransactionScript = tests_data['test'][i]['transactionScript']
                #Optional
                create_transaction_test()
            except Exception as e:
                print("Error migrating Transaction tests: " +  str(e))        

        if str(tests_data['test'][i]['type']) == 'page-load':
            try:
                #Required  
                fetch_test_details.tinterval = tests_data['test'][i]['interval']
                fetch_test_details.tagents = "["
                fetch_agent_details_url = "https://api.thousandeyes.com/v6/tests/" + str(tests_data['test'][i]['testId']) + ".json"
                fetch_agent_details_response = requests.request("GET", fetch_agent_details_url, headers=headers, data=payload)
                test_data_agents = json.loads(fetch_agent_details_response.text)
                for j in range(0,len(test_data_agents['test'][0]['agents'])):
                    if str(test_data_agents['test'][0]['agents'][j]['agentType']) == 'Cloud':
                        fetch_test_details.tagents = fetch_test_details.tagents + '{"agentId":' + str(test_data_agents['test'][0]['agents'][j]['agentId']) + '},'
                fetch_test_details.tagents = fetch_test_details.tagents[:-1] + ']'
                fetch_test_details.turl = tests_data['test'][i]['url']
                fetch_test_details.thttpInterval = tests_data['test'][i]['httpInterval']
                #Optional
                create_page_test()
            except Exception as e:
                print("Error migrating Page Load tests: " +  str(e))        
        
        if str(tests_data['test'][i]['type']) == 'http-server':
            try:
                #Required  
                fetch_test_details.tinterval = tests_data['test'][i]['interval']
                fetch_test_details.tagents = "["
                fetch_agent_details_url = "https://api.thousandeyes.com/v6/tests/" + str(tests_data['test'][i]['testId']) + ".json"
                fetch_agent_details_response = requests.request("GET", fetch_agent_details_url, headers=headers, data=payload)
                test_data_agents = json.loads(fetch_agent_details_response.text)
                for j in range(0,len(test_data_agents['test'][0]['agents'])):
                    if str(test_data_agents['test'][0]['agents'][j]['agentType']) == 'Cloud':
                        fetch_test_details.tagents = fetch_test_details.tagents + '{"agentId":' + str(test_data_agents['test'][0]['agents'][j]['agentId']) + '},'
                fetch_test_details.tagents = fetch_test_details.tagents[:-1] + ']'
                fetch_test_details.turl = tests_data['test'][i]['url']
                #Optional
                create_http_test()
            except Exception as e:
                print("Error migrating HTTP Server tests: " +  str(e))        

        if str(tests_data['test'][i]['type']) == 'dns-dnssec':
            try:
                #Required  
                fetch_test_details.tinterval = tests_data['test'][i]['interval']
                fetch_test_details.tagents = "["
                fetch_agent_details_url = "https://api.thousandeyes.com/v6/tests/" + str(tests_data['test'][i]['testId']) + ".json"
                fetch_agent_details_response = requests.request("GET", fetch_agent_details_url, headers=headers, data=payload)
                test_data_agents = json.loads(fetch_agent_details_response.text)
                for j in range(0,len(test_data_agents['test'][0]['agents'])):
                    if str(test_data_agents['test'][0]['agents'][j]['agentType']) == 'Cloud':
                        fetch_test_details.tagents = fetch_test_details.tagents + '{"agentId":' + str(test_data_agents['test'][0]['agents'][j]['agentId']) + '},'
                fetch_test_details.tagents = fetch_test_details.tagents[:-1] + ']'
                fetch_test_details.tdomain = tests_data['test'][i]['domain']
                #Optional
                create_dnssec_test()
            except Exception as e:
                print("Error migrating DNSSEC tests: " +  str(e)) 

        if str(tests_data['test'][i]['type']) == 'dns-trace':
            try:
                #Required  
                fetch_test_details.tinterval = tests_data['test'][i]['interval']
                fetch_test_details.tagents = "["
                fetch_agent_details_url = "https://api.thousandeyes.com/v6/tests/" + str(tests_data['test'][i]['testId']) + ".json"
                fetch_agent_details_response = requests.request("GET", fetch_agent_details_url, headers=headers, data=payload)
                test_data_agents = json.loads(fetch_agent_details_response.text)
                for j in range(0,len(test_data_agents['test'][0]['agents'])):
                    if str(test_data_agents['test'][0]['agents'][j]['agentType']) == 'Cloud':
                        fetch_test_details.tagents = fetch_test_details.tagents + '{"agentId":' + str(test_data_agents['test'][0]['agents'][j]['agentId']) + '},'
                fetch_test_details.tagents = fetch_test_details.tagents[:-1] + ']'
                fetch_test_details.tdomain = tests_data['test'][i]['domain']
                #Optional
                create_dnstrace_test()
            except Exception as e:
                print("Error migrating DNS Trace tests: " +  str(e))

        if str(tests_data['test'][i]['type']) == 'dns-server':
            try:
                #Required  
                fetch_test_details.tinterval = tests_data['test'][i]['interval']
                fetch_test_details.tagents = "["
                fetch_agent_details_url = "https://api.thousandeyes.com/v6/tests/" + str(tests_data['test'][i]['testId']) + ".json"
                fetch_agent_details_response = requests.request("GET", fetch_agent_details_url, headers=headers, data=payload)
                test_data_agents = json.loads(fetch_agent_details_response.text)
                for j in range(0,len(test_data_agents['test'][0]['agents'])):
                    if str(test_data_agents['test'][0]['agents'][j]['agentType']) == 'Cloud':
                        fetch_test_details.tagents = fetch_test_details.tagents + '{"agentId":' + str(test_data_agents['test'][0]['agents'][j]['agentId']) + '},'
                fetch_test_details.tagents = fetch_test_details.tagents[:-1] + ']'
                fetch_test_details.tdomain = tests_data['test'][i]['domain']
                fetch_test_details.tdnsServers = tests_data['test'][i]['dnsServers']
                #Optional
                create_dnsserv_test()
            except Exception as e:
                print("Error migrating DNS Server tests: " +  str(e))
        
        if str(tests_data['test'][i]['type']) == 'agent-to-agent':
            try:
                #Required  
                fetch_test_details.tinterval = tests_data['test'][i]['interval']
                fetch_test_details.tagents = "["
                fetch_agent_details_url = "https://api.thousandeyes.com/v6/tests/" + str(tests_data['test'][i]['testId']) + ".json"
                fetch_agent_details_response = requests.request("GET", fetch_agent_details_url, headers=headers, data=payload)
                test_data_agents = json.loads(fetch_agent_details_response.text)
                for j in range(0,len(test_data_agents['test'][0]['agents'])):
                    if str(test_data_agents['test'][0]['agents'][j]['agentType']) == 'Cloud':
                        fetch_test_details.tagents = fetch_test_details.tagents + '{"agentId":' + str(test_data_agents['test'][0]['agents'][j]['agentId']) + '},'
                fetch_test_details.tagents = fetch_test_details.tagents[:-1] + ']'
                fetch_test_details.ttargetAgentId = tests_data['test'][i]['targetAgentId']
                #Optional
                create_a2a_test()
            except Exception as e:
                print("Error migrating Agent to Agent tests: " +  str(e))

        if str(tests_data['test'][i]['type']) == 'agent-to-server':
            try:
                #Required  
                fetch_test_details.tinterval = tests_data['test'][i]['interval']
                fetch_test_details.tagents = "["
                fetch_agent_details_url = "https://api.thousandeyes.com/v6/tests/" + str(tests_data['test'][i]['testId']) + ".json"
                fetch_agent_details_response = requests.request("GET", fetch_agent_details_url, headers=headers, data=payload)
                test_data_agents = json.loads(fetch_agent_details_response.text)
                for j in range(0,len(test_data_agents['test'][0]['agents'])):
                    if str(test_data_agents['test'][0]['agents'][j]['agentType']) == 'Cloud':
                        fetch_test_details.tagents = fetch_test_details.tagents + '{"agentId":' + str(test_data_agents['test'][0]['agents'][j]['agentId']) + '},'
                fetch_test_details.tagents = fetch_test_details.tagents[:-1] + ']'
                fetch_test_details.tserver = tests_data['test'][i]['server']
                if ":" in fetch_test_details.tserver:
                    fetch_test_details.tport = int(fetch_test_details.tserver.split(":")[1])
                else:
                    fetch_test_details.tport = None
                #Optional
                fetch_test_details.tprotocol = tests_data['test'][i]['protocol']    
                fetch_test_details.tprobeMode = tests_data['test'][i]['probeMode']
                fetch_test_details.tpathTraceMode = tests_data['test'][i]['pathTraceMode']    
                fetch_test_details.tnetworkMeasurements = tests_data['test'][i]['networkMeasurements']
                fetch_test_details.tcontinuousMode = tests_data['test'][i]['continuousMode']
                fetch_test_details.tmtuMeasurements = tests_data['test'][i]['mtuMeasurements']
                fetch_test_details.tbgpMeasurements = tests_data['test'][i]['bgpMeasurements']
                fetch_test_details.tpingPayloadSize = tests_data['test'][i]['pingPayloadSize']
                if('fixedPacketRate' in tests_data['test'][i]):
                    fetch_test_details.tfixedPacketRate = tests_data['test'][i]['fixedPacketRate']
                else:
                    fetch_test_details.tfixedPacketRate = 0
                fetch_test_details.tnumPathTraces = tests_data['test'][i]['numPathTraces']
                fetch_test_details.tdscp = tests_data['test'][i]['dscp']
                fetch_test_details.tdscpId = tests_data['test'][i]['dscpId']
                fetch_test_details.tipv6Policy = tests_data['test'][i]['ipv6Policy']
                create_a2s_test()
            except Exception as e:
                print("Error migrating Agent to Server tests: " +  str(e))


def create_epa_a2s_test():
    global headers
    payload = json.dumps({
    "testName": str(fetch_epa_test_details.tname),
    "alertsEnabled": str(fetch_epa_test_details.talertsEnabled),
    "interval": int(fetch_epa_test_details.tinterval),
    "maxMachines": int(fetch_epa_test_details.tmaxMachines),
    "agentSelectorType":  str(fetch_epa_test_details.tagentSelectorType),
    "serverName": str(fetch_epa_test_details.tserver)
    })
    create_tests_url = "https://api.thousandeyes.com/v6/endpoint-tests/" + 'agent-to-server' + "/new.json"
    response = requests.request("POST", create_tests_url, headers=headers, data=payload)
    print(response.status_code)        
    
def create_epa_http_test():
    global headers
    payload = json.dumps({
    "testName": str(fetch_epa_test_details.tname),
    "alertsEnabled": str(fetch_epa_test_details.talertsEnabled),
    "interval": int(fetch_epa_test_details.tinterval),
    "maxMachines": int(fetch_epa_test_details.tmaxMachines),
    "agentSelectorType":  str(fetch_epa_test_details.tagentSelectorType),
    "url":  str(fetch_epa_test_details.tserver),
    "verifyCertHostname": bool(fetch_epa_test_details.tverifyCertHostname),
    "sslVersion": int(fetch_epa_test_details.tsslVersion),
    "targetResponseTime": int(fetch_epa_test_details.ttargetResponseTime),
    "httpTimeLimit": int(fetch_epa_test_details.thttpTimeLimit)
    })
    create_tests_url = "https://api.thousandeyes.com/v6/endpoint-tests/" + 'http-server' + "/new.json"
    response = requests.request("POST", create_tests_url, headers=headers, data=payload)
    print(response.status_code)
     
def fetch_epa_test_details():
    payload = {}
    headers = {
    'Authorization': 'Bearer ' + str(auth_bearer1)
    }
    fetch_tests_url = "https://api.thousandeyes.com/v6/endpoint-tests.json"
    fetch_tests_response = requests.request("GET", fetch_tests_url, headers=headers, data=payload)
    epa_tests_data = json.loads(fetch_tests_response.text)

    for i in range(0,len(epa_tests_data['endpointTest'])):
        fetch_epa_test_details.tname = epa_tests_data['endpointTest'][i]['testName']
        fetch_epa_test_details.tagentSelectorType = epa_tests_data['endpointTest'][i]['agentSelectorConfig']['agentSelectorType']
        fetch_epa_test_details.tinterval = epa_tests_data['endpointTest'][i]['interval']
        fetch_epa_test_details.tserver = epa_tests_data['endpointTest'][i]['server']
        fetch_epa_test_details.tmaxMachines = epa_tests_data['endpointTest'][i]['agentSelectorConfig']['maxMachines']   
        fetch_epa_test_details.tlabelIds = epa_tests_data['endpointTest'][i]['agentSelectorConfig']['labelIds']            
        fetch_epa_test_details.talertsEnabled = epa_tests_data['endpointTest'][i]['alertsEnabled']
        
        if str(epa_tests_data['endpointTest'][i]['type']) == 'agent-to-server':
            create_epa_a2s_test()
        
        if  str(epa_tests_data['endpointTest'][i]['type']) == 'http-server':
            fetch_epa_test_details.tverifyCertHostname = epa_tests_data['endpointTest'][i]['verifyCertificate']
            fetch_epa_test_details.tsslVersion = epa_tests_data['endpointTest'][i]['sslVersionId']
            fetch_epa_test_details.ttargetResponseTime = epa_tests_data['endpointTest'][i]['httpTargetTime']
            fetch_epa_test_details.thttpTimeLimit = epa_tests_data['endpointTest'][i]['httpTimeLimit']        
            create_epa_http_test()

def main():
    fetch_test_details()
    fetch_epa_test_details()

if __name__ == "__main__":
    main()
