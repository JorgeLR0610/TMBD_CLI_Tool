from fastapi import FastAPI
import core.tmdb_client 

app =  FastAPI()

@app.get("/now_playing")
async def now_playing():
    return await core.tmdb_client.fetch_now_playing()