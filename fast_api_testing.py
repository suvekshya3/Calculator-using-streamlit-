import requests

API_URL = "http://127.0.0.1:8000/"

#filter__pram={"age": 20}
#response=requests.get(f"{API_URL}/students", params=filter__pram)
#print(response.json())
#print(response.status_code)
user_data={"name":"Subekshya", "age": 21, "college": "XYZ University"}
response = requests.post(f"{API_URL}/students/3", json=user_data)
print(response.status_code)