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

#Fetch List of all Account Groups 

url ="https://api.thousandeyes.com/v6/account-groups.json"

print("======================================================================================================")
print("\t\tEnter the OAuth Bearer Token for the Source and Destination")
print("======================================================================================================\n")

while True:
    auth_bearer1 = input("Enter Source Organization's OAuth Bearer Token : ")
    headers1 = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'Authorization': 'Bearer ' + str(auth_bearer1)
    }  
    payload={}  
    fetch_org1_response = requests.request("GET", url, headers=headers1, data=payload)
    if(fetch_org1_response.status_code==200):
        break
    else:
        print("Please enter a valid OAuth Bearer Token")
        continue
    
while True:
    auth_bearer2 = input("Enter Destination Organization's OAuth Bearer Token : ")
    headers2 = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'Authorization': 'Bearer ' + str(auth_bearer2)
    } 
    payload={}  
    fetch_org2_response = requests.request("GET", url, headers=headers2, data=payload)
    if(fetch_org2_response.status_code==200):
        break
    else:
        print("Please enter a valid OAuth Bearer Token")
        continue

ag_data1 = json.loads(fetch_org1_response.text)
ag_data2 = json.loads(fetch_org2_response.text)

#======================================================================================================#

#Choose your account group of choice

ag_aid_dict1 = {}
ag_aid_dict2 = {}
print("\n======================================================================================================")
print("\t\tSelect Source and Destination Account Groups")
print("======================================================================================================\n")
print("Enter the name of the account group to copy the tests from in the source organization : \n")
for i in range(0,len(ag_data1['accountGroups'])):
    ag_aid_dict1[str(ag_data1['accountGroups'][i]['accountGroupName'])] = ag_data1['accountGroups'][i]['aid']
    print(str(i+1) + "." + ag_data1['accountGroups'][i]['accountGroupName'])

while True:
    ag1 = input("\nChoose the option number (e.g. 1) : ")
    if ag1.isdigit():
        if int(ag1) in range(1,i+2):
            break
        else:
            print("Please enter a value between 1 and "  + str(i+1) + " only")
    else:
        print("Please enter only the option number from the list above")
        continue 
src_aid = list(ag_aid_dict1.items())[int(ag1)-1][1]
print("Source AID selected as - " + str(src_aid))

print("\nEnter the name of the account group to copy the tests to in the destination organization : \n")
for i in range(0,len(ag_data2['accountGroups'])):
    ag_aid_dict2[str(ag_data2['accountGroups'][i]['accountGroupName'])] = ag_data2['accountGroups'][i]['aid']
    print(str(i+1) + "." + ag_data2['accountGroups'][i]['accountGroupName'])

while True:
    ag2 = input("\nChoose the option number (e.g. 1) : ")
    if ag2.isdigit():
        if int(ag2) in range(1,i+2):
            break
        else:
            print("Please enter a value between 1 and "  + str(i+1) + " only")
    else:
        print("Please enter only the option number from the list above")
        continue 
dst_aid = list(ag_aid_dict2.items())[int(ag2)-1][1]
print("Destination AID selected as - " + str(dst_aid))

#Add error handling for list out of range and please choose a value from the range mentioned above

#======================================================================================================#

#Choose which type of tests are to be migrated -

print("\n======================================================================================================")
print("\t\tSelect Test Types to be Migrated")
print("======================================================================================================")
while True:
    ea_tests_flag = input("\nDo you wish to migrate Enterprise Agent Tests (1 = Yes, 0 = No) : ")
    if(ea_tests_flag=="1"):
        all_ea_tests = input("\nMigrate all test types? (1 = Yes, 0 = No) : ")
        if (all_ea_tests == "1"):
            bgp_flag = 1
            ea_a2s_flag = 1
            a2a_flag = 1
            ea_http_server_flag = 1
            page_load_flag = 1
            web_transaction_flag = 1
            ftp_flag = 1
            dns_server_flag = 1
            dns_trace_flag = 1
            dnssec_flag = 1
            sip_server_flag = 1
            rtp_server_flag = 1
            break
        else:    
            print("\nChoose the type of tests you wish to migrate (1 = Yes, 0 = No) - \n")
            while True:
                bgp_flag = input("Migrate BGP Tests? : ")
                if bgp_flag=="1" or bgp_flag=="0":
                    break
                else:
                    print("Please enter only a 1 (Yes) or 0 (No)")
                    continue      
            while True:
                ea_a2s_flag = input("Migrate Agent-to-Server Tests? : ")
                if ea_a2s_flag=="1" or ea_a2s_flag=="0":
                    break
                else:
                    print("Please enter only a 1 (Yes) or 0 (No)")
                    continue      
            while True:
                a2a_flag = input("Migrate Agent-to-Agent Server Tests? : ")
                if a2a_flag=="1" or a2a_flag=="0":
                    break
                else:
                    print("Please enter only a 1 (Yes) or 0 (No)")
                    continue
            while True:
                ea_http_server_flag = input("Migrate HTTP Server Tests? : ")
                if ea_http_server_flag=="1" or ea_http_server_flag=="0":
                    break
                else:
                    print("Please enter only a 1 (Yes) or 0 (No)")
                    continue
            while True:
                page_load_flag = input("Migrate Page Load Tests? : ")
                if page_load_flag=="1" or page_load_flag=="0":
                    break
                else:
                    print("Please enter only a 1 (Yes) or 0 (No)")
                    continue
            while True:
                web_transaction_flag = input("Migrate Web Transaction Tests? : ")
                if web_transaction_flag=="1" or web_transaction_flag=="0":
                    break
                else:
                    print("Please enter only a 1 (Yes) or 0 (No)")
                    continue 
            while True:
                ftp_flag = input("Migrate FTP Server Tests? : ")
                if ftp_flag=="1" or ftp_flag=="0":
                    break
                else:
                    print("Please enter only a 1 (Yes) or 0 (No)")
                    continue 
            while True:
                dns_server_flag = input("Migrate DNS Server Tests? : ")
                if dns_server_flag=="1" or dns_server_flag=="0":
                    break
                else:
                    print("Please enter only a 1 (Yes) or 0 (No)")
                    continue
            while True:
                dns_trace_flag = input("Migrate DNS Trace Tests? : ")
                if dns_trace_flag=="1" or dns_trace_flag=="0":
                    break
                else:
                    print("Please enter only a 1 (Yes) or 0 (No)")
                    continue
            while True:
                dnssec_flag = input("Migrate DNSSEC Tests? : ")
                if dnssec_flag=="1" or dnssec_flag=="0":
                    break
                else:
                    print("Please enter only a 1 (Yes) or 0 (No)")
                    continue
            while True:
                sip_server_flag = input("Migrate SIP Server Tests? : ")
                if sip_server_flag=="1" or sip_server_flag=="0":
                    break
                else:
                    print("Please enter only a 1 (Yes) or 0 (No)")
                    continue    
            while True:
                rtp_server_flag = input("Migrate RTP Stream Tests? : ")
                if rtp_server_flag=="1" or rtp_server_flag=="0":
                    break
                else:
                    print("Please enter only a 1 (Yes) or 0 (No)")
                    continue
            break                  
    elif (ea_tests_flag=="0"):
        break 
    else:
        print("Please enter only a 1 (Yes) or 0 (No)")
        continue

while True:
    epa_tests_flag = input("\nDo you wish to migrate Endpoint Agent Tests (1 = Yes, 0 = No) : ")
    if(epa_tests_flag=="1"):
        all_epa_tests = input("\nMigrate all test types? (1 = Yes, 0 = No) : ")
        if (all_epa_tests == "1"):
            epa_a2s_flag = 1
            epa_http_server_flag = 1
            ast_test = 1
            break
        else :
            print("\nChoose the type of tests you wish to migrate (1 = Yes, 0 = No) - \n")
            while True:
                epa_a2s_flag = input("Migrate EPA Agent-to-Server Tests? : ")
                if epa_a2s_flag=="1" or epa_a2s_flag=="0":
                    break
                else:
                    print("Please enter only a 1 (Yes) or 0 (No)")
                    continue
            while True:
                epa_http_server_flag = input("Migrate EPA HTTP Server Tests? : ")
                if epa_http_server_flag=="1" or epa_http_server_flag=="0":
                    break
                else:
                    print("Please enter only a 1 (Yes) or 0 (No)")
                    continue
            #while True:
                ast_test = input("Migrate Automated Session Tests (AST)? : ")
                if ast_test=="1" or ast_test=="0":
                    break
                else:
                    print("Please enter only a 1 (Yes) or 0 (No)")
                    continue
            break
    elif (epa_tests_flag=="0"):
        break 
    else:
        print("Please enter only a 1 (Yes) or 0 (No)")
        continue      
print("\n======================================================================================================")        

#======================================================================================================#

#Fetch EA tests from the specified source AG from the source ORG

