import asyncio

# print_sum协程嵌套await_compute协程
async def compute(x, y):                
    print("Compute %s + %s ..." %(x, y))
    await asyncio.sleep(1.0)                    # 3
    print("Compute %s + %s ..." %(x, y))
    return x + y                                # 4
    
async def print_sum(x, y):
    result = await compute(x, y)                # 2
    print("%s + %s = %s" %(x, y, result))       # 5

loop = asyncio.get_event_loop()
loop.run_until_complete(print_sum(1, 2))        # 1
loop.close()
print("code end")