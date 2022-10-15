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
        print("Error Code : "+ str(response.status_code) + "\nError Message : " + str(response.text))        

def create_rtp_test():
    global headers
    payload = json.dumps({
    "testName": str(fetch_test_details.tname),
    "description": str(fetch_test_details.tdesc),
    "alertsEnabled": str(fetch_test_details.talertsEnabled),
    "interval": int(fetch_test_details.tinterval),
    "agents": json.loads(fetch_test_details.tagents),
    "targetAgentId": str(fetch_test_details.ttargetAgentId),
    "server": str(fetch_test_details.tserver),
    "codec": str(fetch_test_details.tcodec),
    "codecId": str(fetch_test_details.tcodecId),
    "duration": str(fetch_test_details.tduration),
    "jitterBuffer": str(fetch_test_details.tjitterBuffer),
    "bgpMeasurements": str(fetch_test_details.tbgpMeasurements),
    "codecId": str(fetch_test_details.tcodecId),
    "numPathTraces": str(fetch_test_details.tnumPathTraces),
    "dscp": str(fetch_test_details.tdscp),
    "dscpId": str(fetch_test_details.tdscpId)
    })
    create_tests_url = "https://api.thousandeyes.com/v6/tests/" + 'voice' + "/new.json"
    response = requests.request("POST", create_tests_url, headers=headers, data=payload)
    if response.status_code != 201:
        print("Error Code : "+ str(response.status_code) + "\nError Message : " + str(response.text))        
    
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
    "password": str(fetch_test_details.tpassword),
    "ftpTimeLimit": str(fetch_test_details.tftpTimeLimit),
    "ftpTargetTime": str(fetch_test_details.tftpTargetTime),
    "networkMeasurements":  str(fetch_test_details.tnetworkMeasurements), 
    "bandwidthMeasurements":  0, 
    "mtuMeasurements":  str(fetch_test_details.tmtuMeasurements), 
    "bgpMeasurements":  str(fetch_test_details.tbgpMeasurements), 
    "protocol":  str(fetch_test_details.tprotocol), 
    "probeMode":  str(fetch_test_details.tprobeMode), 
    "pathTraceMode":  str(fetch_test_details.tpathTraceMode),
    "ipv6Policy":  str(fetch_test_details.tipv6Policy),
    })
    if fetch_test_details.tdownloadLimit!= 0:
        payload = payload[:-1]
        payload = payload + ', ' + "\"downloadLimit\":" + str(fetch_test_details.tdownloadLimit) + "}"
    else:
        pass
    if fetch_test_details.tuploadFileSize!= 0:
        payload = payload[:-1]
        payload = payload + ', ' + "\"uploadFileSize\":" + str(fetch_test_details.tuploadFileSize) + "}"
    else:
        pass
    if fetch_test_details.tcontentRegex!= 0:
        payload = payload[:-1]
        payload = payload + ', ' + "\"contentRegex\": \"" + str(fetch_test_details.tcontentRegex) + "\"}"
    else:
        pass
    if fetch_test_details.tfixedPacketRate!= 0:
        payload = payload[:-1]
        payload = payload + ', ' + "\"fixedPacketRate\":" + str(fetch_test_details.tfixedPacketRate) + "}"
    else:
        pass
    if fetch_test_details.tnumPathTraces!= 0:
        payload = payload[:-1]
        payload = payload + ', ' + "\"numPathTraces\":" + str(fetch_test_details.tnumPathTraces) + "}"
    else:
        pass
    if fetch_test_details.tuseActiveFtp!= 0:
        payload = payload[:-1]
        payload = payload + ', ' + "\"useActiveFtp\":" + str(fetch_test_details.tuseActiveFtp) + "}"
    else:
        pass
    if fetch_test_details.tuseExplicitFtps!= 0:
        payload = payload[:-1]
        payload = payload + ', ' + "\"useExplicitFtps\":" + str(fetch_test_details.tuseExplicitFtps) + "}"
    else:
        pass
    
    if fetch_test_details.tdesiredReplyCode!= 0:
        payload = payload[:-1]
        payload = payload + ', ' + "\"desiredReplyCode\": \"" + str(fetch_test_details.tdesiredReplyCode) + "\"}"
    else:
        pass
    create_tests_url = "https://api.thousandeyes.com/v6/tests/" + 'ftp-server' + "/new.json"
    response = requests.request("POST", create_tests_url, headers=headers, data=payload)
    if response.status_code != 201:
        print("Error Code : "+ str(response.status_code) + "\nError Message : " + str(response.text))         

