from fastapi import FASTAPI

app = FASTAPI()

@app.get("/")
def hello_sillians():
    return {"Hello": "San Francisco!!!"}

@app.get("/")
def read_root():
    return {"Hello": "World"}