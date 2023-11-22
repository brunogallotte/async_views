import asyncio
from time import sleep
from random import shuffle
import httpx
from django.http import HttpResponse


async def http_call_async():
    karts = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]
    shuffle(karts)
    cont = 0

    for kart in karts:
        cont += 1
        await asyncio.sleep(1)
        print(f'The user id: {cont} was drawn with the kart: {kart}')
    async with httpx.AsyncClient() as client:
        r = await client.get("https://httpbin.org")
        print(r)

async def async_view(request):
    loop = asyncio.get_event_loop()
    loop.create_task(http_call_async())
    return HttpResponse('Non-blocking HTTP request')