def fetch_ea_test_details():
    payload = {}
    headers = {
    'Content-Type': 'application/json',
    'Accept': 'application/json',
    'Authorization': 'Bearer ' + str(auth_bearer1)
    }
    fetch_tests_url = "https://api.thousandeyes.com/v6/tests.json" + "?aid=" + str(src_aid)
    fetch_tests_response = requests.request("GET", fetch_tests_url, headers=headers, data=payload)
    tests_data = json.loads(fetch_tests_response.text)

    if ea_tests_flag == "1":  
        for i in range(0,len(tests_data['test'])):
            fetch_ea_test_details.tname = tests_data['test'][i]['testName']
            if('description' in tests_data['test'][i]):
                fetch_ea_test_details.tdesc = tests_data['test'][i]['description']
            else:
                fetch_ea_test_details.tdesc = ""
            fetch_ea_test_details.talertsEnabled = tests_data['test'][i]['alertsEnabled']  

            if str(tests_data['test'][i]['type']) == 'bgp' and (int(tests_data['test'][i]['enabled']) == 1) and (int(bgp_flag) == 1 or int(all_ea_tests) == 1):    
                try:
                    #Required
                    logger.debug('Fetching Required parameters for bgp test')
                    fetch_ea_test_details.tprefix = tests_data['test'][i]['prefix']
                    #Optional
                    logger.debug('Fetching Optional parameters for bgp test')
                    fetch_ea_test_details.tincludeCoveredPrefixes = tests_data['test'][i]['includeCoveredPrefixes']
                    fetch_ea_test_details.tusePublicBgp = tests_data['test'][i]['usePublicBgp']
                    logger.info('About to create new bgp test')
                    create_bgp_test()
                except Exception as e:
                    print(e)
                    logger.error('Error migrating bgp test - ' +  str(e) + ' when creating \"' + str(fetch_ea_test_details.tname) + '\"')

            if str(tests_data['test'][i]['type']) == 'agent-to-server' and (int(tests_data['test'][i]['enabled']) == 1) and (int(ea_a2s_flag) == 1 or int(all_ea_tests) == 1):    
                try:
                    #Required
                    logger.debug('Fetching required parameters for agent-to-server test')  
                    fetch_ea_test_details.tinterval = tests_data['test'][i]['interval']
                    fetch_ea_test_details.tagents = "["
                    fetch_agent_details_url = "https://api.thousandeyes.com/v6/tests/" + str(tests_data['test'][i]['testId']) + ".json" + "?aid=" + str(src_aid)
                    fetch_agent_details_response = requests.request("GET", fetch_agent_details_url, headers=headers, data=payload)
                    test_data_agents = json.loads(fetch_agent_details_response.text)
                    for j in range(0,len(test_data_agents['test'][0]['agents'])):
                        if str(test_data_agents['test'][0]['agents'][j]['agentType']) == 'Cloud':
                            fetch_ea_test_details.tagents = fetch_ea_test_details.tagents + '{"agentId":' + str(test_data_agents['test'][0]['agents'][j]['agentId']) + '},'
                    fetch_ea_test_details.tagents = fetch_ea_test_details.tagents[:-1] + ']'
                    fetch_ea_test_details.tserver = tests_data['test'][i]['server']
                    if ":" in fetch_ea_test_details.tserver:
                        fetch_ea_test_details.tport = int(fetch_ea_test_details.tserver.split(":")[1])
                    else:
                        fetch_ea_test_details.tport = None
                    #Optional
                    logger.debug('Fetching optional parameters for agent-to-server test')
                    fetch_ea_test_details.tprotocol = tests_data['test'][i]['protocol']    
                    fetch_ea_test_details.tprobeMode = tests_data['test'][i]['probeMode']
                    fetch_ea_test_details.tpathTraceMode = tests_data['test'][i]['pathTraceMode']    
                    fetch_ea_test_details.tnetworkMeasurements = tests_data['test'][i]['networkMeasurements']
                    fetch_ea_test_details.tcontinuousMode = tests_data['test'][i]['continuousMode']
                    fetch_ea_test_details.tmtuMeasurements = tests_data['test'][i]['mtuMeasurements']
                    fetch_ea_test_details.tbgpMeasurements = tests_data['test'][i]['bgpMeasurements']
                    fetch_ea_test_details.tpingPayloadSize = tests_data['test'][i]['pingPayloadSize']
                    if('fixedPacketRate' in tests_data['test'][i]):
                        fetch_ea_test_details.tfixedPacketRate = tests_data['test'][i]['fixedPacketRate']
                    else:
                        fetch_ea_test_details.tfixedPacketRate = 0
                    fetch_ea_test_details.tnumPathTraces = tests_data['test'][i]['numPathTraces']
                    fetch_ea_test_details.tdscp = tests_data['test'][i]['dscp']
                    fetch_ea_test_details.tdscpId = tests_data['test'][i]['dscpId']
                    fetch_ea_test_details.tipv6Policy = tests_data['test'][i]['ipv6Policy']
                    logger.info('About to create new agent-to-server test')
                    create_a2s_test()
                except Exception as e:
                    logger.error('Error migrating agent-to-server test - ' +  str(e) + ' when creating \"' + str(fetch_ea_test_details.tname) + '\". Check if only enterprise agents assigned')

            if str(tests_data['test'][i]['type']) == 'agent-to-agent' and (int(tests_data['test'][i]['enabled']) == 1) and (int(a2a_flag) == 1 or int(all_ea_tests) == 1):    
                try:
                    #Required
                    logger.debug('Fetching required parameters for agent-to-agent test')  
                    fetch_ea_test_details.tinterval = tests_data['test'][i]['interval']
                    fetch_ea_test_details.tagents = "["
                    fetch_agent_details_url = "https://api.thousandeyes.com/v6/tests/" + str(tests_data['test'][i]['testId']) + ".json" + "?aid=" + str(src_aid)
                    fetch_agent_details_response = requests.request("GET", fetch_agent_details_url, headers=headers, data=payload)
                    test_data_agents = json.loads(fetch_agent_details_response.text)
                    for j in range(0,len(test_data_agents['test'][0]['agents'])):
                        if str(test_data_agents['test'][0]['agents'][j]['agentType']) == 'Cloud':
                            fetch_ea_test_details.tagents = fetch_ea_test_details.tagents + '{"agentId":' + str(test_data_agents['test'][0]['agents'][j]['agentId']) + '},'
                    fetch_ea_test_details.tagents = fetch_ea_test_details.tagents[:-1] + ']'
                    fetch_ea_test_details.ttargetAgentId = tests_data['test'][i]['targetAgentId']
                    #Optional
                    logger.debug('Fetching optional parameters for agent-to-agent test')
                    fetch_ea_test_details.tdirection = tests_data['test'][i]['direction']
                    fetch_ea_test_details.tprotocol = tests_data['test'][i]['protocol']
                    fetch_ea_test_details.tpathTraceMode = tests_data['test'][i]['pathTraceMode']    
                    fetch_ea_test_details.tport = tests_data['test'][i]['port']
                    if('mss' in tests_data['test'][i]):
                        fetch_ea_test_details.tmss = tests_data['test'][i]['mss']
                    else:
                        fetch_ea_test_details.tmss = 0
                    fetch_ea_test_details.tbgpMeasurements = tests_data['test'][i]['bgpMeasurements']
                    if('fixedPacketRate' in tests_data['test'][i]):
                        fetch_ea_test_details.tfixedPacketRate = tests_data['test'][i]['fixedPacketRate']
                    else:
                        fetch_ea_test_details.tfixedPacketRate = 0
                    fetch_ea_test_details.tnumPathTraces = tests_data['test'][i]['numPathTraces']
                    fetch_ea_test_details.tdscp = tests_data['test'][i]['dscp']
                    fetch_ea_test_details.tdscpId = tests_data['test'][i]['dscpId']
                    logger.info('About to create new agent-to-agent test')
                    create_a2a_test()
                except Exception as e:
                    logger.error('Error migrating agent-to-agent test - ' +  str(e) + ' when creating \"' + str(fetch_ea_test_details.tname) + '\"')

            if str(tests_data['test'][i]['type']) == 'dns-server' and (int(tests_data['test'][i]['enabled']) == 1) and (int(dns_server_flag) == 1 or int(all_ea_tests) == 1):    
                try:
                    #Required
                    logger.debug('Fetching required parameters for dnsserv test')  
                    fetch_ea_test_details.tinterval = tests_data['test'][i]['interval']
                    fetch_ea_test_details.tagents = "["
                    fetch_agent_details_url = "https://api.thousandeyes.com/v6/tests/" + str(tests_data['test'][i]['testId']) + ".json" + "?aid=" + str(src_aid)
                    fetch_agent_details_response = requests.request("GET", fetch_agent_details_url, headers=headers, data=payload)
                    test_data_agents = json.loads(fetch_agent_details_response.text)
                    for j in range(0,len(test_data_agents['test'][0]['agents'])):
                        if str(test_data_agents['test'][0]['agents'][j]['agentType']) == 'Cloud':
                            fetch_ea_test_details.tagents = fetch_ea_test_details.tagents + '{"agentId":' + str(test_data_agents['test'][0]['agents'][j]['agentId']) + '},'
                    fetch_ea_test_details.tagents = fetch_ea_test_details.tagents[:-1] + ']'
                    fetch_ea_test_details.tdomain = tests_data['test'][i]['domain']
                    fetch_ea_test_details.tdnsServers = tests_data['test'][i]['dnsServers']
                    #Optional
                    logger.debug('Fetching optional parameters for dnsserv test')
                    fetch_ea_test_details.tdnsQueryClass = tests_data['test'][i]['dnsQueryClass']
                    fetch_ea_test_details.tnetworkMeasurements = tests_data['test'][i]['networkMeasurements']
                    fetch_ea_test_details.tmtuMeasurements = tests_data['test'][i]['mtuMeasurements']
                    fetch_ea_test_details.tbgpMeasurements = tests_data['test'][i]['bgpMeasurements']
                    fetch_ea_test_details.tprobeMode = tests_data['test'][i]['probeMode']
                    fetch_ea_test_details.tpathTraceMode = tests_data['test'][i]['pathTraceMode']    
                    if('fixedPacketRate' in tests_data['test'][i]):
                        fetch_ea_test_details.tfixedPacketRate = tests_data['test'][i]['fixedPacketRate']
                    else:
                        fetch_ea_test_details.tfixedPacketRate = 0
                    fetch_ea_test_details.trecursiveQueries = tests_data['test'][i]['recursiveQueries']
                    if('numPathTraces' in tests_data['test'][i]):
                        fetch_ea_test_details.tnumPathTraces = tests_data['test'][i]['numPathTraces']
                    else:
                        fetch_ea_test_details.tnumPathTraces = 0            
                    fetch_ea_test_details.tipv6Policy = tests_data['test'][i]['ipv6Policy']
                    logger.info('About to create new dnsserv test')
                    create_dnsserv_test()
                except Exception as e:
                    logger.error('Error migrating dnsserv test - ' +  str(e) + ' when creating \"' + str(fetch_ea_test_details.tname) + '\"')
                    
            if str(tests_data['test'][i]['type']) == 'dns-trace' and (int(tests_data['test'][i]['enabled']) == 1) and (int(dns_trace_flag) == 1 or int(all_ea_tests) == 1):    
                try:
                    #Required
                    logger.debug('Fetching required parameters for dns-trace test')  
                    fetch_ea_test_details.tinterval = tests_data['test'][i]['interval']
                    fetch_ea_test_details.tagents = "["
                    fetch_agent_details_url = "https://api.thousandeyes.com/v6/tests/" + str(tests_data['test'][i]['testId']) + ".json" + "?aid=" + str(src_aid)
                    fetch_agent_details_response = requests.request("GET", fetch_agent_details_url, headers=headers, data=payload)
                    test_data_agents = json.loads(fetch_agent_details_response.text)
                    for j in range(0,len(test_data_agents['test'][0]['agents'])):
                        if str(test_data_agents['test'][0]['agents'][j]['agentType']) == 'Cloud':
                            fetch_ea_test_details.tagents = fetch_ea_test_details.tagents + '{"agentId":' + str(test_data_agents['test'][0]['agents'][j]['agentId']) + '},'
                    fetch_ea_test_details.tagents = fetch_ea_test_details.tagents[:-1] + ']'
                    fetch_ea_test_details.tdomain = tests_data['test'][i]['domain']
                    #Optional
                    logger.debug('Fetching optional parameters for dns-trace test')
                    fetch_ea_test_details.tdnsTransportProtocol = tests_data['test'][i]['dnsTransportProtocol']
                    logger.info('About to create new dnstrace test')
                    create_dnstrace_test()
                except Exception as e:
                    logger.error('Error migrating dns trace test - ' +  str(e) + ' when creating \"' + str(fetch_ea_test_details.tname) + '\"')
            
            if str(tests_data['test'][i]['type']) == 'dns-dnssec' and (int(tests_data['test'][i]['enabled']) == 1) and (int(dnssec_flag) == 1 or int(all_ea_tests) == 1):        
                try:
                    #Required
                    logger.debug('Fetching required parameters for dnssec test')  
                    fetch_ea_test_details.tinterval = tests_data['test'][i]['interval']
                    fetch_ea_test_details.tagents = "["
                    fetch_agent_details_url = "https://api.thousandeyes.com/v6/tests/" + str(tests_data['test'][i]['testId']) + ".json" + "?aid=" + str(src_aid)
                    fetch_agent_details_response = requests.request("GET", fetch_agent_details_url, headers=headers, data=payload)
                    test_data_agents = json.loads(fetch_agent_details_response.text)
                    for j in range(0,len(test_data_agents['test'][0]['agents'])):
                        if str(test_data_agents['test'][0]['agents'][j]['agentType']) == 'Cloud':
                            fetch_ea_test_details.tagents = fetch_ea_test_details.tagents + '{"agentId":' + str(test_data_agents['test'][0]['agents'][j]['agentId']) + '},'
                    fetch_ea_test_details.tagents = fetch_ea_test_details.tagents[:-1] + ']'
                    fetch_ea_test_details.tdomain = tests_data['test'][i]['domain']
                    #Optional
                    logger.info('About to create new dnssec test')
                    create_dnssec_test()
                except Exception as e:
                    logger.error('Error migrating dnssec test - ' +  str(e) + ' when creating \"' + str(fetch_ea_test_details.tname) + '\"')
                    
            if str(tests_data['test'][i]['type']) == 'http-server' and (int(tests_data['test'][i]['enabled']) == 1) and (int(ea_http_server_flag) == 1 or int(all_ea_tests) == 1):
                try:
                    #Required
                    logger.debug('Fetching required parameters for http-server test')  
                    fetch_ea_test_details.tinterval = tests_data['test'][i]['interval']
                    fetch_ea_test_details.tagents = "["
                    fetch_agent_details_url = "https://api.thousandeyes.com/v6/tests/" + str(tests_data['test'][i]['testId']) + ".json" + "?aid=" + str(src_aid)
                    fetch_agent_details_response = requests.request("GET", fetch_agent_details_url, headers=headers, data=payload)
                    test_data_agents = json.loads(fetch_agent_details_response.text)
                    for j in range(0,len(test_data_agents['test'][0]['agents'])):
                        if str(test_data_agents['test'][0]['agents'][j]['agentType']) == 'Cloud':
                            fetch_ea_test_details.tagents = fetch_ea_test_details.tagents + '{"agentId":' + str(test_data_agents['test'][0]['agents'][j]['agentId']) + '},'
                    fetch_ea_test_details.tagents = fetch_ea_test_details.tagents[:-1] + ']'
                    fetch_ea_test_details.turl = tests_data['test'][i]['url']
                    #Optional
                    logger.debug('Fetching optional parameters for http-server test')
                    fetch_ea_test_details.thttpTimeLimit = tests_data['test'][i]['httpTimeLimit']
                    fetch_ea_test_details.thttpTargetTime = tests_data['test'][i]['httpTargetTime']
                    fetch_ea_test_details.tnetworkMeasurements = tests_data['test'][i]['networkMeasurements']
                    fetch_ea_test_details.tmtuMeasurements = tests_data['test'][i]['mtuMeasurements']
                    fetch_ea_test_details.tbgpMeasurements = tests_data['test'][i]['bgpMeasurements']
                    fetch_ea_test_details.tprotocol = tests_data['test'][i]['protocol']
                    fetch_ea_test_details.tprobeMode = tests_data['test'][i]['probeMode']
                    fetch_ea_test_details.tpathTraceMode = tests_data['test'][i]['pathTraceMode']    
                    if('fixedPacketRate' in tests_data['test'][i]):
                        fetch_ea_test_details.tfixedPacketRate = tests_data['test'][i]['fixedPacketRate']
                    else:
                        fetch_ea_test_details.tfixedPacketRate = 0
                    if('numPathTraces' in tests_data['test'][i]):
                        fetch_ea_test_details.tnumPathTraces = tests_data['test'][i]['numPathTraces']
                    else:
                        fetch_ea_test_details.tnumPathTraces = 0
                    fetch_ea_test_details.tipv6Policy = tests_data['test'][i]['ipv6Policy']
                    fetch_ea_test_details.tsslVersionId = tests_data['test'][i]['sslVersionId']
                    fetch_ea_test_details.tsslVersion = tests_data['test'][i]['sslVersion']
                    fetch_ea_test_details.tverifyCertificate = tests_data['test'][i]['verifyCertificate']
                    if('clientCertificate' in tests_data['test'][i]):
                        fetch_ea_test_details.tclientCertificate = tests_data['test'][i]['clientCertificate']
                    else:
                        fetch_ea_test_details.tclientCertificate = 0
                    fetch_ea_test_details.tauthType = tests_data['test'][i]['authType']
                    fetch_ea_test_details.tuseNtlm = tests_data['test'][i]['useNtlm']
                    if('username' in tests_data['test'][i]):
                        fetch_ea_test_details.tusername = tests_data['test'][i]['username']
                        fetch_ea_test_details.tpassword = input("Enter the password for HTTP server - " + str(fetch_ea_test_details.turl) + ", with username - " + str(fetch_ea_test_details.tusername) + " : ")
                    else:
                        fetch_ea_test_details.tusername = 0
                    fetch_ea_test_details.thttpVersion = tests_data['test'][i]['httpVersion']
                    if('postBody' in tests_data['test'][i]):
                        fetch_ea_test_details.tpostBody = tests_data['test'][i]['postBody']
                    else:
                        fetch_ea_test_details.tpostBody = 0
                    fetch_ea_test_details.tfollowRedirects = tests_data['test'][i]['followRedirects']
                    if('userAgent' in tests_data['test'][i]):
                        fetch_ea_test_details.tuserAgent = tests_data['test'][i]['userAgent']
                    else:
                        fetch_ea_test_details.tuserAgent = 0
                    if('dnsOverride' in tests_data['test'][i]):
                        fetch_ea_test_details.tdnsOverride = tests_data['test'][i]['dnsOverride']
                    else:
                        fetch_ea_test_details.tdnsOverride = 0
                    if('desiredStatusCode' in tests_data['test'][i]):
                        fetch_ea_test_details.tdesiredStatusCode = tests_data['test'][i]['desiredStatusCode']
                    else:
                        fetch_ea_test_details.tdesiredStatusCode = 0
                    if('downloadLimit' in tests_data['test'][i]):
                        fetch_ea_test_details.tdownloadLimit = tests_data['test'][i]['downloadLimit']
                    else:
                        fetch_ea_test_details.tdownloadLimit = 0
                    fetch_ea_test_details.tcontentRegex = tests_data['test'][i]['contentRegex']
                    logger.info('About to create new http server test')
                    create_http_test()
                except Exception as e:
                    logger.error('Error migrating http server test - ' +  str(e) + ' when creating \"' + str(fetch_ea_test_details.tname) + '\"')

            if str(tests_data['test'][i]['type']) == 'page-load' and (int(tests_data['test'][i]['enabled']) == 1) and (int(page_load_flag) == 1 or int(all_ea_tests) == 1):
                try:
                    #Required  
                    logger.debug('Fetching required parameters for page-load test')
                    fetch_ea_test_details.tinterval = tests_data['test'][i]['interval']
                    fetch_ea_test_details.tagents = "["
                    fetch_agent_details_url = "https://api.thousandeyes.com/v6/tests/" + str(tests_data['test'][i]['testId']) + ".json" + "?aid=" + str(src_aid)
                    fetch_agent_details_response = requests.request("GET", fetch_agent_details_url, headers=headers, data=payload)
                    test_data_agents = json.loads(fetch_agent_details_response.text)
                    for j in range(0,len(test_data_agents['test'][0]['agents'])):
                        if str(test_data_agents['test'][0]['agents'][j]['agentType']) == 'Cloud':
                            fetch_ea_test_details.tagents = fetch_ea_test_details.tagents + '{"agentId":' + str(test_data_agents['test'][0]['agents'][j]['agentId']) + '},'
                    fetch_ea_test_details.tagents = fetch_ea_test_details.tagents[:-1] + ']'
                    fetch_ea_test_details.turl = tests_data['test'][i]['url']
                    fetch_ea_test_details.thttpInterval = tests_data['test'][i]['httpInterval']
                    #Optional
                    logger.debug('Fetching optional parameters for page-load test')
                    fetch_ea_test_details.tinterval = tests_data['test'][i]['interval']
                    if('subinterval' in tests_data['test'][i]):
                        fetch_ea_test_details.tsubinterval = tests_data['test'][i]['subinterval']
                    else:
                        fetch_ea_test_details.tsubinterval = 0
                    fetch_ea_test_details.thttpTimeLimit = tests_data['test'][i]['httpTimeLimit']
                    fetch_ea_test_details.thttpTargetTime = tests_data['test'][i]['httpTargetTime']
                    fetch_ea_test_details.tpageLoadTimeLimit = tests_data['test'][i]['pageLoadTimeLimit']
                    fetch_ea_test_details.tpageLoadTargetTime = tests_data['test'][i]['pageLoadTargetTime']
                    fetch_ea_test_details.tnetworkMeasurements = tests_data['test'][i]['networkMeasurements']
                    fetch_ea_test_details.tmtuMeasurements = tests_data['test'][i]['mtuMeasurements']
                    fetch_ea_test_details.tbgpMeasurements = tests_data['test'][i]['bgpMeasurements']
                    fetch_ea_test_details.tprotocol = tests_data['test'][i]['protocol']
                    fetch_ea_test_details.tprobeMode = tests_data['test'][i]['probeMode']
                    fetch_ea_test_details.tpathTraceMode = tests_data['test'][i]['pathTraceMode']    
                    if('fixedPacketRate' in tests_data['test'][i]):
                        fetch_ea_test_details.tfixedPacketRate = tests_data['test'][i]['fixedPacketRate']
                    else:
                        fetch_ea_test_details.tfixedPacketRate = 0
                    if('numPathTraces' in tests_data['test'][i]):
                        fetch_ea_test_details.tnumPathTraces = tests_data['test'][i]['numPathTraces']
                    else:
                        fetch_ea_test_details.tnumPathTraces = 0
                    fetch_ea_test_details.tsslVersionId = tests_data['test'][i]['sslVersionId']
                    fetch_ea_test_details.tsslVersion = tests_data['test'][i]['sslVersion']
                    fetch_ea_test_details.tverifyCertificate = tests_data['test'][i]['verifyCertificate']
                    fetch_ea_test_details.tauthType = tests_data['test'][i]['authType']
                    fetch_ea_test_details.tuseNtlm = tests_data['test'][i]['useNtlm']
                    if('username' in tests_data['test'][i]):
                        fetch_ea_test_details.tusername = tests_data['test'][i]['username']
                        fetch_ea_test_details.tpassword = input("Enter the password for Page Load test (HTTP auth) - " + str(fetch_ea_test_details.turl) + ", with username - " + str(fetch_ea_test_details.tusername) + " : ")
                    else:
                        fetch_ea_test_details.tusername = 0
                    fetch_ea_test_details.thttpVersion = tests_data['test'][i]['httpVersion']
                    fetch_ea_test_details.tfollowRedirects = tests_data['test'][i]['followRedirects']
                    if('userAgent' in tests_data['test'][i]):
                        fetch_ea_test_details.tuserAgent = tests_data['test'][i]['userAgent']
                    else:
                        fetch_ea_test_details.tuserAgent = 0
                    fetch_ea_test_details.tidentifyAgentTrafficWithUserAgent = tests_data['test'][i]['identifyAgentTrafficWithUserAgent']
                    if('desiredStatusCode' in tests_data['test'][i]):
                        fetch_ea_test_details.tdesiredStatusCode = tests_data['test'][i]['desiredStatusCode']
                    else:
                        fetch_ea_test_details.tdesiredStatusCode = 0
                    fetch_ea_test_details.tcontentRegex = tests_data['test'][i]['contentRegex']
                    fetch_ea_test_details.tincludeHeaders = tests_data['test'][i]['includeHeaders']
                    logger.info('About to create new pageload test')
                    create_page_test()
                    
                except Exception as e:
                    logger.error('Error migrating pageload test - ' +  str(e) + ' when creating \"' + str(fetch_ea_test_details.tname) + '\"')
            
            if str(tests_data['test'][i]['type']) == 'web-transactions' and (int(tests_data['test'][i]['enabled']) == 1) and (int(web_transaction_flag) == 1 or int(all_ea_tests) == 1):
                try:
                    #Required
                    logger.debug('Fetching required parameters for transaction test')  
                    fetch_ea_test_details.tinterval = tests_data['test'][i]['interval']
                    fetch_ea_test_details.tagents = "["
                    fetch_agent_details_url = "https://api.thousandeyes.com/v6/tests/" + str(tests_data['test'][i]['testId']) + ".json" + "?aid=" + str(src_aid)
                    fetch_agent_details_response = requests.request("GET", fetch_agent_details_url, headers=headers, data=payload)
                    test_data_agents = json.loads(fetch_agent_details_response.text)
                    for j in range(0,len(test_data_agents['test'][0]['agents'])):
                        if str(test_data_agents['test'][0]['agents'][j]['agentType']) == 'Cloud':
                            fetch_ea_test_details.tagents = fetch_ea_test_details.tagents + '{"agentId":' + str(test_data_agents['test'][0]['agents'][j]['agentId']) + '},'
                    fetch_ea_test_details.tagents = fetch_ea_test_details.tagents[:-1] + ']'
                    fetch_ea_test_details.turl = tests_data['test'][i]['url']
                    fetch_ea_test_details.ttransactionScript = tests_data['test'][i]['transactionScript']
                    #Optional
                    logger.debug('Fetching optional parameters for transaction test')
                    if('subinterval' in tests_data['test'][i]):
                        fetch_ea_test_details.tsubinterval = tests_data['test'][i]['subinterval']
                    else:
                        fetch_ea_test_details.tsubinterval = 0
                    fetch_ea_test_details.ttimeLimit = tests_data['test'][i]['timeLimit']
                    fetch_ea_test_details.ttargetTime = tests_data['test'][i]['targetTime']
                    fetch_ea_test_details.thttpTimeLimit = tests_data['test'][i]['httpTimeLimit']
                    fetch_ea_test_details.thttpTargetTime = tests_data['test'][i]['httpTargetTime']
                    fetch_ea_test_details.tnetworkMeasurements = tests_data['test'][i]['networkMeasurements']
                    fetch_ea_test_details.tmtuMeasurements = tests_data['test'][i]['mtuMeasurements']
                    fetch_ea_test_details.tbgpMeasurements = tests_data['test'][i]['bgpMeasurements']
                    fetch_ea_test_details.tprotocol = tests_data['test'][i]['protocol']
                    fetch_ea_test_details.tprobeMode = tests_data['test'][i]['probeMode']
                    fetch_ea_test_details.tpathTraceMode = tests_data['test'][i]['pathTraceMode']    
                    if('fixedPacketRate' in tests_data['test'][i]):
                        fetch_ea_test_details.tfixedPacketRate = tests_data['test'][i]['fixedPacketRate']
                    else:
                        fetch_ea_test_details.tfixedPacketRate = 0
                    if('numPathTraces' in tests_data['test'][i]):
                        fetch_ea_test_details.tnumPathTraces = tests_data['test'][i]['numPathTraces']
                    else:
                        fetch_ea_test_details.tnumPathTraces = 0
                    fetch_ea_test_details.tsslVersionId = tests_data['test'][i]['sslVersionId']
                    fetch_ea_test_details.tsslVersion = tests_data['test'][i]['sslVersion']
                    fetch_ea_test_details.tverifyCertificate = tests_data['test'][i]['verifyCertificate']
                    fetch_ea_test_details.tauthType = tests_data['test'][i]['authType']
                    fetch_ea_test_details.tuseNtlm = tests_data['test'][i]['useNtlm']
                    if('username' in tests_data['test'][i]):
                        fetch_ea_test_details.tusername = tests_data['test'][i]['username']
                        fetch_ea_test_details.tpassword = input("Enter the password for Page Load test (HTTP auth) - " + str(fetch_ea_test_details.turl) + ", with username - " + str(fetch_ea_test_details.tusername) + " : ")
                    else:
                        fetch_ea_test_details.tusername = 0
                    fetch_ea_test_details.thttpVersion = tests_data['test'][i]['httpVersion']
                    fetch_ea_test_details.tfollowRedirects = tests_data['test'][i]['followRedirects']
                    if('userAgent' in tests_data['test'][i]):
                        fetch_ea_test_details.tuserAgent = tests_data['test'][i]['userAgent']
                    else:
                        fetch_ea_test_details.tuserAgent = 0
                    fetch_ea_test_details.tidentifyAgentTrafficWithUserAgent = tests_data['test'][i]['identifyAgentTrafficWithUserAgent']
                    if('desiredStatusCode' in tests_data['test'][i]):
                        fetch_ea_test_details.tdesiredStatusCode = tests_data['test'][i]['desiredStatusCode']
                    else:
                        fetch_ea_test_details.tdesiredStatusCode = 0
                    fetch_ea_test_details.tcontentRegex = tests_data['test'][i]['contentRegex']
                    fetch_ea_test_details.tincludeHeaders = tests_data['test'][i]['includeHeaders']
                    logger.info('About to create new transaction test')
                    create_transaction_test()
                except Exception as e:
                    logger.error('Error migrating transaction test - ' +  str(e) + ' when creating \"' + str(fetch_ea_test_details.tname) + '\"')

            if str(tests_data['test'][i]['type']) == 'ftp-server' and (int(tests_data['test'][i]['enabled']) == 1) and (int(ftp_flag) == 1 or int(all_ea_tests) == 1):
                try:
                    #Required    
                    logger.debug('Fetching required parameters for ftp test')
                    fetch_ea_test_details.tinterval = tests_data['test'][i]['interval']
                    fetch_ea_test_details.tagents = "["
                    fetch_agent_details_url = "https://api.thousandeyes.com/v6/tests/" + str(tests_data['test'][i]['testId']) + ".json" + "?aid=" + str(src_aid)
                    fetch_agent_details_response = requests.request("GET", fetch_agent_details_url, headers=headers, data=payload)
                    test_data_agents = json.loads(fetch_agent_details_response.text)
                    for j in range(0,len(test_data_agents['test'][0]['agents'])):
                        if str(test_data_agents['test'][0]['agents'][j]['agentType']) == 'Cloud':
                            fetch_ea_test_details.tagents = fetch_ea_test_details.tagents + '{"agentId":' + str(test_data_agents['test'][0]['agents'][j]['agentId']) + '},'
                    fetch_ea_test_details.tagents = fetch_ea_test_details.tagents[:-1] + ']'
                    fetch_ea_test_details.turl = tests_data['test'][i]['url']
                    fetch_ea_test_details.trequestType = tests_data['test'][i]['requestType']
                    fetch_ea_test_details.tusername = tests_data['test'][i]['username']
                    #Optional
                    logger.debug('Fetching optional parameters for ftp test')
                    if('downloadLimit' in tests_data['test'][i]):
                        fetch_ea_test_details.tdownloadLimit = tests_data['test'][i]['downloadLimit']
                    else:
                        fetch_ea_test_details.tdownloadLimit = 0  
                    if('uploadFileSize' in tests_data['test'][i]):
                        fetch_ea_test_details.tuploadFileSize = tests_data['test'][i]['uploadFileSize']
                    else:
                        fetch_ea_test_details.tuploadFileSize = 0
                    if('contentRegex' in tests_data['test'][i]):
                        fetch_ea_test_details.tcontentRegex = tests_data['test'][i]['contentRegex']
                    else:
                        fetch_ea_test_details.tcontentRegex = 0           
                    fetch_ea_test_details.tftpTimeLimit = tests_data['test'][i]['ftpTimeLimit']
                    fetch_ea_test_details.tftpTargetTime = tests_data['test'][i]['ftpTargetTime']
                    fetch_ea_test_details.tnetworkMeasurements = tests_data['test'][i]['networkMeasurements']
                    fetch_ea_test_details.tmtuMeasurements = tests_data['test'][i]['mtuMeasurements']
                    fetch_ea_test_details.tbgpMeasurements = tests_data['test'][i]['bgpMeasurements']
                    fetch_ea_test_details.tprotocol = tests_data['test'][i]['protocol']
                    fetch_ea_test_details.tprobeMode = tests_data['test'][i]['probeMode']
                    fetch_ea_test_details.tpathTraceMode = tests_data['test'][i]['pathTraceMode']    
                    if('fixedPacketRate' in tests_data['test'][i]):
                        fetch_ea_test_details.tfixedPacketRate = tests_data['test'][i]['fixedPacketRate']
                    else:
                        fetch_ea_test_details.tfixedPacketRate = 0
                    if('numPathTraces' in tests_data['test'][i]):
                        fetch_ea_test_details.tnumPathTraces = tests_data['test'][i]['numPathTraces']
                    else:
                        fetch_ea_test_details.tnumPathTraces = 0
                    if('useActiveFtp' in tests_data['test'][i]):
                        fetch_ea_test_details.tuseActiveFtp = tests_data['test'][i]['useActiveFtp']
                    else:
                        fetch_ea_test_details.tuseActiveFtp = 0
                    if('useExplicitFtps' in tests_data['test'][i]):
                        fetch_ea_test_details.tuseExplicitFtps = tests_data['test'][i]['useExplicitFtps']
                    else:
                        fetch_ea_test_details.tuseExplicitFtps = 0
                    if('desiredReplyCode' in tests_data['test'][i]):
                        fetch_ea_test_details.tdesiredReplyCode = tests_data['test'][i]['desiredReplyCode']
                    else:
                        fetch_ea_test_details.tdesiredReplyCode = 0
                    fetch_ea_test_details.tipv6Policy = tests_data['test'][i]['ipv6Policy']
                    logger.info('About to create new ftp test')
                    create_ftp_test()
                except Exception as e:
                    logger.error('Error migrating ftp test - ' +  str(e) + ' when creating \"' + str(fetch_ea_test_details.tname) + '\"')

            if str(tests_data['test'][i]['type']) == 'sip-server' and (int(tests_data['test'][i]['enabled']) == 1) and (int(sip_server_flag) == 1 or int(all_ea_tests) == 1):
                try:
                    #Required    
                    logger.debug('Fetching Required parameters for sip test')
                    fetch_ea_test_details.tinterval = tests_data['test'][i]['interval']
                    fetch_ea_test_details.tagents = "["
                    fetch_agent_details_url = "https://api.thousandeyes.com/v6/tests/" + str(tests_data['test'][i]['testId']) + ".json" + "?aid=" + str(src_aid)
                    fetch_agent_details_response = requests.request("GET", fetch_agent_details_url, headers=headers, data=payload)
                    test_data_agents = json.loads(fetch_agent_details_response.text)
                    for j in range(0,len(test_data_agents['test'][0]['agents'])):
                        if str(test_data_agents['test'][0]['agents'][j]['agentType']) == 'Cloud':
                            fetch_ea_test_details.tagents = fetch_ea_test_details.tagents + '{"agentId":' + str(test_data_agents['test'][0]['agents'][j]['agentId']) + '},'
                    fetch_ea_test_details.tagents = fetch_ea_test_details.tagents[:-1] + ']'
                    fetch_ea_test_details.tsipRegistrar = tests_data['test'][i]['sipRegistrar']
                    fetch_ea_test_details.tport = tests_data['test'][i]['port']
                    fetch_ea_test_details.tprotocol = tests_data['test'][i]['protocol']
                    #Optional
                    fetch_ea_test_details.tprobeMode = tests_data['test'][i]['probeMode']
                    fetch_ea_test_details.tpathTraceMode = tests_data['test'][i]['pathTraceMode']
                    fetch_ea_test_details.tsipProxy = tests_data['test'][i]['sipProxy']
                    fetch_ea_test_details.tsipTimeLimit = tests_data['test'][i]['sipTimeLimit']  
                    fetch_ea_test_details.tsipTargetTime = tests_data['test'][i]['sipTargetTime']  
                    fetch_ea_test_details.tnetworkMeasurements = tests_data['test'][i]['networkMeasurements']
                    fetch_ea_test_details.tmtuMeasurements = tests_data['test'][i]['mtuMeasurements']
                    fetch_ea_test_details.tbgpMeasurements = tests_data['test'][i]['bgpMeasurements']
                    if('fixedPacketRate' in tests_data['test'][i]):
                        fetch_ea_test_details.tfixedPacketRate = tests_data['test'][i]['fixedPacketRate']
                    else:
                        fetch_ea_test_details.tfixedPacketRate = 0
                    if('numPathTraces' in tests_data['test'][i]):
                        fetch_ea_test_details.tnumPathTraces = tests_data['test'][i]['numPathTraces']
                    else:
                        fetch_ea_test_details.tnumPathTraces = 0
                    fetch_ea_test_details.tregisterEnabled = tests_data['test'][i]['registerEnabled']
                    if('user' in tests_data['test'][i]):
                        fetch_ea_test_details.tuser = tests_data['test'][i]['user']
                        fetch_ea_test_details.tpassword = input("Enter the password for SIP server - " + str(fetch_ea_test_details.tsipRegistrar) + ", with username - " + str(fetch_ea_test_details.tuser) + " : ")
                    else:
                        fetch_ea_test_details.tuser = 0
                    if('authUser' in tests_data['test'][i]):
                        fetch_ea_test_details.tauthUser = tests_data['test'][i]['authUser']
                    else:
                        fetch_ea_test_details.tauthUser = 0  
                    if('optionsRegex' in tests_data['test'][i]):
                        fetch_ea_test_details.toptionsRegex = tests_data['test'][i]['optionsRegex']
                    else:
                        fetch_ea_test_details.toptionsRegex = 0
                    fetch_ea_test_details.tipv6Policy = tests_data['test'][i]['ipv6Policy']                               
                    logger.debug('Fetching optional parameters for sip test')
                    logger.info('About to create new sip test')
                    create_sip_test()
                except Exception as e:
                    logger.error('Error migrating sip test - ' +  str(e) + ' when creating \"' + str(fetch_ea_test_details.tname) + '\"')

            if str(tests_data['test'][i]['type']) == 'voice' and (int(tests_data['test'][i]['enabled']) == 1) and (int(rtp_server_flag) == 1 or int(all_ea_tests) == 1):
                try:
                    #Required
                    logger.debug('Fetching required parameters for voice test')    
                    fetch_ea_test_details.tinterval = tests_data['test'][i]['interval']
                    fetch_ea_test_details.tagents = "["
                    fetch_agent_details_url = "https://api.thousandeyes.com/v6/tests/" + str(tests_data['test'][i]['testId']) + ".json" + "?aid=" + str(src_aid)
                    fetch_agent_details_response = requests.request("GET", fetch_agent_details_url, headers=headers, data=payload)
                    test_data_agents = json.loads(fetch_agent_details_response.text)
                    for j in range(0,len(test_data_agents['test'][0]['agents'])):
                        if str(test_data_agents['test'][0]['agents'][j]['agentType']) == 'Cloud':
                            fetch_ea_test_details.tagents = fetch_ea_test_details.tagents + '{"agentId":' + str(test_data_agents['test'][0]['agents'][j]['agentId']) + '},'
                    fetch_ea_test_details.tagents = fetch_ea_test_details.tagents[:-1] + ']'
                    fetch_ea_test_details.ttargetAgentId = tests_data['test'][i]['targetAgentId']
                    #Optional
                    logger.debug('Fetching optional parameters for voice test')
                    fetch_ea_test_details.tserver = tests_data['test'][i]['server']
                    fetch_ea_test_details.tcodec = tests_data['test'][i]['codec']
                    fetch_ea_test_details.tcodecId = tests_data['test'][i]['codecId']
                    fetch_ea_test_details.tduration = tests_data['test'][i]['duration']
                    fetch_ea_test_details.tjitterBuffer = tests_data['test'][i]['jitterBuffer']
                    fetch_ea_test_details.tbgpMeasurements = tests_data['test'][i]['bgpMeasurements']
                    fetch_ea_test_details.tcodecId = tests_data['test'][i]['codecId']
                    fetch_ea_test_details.tnumPathTraces = tests_data['test'][i]['numPathTraces']
                    fetch_ea_test_details.tdscp = tests_data['test'][i]['dscp']
                    fetch_ea_test_details.tdscpId = tests_data['test'][i]['dscpId']
                    logger.info('About to create new voice test')
                    create_rtp_test()
                except Exception as e:
                    logger.error('Error migrating voice test - ' +  str(e) + ' when creating \"' + str(fetch_ea_test_details.tname) + '\"')
    else:
        print("No EA Test selected for Migration")
