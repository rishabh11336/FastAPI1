import requests

  
r = requests.post("http://localhost:8000/test/post")
print("POST response", r.text)

r = requests.post("http://localhost:8000/test/post_data", json={"name": "Dote", "age": 18,})
print("POST data 1 response", r.text)
  
r = requests.post("http://localhost:8000/test/post_data", json={"name": "Dote", "age": 18, "country": "Canada"})
print("POST data 2 response", r.text)