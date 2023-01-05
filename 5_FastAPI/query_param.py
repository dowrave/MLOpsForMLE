from fastapi import FastAPI

app = FastAPI()

fake_items_db = [{"item_name" : "db"}, {"item_name" : "foo"}, {"item_name" : "bar"}]

@app.get("/items/")
def read_time(skip: int = 0, limit: int = 10):
    return fake_items_db[skip : skip + limit]