#======================================================================================================#

#Create tests to the specified destination AG from the destination ORG

def create_bgp_test():
    headers = {
    'Content-Type': 'application/json',
    'Accept': 'application/json',
    'Authorization': 'Bearer ' + str(auth_bearer2)
    }
    payload = json.dumps({
    "testName": str(fetch_ea_test_details.tname),
    "description": str(fetch_ea_test_details.tdesc),
    "alertsEnabled": str(fetch_ea_test_details.talertsEnabled),
    "prefix": str(fetch_ea_test_details.tprefix),
    "includeCoveredPrefixes": int(fetch_ea_test_details.tincludeCoveredPrefixes),
    "usePublicBgp": int(fetch_ea_test_details.tusePublicBgp)
    })

    create_tests_url = "https://api.thousandeyes.com/v6/tests/" + 'bgp' + "/new.json" + "?aid=" + str(dst_aid)
    logger.info('Creating bgp test - '+ str(fetch_ea_test_details.tname))
    response = requests.request("POST", create_tests_url, headers=headers, data=payload)
    logger.debug('BGP test named \"'+ str(fetch_ea_test_details.tname) + '\" create request sent')

    if response.status_code != 201:
        print(response.text)
        logger.error('Exited with error code : '+ str(response.status_code) + ' when creating \"' + str(fetch_ea_test_details.tname) + '\"'+ '; Error Message : ' + str(response.text))
    else:
        logger.info('Test \"' + str(fetch_ea_test_details.tname) + '\" has been created')
        print("BGP Test created")