def create_transaction_test():
    global headers
    payload = json.dumps({
    "testName": str(fetch_test_details.tname),
    "description": str(fetch_test_details.tdesc),
    "alertsEnabled": str(fetch_test_details.talertsEnabled),
    "interval": int(fetch_test_details.tinterval),
    "agents": json.loads(fetch_test_details.tagents),
    "url":  str(fetch_test_details.turl),
    "transactionScript": str(fetch_test_details.ttransactionScript),
    "timeLimit": str(fetch_test_details.ttimeLimit),
    "targetTime": str(fetch_test_details.ttargetTime),
    "httpTimeLimit":  str(fetch_test_details.thttpTimeLimit),
    "httpTargetTime":  str(fetch_test_details.thttpTargetTime),
    "networkMeasurements":  str(fetch_test_details.tnetworkMeasurements), 
    "bandwidthMeasurements":  0, 
    "mtuMeasurements":  str(fetch_test_details.tmtuMeasurements), 
    "bgpMeasurements":  str(fetch_test_details.tbgpMeasurements), 
    "protocol":  str(fetch_test_details.tprotocol), 
    "probeMode":  str(fetch_test_details.tprobeMode), 
    "pathTraceMode":  str(fetch_test_details.tpathTraceMode),
    "sslVersionId":  str(fetch_test_details.tsslVersionId),
    "sslVersion":  str(fetch_test_details.tsslVersion),
    "verifyCertificate":  str(fetch_test_details.tverifyCertificate),
    "authType": str(fetch_test_details.tauthType),
    "useNtlm": str(fetch_test_details.tuseNtlm),
    "httpVersion": str(fetch_test_details.thttpVersion),
    "followRedirects": str(fetch_test_details.tfollowRedirects),
    "identifyAgentTrafficWithUserAgent": str(fetch_test_details.tidentifyAgentTrafficWithUserAgent),
    "contentRegex": str(fetch_test_details.tcontentRegex),
    "includeHeaders": str(fetch_test_details.tincludeHeaders)

    })
    if fetch_test_details.tsubinterval!= 0:
        payload = payload[:-1]
        payload = payload + ', ' + "\"subinterval\":" + str(fetch_test_details.tsubinterval) + "}"
    else:
        pass
    if fetch_test_details.tfixedPacketRate!= 0:
        payload = payload[:-1]
        payload = payload + ', ' + "\"fixedPacketRate\":" + str(fetch_test_details.tfixedPacketRate) + "}"
    else:
        pass
    if fetch_test_details.tnumPathTraces!= 0:
        payload = payload[:-1]
        payload = payload + ', ' + "\"numPathTraces\":" + str(fetch_test_details.tnumPathTraces) + "}"
    else:
        pass
    if fetch_test_details.tusername!= 0:
        payload = payload[:-1]
        payload = payload + ', ' + "\"username\": \"" + str(fetch_test_details.tusername) + "\"}"
        payload = payload[:-1]
        payload = payload + ', ' + "\"password\": \"" + str(fetch_test_details.tpassword) + "\"}"
    else:
        pass
    if fetch_test_details.tuserAgent!= 0:
        payload = payload[:-1]
        payload = payload + ', ' + "\"userAgent\": \"" + str(fetch_test_details.tuserAgent) + "\"}"
    else:
        pass
    if fetch_test_details.tdesiredStatusCode!= 0:
        payload = payload[:-1]
        payload = payload + ', ' + "\"desiredStatusCode\": \"" + str(fetch_test_details.tdesiredStatusCode) + "\"}"
    else:
        pass
    create_tests_url = "https://api.thousandeyes.com/v6/tests/" + 'web-transactions' + "/new.json"
    response = requests.request("POST", create_tests_url, headers=headers, data=payload)
    if response.status_code != 201:
        print("Error Code : "+ str(response.status_code) + "\nError Message : " + str(response.text))      

