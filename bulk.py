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
			"value": role.strip()
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


now = datetime.now()

#logdate = str('%d%d%d%d%d%d', now.month, now.day, now.year, now.hour, now.minute, now.second)

logging.basicConfig(filename='bulk_.log',level=logging.INFO)
logging.getLogger().addHandler(logging.StreamHandler())


#get bearer token
r = requests.post(tokenurl + '/token',body,header)

response = r.json()

#print (response)
token = response['access_token']

#print (token)

header = { "Content-Type": "application/json",
			"Authorization": "Bearer " + token
		}

#print(header)

with open('./sample.csv') as csvfile:
	csvreader = csv.DictReader(csvfile, delimiter=';')
	for row in csvreader:
		ncontacts = 0
		nroles = 0
		naccounts = 0

		email  = row['email address'] 
		
		#email  = row['User First Name'] + '.' + row['User Last Name'] + '@' + row['ShipTo'] + '.example.com'


		a = datetime.now()
		#print(payload)

		# get the shipto account id
		r = requests.get(serviceurl + '/account?accountNumber=' + row['ShipTo'] + '10004040',  headers=header)
		response = r.json()
		#print(response)
		if r.status_code==200 and len(response)>0:
			account_id = response[0]['id']
			logging.debug('contact %s - retrieve account %s id %s - exists...', email, account_id, row['ShipTo'])
		else:
			logging.debug('contact %s - retrieve account %s - doesnt exist - code: %d...', email, row['ShipTo'], r.status_code)
			continue

		#check if the user exists
		r = requests.get(serviceurl + '/user?email=' + email, headers=header)
		response = r.json()		
		#print(response)

		if r.status_code == 200 and len(response)>0:
			#already exists
			logging.debug('contact %s already exists - Updating Accounts only...', email)

			uuid = response[0]['uuid']

			payload = {
				"uuid": uuid,
				"accountid": account_id
			}
			#add the shipto account to the user
			logging.debug(serviceurl + '/user/' + uuid +'/accounts' )
			logging.debug(json.dumps(payload))
			r = requests.post(serviceurl + '/user/' + uuid +'/accounts', data=json.dumps(payload), headers=header)
			logging.debug('contact %s alreadt exists - account %s added with status %d', email, account_id, r.status_code )
			if r.status_code == 200 or r.status_code == 201:
				naccounts = naccounts + 1
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
			logging.debug('contact %s doesn`t exist - Created: Status %d ...', email, r.status_code)	
			if r.status_code == 200 or r.status_code == 201:
				response = r.json()
				uuid = response['uuid']
				ncontacts = ncontacts + 1

				# build roles array
				roles = build_roles(row['Roles'], uuid)
				logging.debug('contact %s roles json %s', email, roles )

				#add the roles account to the user
				r = requests.post(serviceurl + '/user/' + uuid +'/frole', data=json.dumps(roles), headers=header)
				logging.debug('contact %s doesn`t exist - roles %s added with status %d', email, account_id, r.status_code )
				if r.status_code == 200 or r.status_code == 201:
					nroles = nroles + 1
			else:
				logging.debug('contact %s doesn`t exist - unable to create -  status %d', email, r.status_code )
				
		
		b =  datetime.now()
		c = b-a
	
		logging.info('Processed contact %s in %2f seconds - created %d contacts %d roles %d accounts.', email, c.microseconds/1000000, ncontacts, nroles, naccounts)
