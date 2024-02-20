import asyncio
import datetime

"""
并发执行协程函数等，返回done和pending状态的任务对象集合
"""


async def task2():
    print("=== task2 START ===")
    await asyncio.sleep(5)
    print("=== task2 END ===")


async def task3():
    print("=== task3 START ===")
    await asyncio.sleep(3)
    print("=== task3 END ===")


def main():
    return asyncio.wait([task2(), task3()])


if __name__ == '__main__':
    print("开始时间:", datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    asyncio.run(main())
    print("结束时间:", datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
