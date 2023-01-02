from fastapi import FastAPI, Query

app = FastAPI()


@app.get('/items')
async def read_items(q: str = Query(..., min_length=3, max_length=3)):
    results = {"items": [{"item_id": "foo"}, {"item_id": "bar"}]}
    if q:
        results.update({"q": q})

    return results


@app.get('/items_list')
async def read_items_list(q: list[str] = Query(..., min_length=3, max_length=3)):
    results = {"items": [{"item_id": "foo"}, {"item_id": "bar"}]}
    if q:
        results.update({"q": q})

    return results
