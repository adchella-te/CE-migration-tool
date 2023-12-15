[![published](https://static.production.devnetcloud.com/codeexchange/assets/images/devnet-published.svg)](https://developer.cisco.com/codeexchange/github/repo/adchella-te/EU-migration-tool)
[![Run in Cisco Cloud IDE](https://static.production.devnetcloud.com/codeexchange/assets/images/devnet-runable-icon.svg)](https://developer.cisco.com/codeexchange/devenv/adchella-te/EU-migration-tool/)
![](https://visitor-badge.glitch.me/badge?page_id=adchella-te.eu-migration-too)

# Latest Release Notes - CEM release 2.0
1. Ability to move a subset of tests (e.g only BGP and HTTP server tests)
2. Ability to move tests from AG in same organisation to another AG in the same organization
3. Better and more robust error handling

# CE Migration Tool
## Table of contents
* [Executive Summary](#executive-summary)
* [Engineering/Product Summary](#usage-summary)

## Executive Summary
### What problem does this tool solve?
ThousandEyes announced the option to create the ThousandEyes controller tenents hosted on the newly launched EU DC on 16th-August-2022, with the goal of enabling customers in EMEA to meet required SaaS/Cloud services regulations. The launch of this new DC in the EU region, saw a lot of our EMEA customers wishing to move their existing test settings from the US DC to the EU DC. This project was created to solve for this problem and it has since evolved to meet the configuration migration needs for general ThousandEyes operations. 

### How does it solve the problem?
Automated migration of tests and other configuration from the one ThousandEyes region to the other
Automated migration of tests (or subset of tests) from one account group to the other 

## Usage Summary
### Current Feature coverage -
Enterprise and Cloud Agent Tests -
1. BGP Test : Full Configuration *
2. Network - Agent-to-server : Full Configuration *
3. Network - Agent-to-agent : Full Configuration *
4. DNS - DNS server : Full Configuration *
5. DNS - DNS trace : Full Configuration *
6. DNS - DNSSEC : Full Configuration *
7. Web - HTTP server : Full Configuration *
8. Web - Page load : Full Configuration *
9. Web - Transaction : Basic Configuration *
10. Web - FTP : Full Configuration *
11. Voice - RTP : Full Configuration *
12. Voice - SIP : Full Configuration *

\* See Limitations

Endpoint Agent Tests -
1. Network - Agent-to-server : Basic Configuration
2. Web - HTTP server : Basic Configuration

Note - Enterprise agent migration not covered. Only cloud agents are migrated currently for all tests. 

### Limitations - 
1. BGP Private monitors migration not covered. Only tests using public monitors can be migrated.
2. "agents.sourceIpAddress", "bandwidthMeasurements" and "bgpMonitors" optional features not covered for A2S tests.
3. Throughput measurement rate selection per protocol not supported for A2A tests.
4. API support for "PingPayloadSize" parameter (only visible when TCP selected as protocol) is missing for A2A tests.
5. API support for "Protocol" parameter is missing for DNS Server tests.
6. Bandwidth measurement option cannot be selected or migrated as it can only be done for enterprise agent which are not migrated.
7. FTP test server credentials have to be re-entered at the time of creation.
8. DNS Server Test Trasport protocol can be set but not fetched.
9. API support to fetch proxy settings and OAuth details for HTTP server tests not available and API support for device emulation not available.
10. Migration for Custom Headers field pending for HTTP, Page-load and Transaction tests.
11. A API support to fetch Server Type and Desired Status Code fields not available. API support to push SIP-Proxy configuration unavailable.
12. Agent assignment for all migrate EPA will be All tests by default

### TechStack:
* Python3.8.9
* ThousandEyes Dev APIv6	

## Instructions to Run the Script

Install the Required Python Libraries :

    $ pip3 install -r requirements.txt

Run the main script :
    
    $ python3 eu-migration-release-2.py

### Disclaimer:
This project is an open source initiative licensed under the MIT License, encouraging collaboration and development within the community. Users are free to use, modify, and distribute the software in accordance with the terms specified in the Apache License. For major services related to this project, users are advised to contact the ThousandEyes account team or email support@thousandeyes.com for assistance. Please note that this project and its maintainers are not directly affiliated with ThousandEyes platform, and any support provided by ThousandEyes is subject to their own terms and conditions.
