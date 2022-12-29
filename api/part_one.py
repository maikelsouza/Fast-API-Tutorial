from fastapi import FastAPI

app = FastAPI()


@app.get('/', description="This is our first get route.")
async def base_get_route():
    return {"message: Hello Word"}


@app.post('/', description="This is our first post route")
async def base_post_route():
    return {"message": "Hello from the post route"}


@app.put('/', description="This is our first put route")
async def base_put_route():
    return {"message": "Hello from the put route"}