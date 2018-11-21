"""
    Azure Functions HTTP Example Code for Python
    
    Created by Anthony Eden
    http://MediaRealm.com.au/
    
    pglynn - Added code to process input from log forwarding profile on PANW NGFW
"""

import sys, os, httplib, json, urllib, ast
sys.path.append(os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'lib')))
from AzureHTTPHelper import HTTPHelper

# This is a little class used to abstract away some basic HTTP functionality
http = HTTPHelper()

#c = httplib.HTTPSConnection("ccc.de")
#c.request("GET", "/")
#response = c.getresponse()
#print response.status, response.reason
#data = response.read()
#print data

# All these print statements get sent to the Azure Functions live log
print "--- GET ---"
print http.get
print

print "--- POST ---"
print http.post
print

print "--- HEADERS ---"
print http.headers
print

print "--- OTHER ENVIRONMENTAL VARIABLES ---"
for x in http.env:
    print x
print
"""
ARMResource = 'https://management.core.windows.net/'

ClientSecret = str(http.post['ClientSecret'])[2:-4]

ResourceGroupName = str(http.post['ResourceGroupName'])[2:-4]

ClientID = str(http.post['ClientID'])[2:-4]

TenantID = str(http.post['TenantID'])[2:-4]

Attacker = str(http.post['Attacker'])[2:-2]

NetworkSecurityGroupName = str(http.post['NetworkSecurityGroupName'])[2:-4]

SubscriptionID = str(http.post['SubscriptionID'])[2:-4]

Region = str(http.post['Region'])[2:-4]

Host = 'login.windows.net'

URL = '/' + TenantID + '/oauth2/token/'

Headers = { 'User-Agent': 'python', 'Content-Type': 'application/x-www-form-urlencoded', }

tempstr = { 'resource' : ARMResource, 'client_id' : ClientID, 'grant_type' : 'client_credentials', 'client_secret' : ClientSecret }

QueryStr = urllib.urlencode(tempstr)

conn = httplib.HTTPSConnection(Host)

conn.request("POST", URL, QueryStr, Headers)

response = conn.getresponse()

data = response.read()

datadict = ast.literal_eval(data)

AccessToken = datadict['access_token']

Host = 'management.azure.com'

URL = '/subscriptions/' + SubscriptionID + '/resourceGroups/' + ResourceGroupName + '/providers/Microsoft.Network/networkSecurityGroups/' + NetworkSecurityGroupName + '/securityRules/' + Attacker + '?api-version=2017-08-01'

Headers = { 'Content-Type': 'application/json', 'Authorization': 'bearer ' + AccessToken }

Body = json.dumps({
  "properties": {
    "protocol": "*",
    "sourceAddressPrefix": Attacker,
    "destinationAddressPrefix": "*",
    "access": "Deny",
    "destinationPortRange": "*",
    "sourcePortRange": "*",
    "priority": 100,
    "direction": "Outbound"
  }
})

conn = httplib.HTTPSConnection(Host)

conn.request("PUT", URL, Body, Headers)

response = conn.getresponse()

data = response.read()

print Host
print ARMResource
print ClientSecret
print ResourceGroupName
print ClientID
print TenantID
print Attacker
print NetworkSecurityGroupName
print SubscriptionID
print QueryStr
print 'Response: ', response.status, response.reason
print 'Data:'
print data
