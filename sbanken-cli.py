#!/usr/bin/python3

import os
import json
import requests

from requests.auth import HTTPBasicAuth

config = json.load(open(os.path.dirname(os.path.realpath(__file__)) + '/config.json'))

token_request = requests.post('https://api.sbanken.no/identityserver/connect/token', {'grant_type': 'client_credentials'}, auth=HTTPBasicAuth(config['clientId'], config['secret']))

token = json.loads(token_request.text)['access_token']

account_details_request = requests.get('https://api.sbanken.no/bank/api/v1/accounts/' + config['userId'], headers={
    'Authorization':  'Bearer ' + token,
})

account_details = json.loads(account_details_request.text)['items']

for account_detail in account_details:
    print(account_detail['name'] + ':\t' + str(account_detail['balance']))
