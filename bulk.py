#!/usr/bin/python

import csv
import requests
import time
import sys
import json
import logging
from datetime import datetime

# functions
def build_roles( roles, uuid ):
	arRoles = []
	for role in roles.split(','):
		roletoadd = {
			"uuid": uuid,
			"value": role
		}

		arRoles.append(roletoadd)
		
	return arRoles

#apikey = 'sCeuYG7DWFP6wGhn8rIIzZMNKUbFH1XQ'
#secret = 'FtBJYUnCc5urVqSv'
apikey = 'R8dbjFAjRXo3DUsetkuCrY6tlvjHm1mT'
secret = 'TI12ZOQDsnzqnfOb'

tokenurl = 'https://vvvdev.apimanagement.us2.hana.ondemand.com:443/usermgmtapi/v1/oauth2'
serviceurl = 'https://vvvdev.apimanagement.us2.hana.ondemand.com:443/valvoline-dash-web/usermgmtapi/v1'

body = {"client_id": apikey, "client_secret": secret, "grant_type": "client_credentials" }
header = { "Content-Type": "application/x-www-form-encoded"}



logging.basicConfig(filename='bulk.log',level=logging.DEBUG)
logging.getLogger().addHandler(logging.StreamHandler())


#get bearer token
r = requests.post(tokenurl + '/token', body,header)

response = r.json()

token = response['access_token']
#token ='3XpjnKMB6G9SlXsGENfqvvidbez9'

print (token)

header = { "Content-Type": "application/json",
			"Authorization": "Bearer " + token
		}

print(header)

with open('./sample.csv') as csvfile:
	csvreader = csv.DictReader(csvfile, delimiter=';')
	for row in csvreader:
		email  = row['email address'] 
		
		#email  = row['User First Name'] + '.' + row['User Last Name'] + '@' + row['ShipTo'] + '.example.com'


		a = datetime.now()
		#print(payload)

		# get the shipto account id
		#r = requests.get(serviceurl + '/account?accountNumber=' + row['ShipTo'] + '10004040')
		#response = r.json()
		#print(response)
		#account_id = response['id']


		logging.debug('contact %s roles json %s', email, roles )

		sys.exit(0)

		#check if the user exists
		r = requests.get(serviceurl + '/user?email=' + email, headers=header)
		if r.status_code == 200:
			#already exists
			logging.debug('contact %s already exists - Updating Accounts only...', email)
			response = r.json()
			uuid = response['uuid']

			payload = {
				"uuid": uuid,
				"accountid": account_id,
				"accountnum": row['ShipTo']
			}
			#add the shipto account to the user
			r = requests.post(serviceurl + '/user/' + uuid +'/accounts', data=json.dumps(payload), headers=header)
			logging.debug('contact %s alreadt exists - account %s added with status %d', email, account_id, response.status_code )
		else:
			logging.debug('contact %s doesn`t exist - Creating...', email)	
			payload = {
				"username": email,	
				"firstname": row['User First Name'],
				"lastname":	row['User Last Name'],			
				"email":	email,
				"directAccount": account_id,
				"admin": "F",
				"status": "A",
				"level": "1"	
			}

			r = requests.post(serviceurl + '/user', data=json.dumps(payload), headers=header)
			logging.debug('contact %s doesn`t exist - Created: Status %d ...', email, response.status_code)	

			response = r.json()
			uuid = response['uuid']

			# build roles array
			roles = build_roles(row['Roles'], uuid)

			#add the roles account to the user
			r = requests.post(serviceurl + '/user/' + uuid +'/frole', data=json.dumps(roles), headers=header)
			logging.debug('contact %s doesn`t exist - roles %s added with status %d', email, account_id, response.status_code )

		
		b =  datetime.now()
		c = b-a
	
		logging.info('Processed contact %s in %d seconds - status %d', email, c.microseconds/1000000, r.status_code)
