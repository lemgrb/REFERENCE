
SUT: https://jsonplaceholder.typicode.com/

## Pre-requisite
0. Install python
1. Install cmder
2. `$ python -m pip install requests`
3. `$ python`

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

## Basics

### Loop
Access value from dict: `my_json['message']`

Print all keys
```python
for key in my_json.keys():
  print(key)
```

### Add to list
```python
url_list = []
for photo in json_data:
    url_list.append(photo['url'])
```

### List to set, count
```python
url_set = set(url_list)
print(len(url_set))
```

### Sort list
```python
numlist=[3,1,2]
print(sorted(numlist)) # [1, 2, 3]
```

### Substring
```python
price='USD500'
price_number = price[3:]
print(price_number) # 500
```
### Replace
```python
price='5,000'
print(price.replace(',','')) # 5000
```
### Enumerate
```python
for index,product_container in enumerate(product_containers)
    driver.find_element(By.XPATH('//div[%s]'%(index+1)))
```
