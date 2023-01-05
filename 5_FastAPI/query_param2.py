from fastapi import FastAPI

app = FastAPI()

@app.get("/items/{item_id}")
def read_user_time(item_id: str, needy: str):
    item = {"item_id" : item_id, "needy":needy}
    return item
