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

def lookup(target):
    # Host: /api/v2/details/host/
    # IP: /api/v2/details/ip/ 
    #target = common.ipfromhost(target)

    req_headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:63.0) Gecko/20100101 Firefox/63.0', 'Referer': 'https://talosintelligence.com'}
    req_data = {'query': '/api/v2/details/ip/', 'query_entry': target}
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

    if data["category"]:
        category = data["category"]['description']
    else:
        category = ""

    blacklists = 0
    for blist in data["blacklists"]:
        if len(data["blacklists"][blist]["rules"]) > 0:
            blacklists = blacklists + 1
            #print(len(data["blacklists"][blist]["rules"]))

    table.add_row([data["ip"], category, data["email_score_name"], data["web_score_name"], blacklists])
    print(common.bcolors.OKBLUE + str(table) + common.bcolors.ENDC)