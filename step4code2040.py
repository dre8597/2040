import json, requests


myToken = '18f7ae041f26ac48d019bcfbb5f4ab4f'
request = requests.post('http://challenge.code2040.org/api/prefix',json={'token':myToken})
arry = json.loads(request.text)
arry = json.loads(request.text)
prefix= arry['prefix']
words = arry['array']
answer = []
for x in words:
    if x.startswith(prefix):
        answer.append(x)
request1 = requests.post('http://challenge.code2040.org/api/prefix/validate',data={'token':myToken,'array':answer})
print(request1.text)
print answer
print prefix
print arry
