import httpx
import os
from dotenv import load_dotenv
from fastapi import HTTPException

load_dotenv()

async def fetch_data_type(type: str):
    base: str = f"https://api.themoviedb.org/3/movie/{type}"
    
    headers = {
        "accept": "application/json",
        "Authorization": os.getenv("access_token")
    }
    
    params: dict = {
        "language": "en-US",
        "page": 1
    }
    
    try:
        async with httpx.AsyncClient() as client:
            resp = await client.get(base, headers=headers, params=params, timeout=30)
            resp.raise_for_status()
            data = resp.json()
        
    except httpx.HTTPStatusError as e: # Case 1: The API returned an error code, like 404, 505 or whatever
        print(f'API error: {e.response.status_code}')
        
        raise HTTPException( # Throw error onto the main program
            status_code=e.response.status_code,
            detail=f"Error fetching movies: {e.response.text}"
        )
        
    except httpx.RequestError as e: # Case 2: Connection error (Timeout, dns, no internet)
        print(f"Conection error: {e}")
        
        raise HTTPException(# Throw error onto the main program
            status_code=503, # Service unavailable
            detail="It wasn't possible to connect with the external movie service"
        )
        
    except Exception as e:
        print(f"Unexpected error: {e}")
        
        raise HTTPException(
            status_code=500,
            detail="Internal server error"
        ) 
        
    return data