def create_a2s_test():
    headers = {
    'Content-Type': 'application/json',
    'Accept': 'application/json',
    'Authorization': 'Bearer ' + str(auth_bearer2)
    }
    payload = json.dumps({
    "testName": str(fetch_ea_test_details.tname),
    "description": str(fetch_ea_test_details.tdesc),
    "alertsEnabled": str(fetch_ea_test_details.talertsEnabled),
    "interval": int(fetch_ea_test_details.tinterval),
    "agents": json.loads(fetch_ea_test_details.tagents),
    "server": str(fetch_ea_test_details.tserver.split(":")[0]),
    "port": fetch_ea_test_details.tport,
    "protocol": str(fetch_ea_test_details.tprotocol),
    "probeMode": str(fetch_ea_test_details.tprobeMode),
    "pingPayloadSize": int(fetch_ea_test_details.tpingPayloadSize),
    "pathTraceMode": str(fetch_ea_test_details.tpathTraceMode),
    "continuousMode": int(fetch_ea_test_details.tcontinuousMode),
    "networkMeasurements": int(fetch_ea_test_details.tnetworkMeasurements),
    "bandwidthMeasurements": 0,
    "mtuMeasurements": str(fetch_ea_test_details.tmtuMeasurements),
    "bgpMeasurements": str(fetch_ea_test_details.tbgpMeasurements),
    "numPathTraces":int(fetch_ea_test_details.tnumPathTraces), 
    "dscp": str(fetch_ea_test_details.tdscp),
    "dscpId": str(fetch_ea_test_details.tdscpId),
    "ipv6Policy": str(fetch_ea_test_details.tipv6Policy)
    })
    if fetch_ea_test_details.tfixedPacketRate!= 0:
        payload = payload[:-1]
        payload = payload + ', ' + "\"fixedPacketRate\":" + str(fetch_ea_test_details.tfixedPacketRate) + "}"
    else:
        pass
    create_tests_url = "https://api.thousandeyes.com/v6/tests/" + 'agent-to-server' + "/new.json" + "?aid=" + str(dst_aid)
    logger.info('Creating agent-to-server test - '+ str(fetch_ea_test_details.tname))
    response = requests.request("POST", create_tests_url, headers=headers, data=payload)
    logger.debug('Agent-to-server test named \"'+ str(fetch_ea_test_details.tname) + '\" create request sent')

    if response.status_code != 201:
        logger.error('Exited with error code : '+ str(response.status_code) + ' when creating \"' + str(fetch_ea_test_details.tname) + '\"'+ '; Error Message : ' + str(response.text))
    else:
        logger.info('Test \"' + str(fetch_ea_test_details.tname) + '\" has been created')
        print("A2S Test created")
        
