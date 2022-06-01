from pydantic import BaseModel
from typing import Optional
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def hello_world():
    return "Hello World"


@app.get("/test/get")
async def test_get_request() -> str:
  return "GET request works!"
  
@app.get("/test/get_params")
async def test_get_params_request(name: str) -> str:
  return f"GET request with param, {name = }"
  
@app.get("/test/get_params2")
async def test_get_params_request2(
    name: str, 
    age: int, country: 
    str = "India (Default)"
  ) -> str:
  
  return f"GET request with param, {name = }, {age = }, {country = }"


class SampleData(BaseModel):
  name: str
  age: int
  country: str = "India (Default)"

@app.post("/test/post")
async def test_post() -> str:
  return "POST request works!"

@app.post("/test/post_data")
async def test_post_data(data: SampleData):
  return data

#llllllllllllllllllllllllllllllllllllllllllllllllllllllllllllll

@app.put("/test/put")
async def test_put_data(data: SampleData):
  return {
    "type": "PUT",
    "data": data,
  }

@app.patch("/test/patch")
async def test_patch_data(data: SampleData):
  return {
    "type": "PATCH",
    "data": data,
  }

@app.delete("/test/patch")
async def test_delete_data():
  return {
    "type": "DELETE",
    "data": None,
  }