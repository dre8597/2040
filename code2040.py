import json, requests

t= '18f7ae041f26ac48d019bcfbb5f4ab4f'
mygit= 'https://github.com/nperello/2040'
request = requests.post('http://challenge.code2040.org/api/register', json={'token':t,'github':mygit})
print(request.text)
