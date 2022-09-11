from fastapi import FastAPI

app_test = FastAPI()


@app_test.get("/")
async def root():
    return {"message": "Hello World"}