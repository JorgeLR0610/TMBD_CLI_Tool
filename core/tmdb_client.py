import httpx
import os
from dotenv import load_dotenv

load_dotenv()

async def fetch_now_playing():
    base: str = "https://api.themoviedb.org/3/movie/now_playing"
    
    headers = {
        "accept": "application/json",
        "Authorization": os.getenv("access_token")
    }
    
    params: dict = {
        "language": "en-US",
        "page": 1
    }
    
    async with httpx.AsyncClient() as client:
        resp = await client.get(base, headers=headers, params=params, timeout=30)
        resp.raise_for_status()
    
    data = resp.json()
    return data