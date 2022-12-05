"""Copyright 2022, Cisco Systems, Inc. and/or its affiliate

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

import requests
import json
from pprint import pprint
import logging

logger = logging.getLogger('migrationlogs')
logger.setLevel(logging.DEBUG)

#logs to be sent to log file
fh = logging.FileHandler('te-migration.log')
fh.setLevel(logging.DEBUG)

#logs to be sent to console
ch = logging.StreamHandler()
ch.setLevel(logging.ERROR)

logger.addHandler(fh)
logger.addHandler(ch)

formatter = logging.Formatter('%(asctime)s.%(msecs)03d %(levelname)s [%(thread)d] {} %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
fh.setFormatter(formatter)
ch.setFormatter(formatter)

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
    logger.info('Creating bgp test - '+ str(fetch_test_details.tname))
    response = requests.request("POST", create_tests_url, headers=headers, data=payload)
    logger.debug('BGP test named \"'+ str(fetch_test_details.tname) + '\" create request sent')

    if response.status_code != 201:
        logger.error('Exited with error code : '+ str(response.status_code) + ' when creating \"' + str(fetch_test_details.tname) + '\"'+ '; Error Message : ' + str(response.text))
    else:
        logger.info('Test \"' + str(fetch_test_details.tname) + '\" has been created')

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
    logger.info('Creating voice test - '+ str(fetch_test_details.tname))
    response = requests.request("POST", create_tests_url, headers=headers, data=payload)
    logger.debug('Voice test named \"'+ str(fetch_test_details.tname) + '\" create request sent')

    if response.status_code != 201:
        logger.error('Exited with error code : '+ str(response.status_code) + ' when creating \"' + str(fetch_test_details.tname) + '\"'+ '; Error Message : ' + str(response.text))
    else:
        logger.info('Test \"' + str(fetch_test_details.tname) + '\" has been created')
    
def create_sip_test():
    global headers
    payload = json.dumps({
    "testName": str(fetch_test_details.tname),
    "description": str(fetch_test_details.tdesc),
    "alertsEnabled": str(fetch_test_details.talertsEnabled),
    "interval": int(fetch_test_details.tinterval),
    "agents": json.loads(fetch_test_details.tagents),
    "sipTimeLimit": str(fetch_test_details.tsipTimeLimit),
    "tsipTargetTime": str(fetch_test_details.tsipTargetTime),
    "networkMeasurements":  str(fetch_test_details.tnetworkMeasurements), 
    "bandwidthMeasurements":  0,
    "mtuMeasurements":  str(fetch_test_details.tmtuMeasurements), 
    "bgpMeasurements":  str(fetch_test_details.tbgpMeasurements),
    "pathTraceMode":  str(fetch_test_details.tpathTraceMode),
    "registerEnabled": str(fetch_test_details.tregisterEnabled),
    "ipv6Policy":  str(fetch_test_details.tipv6Policy)
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
    if fetch_test_details.toptionsRegex!= 0:
        payload = payload[:-1]
        payload = payload + ', ' + "\"optionsRegex\": \"" + str(fetch_test_details.toptionsRegex) + "\"}"
    else:
        pass
    payload = payload[:-1]
    payload = payload + ', ' + '\"targetSipCredentials\": { \"sipRegistrar\": \"' + str(fetch_test_details.tsipRegistrar) + '\", \"port\": ' + str(fetch_test_details.tport) + ', \"protocol\": \"' + str(fetch_test_details.tprotocol) + '\"}}'
    if fetch_test_details.tuser!= 0:
        payload = payload[:-2]
        payload = payload + ', ' + "\"user\": \"" + str(fetch_test_details.tuser) + "\"}"
        payload = payload[:-1]
        payload = payload + ', ' + "\"password\": \"" + str(fetch_test_details.tpassword) + "\"}}"
    else:
        pass
    if fetch_test_details.tauthUser!= 0:
        payload = payload[:-2]
        payload = payload + ', ' + "\"authUser\": \"" + str(fetch_test_details.tauthUser) + "\"}}"
    else:
        pass
    
    create_tests_url = "https://api.thousandeyes.com/v6/tests/" + 'sip-server' + "/new.json"
    logger.info('Creating sip test - '+ str(fetch_test_details.tname))
    response = requests.request("POST", create_tests_url, headers=headers, data=payload)
    logger.debug('SIP test named \"'+ str(fetch_test_details.tname) + '\" create request sent')

    if response.status_code != 201:
        logger.error('Exited with error code : '+ str(response.status_code) + ' when creating \"' + str(fetch_test_details.tname) + '\"'+ '; Error Message : ' + str(response.text))   
    else:
        logger.info('Test \"' + str(fetch_test_details.tname) + '\" has been created')
        
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
    "ipv6Policy":  str(fetch_test_details.tipv6Policy)
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

    logger.info('Creating ftp test - '+ str(fetch_test_details.tname))
    response = requests.request("POST", create_tests_url, headers=headers, data=payload)
    logger.debug('FTP test named \"'+ str(fetch_test_details.tname) + '\" create request sent')

    if response.status_code != 201:
        logger.error('Exited with error code : '+ str(response.status_code) + ' when creating \"' + str(fetch_test_details.tname) + '\"'+ '; Error Message : ' + str(response.text))
    else:
        logger.info('Test \"' + str(fetch_test_details.tname) + '\" has been created')

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
    logger.info('Creating transaction test - '+ str(fetch_test_details.tname))
    response = requests.request("POST", create_tests_url, headers=headers, data=payload)
    logger.debug('Transaction test named \"'+ str(fetch_test_details.tname) + '\" create request sent')

    if response.status_code != 201:
        logger.error('Exited with error code : '+ str(response.status_code) + ' when creating \"' + str(fetch_test_details.tname) + '\"'+ '; Error Message : ' + str(response.text))
    else:
        logger.info('Test \"' + str(fetch_test_details.tname) + '\" has been created')

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
    logger.info('Creating page load test - '+ str(fetch_test_details.tname))
    response = requests.request("POST", create_tests_url, headers=headers, data=payload)
    logger.debug('Page load test named \"'+ str(fetch_test_details.tname) + '\" create request sent')
    if response.status_code != 201:
        logger.error('Exited with error code : '+ str(response.status_code) + ' when creating \"' + str(fetch_test_details.tname) + '\"'+ '; Error Message : ' + str(response.text))
    else:
        logger.info('Test \"' + str(fetch_test_details.tname) + '\" has been created')

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
    logger.info('Creating http server test - '+ str(fetch_test_details.tname))
    response = requests.request("POST", create_tests_url, headers=headers, data=payload)
    logger.debug('HTTP server test named \"'+ str(fetch_test_details.tname) + '\" create request sent')

    if response.status_code != 201:
        logger.error('Exited with error code : '+ str(response.status_code) + ' when creating \"' + str(fetch_test_details.tname) + '\"'+ '; Error Message : ' + str(response.text))
    else:
        logger.info('Test \"' + str(fetch_test_details.tname) + '\" has been created')
           
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
    logger.info('Creating dnssec test - '+ str(fetch_test_details.tname))
    response = requests.request("POST", create_tests_url, headers=headers, data=payload)
    logger.debug('DNSSEC test named \"'+ str(fetch_test_details.tname) + '\" create request sent')

    if response.status_code != 201:
        logger.error('Exited with error code : '+ str(response.status_code) + ' when creating \"' + str(fetch_test_details.tname) + '\"'+ '; Error Message : ' + str(response.text))
    else:
        logger.info('Test \"' + str(fetch_test_details.tname) + '\" has been created')
      
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
    logger.info('Creating dns trace test - '+ str(fetch_test_details.tname))
    response = requests.request("POST", create_tests_url, headers=headers, data=payload)
    logger.debug('DNS trace test named \"'+ str(fetch_test_details.tname) + '\" create request sent')

    if response.status_code != 201:
        logger.error('Exited with error code : '+ str(response.status_code) + ' when creating \"' + str(fetch_test_details.tname) + '\"'+ '; Error Message : ' + str(response.text))
    else:
        logger.info('Test \"' + str(fetch_test_details.tname) + '\" has been created')
    
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
    logger.info('Creating dnsserv test - '+ str(fetch_test_details.tname))
    response = requests.request("POST", create_tests_url, headers=headers, data=payload)
    logger.debug('DNSserv test named \"'+ str(fetch_test_details.tname) + '\" create request sent')

    if response.status_code != 201:
        logger.error('Exited with error code : '+ str(response.status_code) + ' when creating \"' + str(fetch_test_details.tname) + '\"'+ '; Error Message : ' + str(response.text))
    else:
        logger.info('Test \"' + str(fetch_test_details.tname) + '\" has been created')

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
    logger.info('Creating agent-to-agent test - '+ str(fetch_test_details.tname))
    response = requests.request("POST", create_tests_url, headers=headers, data=payload)
    logger.debug('Agent-to-agent test named \"'+ str(fetch_test_details.tname) + '\" create request sent')

    if response.status_code != 201:
        logger.error('Exited with error code : '+ str(response.status_code) + ' when creating \"' + str(fetch_test_details.tname) + '\"'+ '; Error Message : ' + str(response.text))
    else:
        logger.info('Test \"' + str(fetch_test_details.tname) + '\" has been created')

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
    logger.info('Creating agent-to-server test - '+ str(fetch_test_details.tname))
    response = requests.request("POST", create_tests_url, headers=headers, data=payload)
    logger.debug('Agent-to-server test named \"'+ str(fetch_test_details.tname) + '\" create request sent')

    if response.status_code != 201:
        logger.error('Exited with error code : '+ str(response.status_code) + ' when creating \"' + str(fetch_test_details.tname) + '\"'+ '; Error Message : ' + str(response.text))
    else:
        logger.info('Test \"' + str(fetch_test_details.tname) + '\" has been created')
    
def fetch_test_details():
    payload = {}
    headers = {
    'Authorization': 'Bearer ' + str(auth_bearer1)
    }
    logger.info('Fetching all tests from source account group')
    fetch_tests_url = "https://api.thousandeyes.com/v6/tests.json"
    fetch_tests_response = requests.request("GET", fetch_tests_url, headers=headers, data=payload)
    tests_data = json.loads(fetch_tests_response.text)
    logger.info('Tests fetch completed')
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
                logger.debug('Fetching Required parameters for bgp test')
                fetch_test_details.tprefix = tests_data['test'][i]['prefix']
                #Optional
                logger.debug('Fetching Optional parameters for bgp test')
                fetch_test_details.tincludeCoveredPrefixes = tests_data['test'][i]['includeCoveredPrefixes']
                fetch_test_details.tusePublicBgp = tests_data['test'][i]['usePublicBgp']
                logger.info('About to create new bgp test')
                create_bgp_test()
            except Exception as e:
                logger.error('Error migrating bgp test - ' +  str(e) + ' when creating \"' + str(fetch_test_details.tname) + '\"')
        
        if str(tests_data['test'][i]['type']) == 'voice':
            try:
                #Required
                logger.debug('Fetching required parameters for voice test')    
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
                logger.debug('Fetching optional parameters for voice test')
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
                logger.info('About to create new voice test')
                create_rtp_test()
            except Exception as e:
                logger.error('Error migrating voice test - ' +  str(e) + ' when creating \"' + str(fetch_test_details.tname) + '\"')
                            
        if str(tests_data['test'][i]['type']) == 'sip-server':
            try:
                #Required    
                logger.debug('Fetching Required parameters for sip test')
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
                fetch_test_details.tprobeMode = tests_data['test'][i]['probeMode']
                fetch_test_details.tpathTraceMode = tests_data['test'][i]['pathTraceMode']
                fetch_test_details.tsipProxy = tests_data['test'][i]['sipProxy']
                fetch_test_details.tsipTimeLimit = tests_data['test'][i]['sipTimeLimit']  
                fetch_test_details.tsipTargetTime = tests_data['test'][i]['sipTargetTime']  
                fetch_test_details.tnetworkMeasurements = tests_data['test'][i]['networkMeasurements']
                fetch_test_details.tmtuMeasurements = tests_data['test'][i]['mtuMeasurements']
                fetch_test_details.tbgpMeasurements = tests_data['test'][i]['bgpMeasurements']
                if('fixedPacketRate' in tests_data['test'][i]):
                    fetch_test_details.tfixedPacketRate = tests_data['test'][i]['fixedPacketRate']
                else:
                    fetch_test_details.tfixedPacketRate = 0
                if('numPathTraces' in tests_data['test'][i]):
                    fetch_test_details.tnumPathTraces = tests_data['test'][i]['numPathTraces']
                else:
                    fetch_test_details.tnumPathTraces = 0
                fetch_test_details.tregisterEnabled = tests_data['test'][i]['registerEnabled']
                if('user' in tests_data['test'][i]):
                    fetch_test_details.tuser = tests_data['test'][i]['user']
                    fetch_test_details.tpassword = input("Enter the password for SIP server - " + str(fetch_test_details.tsipRegistrar) + ", with username - " + str(fetch_test_details.tuser) + " : ")
                else:
                    fetch_test_details.tuser = 0
                if('authUser' in tests_data['test'][i]):
                    fetch_test_details.tauthUser = tests_data['test'][i]['authUser']
                else:
                    fetch_test_details.tauthUser = 0  
                if('optionsRegex' in tests_data['test'][i]):
                    fetch_test_details.toptionsRegex = tests_data['test'][i]['optionsRegex']
                else:
                    fetch_test_details.toptionsRegex = 0
                fetch_test_details.tipv6Policy = tests_data['test'][i]['ipv6Policy']                               
                logger.debug('Fetching optional parameters for sip test')
                logger.info('About to create new sip test')
                create_sip_test()
            except Exception as e:
                logger.error('Error migrating sip test - ' +  str(e) + ' when creating \"' + str(fetch_test_details.tname) + '\"')

        if str(tests_data['test'][i]['type']) == 'ftp-server':
            try:
                #Required    
                logger.debug('Fetching required parameters for ftp test')
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
                logger.debug('Fetching optional parameters for ftp test')
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
                logger.info('About to create new ftp test')
                create_ftp_test()
            except Exception as e:
                logger.error('Error migrating ftp test - ' +  str(e) + ' when creating \"' + str(fetch_test_details.tname) + '\"')

        if str(tests_data['test'][i]['type']) == 'web-transactions':
            try:
                #Required
                logger.debug('Fetching required parameters for transaction test')  
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
                logger.debug('Fetching optional parameters for transaction test')
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
                logger.info('About to create new transaction test')
                create_transaction_test()
            except Exception as e:
                logger.error('Error migrating transaction test - ' +  str(e) + ' when creating \"' + str(fetch_test_details.tname) + '\"')

        if str(tests_data['test'][i]['type']) == 'page-load':
            try:
                #Required  
                logger.debug('Fetching required parameters for page-load test')
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
                logger.debug('Fetching optional parameters for page-load test')
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
                logger.info('About to create new pageload test')
                create_page_test()
                
            except Exception as e:
                logger.error('Error migrating pageload test - ' +  str(e) + ' when creating \"' + str(fetch_test_details.tname) + '\"')
        
        if str(tests_data['test'][i]['type']) == 'http-server':
            try:
                #Required
                logger.debug('Fetching required parameters for http-server test')  
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
                logger.debug('Fetching optional parameters for http-server test')
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
                logger.info('About to create new http server test')
                create_http_test()
            except Exception as e:
                logger.error('Error migrating http server test - ' +  str(e) + ' when creating \"' + str(fetch_test_details.tname) + '\"')

        if str(tests_data['test'][i]['type']) == 'dns-dnssec':
            try:
                #Required
                logger.debug('Fetching required parameters for dnssec test')  
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
                logger.info('About to create new dnssec test')
                create_dnssec_test()
            except Exception as e:
                logger.error('Error migrating dnssec test - ' +  str(e) + ' when creating \"' + str(fetch_test_details.tname) + '\"')

        if str(tests_data['test'][i]['type']) == 'dns-trace':
            try:
                #Required
                logger.debug('Fetching required parameters for dns-trace test')  
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
                logger.debug('Fetching optional parameters for dns-trace test')
                fetch_test_details.tdnsTransportProtocol = tests_data['test'][i]['dnsTransportProtocol']
                logger.info('About to create new dnstrace test')
                create_dnstrace_test()
            except Exception as e:
                logger.error('Error migrating dns trace test - ' +  str(e) + ' when creating \"' + str(fetch_test_details.tname) + '\"')

        if str(tests_data['test'][i]['type']) == 'dns-server':
            try:
                #Required
                logger.debug('Fetching required parameters for dnsserv test')  
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
                logger.debug('Fetching optional parameters for dnsserv test')
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
                logger.info('About to create new dnsserv test')
                create_dnsserv_test()
            except Exception as e:
                logger.error('Error migrating dnsserv test - ' +  str(e) + ' when creating \"' + str(fetch_test_details.tname) + '\"')
        
        if str(tests_data['test'][i]['type']) == 'agent-to-agent':
            try:
                #Required
                logger.debug('Fetching required parameters for agent-to-agent test')  
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
                logger.debug('Fetching optional parameters for agent-to-agent test')
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
                logger.info('About to create new agent-to-agent test')
                create_a2a_test()
            except Exception as e:
                logger.error('Error migrating agent-to-agent test - ' +  str(e) + ' when creating \"' + str(fetch_test_details.tname) + '\"')

        if str(tests_data['test'][i]['type']) == 'agent-to-server':
            try:
                #Required
                logger.debug('Fetching required parameters for agent-to-server test')  
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
                logger.debug('Fetching optional parameters for agent-to-server test')
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
                logger.info('About to create new agent-to-server test')
                create_a2s_test()
            except Exception as e:
                logger.error('Error migrating agent-to-server test - ' +  str(e) + ' when creating \"' + str(fetch_test_details.tname) + '\". Check if only enterprise agents assigned')

                
def create_epa_a2s_test():
    global headers
    payload = json.dumps({
    "testName": str(fetch_epa_test_details.tname),
    "alertsEnabled": str(fetch_epa_test_details.talertsEnabled),
    "interval": int(fetch_epa_test_details.tinterval),
    "maxMachines": int(fetch_epa_test_details.tmaxMachines),
    "agentSelectorType":  str(fetch_epa_test_details.tagentSelectorType),
    "serverName": str(fetch_epa_test_details.tserver),
    "networkProtocol": str(fetch_epa_test_details.tprotocol),
    "port": str(fetch_epa_test_details.tport),
    "pathtraceInSession": bool(fetch_epa_test_details.tpathtraceInSession),
    "networkMeasurements": int(fetch_epa_test_details.tnetworkMeasurements),
    "bandwidthMeasurements": int(fetch_epa_test_details.tnetworkMeasurements),
    "mtuMeasurements": int(fetch_epa_test_details.tmtuMeasurements),
    "bgpMeasurements": int(fetch_epa_test_details.tbgpMeasurements),
    })
    if fetch_epa_test_details.ttcpProbeMode!= 0:
        payload = payload[:-1]
        payload = payload + ', ' + "\"tcpProbeMode\":\"" + str(fetch_epa_test_details.ttcpProbeMode) + "\"}"
    else:
        pass
    create_tests_url = "https://api.thousandeyes.com/v6/endpoint-tests/" + 'agent-to-server' + "/new.json"
    response = requests.request("POST", create_tests_url, headers=headers, data=payload)
    if response.status_code != 201:
        logger.error('Exited with error code : '+ str(response.status_code) + ' when creating \"' + str(fetch_epa_test_details.tname) + '\"'+ '; Error Message : ' + str(response.text))
    else:
        logger.info('Test \"' + str(fetch_epa_test_details.tname) + '\" has been created')
    
def create_epa_http_test():
    global headers
    payload = json.dumps({
    "testName": str(fetch_epa_test_details.tname),
    "alertsEnabled": str(fetch_epa_test_details.talertsEnabled),
    "interval": int(fetch_epa_test_details.tinterval),
    "maxMachines": int(fetch_epa_test_details.tmaxMachines),
    "agentSelectorType":  str(fetch_epa_test_details.tagentSelectorType),
    "url":  str(fetch_epa_test_details.tserver),
    "targetResponseTime": int(fetch_epa_test_details.thttpTargetTime),
    "httpTimeLimit": int(fetch_epa_test_details.thttpTimeLimit),
    "httpVersion": str(fetch_epa_test_details.thttpVersion),
    "networkProtocol": str(fetch_epa_test_details.tprotocol),
    "port": str(fetch_epa_test_details.tport),
    "pathtraceInSession": bool(fetch_epa_test_details.tpathtraceInSession),
    "networkMeasurements": int(fetch_epa_test_details.tnetworkMeasurements),
    "bandwidthMeasurements": int(fetch_epa_test_details.tnetworkMeasurements),
    "mtuMeasurements": int(fetch_epa_test_details.tmtuMeasurements),
    "bgpMeasurements": int(fetch_epa_test_details.tbgpMeasurements),
    "sslVersion": str(fetch_epa_test_details.tsslVersion),
    "sslVersionId": str(fetch_epa_test_details.tsslVersionId),
    "verifyCertHostname": bool(fetch_epa_test_details.tverifyCertHostname),
    "authType": str(fetch_epa_test_details.tauthType),
    "useNtlm": int(fetch_epa_test_details.tuseNtlm),
    "followRedirects": int(fetch_epa_test_details.tfollowRedirects),
    })
    if fetch_epa_test_details.ttcpProbeMode!= 0:
        payload = payload[:-1]
        payload = payload + ', ' + "\"tcpProbeMode\":\"" + str(fetch_epa_test_details.ttcpProbeMode) + "\"}"
    else:
        pass
    if fetch_epa_test_details.tusername!= 0:
        payload = payload[:-1]
        payload = payload + ', ' + "\"username\":\"" + str(fetch_epa_test_details.tusername) + "\"}"
        payload = payload[:-1]
        payload = payload + ', ' + "\"password\":\"" + str(fetch_epa_test_details.tpassword) + "\"}"
    else:
        pass
    if fetch_epa_test_details.tpostBody!= 0:
        payload = payload[:-1]
        payload = payload + ', ' + "\"postBody\":\"" + str(fetch_epa_test_details.tpostBody) + "\"}"
    else:
        pass
    if fetch_epa_test_details.tuserAgent!= 0:
        payload = payload[:-1]
        payload = payload + ', ' + "\"userAgent\":\"" + str(fetch_epa_test_details.tuserAgent) + "\"}"
    else:
        pass
    if fetch_epa_test_details.tcontentRegex!= 0:
        payload = payload[:-1]
        payload = payload + ', ' + "\"contentRegex\":\"" + str(fetch_epa_test_details.tcontentRegex) + "\"}"
    else:
        pass
    create_tests_url = "https://api.thousandeyes.com/v6/endpoint-tests/" + 'http-server' + "/new.json"
    response = requests.request("POST", create_tests_url, headers=headers, data=payload)
    if response.status_code != 201:
        logger.error('Exited with error code : '+ str(response.status_code) + ' when creating \"' + str(fetch_epa_test_details.tname) + '\"'+ '; Error Message : ' + str(response.text))
        pprint(payload)
    else:
        logger.info('Test \"' + str(fetch_epa_test_details.tname) + '\" has been created')

     
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
            #Optional Parameters
            fetch_epa_test_details.tprotocol = epa_tests_data['endpointTest'][i]['protocol']
            fetch_epa_test_details.tport = epa_tests_data['endpointTest'][i]['port']
            if('tcpProbeMode' in epa_tests_data['endpointTest'][i]):
                fetch_epa_test_details.ttcpProbeMode = epa_tests_data['endpointTest'][i]['tcpProbeMode']
            else:
                fetch_epa_test_details.ttcpProbeMode = 0
            fetch_epa_test_details.tpathtraceInSession = epa_tests_data['endpointTest'][i]['pathtraceInSession']
            fetch_epa_test_details.tnetworkMeasurements = epa_tests_data['endpointTest'][i]['networkMeasurements']
            fetch_epa_test_details.tmtuMeasurements = epa_tests_data['endpointTest'][i]['mtuMeasurements']
            fetch_epa_test_details.tbgpMeasurements = epa_tests_data['endpointTest'][i]['bgpMeasurements']            
            fetch_epa_test_details.tbandwidthMeasurements = epa_tests_data['endpointTest'][i]['bandwidthMeasurements']            
            create_epa_a2s_test()
        
        if  str(epa_tests_data['endpointTest'][i]['type']) == 'http-server':
            #Required Configurations
            if('tcpProbeMode' in epa_tests_data['endpointTest'][i]):
                fetch_epa_test_details.ttcpProbeMode = epa_tests_data['endpointTest'][i]['tcpProbeMode']
            else:
                fetch_epa_test_details.ttcpProbeMode = 0
            fetch_epa_test_details.tprotocol = epa_tests_data['endpointTest'][i]['protocol']
            fetch_epa_test_details.tpathtraceInSession = epa_tests_data['endpointTest'][i]['pathtraceInSession']
            fetch_epa_test_details.thttpTargetTime = epa_tests_data['endpointTest'][i]['httpTargetTime']
            fetch_epa_test_details.thttpTimeLimit = epa_tests_data['endpointTest'][i]['httpTimeLimit']
            #Optional Configurations
            fetch_epa_test_details.thttpVersion = epa_tests_data['endpointTest'][i]['httpVersion']
            fetch_epa_test_details.tnetworkMeasurements = epa_tests_data['endpointTest'][i]['networkMeasurements']
            fetch_epa_test_details.tmtuMeasurements = epa_tests_data['endpointTest'][i]['mtuMeasurements']
            fetch_epa_test_details.tbgpMeasurements = epa_tests_data['endpointTest'][i]['bgpMeasurements']            
            fetch_epa_test_details.tbandwidthMeasurements = epa_tests_data['endpointTest'][i]['bandwidthMeasurements'] 
            fetch_epa_test_details.tauthType = epa_tests_data['endpointTest'][i]['authType']
            fetch_epa_test_details.tuseNtlm = epa_tests_data['endpointTest'][i]['useNtlm']
            if(epa_tests_data['endpointTest'][i]['username'] != ""):
                fetch_epa_test_details.tusername = epa_tests_data['endpointTest'][i]['username']
                fetch_epa_test_details.tpassword = input("Enter the password for HTTP server - " + str(fetch_epa_test_details.tserver) + ", with username - " + str(fetch_epa_test_details.tusername) + " : ")
            else:
                fetch_epa_test_details.tusername = 0
            if('postBody' in epa_tests_data['endpointTest'][i]):
                fetch_epa_test_details.tpostBody = epa_tests_data['endpointTest'][i]['postBody']
            else:
                fetch_epa_test_details.tpostBody = 0
            fetch_epa_test_details.tfollowRedirects = epa_tests_data['endpointTest'][i]['followRedirects']
            fetch_epa_test_details.tsslVersionId = epa_tests_data['endpointTest'][i]['sslVersionId']
            fetch_epa_test_details.tverifyCertHostname = epa_tests_data['endpointTest'][i]['verifyCertificate']
            fetch_epa_test_details.tsslVersion = epa_tests_data['endpointTest'][i]['sslVersionId']
            if('userAgent' in epa_tests_data['endpointTest'][i]):
                fetch_epa_test_details.tuserAgent = epa_tests_data['endpointTest'][i]['userAgent']
            else:
                fetch_epa_test_details.tuserAgent = 0
            if('contentRegex' in epa_tests_data['endpointTest'][i]):
                fetch_epa_test_details.tcontentRegex = epa_tests_data['endpointTest'][i]['contentRegex']
            else:
                fetch_epa_test_details.tcontentRegex = 0
            create_epa_http_test()


def main():
    fetch_test_details()
    fetch_epa_test_details()

if __name__ == "__main__":
    main()