def create_page_test():
    global headers
    payload = json.dumps({
    "testName": str(fetch_test_details.tname),
    "description": str(fetch_test_details.tdesc),
    "alertsEnabled": str(fetch_test_details.talertsEnabled),
    "interval": int(fetch_test_details.tinterval),
    "agents": json.loads(fetch_test_details.tagents),
    "url":  str(fetch_test_details.turl),
    "httpInterval": int(fetch_test_details.thttpInterval),
    "httpTimeLimit":  str(fetch_test_details.thttpTimeLimit),
    "httpTargetTime":  str(fetch_test_details.thttpTargetTime),
    "pageLoadTimeLimit": str(fetch_test_details.tpageLoadTimeLimit),
    "pageLoadTargetTime": str(fetch_test_details.tpageLoadTargetTime),
    "networkMeasurements":  str(fetch_test_details.tnetworkMeasurements), 
    "bandwidthMeasurements":  0, 
    "mtuMeasurements":  str(fetch_test_details.tmtuMeasurements), 
    "bgpMeasurements":  str(fetch_test_details.tbgpMeasurements), 
    "protocol":  str(fetch_test_details.tprotocol), 
    "probeMode":  str(fetch_test_details.tprobeMode), 
    "pathTraceMode":  str(fetch_test_details.tpathTraceMode),
    "sslVersionId":  str(fetch_test_details.tsslVersionId),
    "sslVersion":  str(fetch_test_details.tsslVersion),
    "verifyCertificate":  str(fetch_test_details.tverifyCertificate),
    "authType": str(fetch_test_details.tauthType),
    "useNtlm": str(fetch_test_details.tuseNtlm),
    "httpVersion": str(fetch_test_details.thttpVersion),
    "followRedirects": str(fetch_test_details.tfollowRedirects),
    "identifyAgentTrafficWithUserAgent": str(fetch_test_details.tidentifyAgentTrafficWithUserAgent),
    "contentRegex": str(fetch_test_details.tcontentRegex),
    "includeHeaders": str(fetch_test_details.tincludeHeaders)
    })
    if fetch_test_details.tsubinterval!= 0:
        payload = payload[:-1]
        payload = payload + ', ' + "\"subinterval\":" + str(fetch_test_details.tsubinterval) + "}"
    else:
        pass
    if fetch_test_details.tfixedPacketRate!= 0:
        payload = payload[:-1]
        payload = payload + ', ' + "\"fixedPacketRate\":" + str(fetch_test_details.tfixedPacketRate) + "}"
    else:
        pass
    if fetch_test_details.tnumPathTraces!= 0:
        payload = payload[:-1]
        payload = payload + ', ' + "\"numPathTraces\":" + str(fetch_test_details.tnumPathTraces) + "}"
    else:
        pass
    if fetch_test_details.tusername!= 0:
        payload = payload[:-1]
        payload = payload + ', ' + "\"username\": \"" + str(fetch_test_details.tusername) + "\"}"
        payload = payload[:-1]
        payload = payload + ', ' + "\"password\": \"" + str(fetch_test_details.tpassword) + "\"}"
    else:
        pass
    if fetch_test_details.tuserAgent!= 0:
        payload = payload[:-1]
        payload = payload + ', ' + "\"userAgent\": \"" + str(fetch_test_details.tuserAgent) + "\"}"
    else:
        pass
    if fetch_test_details.tdesiredStatusCode!= 0:
        payload = payload[:-1]
        payload = payload + ', ' + "\"desiredStatusCode\": \"" + str(fetch_test_details.tdesiredStatusCode) + "\"}"
    else:
        pass
    
    create_tests_url = "https://api.thousandeyes.com/v6/tests/" + 'page-load' + "/new.json"
    response = requests.request("POST", create_tests_url, headers=headers, data=payload)
    if response.status_code != 201:
        print("Error Code : "+ str(response.status_code) + "\nError Message : " + str(response.text))             

def create_http_test():
    global headers
    payload = json.dumps({
    "testName": str(fetch_test_details.tname),
    "description": str(fetch_test_details.tdesc),
    "alertsEnabled": str(fetch_test_details.talertsEnabled),
    "interval": int(fetch_test_details.tinterval),
    "agents": json.loads(fetch_test_details.tagents),
    "url":  str(fetch_test_details.turl),
    "httpTimeLimit":  str(fetch_test_details.thttpTimeLimit),
    "httpTargetTime":  str(fetch_test_details.thttpTargetTime), 
    "networkMeasurements":  str(fetch_test_details.tnetworkMeasurements), 
    "bandwidthMeasurements":  0, 
    "mtuMeasurements":  str(fetch_test_details.tmtuMeasurements), 
    "bgpMeasurements":  str(fetch_test_details.tbgpMeasurements), 
    "protocol":  str(fetch_test_details.tprotocol), 
    "probeMode":  str(fetch_test_details.tprobeMode), 
    "pathTraceMode":  str(fetch_test_details.tpathTraceMode),
    "ipv6Policy":  str(fetch_test_details.tipv6Policy),
    "sslVersionId":  str(fetch_test_details.tsslVersionId),
    "sslVersion":  str(fetch_test_details.tsslVersion),
    "verifyCertificate":  str(fetch_test_details.tverifyCertificate),
    "authType": str(fetch_test_details.tauthType),
    "useNtlm": str(fetch_test_details.tuseNtlm),
    "httpVersion": str(fetch_test_details.thttpVersion),
    "followRedirects": str(fetch_test_details.tfollowRedirects),
    "contentRegex": str(fetch_test_details.tcontentRegex)
    })
    if fetch_test_details.tfixedPacketRate!= 0:
        payload = payload[:-1]
        payload = payload + ', ' + "\"fixedPacketRate\":" + str(fetch_test_details.tfixedPacketRate) + "}"
    else:
        pass
    if fetch_test_details.tnumPathTraces!= 0:
        payload = payload[:-1]
        payload = payload + ', ' + "\"numPathTraces\":" + str(fetch_test_details.tnumPathTraces) + "}"
    else:
        pass
    if fetch_test_details.tclientCertificate!= 0:
        payload = payload[:-1]
        payload = payload + ', ' + "\"clientCertificate\": \"" + str(fetch_test_details.tclientCertificate) + "\"}"
    else:
        pass
    if fetch_test_details.tusername!= 0:
        payload = payload[:-1]
        payload = payload + ', ' + "\"username\": \"" + str(fetch_test_details.tusername) + "\"}"
        payload = payload[:-1]
        payload = payload + ', ' + "\"password\": \"" + str(fetch_test_details.tpassword) + "\"}"
    else:
        pass
    if fetch_test_details.tpostBody!= 0:
        payload = payload[:-1]
        payload = payload + ', ' + "\"postBody\": \"" + str(fetch_test_details.tpostBody) + "\"}"
    else:
        pass
    if fetch_test_details.tuserAgent!= 0:
        payload = payload[:-1]
        payload = payload + ', ' + "\"userAgent\": \"" + str(fetch_test_details.tuserAgent) + "\"}"
    else:
        pass
    if fetch_test_details.tdnsOverride!= 0:
        payload = payload[:-1]
        payload = payload + ', ' + "\"dnsOverride\": \"" + str(fetch_test_details.tdnsOverride) + "\"}"
    else:
        pass
    if fetch_test_details.tdesiredStatusCode!= 0:
        payload = payload[:-1]
        payload = payload + ', ' + "\"desiredStatusCode\": \"" + str(fetch_test_details.tdesiredStatusCode) + "\"}"
    else:
        pass
    if fetch_test_details.tdownloadLimit!= 0:
        payload = payload[:-1]
        payload = payload + ', ' + "\"downloadLimit\": \"" + str(fetch_test_details.tdownloadLimit) + "\"}"
    else:
        pass
    
    create_tests_url = "https://api.thousandeyes.com/v6/tests/" + 'http-server' + "/new.json"
    response = requests.request("POST", create_tests_url, headers=headers, data=payload)
    if response.status_code != 201:
        print("Error Code : "+ str(response.status_code) + "\nError Message : " + str(response.text))                     
           
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
    if response.status_code != 201:
        print("Error Code : "+ str(response.status_code) + "\nError Message : " + str(response.text))                     
      
