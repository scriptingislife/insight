import common
import requests
from prettytable import PrettyTable

def lookup(target, key):
    if key is None:
        print('Missing Shodan API key. Skipping...')
        return None

    response = requests.get('https://api.shodan.io/shodan/host/{}?key={}'.format(target, key))
    if response.status_code != 200:
        print('Got status {} from Shodan. Skipping...'.format(response.status_code))
        return None
    data = response.json()

    table = PrettyTable()
    table.field_names = ["Shodan", "Country", "Ports"]
    table.add_row([data["ip_str"], data["country_name"], ""])
    for port in data["ports"]:
        table.add_row(["", "", port])

    print(common.bcolors.FAIL + str(table) + common.bcolors.ENDC)