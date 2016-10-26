import json, requests

def reverseString(word):
    return word[::-1] #just slice it

myToken = '18f7ae041f26ac48d019bcfbb5f4ab4f'
request = requests.post('http://challenge.code2040.org/api/reverse',json={'token':myToken})
reverse = reverseString(request.text)
request1 = requests.post('http://challenge.code2040.org/api/reverse/validate',json={'token':myToken,'string':reverse})