def create_dnstrace_test():
    global headers
    payload = json.dumps({
    "testName": str(fetch_test_details.tname),
    "description": str(fetch_test_details.tdesc),
    "alertsEnabled": str(fetch_test_details.talertsEnabled),
    "interval": int(fetch_test_details.tinterval),
    "agents": json.loads(fetch_test_details.tagents),
    "domain":  str(fetch_test_details.tdomain),
    "dnsTransportProtocol":  str(fetch_test_details.tdnsTransportProtocol),
    })
    create_tests_url = "https://api.thousandeyes.com/v6/tests/" + 'dns-trace' + "/new.json"
    response = requests.request("POST", create_tests_url, headers=headers, data=payload)
    if response.status_code != 201:
        print("Error Code : "+ str(response.status_code) + "\nError Message : " + str(response.text))                     
    
def create_dnsserv_test():
    global headers
    payload = json.dumps({
    "testName": str(fetch_test_details.tname),
    "description": str(fetch_test_details.tdesc),
    "alertsEnabled": str(fetch_test_details.talertsEnabled),
    "interval": int(fetch_test_details.tinterval),
    "agents": json.loads(fetch_test_details.tagents),
    "domain":  str(fetch_test_details.tdomain),
    "dnsServers": fetch_test_details.tdnsServers,
    "dnsQueryClass":str(fetch_test_details.tdnsQueryClass),
    "networkMeasurements": int(fetch_test_details.tnetworkMeasurements),
    "bandwidthMeasurements": 0,
    "mtuMeasurements": str(fetch_test_details.tmtuMeasurements),
    "bgpMeasurements": str(fetch_test_details.tbgpMeasurements),
    "probeMode": str(fetch_test_details.tprobeMode),
    "ipv6Policy": str(fetch_test_details.tipv6Policy),
    "dnsTransportProtocol":"UDP",
    "recursiveQueries":str(fetch_test_details.trecursiveQueries)
    })
    if fetch_test_details.tnumPathTraces!= 0:
        payload = payload[:-1]
        payload = payload + ', ' + "\"numPathTraces\":" + str(fetch_test_details.tnumPathTraces) + "}"
    else:
        pass
    if fetch_test_details.tfixedPacketRate!= 0:
        payload = payload[:-1]
        payload = payload + ', ' + "\"fixedPacketRate\":" + str(fetch_test_details.tfixedPacketRate) + "}"
    else:
        pass
    create_tests_url = "https://api.thousandeyes.com/v6/tests/" + 'dns-server' + "/new.json"
    response = requests.request("POST", create_tests_url, headers=headers, data=payload)
    if response.status_code != 201:
        print("Error Code : "+ str(response.status_code) + "\nError Message : " + str(response.text))                     

