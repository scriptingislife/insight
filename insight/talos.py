#
# Cisco Talos Intelligence
# ------------------------
# Reputation
# - Email Reputation
# - Web Reputation
# Details
# - Category
# - Hostname

import common
import requests
from prettytable import PrettyTable

def whois(target, color=common.bcolors.OKBLUE):
    target_is_ip = common.isip(target)

    req_headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:63.0) Gecko/20100101 Firefox/63.0', 'Referer': 'https://talosintelligence.com'}
    req_data = {'offset': 0, 'order': 'ip asc', 'query': '/api/v2/whois/', 'query_entry': target}
    response = requests.get('https://talosintelligence.com/sb_api/query_lookup', headers=req_headers, data=req_data)
    if response.status_code != 201:
        print('Got status {} from Talos WHOIS. Skipping...'.format(response.status_code))
        return None
    
    data = response.json()
    try:
        if data["error"]:
            print('Talos returned error: {}'.format(data["error"]))
            return None
    except KeyError:
        pass

    data = response.json()['data'].replace('\r', '').split('\n')
    
    table = PrettyTable()
    if target_is_ip:
        table.field_names = ["WHOIS IP Space", "Creation Date", "Last Updated", "Registrar"]
    else:
        table.field_names = ["WHOIS Domain", "Creation Date", "Expiry Date", "Registrar"]

    create_date = ""
    expire_date = ""
    registrar = ""
    for line in data:
        if target_is_ip:
#            if "NetRange" in line:
#                net_range = line[line.index(':')+1:].strip()
            if "RegDate:" in line:
                create_date = line[line.index(':')+1:].strip()
            elif "Updated" in line:
                expire_date = line[line.index(':')+1:].strip()
            elif "OrgName" in line:
                registrar = line[line.index(':')+1:].strip()
        else:
            if "Creation Date:" in line:
                create_date = line[line.index(':')+1:line.rfind('T')].strip()
            elif "Registry Expiry Date:" in line:
                expire_date = line[line.index(':')+1:line.rfind('T')].strip()
            elif "Registrar:" in line:
                registrar = line[line.index(':')+1:].strip()
            if create_date != "" and expire_date != "" and registrar != "":
                break

    table.add_row([target, create_date, expire_date, registrar])
    print(color + str(table) + common.bcolors.ENDC)



def lookup(target, color=common.bcolors.OKBLUE):
    target = common.ipfromhost(target)
    API_PATH = '/api/v2/details/ip/'
    #if not common.isip(target):
    #    API_PATH = '/api/v2/details/domain/'
    #else:
    #    API_PATH = '/api/v2/details/ip/'

    req_headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:63.0) Gecko/20100101 Firefox/63.0', 'Referer': 'https://talosintelligence.com'}
    req_data = {'query': API_PATH, 'query_entry': target}
    response = requests.get('https://talosintelligence.com/sb_api/query_lookup', headers=req_headers, data=req_data)
    if response.status_code != 201:
        print('Got status {} from Talos. Skipping...'.format(response.status_code))
        return None

    data = response.json()

    try:
        if data["error"]:
            print('Talos returned error: {}'.format(data["error"]))
            return None
    except KeyError:
        pass

    table = PrettyTable()
    table.field_names = ["Talos Intelligence", "Category", "Email Score", "Web Score", "Blacklists"]

    category = ""
    try:
        if data["category"]:
            category = data["category"]['description']
    except KeyError:
        pass

    blacklists = 0
    for blist in data["blacklists"]:
        if len(data["blacklists"][blist]["rules"]) > 0:
            blacklists = blacklists + 1
            #print(len(data["blacklists"][blist]["rules"]))

    table.add_row([data["ip"], category, data["email_score_name"], data["web_score_name"], blacklists])
    print(color + str(table) + common.bcolors.ENDC)