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

    for domain in sorted(subdomains)[:ROW_LIMIT]:
        table.add_row([domain])

    if len(subdomains) > ROW_LIMIT:
        table.add_row(['+{} MORE'.format(len(subdomains) - ROW_LIMIT)])

    print(color + str(table) + common.bcolors.ENDC)