def create_a2a_test():
    global headers
    payload = json.dumps({
    "testName": str(fetch_test_details.tname),
    "description": str(fetch_test_details.tdesc),
    "alertsEnabled": str(fetch_test_details.talertsEnabled),
    "interval": int(fetch_test_details.tinterval),
    "agents": json.loads(fetch_test_details.tagents),
    "targetAgentId":  str(fetch_test_details.ttargetAgentId),
    "direction":  str(fetch_test_details.tdirection),
    "protocol": str(fetch_test_details.tprotocol),
    "pathTraceMode": str(fetch_test_details.tpathTraceMode),
    "port": fetch_test_details.tport,
    "bgpMeasurements": str(fetch_test_details.tbgpMeasurements),
    "bandwidthMeasurements": 0,
    "numPathTraces":int(fetch_test_details.tnumPathTraces), 
    "dscp": str(fetch_test_details.tdscp),
    "dscpId": str(fetch_test_details.tdscpId),
    })
    if fetch_test_details.tfixedPacketRate!= 0:
        payload = payload[:-1]
        payload = payload + ', ' + "\"fixedPacketRate\":" + str(fetch_test_details.tfixedPacketRate) + "}"
    else:
        pass
    if fetch_test_details.tmss!= 0:
        payload = payload[:-1]
        payload = payload + ', ' + "\"mss\":" + str(fetch_test_details.tmss) + "}"
    else:
        pass
    create_tests_url = "https://api.thousandeyes.com/v6/tests/" + 'agent-to-agent' + "/new.json"
    response = requests.request("POST", create_tests_url, headers=headers, data=payload)
    if response.status_code != 201:
        print("Error Code : "+ str(response.status_code) + "\nError Message : " + str(response.text))                    

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
    "pingPayloadSize": int(fetch_test_details.tpingPayloadSize),
    "pathTraceMode": str(fetch_test_details.tpathTraceMode),
    "continuousMode": int(fetch_test_details.tcontinuousMode),
    "networkMeasurements": int(fetch_test_details.tnetworkMeasurements),
    "bandwidthMeasurements": 0,
    "mtuMeasurements": str(fetch_test_details.tmtuMeasurements),
    "bgpMeasurements": str(fetch_test_details.tbgpMeasurements),
    "numPathTraces":int(fetch_test_details.tnumPathTraces), 
    "dscp": str(fetch_test_details.tdscp),
    "dscpId": str(fetch_test_details.tdscpId),
    "ipv6Policy": str(fetch_test_details.tipv6Policy)
    })
    if fetch_test_details.tfixedPacketRate!= 0:
        payload = payload[:-1]
        payload = payload + ', ' + "\"fixedPacketRate\":" + str(fetch_test_details.tfixedPacketRate) + "}"
    else:
        pass
    create_tests_url = "https://api.thousandeyes.com/v6/tests/" + 'agent-to-server' + "/new.json"
    response = requests.request("POST", create_tests_url, headers=headers, data=payload)
    if response.status_code != 201:
        print("Error Code : "+ str(response.status_code) + "\nError Message : " + str(response.text))               
    
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
                #create_bgp_test()
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
                fetch_test_details.tserver = tests_data['test'][i]['server']
                fetch_test_details.tcodec = tests_data['test'][i]['codec']
                fetch_test_details.tcodecId = tests_data['test'][i]['codecId']
                fetch_test_details.tduration = tests_data['test'][i]['duration']
                fetch_test_details.tjitterBuffer = tests_data['test'][i]['jitterBuffer']
                fetch_test_details.tbgpMeasurements = tests_data['test'][i]['bgpMeasurements']
                fetch_test_details.tcodecId = tests_data['test'][i]['codecId']
                fetch_test_details.tnumPathTraces = tests_data['test'][i]['numPathTraces']
                fetch_test_details.tdscp = tests_data['test'][i]['dscp']
                fetch_test_details.tdscpId = tests_data['test'][i]['dscpId']

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
                if('downloadLimit' in tests_data['test'][i]):
                    fetch_test_details.tdownloadLimit = tests_data['test'][i]['downloadLimit']
                else:
                    fetch_test_details.tdownloadLimit = 0  
                if('uploadFileSize' in tests_data['test'][i]):
                    fetch_test_details.tuploadFileSize = tests_data['test'][i]['uploadFileSize']
                else:
                    fetch_test_details.tuploadFileSize = 0
                if('contentRegex' in tests_data['test'][i]):
                    fetch_test_details.tcontentRegex = tests_data['test'][i]['contentRegex']
                else:
                    fetch_test_details.tcontentRegex = 0           
                fetch_test_details.tftpTimeLimit = tests_data['test'][i]['ftpTimeLimit']
                fetch_test_details.tftpTargetTime = tests_data['test'][i]['ftpTargetTime']
                fetch_test_details.tnetworkMeasurements = tests_data['test'][i]['networkMeasurements']
                fetch_test_details.tmtuMeasurements = tests_data['test'][i]['mtuMeasurements']
                fetch_test_details.tbgpMeasurements = tests_data['test'][i]['bgpMeasurements']
                fetch_test_details.tprotocol = tests_data['test'][i]['protocol']
                fetch_test_details.tprobeMode = tests_data['test'][i]['probeMode']
                fetch_test_details.tpathTraceMode = tests_data['test'][i]['pathTraceMode']    
                if('fixedPacketRate' in tests_data['test'][i]):
                    fetch_test_details.tfixedPacketRate = tests_data['test'][i]['fixedPacketRate']
                else:
                    fetch_test_details.tfixedPacketRate = 0
                if('numPathTraces' in tests_data['test'][i]):
                    fetch_test_details.tnumPathTraces = tests_data['test'][i]['numPathTraces']
                else:
                    fetch_test_details.tnumPathTraces = 0
                if('useActiveFtp' in tests_data['test'][i]):
                    fetch_test_details.tuseActiveFtp = tests_data['test'][i]['useActiveFtp']
                else:
                    fetch_test_details.tuseActiveFtp = 0
                if('useExplicitFtps' in tests_data['test'][i]):
                    fetch_test_details.tuseExplicitFtps = tests_data['test'][i]['useExplicitFtps']
                else:
                    fetch_test_details.tuseExplicitFtps = 0
                if('desiredReplyCode' in tests_data['test'][i]):
                    fetch_test_details.tdesiredReplyCode = tests_data['test'][i]['desiredReplyCode']
                else:
                    fetch_test_details.tdesiredReplyCode = 0
                fetch_test_details.tipv6Policy = tests_data['test'][i]['ipv6Policy']
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
                if('subinterval' in tests_data['test'][i]):
                    fetch_test_details.tsubinterval = tests_data['test'][i]['subinterval']
                else:
                    fetch_test_details.tsubinterval = 0
                fetch_test_details.ttimeLimit = tests_data['test'][i]['timeLimit']
                fetch_test_details.ttargetTime = tests_data['test'][i]['targetTime']
                fetch_test_details.thttpTimeLimit = tests_data['test'][i]['httpTimeLimit']
                fetch_test_details.thttpTargetTime = tests_data['test'][i]['httpTargetTime']
                fetch_test_details.tnetworkMeasurements = tests_data['test'][i]['networkMeasurements']
                fetch_test_details.tmtuMeasurements = tests_data['test'][i]['mtuMeasurements']
                fetch_test_details.tbgpMeasurements = tests_data['test'][i]['bgpMeasurements']
                fetch_test_details.tprotocol = tests_data['test'][i]['protocol']
                fetch_test_details.tprobeMode = tests_data['test'][i]['probeMode']
                fetch_test_details.tpathTraceMode = tests_data['test'][i]['pathTraceMode']    
                if('fixedPacketRate' in tests_data['test'][i]):
                    fetch_test_details.tfixedPacketRate = tests_data['test'][i]['fixedPacketRate']
                else:
                    fetch_test_details.tfixedPacketRate = 0
                if('numPathTraces' in tests_data['test'][i]):
                    fetch_test_details.tnumPathTraces = tests_data['test'][i]['numPathTraces']
                else:
                    fetch_test_details.tnumPathTraces = 0
                fetch_test_details.tsslVersionId = tests_data['test'][i]['sslVersionId']
                fetch_test_details.tsslVersion = tests_data['test'][i]['sslVersion']
                fetch_test_details.tverifyCertificate = tests_data['test'][i]['verifyCertificate']
                fetch_test_details.tauthType = tests_data['test'][i]['authType']
                fetch_test_details.tuseNtlm = tests_data['test'][i]['useNtlm']
                if('username' in tests_data['test'][i]):
                    fetch_test_details.tusername = tests_data['test'][i]['username']
                    fetch_test_details.tpassword = input("Enter the password for Page Load test (HTTP auth) - " + str(fetch_test_details.turl) + ", with username - " + str(fetch_test_details.tusername) + " : ")
                else:
                    fetch_test_details.tusername = 0
                fetch_test_details.thttpVersion = tests_data['test'][i]['httpVersion']
                fetch_test_details.tfollowRedirects = tests_data['test'][i]['followRedirects']
                if('userAgent' in tests_data['test'][i]):
                    fetch_test_details.tuserAgent = tests_data['test'][i]['userAgent']
                else:
                    fetch_test_details.tuserAgent = 0
                fetch_test_details.tidentifyAgentTrafficWithUserAgent = tests_data['test'][i]['identifyAgentTrafficWithUserAgent']
                if('desiredStatusCode' in tests_data['test'][i]):
                    fetch_test_details.tdesiredStatusCode = tests_data['test'][i]['desiredStatusCode']
                else:
                    fetch_test_details.tdesiredStatusCode = 0
                fetch_test_details.tcontentRegex = tests_data['test'][i]['contentRegex']
                fetch_test_details.tincludeHeaders = tests_data['test'][i]['includeHeaders']

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
                fetch_test_details.tinterval = tests_data['test'][i]['interval']
                if('subinterval' in tests_data['test'][i]):
                    fetch_test_details.tsubinterval = tests_data['test'][i]['subinterval']
                else:
                    fetch_test_details.tsubinterval = 0
                fetch_test_details.thttpTimeLimit = tests_data['test'][i]['httpTimeLimit']
                fetch_test_details.thttpTargetTime = tests_data['test'][i]['httpTargetTime']
                fetch_test_details.tpageLoadTimeLimit = tests_data['test'][i]['pageLoadTimeLimit']
                fetch_test_details.tpageLoadTargetTime = tests_data['test'][i]['pageLoadTargetTime']
                fetch_test_details.tnetworkMeasurements = tests_data['test'][i]['networkMeasurements']
                fetch_test_details.tmtuMeasurements = tests_data['test'][i]['mtuMeasurements']
                fetch_test_details.tbgpMeasurements = tests_data['test'][i]['bgpMeasurements']
                fetch_test_details.tprotocol = tests_data['test'][i]['protocol']
                fetch_test_details.tprobeMode = tests_data['test'][i]['probeMode']
                fetch_test_details.tpathTraceMode = tests_data['test'][i]['pathTraceMode']    
                if('fixedPacketRate' in tests_data['test'][i]):
                    fetch_test_details.tfixedPacketRate = tests_data['test'][i]['fixedPacketRate']
                else:
                    fetch_test_details.tfixedPacketRate = 0
                if('numPathTraces' in tests_data['test'][i]):
                    fetch_test_details.tnumPathTraces = tests_data['test'][i]['numPathTraces']
                else:
                    fetch_test_details.tnumPathTraces = 0
                fetch_test_details.tsslVersionId = tests_data['test'][i]['sslVersionId']
                fetch_test_details.tsslVersion = tests_data['test'][i]['sslVersion']
                fetch_test_details.tverifyCertificate = tests_data['test'][i]['verifyCertificate']
                fetch_test_details.tauthType = tests_data['test'][i]['authType']
                fetch_test_details.tuseNtlm = tests_data['test'][i]['useNtlm']
                if('username' in tests_data['test'][i]):
                    fetch_test_details.tusername = tests_data['test'][i]['username']
                    fetch_test_details.tpassword = input("Enter the password for Page Load test (HTTP auth) - " + str(fetch_test_details.turl) + ", with username - " + str(fetch_test_details.tusername) + " : ")
                else:
                    fetch_test_details.tusername = 0
                fetch_test_details.thttpVersion = tests_data['test'][i]['httpVersion']
                fetch_test_details.tfollowRedirects = tests_data['test'][i]['followRedirects']
                if('userAgent' in tests_data['test'][i]):
                    fetch_test_details.tuserAgent = tests_data['test'][i]['userAgent']
                else:
                    fetch_test_details.tuserAgent = 0
                fetch_test_details.tidentifyAgentTrafficWithUserAgent = tests_data['test'][i]['identifyAgentTrafficWithUserAgent']
                if('desiredStatusCode' in tests_data['test'][i]):
                    fetch_test_details.tdesiredStatusCode = tests_data['test'][i]['desiredStatusCode']
                else:
                    fetch_test_details.tdesiredStatusCode = 0
                fetch_test_details.tcontentRegex = tests_data['test'][i]['contentRegex']
                fetch_test_details.tincludeHeaders = tests_data['test'][i]['includeHeaders']
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
                fetch_test_details.thttpTimeLimit = tests_data['test'][i]['httpTimeLimit']
                fetch_test_details.thttpTargetTime = tests_data['test'][i]['httpTargetTime']
                fetch_test_details.tnetworkMeasurements = tests_data['test'][i]['networkMeasurements']
                fetch_test_details.tmtuMeasurements = tests_data['test'][i]['mtuMeasurements']
                fetch_test_details.tbgpMeasurements = tests_data['test'][i]['bgpMeasurements']
                fetch_test_details.tprotocol = tests_data['test'][i]['protocol']
                fetch_test_details.tprobeMode = tests_data['test'][i]['probeMode']
                fetch_test_details.tpathTraceMode = tests_data['test'][i]['pathTraceMode']    
                if('fixedPacketRate' in tests_data['test'][i]):
                    fetch_test_details.tfixedPacketRate = tests_data['test'][i]['fixedPacketRate']
                else:
                    fetch_test_details.tfixedPacketRate = 0
                if('numPathTraces' in tests_data['test'][i]):
                    fetch_test_details.tnumPathTraces = tests_data['test'][i]['numPathTraces']
                else:
                    fetch_test_details.tnumPathTraces = 0
                fetch_test_details.tipv6Policy = tests_data['test'][i]['ipv6Policy']
                fetch_test_details.tsslVersionId = tests_data['test'][i]['sslVersionId']
                fetch_test_details.tsslVersion = tests_data['test'][i]['sslVersion']
                fetch_test_details.tverifyCertificate = tests_data['test'][i]['verifyCertificate']
                if('clientCertificate' in tests_data['test'][i]):
                    fetch_test_details.tclientCertificate = tests_data['test'][i]['clientCertificate']
                else:
                    fetch_test_details.tclientCertificate = 0
                fetch_test_details.tauthType = tests_data['test'][i]['authType']
                fetch_test_details.tuseNtlm = tests_data['test'][i]['useNtlm']
                if('username' in tests_data['test'][i]):
                    fetch_test_details.tusername = tests_data['test'][i]['username']
                    fetch_test_details.tpassword = input("Enter the password for HTTP server - " + str(fetch_test_details.turl) + ", with username - " + str(fetch_test_details.tusername) + " : ")
                else:
                    fetch_test_details.tusername = 0
                fetch_test_details.thttpVersion = tests_data['test'][i]['httpVersion']
                if('postBody' in tests_data['test'][i]):
                    fetch_test_details.tpostBody = tests_data['test'][i]['postBody']
                else:
                    fetch_test_details.tpostBody = 0
                fetch_test_details.tfollowRedirects = tests_data['test'][i]['followRedirects']
                if('userAgent' in tests_data['test'][i]):
                    fetch_test_details.tuserAgent = tests_data['test'][i]['userAgent']
                else:
                    fetch_test_details.tuserAgent = 0
                if('dnsOverride' in tests_data['test'][i]):
                    fetch_test_details.tdnsOverride = tests_data['test'][i]['dnsOverride']
                else:
                    fetch_test_details.tdnsOverride = 0
                if('desiredStatusCode' in tests_data['test'][i]):
                    fetch_test_details.tdesiredStatusCode = tests_data['test'][i]['desiredStatusCode']
                else:
                    fetch_test_details.tdesiredStatusCode = 0
                if('downloadLimit' in tests_data['test'][i]):
                    fetch_test_details.tdownloadLimit = tests_data['test'][i]['downloadLimit']
                else:
                    fetch_test_details.tdownloadLimit = 0
                fetch_test_details.tcontentRegex = tests_data['test'][i]['contentRegex']

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
                fetch_test_details.tdnsTransportProtocol = tests_data['test'][i]['dnsTransportProtocol']
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
                fetch_test_details.tdnsQueryClass = tests_data['test'][i]['dnsQueryClass']
                fetch_test_details.tnetworkMeasurements = tests_data['test'][i]['networkMeasurements']
                fetch_test_details.tmtuMeasurements = tests_data['test'][i]['mtuMeasurements']
                fetch_test_details.tbgpMeasurements = tests_data['test'][i]['bgpMeasurements']
                fetch_test_details.tprobeMode = tests_data['test'][i]['probeMode']
                fetch_test_details.tpathTraceMode = tests_data['test'][i]['pathTraceMode']    
                if('fixedPacketRate' in tests_data['test'][i]):
                    fetch_test_details.tfixedPacketRate = tests_data['test'][i]['fixedPacketRate']
                else:
                    fetch_test_details.tfixedPacketRate = 0
                fetch_test_details.trecursiveQueries = tests_data['test'][i]['recursiveQueries']
                if('numPathTraces' in tests_data['test'][i]):
                    fetch_test_details.tnumPathTraces = tests_data['test'][i]['numPathTraces']
                else:
                    fetch_test_details.tnumPathTraces = 0            
                fetch_test_details.tipv6Policy = tests_data['test'][i]['ipv6Policy']
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
                fetch_test_details.tdirection = tests_data['test'][i]['direction']
                fetch_test_details.tprotocol = tests_data['test'][i]['protocol']
                fetch_test_details.tpathTraceMode = tests_data['test'][i]['pathTraceMode']    
                fetch_test_details.tport = tests_data['test'][i]['port']
                if('mss' in tests_data['test'][i]):
                    fetch_test_details.tmss = tests_data['test'][i]['mss']
                else:
                    fetch_test_details.tmss = 0
                fetch_test_details.tbgpMeasurements = tests_data['test'][i]['bgpMeasurements']
                if('fixedPacketRate' in tests_data['test'][i]):
                    fetch_test_details.tfixedPacketRate = tests_data['test'][i]['fixedPacketRate']
                else:
                    fetch_test_details.tfixedPacketRate = 0
                fetch_test_details.tnumPathTraces = tests_data['test'][i]['numPathTraces']
                fetch_test_details.tdscp = tests_data['test'][i]['dscp']
                fetch_test_details.tdscpId = tests_data['test'][i]['dscpId']
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
                print("Error migrating Agent to Server tests: " + str(e) + ". Check if only enterprise agents are assigned to this test.")


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
