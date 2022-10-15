![](https://visitor-badge.glitch.me/badge?page_id=adchella-te.eu-migration-tool)

# EU Migration Tool
## Table of contents
* [Executive Summary](#executive-summary)
* [Engineering/Product Summary](#engineering-summary)

## Executive Summary
### What problem does this tool solve?
ThousandEyes announced general availability for EU-multi-region cloud support on 16th-August-2022. The primary goal being to enable our customers to address any regulatory concerns they have that require SaaS or Cloud services to be based in the EU. With this launch it can be expected that some of our EMEA customers would wish to move their existing test settings from the US data-center to the EU data-center. Currently we do not have an automated process to assist customers in this endevour.

### How does it solve the problem?
With the help of this tool, customers can migrate their tests and other configuration from the US DC seemlessly to their account groups in the EU DC. The tool is scalable such that customers would not only be able to migrate their account group settings from US to EU but essentially form Account Group A to Account Group B as needed.

## Engineering Summary
### Current Feature coverage -
Enterprise and Cloud Agent Tests -
1. BGP Test : Full Configuration *
2. Network - Agent-to-server : Full Configuration *
3. Network - Agent-to-agent : Full Configuration *
4. DNS - DNS server : Full Configuration *
5. DNS - DNS trace : Full Configuration *
6. DNS - DNSSEC : Full Configuration *
7. Web - HTTP server : Full Configuration *
8. Web - Page load : Basic Configuration
9. Web - Transaction : Basic Configuration
10. Web - FTP : Basic Configuration
11. Voice - RTP : Basic Configuration
12. Voice - SIP : Basic Configuration

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
9. API support to fetch proxy settings for HTTP server tests not available.
10. API support to fetch OAuth details for HTTP server tests not available.
11. Migration for Custom Headers field pending for HTTP and Pageload tests.
12. API support for device emulation not available.

### TechStack:
* Python3
* ThousandEyes Dev APIv6	
