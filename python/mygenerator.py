import asyncio
import time

# 定义异步函数
async def get_html(url):
    print("start get url")
    await asyncio.sleep(2)
    #time.sleep(5)   # 协程是单线程执行，time.sleep是同步阻塞接口，不应在协程中实现
    print("end get url")

start_time = time.time()
loop = asyncio.get_event_loop()     # 创建事件循环（单线程：所有的函数调用都在loop中执行）
tasks = [
    get_html("http://www.imooc.com") for i in range(10)
]
loop.run_until_complete(asyncio.wait(tasks))    # 类似join，等待协程执行完成才往下执行
print(time.time() - start_time)