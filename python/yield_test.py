# @Time    : 2018/1/24 10:46
# @Author  : Py.qi
# @File    : yield_xiecheng.py
# @Software: PyCharm

def consumer(name):
    print('开始吃包子...')
    while True:
        print('\033[31;1m[consumer]%s需要包子\033[0m'%name)
        bone = yield   #接收send发送的数据
        print('\033[31;1m[%s]吃了%s个包子\033[0m'%(name,bone))
def producer(obj1):
    obj1.send(None)   #必须先发送None
    for i in range(3):
        print('\033[32;1m[producer]\033[0m正在做%s个包子'%i)
        obj1.send(i)


if __name__ == '__main__':
    con1 = consumer('消费者A')  #创建消费者对象
    producer(con1)
