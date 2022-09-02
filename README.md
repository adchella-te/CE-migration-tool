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
1. BGP Test : Basic Configuration
2. Network - Agent-to-server : Basic Configuration
3. Network - Agent-to-agent : Basic Configuration
4. DNS - DNS server : Basic Configuration
5. DNS - DNS trace : Basic Configuration
6. DNS - DNSSEC : Basic Configuration
7. Web - HTTP server : Basic Configuration
8. Web - Page load : Basic Configuration
9. Web - Transaction : Not Covered
10. Web - FTP : Not Covered
11. Voice - RTP : Not Covered
12. Voice - SIP : Not Covered

Note - Enterprise agent migration not covered. Only cloud agents are migrated currently for all tests. 

### TechStack:
* Python3
* ThousandEyes Dev APIv6	
