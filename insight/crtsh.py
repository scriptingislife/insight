import common
import requests
from prettytable import PrettyTable

def lookup(target, color=common.bcolors.OKGREEN):
    ROW_LIMIT = 20
    API_URL = 'https://crt.sh/?q=%.{}&output=json'
    response = requests.get(API_URL.format  (common.extract_domain(target)))
    if response.status_code != 200:
        print('Got status {} from crt.sh. Skipping...'.format(response.status_code))
        return None
    data = response.json()
    
    subdomains = set()
    for entry in data:
        subdomains.add(entry['name_value'])

    table = PrettyTable()
    table.field_names = ['Enumerated Subdomains']
    for domain in sorted(subdomains):
        table.add_row([domain])
    # TODO: Row limits. Set not subscriptable.
    #if len(subdomains) > 20:
    #    table.add_row(['...'])

    print(color + str(table) + common.bcolors.ENDC)