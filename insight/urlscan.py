#
# URLScan.io
# ----------
# - Check if domain or IP appears in URLScan.io scans
#
import common
import requests
from prettytable import PrettyTable

def lookup(target):
    response = requests.get('https://urlscan.io/api/v1/search/?q=domain:{}'.format(target))
    if response.status_code != 200:
        print('Got status {} from URLScan. Skipping...'.format(response.status_code))
        return None
    data = response.json()

    table = PrettyTable()
    table.field_names = ["URLScan", "Times Scanned"]

    scanned = len(data["results"])
    if scanned == 100:
        scanned = str(scanned) + '+'
    
    table.add_row([target, scanned])
    print(common.bcolors.WARNING + str(table) + common.bcolors.ENDC)