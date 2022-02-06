from fastapi import FASTAPI

app = FASTAPI()

@app.get("/")
def hello_sillians():
    return {"Hello": "San Francisco!!!"}