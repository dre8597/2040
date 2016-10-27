import json, requests

myToken = '18f7ae041f26ac48d019bcfbb5f4ab4f'
request = requests.post('http://challenge.code2040.org/api/haystack',json={'token':myToken})
arry = json.loads(request.text)
needle = arry['needle']
hay = arry['haystack']
index = 0
for x in hay:
    if x == needle:
        break
    else:
        index+=1
request1 = requests.post('http://challenge.code2040.org/api/haystack/validate',json={'token':myToken,'needle':index})
print(request1.text)