def create_a2a_test():
    headers = {
    'Content-Type': 'application/json',
    'Accept': 'application/json',
    'Authorization': 'Bearer ' + str(auth_bearer2)
    }
    payload = json.dumps({
    "testName": str(fetch_ea_test_details.tname),
    "description": str(fetch_ea_test_details.tdesc),
    "alertsEnabled": str(fetch_ea_test_details.talertsEnabled),
    "interval": int(fetch_ea_test_details.tinterval),
    "agents": json.loads(fetch_ea_test_details.tagents),
    "targetAgentId":  str(fetch_ea_test_details.ttargetAgentId),
    "direction":  str(fetch_ea_test_details.tdirection),
    "protocol": str(fetch_ea_test_details.tprotocol),
    "pathTraceMode": str(fetch_ea_test_details.tpathTraceMode),
    "port": fetch_ea_test_details.tport,
    "bgpMeasurements": str(fetch_ea_test_details.tbgpMeasurements),
    "bandwidthMeasurements": 0,
    "numPathTraces":int(fetch_ea_test_details.tnumPathTraces), 
    "dscp": str(fetch_ea_test_details.tdscp),
    "dscpId": str(fetch_ea_test_details.tdscpId),
    })
    if fetch_ea_test_details.tfixedPacketRate!= 0:
        payload = payload[:-1]
        payload = payload + ', ' + "\"fixedPacketRate\":" + str(fetch_ea_test_details.tfixedPacketRate) + "}"
    else:
        pass
    if fetch_ea_test_details.tmss!= 0:
        payload = payload[:-1]
        payload = payload + ', ' + "\"mss\":" + str(fetch_ea_test_details.tmss) + "}"
    else:
        pass
    create_tests_url = "https://api.thousandeyes.com/v6/tests/" + 'agent-to-agent' + "/new.json" + "?aid=" + str(dst_aid)
    logger.info('Creating agent-to-agent test - '+ str(fetch_ea_test_details.tname))
    response = requests.request("POST", create_tests_url, headers=headers, data=payload)
    logger.debug('Agent-to-agent test named \"'+ str(fetch_ea_test_details.tname) + '\" create request sent')

    if response.status_code != 201:
        logger.error('Exited with error code : '+ str(response.status_code) + ' when creating \"' + str(fetch_ea_test_details.tname) + '\"'+ '; Error Message : ' + str(response.text))
    else:
        logger.info('Test \"' + str(fetch_ea_test_details.tname) + '\" has been created')
        print("A2A Test created")

