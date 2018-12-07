#
# Censys
# ------
# - Gather certificate information
#
#
import common
import requests
from prettytable import PrettyTable


API_URL = 'https://censys.io/api/v1'

def raw_cert(id, uid, secret):
    API_PATH = '/view/certificates/{}'.format(id)
    response = requests.get(API_URL + API_PATH, auth=(uid, secret))
    if response.status_code != 200:
        print('Got status {} from Censys Certificates. Skipping...'.format(response.status_code))
        print(response.json()['error'])
        return None
    return response.json()


def lookup(target, uid, secret, color=common.bcolors.WARNING):
    if uid is None or secret is None:
        print('Missing Censys API UID or secret. Skipping...')
        return None

    API_URL = 'https://censys.io/api/v1'
    API_PATH = '/search/certificates'
    response = requests.post(API_URL + API_PATH, auth=(uid, secret), json={'query': 'parsed.names:{}'.format(target)})
    if response.status_code != 200:
        print('Got status {} from Censys search. Skipping...'.format(response.status_code))
        print(response.json()['error'])
        return None
    data = response.json()

    table = PrettyTable()
    table.field_names = ["Censys Certificates", "Trust", "Issuer", "Issued", "Expires"]

    for cert in data['results'][:5]:
        cert_data = raw_cert(cert['parsed.fingerprint_sha256'], uid, secret)

        cert_names = cert_data['parsed']['names']
        cert_names_len = len(cert_names)
        if cert_names_len == 1:
            cert_names = cert_names[0]
        elif cert_names_len > 3:
            cert_names = 'Valid for ' + str(len(cert_names)) + ' domains'

        cert_start = cert_data['parsed']['validity']['start']
        cert_start = cert_start[:cert_start.index('T')]

        cert_end = cert_data['parsed']['validity']['end']
        cert_end = cert_end[:cert_end.index('T')]

        cert_trusted = ''
        try:
            if 'trusted' in cert_data['tags']:
                cert_trusted = "Trusted"
        except KeyError:
            pass

        table.add_row([cert_names, cert_trusted, cert_data['parsed']['issuer']['common_name'][0], cert_start, cert_end])
        common.sleep(1)
    if data['metadata']['count'] > 5:
        table.add_row(['...', '...', '...', '...', '...'])
    table.add_row(['Total Results', data['metadata']['count'], "", "", ""])

    print(color + str(table) + common.bcolors.ENDC)