import csv
import requests
import time
import sys
import json
from datetime import datetime

apikey = 'sCeuYG7DWFP6wGhn8rIIzZMNKUbFH1XQ'
secret = 'FtBJYUnCc5urVqSv'
tokenurl = 'https://vvvqa.apimanagement.us2.hana.ondemand.com:443/usermgmtapi/v1/oauth2'
serviceurl = 'https://vvvqa.apimanagement.us2.hana.ondemand.com:443/valvoline-dash-web/usermgmtapi/v1'

body = {"client_id": apikey, "client_secret": secret, "grant_type": "client_credentials" }
header = { "Content-Type": "application/x-www-form-encoded"}

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

with open('./ecomm.csv') as csvfile:
	csvreader = csv.DictReader(csvfile, delimiter=';')
	for row in csvreader:
		email  = row['User First Name'] + '.' + row['User Last Name'] + '@' + row['ShipTo'] + '.example.com'

		payload = {
			"username": row['email address'],	
			"firstname": row['User First Name'],
			"lastname":	row['User Last Name'],			
			"email":	row['email address'],
			  "directAccount": "0013700000ASCoQAAX",
			"admin": "F",
			"status": "A",
			"level": "1"	
		}

		a = datetime.now()
		print(payload)

		r = requests.post(serviceurl + '/user', data=json.dumps(payload), headers=header)
		
		#time.sleep(1);
		b =  datetime.now()
		c = b-a

		print(email, c.microseconds/1000000, r.status_code)
		sys.stdout.flush()
		
		with open ('./log.csv', 'w') as logfile:
			wr = csv.writer(logfile, quoting=csv.QUOTE_MINIMAL)
			wr.writerow([row['email address'], r.status_code, c.microseconds / 1000000])
