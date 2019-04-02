import asyncio,aiohttp

async def fetch_async(url):
    print(url)
    async with aiohttp.request("GET",url) as r:
        #或者直接await r.read()不编码，直接读取，适合于图像等无法编码文件
        reponse = await r.text(encoding="utf-8")
        #print(reponse)
        print("end")

tasks = [fetch_async('http://www.baidu.com/'), fetch_async('http://www.chouti.com/')]

event_loop = asyncio.get_event_loop()
results = event_loop.run_until_complete(asyncio.gather(*tasks))
event_loop.close()