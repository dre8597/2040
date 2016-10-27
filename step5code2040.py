import json, requests, datetime, dateutil.parser


myToken = '18f7ae041f26ac48d019bcfbb5f4ab4f'
request = requests.post('http://challenge.code2040.org/api/dating',json={'token':myToken})
arry = json.loads(request.text)
date= arry['datestamp']
timeAdd = arry['interval']
date = datetime.datetime.strptime(str(dateutil.parser.parse(date))[:-6], '%Y-%m-%d %H:%M:%S')
newTime= date + datetime.timedelta(seconds=timeAdd)
#hard coding in yay
strTime= str(newTime) + 'Z'
strTime = strTime.replace(' ', 'T')
request1 = requests.post('http://challenge.code2040.org/api/dating/validate',data={'token':myToken,'datestamp':strTime})
print(request1.text)
