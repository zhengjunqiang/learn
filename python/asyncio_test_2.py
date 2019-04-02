import asyncio
import time
from functools import partial

async def get_html(url):
    print("start get url")
    await asyncio.sleep(2)
    return "ywh"

def callback(url, future):
    print(url)
    print("send email to ywh")

start_time = time.time()
loop = asyncio.get_event_loop()
# get_future = asyncio.ensure_future(get_html("http://www.imooc.com"))
task = loop.create_task(get_html("http://www.imooc.com"))   # 创建一个任务，返回Future对象
task.add_done_callback(             
    partial(callback, "http://www.imooc.com")           # 把callback包装可接收参数的偏函数
)       # 执行get_html，完成后调用回调函数callback，最后再返回get_html的结果
loop.run_until_complete(task)

print(task.result())        # 获取Future对象的结果