def create_dnsserv_test():
    headers = {
    'Content-Type': 'application/json',
    'Accept': 'application/json',
    'Authorization': 'Bearer ' + str(auth_bearer2)
    }
    payload = json.dumps({
    "testName": str(fetch_ea_test_details.tname),
    "description": str(fetch_ea_test_details.tdesc),
    "alertsEnabled": str(fetch_ea_test_details.talertsEnabled),
    "interval": int(fetch_ea_test_details.tinterval),
    "agents": json.loads(fetch_ea_test_details.tagents),
    "domain":  str(fetch_ea_test_details.tdomain),
    "dnsServers": fetch_ea_test_details.tdnsServers,
    "dnsQueryClass":str(fetch_ea_test_details.tdnsQueryClass),
    "networkMeasurements": int(fetch_ea_test_details.tnetworkMeasurements),
    "bandwidthMeasurements": 0,
    "mtuMeasurements": str(fetch_ea_test_details.tmtuMeasurements),
    "bgpMeasurements": str(fetch_ea_test_details.tbgpMeasurements),
    "probeMode": str(fetch_ea_test_details.tprobeMode),
    "ipv6Policy": str(fetch_ea_test_details.tipv6Policy),
    "dnsTransportProtocol":"UDP",
    "recursiveQueries":str(fetch_ea_test_details.trecursiveQueries)
    })
    if fetch_ea_test_details.tnumPathTraces!= 0:
        payload = payload[:-1]
        payload = payload + ', ' + "\"numPathTraces\":" + str(fetch_ea_test_details.tnumPathTraces) + "}"
    else:
        pass
    if fetch_ea_test_details.tfixedPacketRate!= 0:
        payload = payload[:-1]
        payload = payload + ', ' + "\"fixedPacketRate\":" + str(fetch_ea_test_details.tfixedPacketRate) + "}"
    else:
        pass
    create_tests_url = "https://api.thousandeyes.com/v6/tests/" + 'dns-server' + "/new.json" + "?aid=" + str(dst_aid)
    logger.info('Creating dnsserv test - '+ str(fetch_ea_test_details.tname))
    response = requests.request("POST", create_tests_url, headers=headers, data=payload)
    logger.debug('DNSserv test named \"'+ str(fetch_ea_test_details.tname) + '\" create request sent')

    if response.status_code != 201:
        logger.error('Exited with error code : '+ str(response.status_code) + ' when creating \"' + str(fetch_ea_test_details.tname) + '\"'+ '; Error Message : ' + str(response.text))
    else:
        logger.info('Test \"' + str(fetch_ea_test_details.tname) + '\" has been created')
        print("DNS Server Test created")        

def create_dnstrace_test():
    headers = {
    'Content-Type': 'application/json',
    'Accept': 'application/json',
    'Authorization': 'Bearer ' + str(auth_bearer2)
    }
    payload = json.dumps({
    "testName": str(fetch_ea_test_details.tname),
    "description": str(fetch_ea_test_details.tdesc),
    "alertsEnabled": str(fetch_ea_test_details.talertsEnabled),
    "interval": int(fetch_ea_test_details.tinterval),
    "agents": json.loads(fetch_ea_test_details.tagents),
    "domain":  str(fetch_ea_test_details.tdomain),
    "dnsTransportProtocol":  str(fetch_ea_test_details.tdnsTransportProtocol),
    })
    create_tests_url = "https://api.thousandeyes.com/v6/tests/" + 'dns-trace' + "/new.json" + "?aid=" + str(dst_aid)
    logger.info('Creating dns trace test - '+ str(fetch_ea_test_details.tname))
    response = requests.request("POST", create_tests_url, headers=headers, data=payload)
    logger.debug('DNS trace test named \"'+ str(fetch_ea_test_details.tname) + '\" create request sent')

    if response.status_code != 201:
        logger.error('Exited with error code : '+ str(response.status_code) + ' when creating \"' + str(fetch_ea_test_details.tname) + '\"'+ '; Error Message : ' + str(response.text))
    else:
        logger.info('Test \"' + str(fetch_ea_test_details.tname) + '\" has been created')
        print("DNS Trace Test created")
        
def create_dnssec_test():
    headers = {
    'Content-Type': 'application/json',
    'Accept': 'application/json',
    'Authorization': 'Bearer ' + str(auth_bearer2)
    }
    payload = json.dumps({
    "testName": str(fetch_ea_test_details.tname),
    "description": str(fetch_ea_test_details.tdesc),
    "alertsEnabled": str(fetch_ea_test_details.talertsEnabled),
    "interval": int(fetch_ea_test_details.tinterval),
    "agents": json.loads(fetch_ea_test_details.tagents),
    "domain":  str(fetch_ea_test_details.tdomain)
    })
    create_tests_url = "https://api.thousandeyes.com/v6/tests/" + 'dns-dnssec' + "/new.json" + "?aid=" + str(dst_aid)
    logger.info('Creating dnssec test - '+ str(fetch_ea_test_details.tname))
    response = requests.request("POST", create_tests_url, headers=headers, data=payload)
    logger.debug('DNSSEC test named \"'+ str(fetch_ea_test_details.tname) + '\" create request sent')

    if response.status_code != 201:
        logger.error('Exited with error code : '+ str(response.status_code) + ' when creating \"' + str(fetch_ea_test_details.tname) + '\"'+ '; Error Message : ' + str(response.text))
    else:
        logger.info('Test \"' + str(fetch_ea_test_details.tname) + '\" has been created')
        print("DNSSEC Test created")
        
def create_http_test():
    headers = {
    'Content-Type': 'application/json',
    'Accept': 'application/json',
    'Authorization': 'Bearer ' + str(auth_bearer2)
    }
    payload = json.dumps({
    "testName": str(fetch_ea_test_details.tname),
    "description": str(fetch_ea_test_details.tdesc),
    "alertsEnabled": str(fetch_ea_test_details.talertsEnabled),
    "interval": int(fetch_ea_test_details.tinterval),
    "agents": json.loads(fetch_ea_test_details.tagents),
    "url":  str(fetch_ea_test_details.turl),
    "httpTimeLimit":  str(fetch_ea_test_details.thttpTimeLimit),
    "httpTargetTime":  str(fetch_ea_test_details.thttpTargetTime), 
    "networkMeasurements":  str(fetch_ea_test_details.tnetworkMeasurements), 
    "bandwidthMeasurements":  0, 
    "mtuMeasurements":  str(fetch_ea_test_details.tmtuMeasurements), 
    "bgpMeasurements":  str(fetch_ea_test_details.tbgpMeasurements), 
    "protocol":  str(fetch_ea_test_details.tprotocol), 
    "probeMode":  str(fetch_ea_test_details.tprobeMode), 
    "pathTraceMode":  str(fetch_ea_test_details.tpathTraceMode),
    "ipv6Policy":  str(fetch_ea_test_details.tipv6Policy),
    "sslVersionId":  str(fetch_ea_test_details.tsslVersionId),
    "sslVersion":  str(fetch_ea_test_details.tsslVersion),
    "verifyCertificate":  str(fetch_ea_test_details.tverifyCertificate),
    "authType": str(fetch_ea_test_details.tauthType),
    "useNtlm": str(fetch_ea_test_details.tuseNtlm),
    "httpVersion": str(fetch_ea_test_details.thttpVersion),
    "followRedirects": str(fetch_ea_test_details.tfollowRedirects),
    "contentRegex": str(fetch_ea_test_details.tcontentRegex)
    })
    if fetch_ea_test_details.tfixedPacketRate!= 0:
        payload = payload[:-1]
        payload = payload + ', ' + "\"fixedPacketRate\":" + str(fetch_ea_test_details.tfixedPacketRate) + "}"
    else:
        pass
    if fetch_ea_test_details.tnumPathTraces!= 0:
        payload = payload[:-1]
        payload = payload + ', ' + "\"numPathTraces\":" + str(fetch_ea_test_details.tnumPathTraces) + "}"
    else:
        pass
    if fetch_ea_test_details.tclientCertificate!= 0:
        payload = payload[:-1]
        payload = payload + ', ' + "\"clientCertificate\": \"" + str(fetch_ea_test_details.tclientCertificate) + "\"}"
    else:
        pass
    if fetch_ea_test_details.tusername!= 0:
        payload = payload[:-1]
        payload = payload + ', ' + "\"username\": \"" + str(fetch_ea_test_details.tusername) + "\"}"
        payload = payload[:-1]
        payload = payload + ', ' + "\"password\": \"" + str(fetch_ea_test_details.tpassword) + "\"}"
    else:
        pass
    if fetch_ea_test_details.tpostBody!= 0:
        payload = payload[:-1]
        payload = payload + ', ' + "\"postBody\": \"" + str(fetch_ea_test_details.tpostBody) + "\"}"
    else:
        pass
    if fetch_ea_test_details.tuserAgent!= 0:
        payload = payload[:-1]
        payload = payload + ', ' + "\"userAgent\": \"" + str(fetch_ea_test_details.tuserAgent) + "\"}"
    else:
        pass
    if fetch_ea_test_details.tdnsOverride!= 0:
        payload = payload[:-1]
        payload = payload + ', ' + "\"dnsOverride\": \"" + str(fetch_ea_test_details.tdnsOverride) + "\"}"
    else:
        pass
    if fetch_ea_test_details.tdesiredStatusCode!= 0:
        payload = payload[:-1]
        payload = payload + ', ' + "\"desiredStatusCode\": \"" + str(fetch_ea_test_details.tdesiredStatusCode) + "\"}"
    else:
        pass
    if fetch_ea_test_details.tdownloadLimit!= 0:
        payload = payload[:-1]
        payload = payload + ', ' + "\"downloadLimit\": \"" + str(fetch_ea_test_details.tdownloadLimit) + "\"}"
    else:
        pass
    create_tests_url = "https://api.thousandeyes.com/v6/tests/" + 'http-server' + "/new.json" + "?aid=" + str(dst_aid)
    logger.info('Creating http server test - '+ str(fetch_ea_test_details.tname))
    response = requests.request("POST", create_tests_url, headers=headers, data=payload)
    logger.debug('HTTP server test named \"'+ str(fetch_ea_test_details.tname) + '\" create request sent')

    if response.status_code != 201:
        logger.error('Exited with error code : '+ str(response.status_code) + ' when creating \"' + str(fetch_ea_test_details.tname) + '\"'+ '; Error Message : ' + str(response.text))
    else:
        logger.info('Test \"' + str(fetch_ea_test_details.tname) + '\" has been created')
        print("HTTP Test created")

