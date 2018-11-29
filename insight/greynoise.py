# Grey Noise
# ----------
# Reputation
# - Tags scanners, bots, worms

import common
import requests
from prettytable import PrettyTable

def lookup(target):
    target = common.ipfromhost(target)

    response = requests.post('http://api.greynoise.io:8888/v1/query/ip', data={'ip': target})
    if response.status_code != 200:
        print('Got status {} from Grey Noise. Skipping...'.format(response.status_code))
        return None
    data = response.json()

    table = PrettyTable()
    if data['status'] == 'ok':
        table.field_names = ["Grey Noise", "Scanner Type"]
        for record in data['records']:
            table.add_row(["", record['name']])
        table.add_row(['Total Records', data['returned_count']])
    else:
        table.field_names = ["Grey Noise", "Status"]
        table.add_row([data['ip'], data['status']])
    print(common.bcolors.OKGREEN + str(table) + common.bcolors.ENDC)