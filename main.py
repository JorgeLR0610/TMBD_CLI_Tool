import asyncio
import core.tmdb_client 
import argparse

parser = argparse.ArgumentParser()

parser.add_argument('-t', "--type", type=str, help="Type the kind of movies you want to display info about, be it 'playing', 'popular', 'top' or 'upcoming'", required=True, choices=['playing', 'top', 'popular', 'upcoming']) #String by default actually
args = parser.parse_args()

async def fetch_data(type: str):
    return await core.tmdb_client.fetch_data_type(type)

if args.type == 'playing':
    type: str = 'now_playing'
    print(asyncio.run(fetch_data(type)))
elif args.type == 'popular':
    print(asyncio.run(fetch_data(args.type)))
elif args.type == 'top':
    type: str = 'top_rated'
    print(asyncio.run(fetch_data(type)))
elif args.type == 'upcoming':
    print(asyncio.run(fetch_data(args.type)))
else:
    print('Type a valid option')