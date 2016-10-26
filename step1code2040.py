import json, requests

myToken = '18f7ae041f26ac48d019bcfbb5f4ab4f'
myGit= 'https://github.com/nperello/2040'
request = requests.post('http://challenge.code2040.org/api/register', json={'token':myToken,'github':myGit})
print(request.text)