def create_page_test():
    headers = {
    'Content-Type': 'application/json',
    'Accept': 'application/json',
    'Authorization': 'Bearer ' + str(auth_bearer2)
    }
    payload = json.dumps({
    "testName": str(fetch_ea_test_details.tname),
    "description": str(fetch_ea_test_details.tdesc),
    "alertsEnabled": str(fetch_ea_test_details.talertsEnabled),
    "interval": int(fetch_ea_test_details.tinterval),
    "agents": json.loads(fetch_ea_test_details.tagents),
    "url":  str(fetch_ea_test_details.turl),
    "httpInterval": int(fetch_ea_test_details.thttpInterval),
    "httpTimeLimit":  str(fetch_ea_test_details.thttpTimeLimit),
    "httpTargetTime":  str(fetch_ea_test_details.thttpTargetTime),
    "pageLoadTimeLimit": str(fetch_ea_test_details.tpageLoadTimeLimit),
    "pageLoadTargetTime": str(fetch_ea_test_details.tpageLoadTargetTime),
    "networkMeasurements":  str(fetch_ea_test_details.tnetworkMeasurements), 
    "bandwidthMeasurements":  0, 
    "mtuMeasurements":  str(fetch_ea_test_details.tmtuMeasurements), 
    "bgpMeasurements":  str(fetch_ea_test_details.tbgpMeasurements), 
    "protocol":  str(fetch_ea_test_details.tprotocol), 
    "probeMode":  str(fetch_ea_test_details.tprobeMode), 
    "pathTraceMode":  str(fetch_ea_test_details.tpathTraceMode),
    "sslVersionId":  str(fetch_ea_test_details.tsslVersionId),
    "sslVersion":  str(fetch_ea_test_details.tsslVersion),
    "verifyCertificate":  str(fetch_ea_test_details.tverifyCertificate),
    "authType": str(fetch_ea_test_details.tauthType),
    "useNtlm": str(fetch_ea_test_details.tuseNtlm),
    "httpVersion": str(fetch_ea_test_details.thttpVersion),
    "followRedirects": str(fetch_ea_test_details.tfollowRedirects),
    "identifyAgentTrafficWithUserAgent": str(fetch_ea_test_details.tidentifyAgentTrafficWithUserAgent),
    "contentRegex": str(fetch_ea_test_details.tcontentRegex),
    "includeHeaders": str(fetch_ea_test_details.tincludeHeaders)
    })
    if fetch_ea_test_details.tsubinterval!= 0:
        payload = payload[:-1]
        payload = payload + ', ' + "\"subinterval\":" + str(fetch_ea_test_details.tsubinterval) + "}"
    else:
        pass
    if fetch_ea_test_details.tfixedPacketRate!= 0:
        payload = payload[:-1]
        payload = payload + ', ' + "\"fixedPacketRate\":" + str(fetch_ea_test_details.tfixedPacketRate) + "}"
    else:
        pass
    if fetch_ea_test_details.tnumPathTraces!= 0:
        payload = payload[:-1]
        payload = payload + ', ' + "\"numPathTraces\":" + str(fetch_ea_test_details.tnumPathTraces) + "}"
    else:
        pass
    if fetch_ea_test_details.tusername!= 0:
        payload = payload[:-1]
        payload = payload + ', ' + "\"username\": \"" + str(fetch_ea_test_details.tusername) + "\"}"
        payload = payload[:-1]
        payload = payload + ', ' + "\"password\": \"" + str(fetch_ea_test_details.tpassword) + "\"}"
    else:
        pass
    if fetch_ea_test_details.tuserAgent!= 0:
        payload = payload[:-1]
        payload = payload + ', ' + "\"userAgent\": \"" + str(fetch_ea_test_details.tuserAgent) + "\"}"
    else:
        pass
    if fetch_ea_test_details.tdesiredStatusCode!= 0:
        payload = payload[:-1]
        payload = payload + ', ' + "\"desiredStatusCode\": \"" + str(fetch_ea_test_details.tdesiredStatusCode) + "\"}"
    else:
        pass
    
    create_tests_url = "https://api.thousandeyes.com/v6/tests/" + 'page-load' + "/new.json" + "?aid=" + str(dst_aid)
    logger.info('Creating page load test - '+ str(fetch_ea_test_details.tname))
    response = requests.request("POST", create_tests_url, headers=headers, data=payload)
    logger.debug('Page load test named \"'+ str(fetch_ea_test_details.tname) + '\" create request sent')
    if response.status_code != 201:
        logger.error('Exited with error code : '+ str(response.status_code) + ' when creating \"' + str(fetch_ea_test_details.tname) + '\"'+ '; Error Message : ' + str(response.text))
    else:
        logger.info('Test \"' + str(fetch_ea_test_details.tname) + '\" has been created')
        print("Page Load Test created")
        
def create_transaction_test():
    headers = {
    'Content-Type': 'application/json',
    'Accept': 'application/json',
    'Authorization': 'Bearer ' + str(auth_bearer2)
    }
    payload = json.dumps({
    "testName": str(fetch_ea_test_details.tname),
    "description": str(fetch_ea_test_details.tdesc),
    "alertsEnabled": str(fetch_ea_test_details.talertsEnabled),
    "interval": int(fetch_ea_test_details.tinterval),
    "agents": json.loads(fetch_ea_test_details.tagents),
    "url":  str(fetch_ea_test_details.turl),
    "transactionScript": str(fetch_ea_test_details.ttransactionScript),
    "timeLimit": str(fetch_ea_test_details.ttimeLimit),
    "targetTime": str(fetch_ea_test_details.ttargetTime),
    "httpTimeLimit":  str(fetch_ea_test_details.thttpTimeLimit),
    "httpTargetTime":  str(fetch_ea_test_details.thttpTargetTime),
    "networkMeasurements":  str(fetch_ea_test_details.tnetworkMeasurements), 
    "bandwidthMeasurements":  0, 
    "mtuMeasurements":  str(fetch_ea_test_details.tmtuMeasurements), 
    "bgpMeasurements":  str(fetch_ea_test_details.tbgpMeasurements), 
    "protocol":  str(fetch_ea_test_details.tprotocol), 
    "probeMode":  str(fetch_ea_test_details.tprobeMode), 
    "pathTraceMode":  str(fetch_ea_test_details.tpathTraceMode),
    "sslVersionId":  str(fetch_ea_test_details.tsslVersionId),
    "sslVersion":  str(fetch_ea_test_details.tsslVersion),
    "verifyCertificate":  str(fetch_ea_test_details.tverifyCertificate),
    "authType": str(fetch_ea_test_details.tauthType),
    "useNtlm": str(fetch_ea_test_details.tuseNtlm),
    "httpVersion": str(fetch_ea_test_details.thttpVersion),
    "followRedirects": str(fetch_ea_test_details.tfollowRedirects),
    "identifyAgentTrafficWithUserAgent": str(fetch_ea_test_details.tidentifyAgentTrafficWithUserAgent),
    "contentRegex": str(fetch_ea_test_details.tcontentRegex),
    "includeHeaders": str(fetch_ea_test_details.tincludeHeaders)

    })
    if fetch_ea_test_details.tsubinterval!= 0:
        payload = payload[:-1]
        payload = payload + ', ' + "\"subinterval\":" + str(fetch_ea_test_details.tsubinterval) + "}"
    else:
        pass
    if fetch_ea_test_details.tfixedPacketRate!= 0:
        payload = payload[:-1]
        payload = payload + ', ' + "\"fixedPacketRate\":" + str(fetch_ea_test_details.tfixedPacketRate) + "}"
    else:
        pass
    if fetch_ea_test_details.tnumPathTraces!= 0:
        payload = payload[:-1]
        payload = payload + ', ' + "\"numPathTraces\":" + str(fetch_ea_test_details.tnumPathTraces) + "}"
    else:
        pass
    if fetch_ea_test_details.tusername!= 0:
        payload = payload[:-1]
        payload = payload + ', ' + "\"username\": \"" + str(fetch_ea_test_details.tusername) + "\"}"
        payload = payload[:-1]
        payload = payload + ', ' + "\"password\": \"" + str(fetch_ea_test_details.tpassword) + "\"}"
    else:
        pass
    if fetch_ea_test_details.tuserAgent!= 0:
        payload = payload[:-1]
        payload = payload + ', ' + "\"userAgent\": \"" + str(fetch_ea_test_details.tuserAgent) + "\"}"
    else:
        pass
    if fetch_ea_test_details.tdesiredStatusCode!= 0:
        payload = payload[:-1]
        payload = payload + ', ' + "\"desiredStatusCode\": \"" + str(fetch_ea_test_details.tdesiredStatusCode) + "\"}"
    else:
        pass
    create_tests_url = "https://api.thousandeyes.com/v6/tests/" + 'web-transactions' + "/new.json" + "?aid=" + str(dst_aid)
    logger.info('Creating transaction test - '+ str(fetch_ea_test_details.tname))
    response = requests.request("POST", create_tests_url, headers=headers, data=payload)
    logger.debug('Transaction test named \"'+ str(fetch_ea_test_details.tname) + '\" create request sent')

    if response.status_code != 201:
        logger.error('Exited with error code : '+ str(response.status_code) + ' when creating \"' + str(fetch_ea_test_details.tname) + '\"'+ '; Error Message : ' + str(response.text))
    else:
        logger.info('Test \"' + str(fetch_ea_test_details.tname) + '\" has been created')
        print("Transaction Test created")

def create_ftp_test():
    headers = {
    'Content-Type': 'application/json',
    'Accept': 'application/json',
    'Authorization': 'Bearer ' + str(auth_bearer2)
    }
    fetch_ea_test_details.tpassword = input("Enter the password for FTP server - " + fetch_ea_test_details.turl + ": ")
    payload = json.dumps({
    "testName": str(fetch_ea_test_details.tname),
    "description": str(fetch_ea_test_details.tdesc),
    "alertsEnabled": str(fetch_ea_test_details.talertsEnabled),
    "interval": int(fetch_ea_test_details.tinterval),
    "agents": json.loads(fetch_ea_test_details.tagents),
    "url":  str(fetch_ea_test_details.turl),
    "requestType": str(fetch_ea_test_details.trequestType),
    "username": str(fetch_ea_test_details.tusername),
    "password": str(fetch_ea_test_details.tpassword),
    "ftpTimeLimit": str(fetch_ea_test_details.tftpTimeLimit),
    "ftpTargetTime": str(fetch_ea_test_details.tftpTargetTime),
    "networkMeasurements":  str(fetch_ea_test_details.tnetworkMeasurements), 
    "bandwidthMeasurements":  0, 
    "mtuMeasurements":  str(fetch_ea_test_details.tmtuMeasurements), 
    "bgpMeasurements":  str(fetch_ea_test_details.tbgpMeasurements), 
    "protocol":  str(fetch_ea_test_details.tprotocol), 
    "probeMode":  str(fetch_ea_test_details.tprobeMode), 
    "pathTraceMode":  str(fetch_ea_test_details.tpathTraceMode),
    "ipv6Policy":  str(fetch_ea_test_details.tipv6Policy)
    })
    if fetch_ea_test_details.tdownloadLimit!= 0:
        payload = payload[:-1]
        payload = payload + ', ' + "\"downloadLimit\":" + str(fetch_ea_test_details.tdownloadLimit) + "}"
    else:
        pass
    if fetch_ea_test_details.tuploadFileSize!= 0:
        payload = payload[:-1]
        payload = payload + ', ' + "\"uploadFileSize\":" + str(fetch_ea_test_details.tuploadFileSize) + "}"
    else:
        pass
    if fetch_ea_test_details.tcontentRegex!= 0:
        payload = payload[:-1]
        payload = payload + ', ' + "\"contentRegex\": \"" + str(fetch_ea_test_details.tcontentRegex) + "\"}"
    else:
        pass
    if fetch_ea_test_details.tfixedPacketRate!= 0:
        payload = payload[:-1]
        payload = payload + ', ' + "\"fixedPacketRate\":" + str(fetch_ea_test_details.tfixedPacketRate) + "}"
    else:
        pass
    if fetch_ea_test_details.tnumPathTraces!= 0:
        payload = payload[:-1]
        payload = payload + ', ' + "\"numPathTraces\":" + str(fetch_ea_test_details.tnumPathTraces) + "}"
    else:
        pass
    if fetch_ea_test_details.tuseActiveFtp!= 0:
        payload = payload[:-1]
        payload = payload + ', ' + "\"useActiveFtp\":" + str(fetch_ea_test_details.tuseActiveFtp) + "}"
    else:
        pass
    if fetch_ea_test_details.tuseExplicitFtps!= 0:
        payload = payload[:-1]
        payload = payload + ', ' + "\"useExplicitFtps\":" + str(fetch_ea_test_details.tuseExplicitFtps) + "}"
    else:
        pass
    
    if fetch_ea_test_details.tdesiredReplyCode!= 0:
        payload = payload[:-1]
        payload = payload + ', ' + "\"desiredReplyCode\": \"" + str(fetch_ea_test_details.tdesiredReplyCode) + "\"}"
    else:
        pass
    create_tests_url = "https://api.thousandeyes.com/v6/tests/" + 'ftp-server' + "/new.json" + "?aid=" + str(dst_aid)

    logger.info('Creating ftp test - '+ str(fetch_ea_test_details.tname))
    response = requests.request("POST", create_tests_url, headers=headers, data=payload)
    logger.debug('FTP test named \"'+ str(fetch_ea_test_details.tname) + '\" create request sent')

    if response.status_code != 201:
        logger.error('Exited with error code : '+ str(response.status_code) + ' when creating \"' + str(fetch_ea_test_details.tname) + '\"'+ '; Error Message : ' + str(response.text))
    else:
        logger.info('Test \"' + str(fetch_ea_test_details.tname) + '\" has been created')
        print("FTP Test created")
        
