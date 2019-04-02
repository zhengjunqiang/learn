import asyncio
import time

async def get_html(sleep_times):
    print("waiting")
    await asyncio.sleep(sleep_times)
    print("done after {}s".format(sleep_times))

tasks = [get_html(2), get_html(3), get_html(4)]     # 模拟三个执行时长不同的任务
loop = asyncio.get_event_loop()
try:
    loop.run_until_complete(asyncio.wait(tasks))
except KeyboardInterrupt as e:                  # 人为制造取消信号：捕捉键盘ctrl + c异常
    all_tasks = asyncio.Task.all_tasks()        # 不需要传入loop：自动从events.get_event_loop中获取loop，并获取loop中的所有task
    for task in all_tasks:                      # 获取所有tasks
        print(task.cancel())                    # 取消task，返回取消结果
    loop.stop()
    loop.run_forever()      # loop调用stop后必须重新调用run_forever，否则会抛出异常
finally:
    loop.close()