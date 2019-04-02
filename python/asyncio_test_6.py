import asyncio

def callback(sleep_times, loop):
    print("success time {}".format(loop.time()))

def stoploop(loop):
    loop.stop()

loop = asyncio.get_event_loop()
now = loop.time()
loop.call_at(now + 2, callback, 2, loop)    # 当前时间的2s后执行
loop.call_at(now + 1, callback, 1, loop)
loop.call_at(now + 3, callback, 3, loop)
# loop.call_soon(stoploop, loop)              # 退出循环
loop.call_soon(callback, 4, loop)           # 立刻执行（在队列中等待到下一个循环即执行），另外还有call_later

# 处理共享变量的线程安全问题可以使用call_soon_threadsafe
loop.run_forever()