def create_sip_test():
    headers = {
    'Content-Type': 'application/json',
    'Accept': 'application/json',
    'Authorization': 'Bearer ' + str(auth_bearer2)
    }
    payload = json.dumps({
    "testName": str(fetch_ea_test_details.tname),
    "description": str(fetch_ea_test_details.tdesc),
    "alertsEnabled": str(fetch_ea_test_details.talertsEnabled),
    "interval": int(fetch_ea_test_details.tinterval),
    "agents": json.loads(fetch_ea_test_details.tagents),
    "sipTimeLimit": str(fetch_ea_test_details.tsipTimeLimit),
    "tsipTargetTime": str(fetch_ea_test_details.tsipTargetTime),
    "networkMeasurements":  str(fetch_ea_test_details.tnetworkMeasurements), 
    "bandwidthMeasurements":  0,
    "mtuMeasurements":  str(fetch_ea_test_details.tmtuMeasurements), 
    "bgpMeasurements":  str(fetch_ea_test_details.tbgpMeasurements),
    "pathTraceMode":  str(fetch_ea_test_details.tpathTraceMode),
    "registerEnabled": str(fetch_ea_test_details.tregisterEnabled),
    "ipv6Policy":  str(fetch_ea_test_details.tipv6Policy)
    })
    if fetch_ea_test_details.tfixedPacketRate!= 0:
        payload = payload[:-1]
        payload = payload + ', ' + "\"fixedPacketRate\":" + str(fetch_ea_test_details.tfixedPacketRate) + "}"
    else:
        pass
    if fetch_ea_test_details.tnumPathTraces!= 0:
        payload = payload[:-1]
        payload = payload + ', ' + "\"numPathTraces\":" + str(fetch_ea_test_details.tnumPathTraces) + "}"
    else:
        pass
    if fetch_ea_test_details.toptionsRegex!= 0:
        payload = payload[:-1]
        payload = payload + ', ' + "\"optionsRegex\": \"" + str(fetch_ea_test_details.toptionsRegex) + "\"}"
    else:
        pass
    payload = payload[:-1]
    payload = payload + ', ' + '\"targetSipCredentials\": { \"sipRegistrar\": \"' + str(fetch_ea_test_details.tsipRegistrar) + '\", \"port\": ' + str(fetch_ea_test_details.tport) + ', \"protocol\": \"' + str(fetch_ea_test_details.tprotocol) + '\"}}'
    if fetch_ea_test_details.tuser!= 0:
        payload = payload[:-2]
        payload = payload + ', ' + "\"user\": \"" + str(fetch_ea_test_details.tuser) + "\"}"
        payload = payload[:-1]
        payload = payload + ', ' + "\"password\": \"" + str(fetch_ea_test_details.tpassword) + "\"}}"
    else:
        pass
    if fetch_ea_test_details.tauthUser!= 0:
        payload = payload[:-2]
        payload = payload + ', ' + "\"authUser\": \"" + str(fetch_ea_test_details.tauthUser) + "\"}}"
    else:
        pass
    
    create_tests_url = "https://api.thousandeyes.com/v6/tests/" + 'sip-server' + "/new.json" + "?aid=" + str(dst_aid)
    logger.info('Creating sip test - '+ str(fetch_ea_test_details.tname))
    response = requests.request("POST", create_tests_url, headers=headers, data=payload)
    logger.debug('SIP test named \"'+ str(fetch_ea_test_details.tname) + '\" create request sent')

    if response.status_code != 201:
        logger.error('Exited with error code : '+ str(response.status_code) + ' when creating \"' + str(fetch_ea_test_details.tname) + '\"'+ '; Error Message : ' + str(response.text))   
    else:
        logger.info('Test \"' + str(fetch_ea_test_details.tname) + '\" has been created')
        print("SIP Test created")

def create_rtp_test():
    headers = {
    'Content-Type': 'application/json',
    'Accept': 'application/json',
    'Authorization': 'Bearer ' + str(auth_bearer2)
    }
    payload = json.dumps({
    "testName": str(fetch_ea_test_details.tname),
    "description": str(fetch_ea_test_details.tdesc),
    "alertsEnabled": str(fetch_ea_test_details.talertsEnabled),
    "interval": int(fetch_ea_test_details.tinterval),
    "agents": json.loads(fetch_ea_test_details.tagents),
    "targetAgentId": str(fetch_ea_test_details.ttargetAgentId),
    "server": str(fetch_ea_test_details.tserver),
    "codec": str(fetch_ea_test_details.tcodec),
    "codecId": str(fetch_ea_test_details.tcodecId),
    "duration": str(fetch_ea_test_details.tduration),
    "jitterBuffer": str(fetch_ea_test_details.tjitterBuffer),
    "bgpMeasurements": str(fetch_ea_test_details.tbgpMeasurements),
    "codecId": str(fetch_ea_test_details.tcodecId),
    "numPathTraces": str(fetch_ea_test_details.tnumPathTraces),
    "dscp": str(fetch_ea_test_details.tdscp),
    "dscpId": str(fetch_ea_test_details.tdscpId)
    })
    create_tests_url = "https://api.thousandeyes.com/v6/tests/" + 'voice' + "/new.json" + "?aid=" + str(dst_aid)
    logger.info('Creating voice test - '+ str(fetch_ea_test_details.tname))
    response = requests.request("POST", create_tests_url, headers=headers, data=payload)
    logger.debug('Voice test named \"'+ str(fetch_ea_test_details.tname) + '\" create request sent')

    if response.status_code != 201:
        logger.error('Exited with error code : '+ str(response.status_code) + ' when creating \"' + str(fetch_ea_test_details.tname) + '\"'+ '; Error Message : ' + str(response.text))
    else:
        logger.info('Test \"' + str(fetch_ea_test_details.tname) + '\" has been created')
        print("RTP Test created")

#======================================================================================================#

#Fetch EPA tests from the specified source AG from the source ORG

def fetch_epa_test_details():
    payload = {}
    headers = {
    'Content-Type': 'application/json',
    'Accept': 'application/json',
    'Authorization': 'Bearer ' + str(auth_bearer1)
    }
    fetch_tests_url = "https://api.thousandeyes.com/v6/endpoint-tests.json" + "?aid=" + str(src_aid)
    fetch_tests_response = requests.request("GET", fetch_tests_url, headers=headers, data=payload)
    epa_tests_data = json.loads(fetch_tests_response.text)

    if epa_tests_flag == "1":  
        for i in range(0,len(epa_tests_data['endpointTest'])):
            fetch_epa_test_details.tname = epa_tests_data['endpointTest'][i]['testName']
            fetch_epa_test_details.tagentSelectorType = epa_tests_data['endpointTest'][i]['agentSelectorConfig']['agentSelectorType']
            fetch_epa_test_details.tinterval = epa_tests_data['endpointTest'][i]['interval']
            fetch_epa_test_details.tserver = epa_tests_data['endpointTest'][i]['server']
            fetch_epa_test_details.tmaxMachines = epa_tests_data['endpointTest'][i]['agentSelectorConfig']['maxMachines']   
            fetch_epa_test_details.tlabelIds = epa_tests_data['endpointTest'][i]['agentSelectorConfig']['labelIds']            
            #fetch_epa_test_details.talertsEnabled = epa_tests_data['endpointTest'][i]['alertsEnabled']
            if str(epa_tests_data['endpointTest'][i]['type']) == 'agent-to-server' and (int(epa_tests_data['endpointTest'][i]['enabled']) == 1) and (int(epa_a2s_flag) == 1 or int(all_epa_tests) == 1):    
                try:
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
                except Exception as e:
                    logger.error('Error migrating EPA agent-to-server test - ' +  str(e) + ' when creating \"' + str(fetch_epa_test_details.tname) + '\". Check the test configuration and EPA agents assigned')

            if str(epa_tests_data['endpointTest'][i]['type']) == 'http-server' and (int(epa_tests_data['endpointTest'][i]['enabled']) == 1) and (int(epa_http_server_flag) == 1 or int(epa_http_server_flag) == 1):    
                try:
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
                except Exception as e:
                    logger.error('Error migrating EPA http-server test - ' +  str(e) + ' when creating \"' + str(fetch_epa_test_details.tname) + '\". Check the test configuration and EPA agents assigned')
    else:
        print("No EPA tests selected for migration")
#======================================================================================================#

#Create tests to the specified destination AG from the destination ORG

def create_epa_a2s_test():
    headers = {
    'Content-Type': 'application/json',
    'Accept': 'application/json',
    'Authorization': 'Bearer ' + str(auth_bearer1)
    }
    payload = json.dumps({
    "testName": str(fetch_epa_test_details.tname),
    #"alertsEnabled": str(fetch_epa_test_details.talertsEnabled),
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
    create_tests_url = "https://api.thousandeyes.com/v6/endpoint-tests/" + 'agent-to-server' + "/new.json" + "?aid=" + str(dst_aid)
    response = requests.request("POST", create_tests_url, headers=headers, data=payload)
    if response.status_code != 201:
        logger.error('Exited with error code : '+ str(response.status_code) + ' when creating \"' + str(fetch_epa_test_details.tname) + '\"'+ '; Error Message : ' + str(response.text))
    else:
        logger.info('Test \"' + str(fetch_epa_test_details.tname) + '\" has been created')
        print("EPA A2S Test created")

    logger.info('Creating agent-to-agent test - '+ str(fetch_ea_test_details.tname))
    response = requests.request("POST", create_tests_url, headers=headers, data=payload)
    logger.debug('Agent-to-agent test named \"'+ str(fetch_ea_test_details.tname) + '\" create request sent')

def create_epa_http_test():
    headers = {
    'Content-Type': 'application/json',
    'Accept': 'application/json',
    'Authorization': 'Bearer ' + str(auth_bearer1)
    }
    payload = json.dumps({
    "testName": str(fetch_epa_test_details.tname),
    #"alertsEnabled": str(fetch_epa_test_details.talertsEnabled),
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
    create_tests_url = "https://api.thousandeyes.com/v6/endpoint-tests/" + 'http-server' + "/new.json" + "?aid=" + str(dst_aid)
    response = requests.request("POST", create_tests_url, headers=headers, data=payload)
    if response.status_code != 201:
        logger.error('Exited with error code : '+ str(response.status_code) + ' when creating \"' + str(fetch_epa_test_details.tname) + '\"'+ '; Error Message : ' + str(response.text))
        pprint(payload)
    else:
        logger.info('Test \"' + str(fetch_epa_test_details.tname) + '\" has been created')
        print("EPA HTTP Test created")

#======================================================================================================#

#Main function call exection flow

def main():
    fetch_ea_test_details()
    fetch_epa_test_details()
    
if __name__ == "__main__":
    main()
