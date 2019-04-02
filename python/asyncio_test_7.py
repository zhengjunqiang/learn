import asyncio
from concurrent.futures import ThreadPoolExecutor
import socket
import time
from urllib.parse import urlparse

def get_url(url):
    url = urlparse(url)
    host = url.netloc
    path = url.path
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # client.setblocking(False)
    client.connect((host, 80))  
    client.send("GET {} HTTP/1.1\r\nHost:{}\r\nConnection:close\r\n\r\n".format(path, host).encode("utf8"))
    data = b""
    while True:
        d = client.recv(1024)
        if d:
            data += d
        else:
            break

    data = data.decode("utf8")
    html_data = data.split("\r\n\r\n")[1]
    print(html_data)
    client.close()

start_time = time.time()
loop = asyncio.get_event_loop()
executor = ThreadPoolExecutor(3)
tasks = []
for url in range(20):
    url = "http://shop.projectsedu.com/goods/{}/".format(url)
    print(url)
    task = loop.run_in_executor(executor, get_url, url)     # 指定线程池，将阻塞IO操作放入loop中，不影响系统运行
    # 把线程中的future包装成协程的future
    tasks.append(task)
loop.run_until_complete(asyncio.wait(tasks))
print("last time:{}".format(time.time() - start_time))