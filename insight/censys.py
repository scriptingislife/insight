import common
import requests
from prettytable import PrettyTable

def lookup(target, uid, secret):
    if uid is None or secret is None:
        print('Missing Censys API UID or secret. Skipping...')
        return None

    API_URL = 'https://censys.io/api/v1/data'
    response = requests.get(API_URL + '/data', auth=(uid, secret))
    if response.status_code != 200:
        print('Got status {} from Censys. Skipping...'.format(response.status_code))
        return None
    data = response.json()

    table = PrettyTable()