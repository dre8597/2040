import json, requests, datetime, dateutil.parser


myToken = '18f7ae041f26ac48d019bcfbb5f4ab4f'
request = requests.post('http://challenge.code2040.org/api/dating',json={'token':myToken})
arry = json.loads(request.text)
date= arry['datestamp']
timeAdd = arry['interval']
print dateutil.parser.parse(date)
print date
