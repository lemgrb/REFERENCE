SUT: https://jsonplaceholder.typicode.com/

## Pre-requisite
0. Install python
1. Install cmder
2. `$ python -m pip install requests`
4. `$ python`


## GET, POST, PUT, DELETE Requests

GET
```python
import requests
url = 'http://jsonplaceholder.typicode.com/photos'
response = requests.get(url)
print (response.json())
```

POST
```python
jsonPayLoad = {'albumId':1, 'title':'test','url':'nothing.com','thumbnailUrl':'nothing.com'}
response = requests.post(url, json=jsonPayLoad)
response.json()
```

PUT
```python
url = 'http://jsonplaceholder.typicode.com/photos/100'
response = requests.put(url, json=jsonPayLoad)
response.json()
```

DELETE
```python
response = requests.delete(url)
response.json()
```

## Authentication

```python
response = requests.get(url,auth=('djw-test','password1'))
resp = requests.get(url,headers={'Authorization': 'Bearer XXX'})
```