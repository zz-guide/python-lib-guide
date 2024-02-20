import asyncio
import datetime

"""
wait_for, 超时会取消可等待对象，会抛出异常，但是参数只接收一个coroutine
"""


async def task4():
    print("=== task4 START ===")
    await asyncio.sleep(5)
    print("=== task4 END ===")


async def task5():
    print("=== task5 START ===")
    await asyncio.sleep(3)
    print("=== task5 END ===")


async def main():
    try:
        await asyncio.wait_for(task4(), timeout=2)
    except asyncio.TimeoutError:
        print("任务超时...")


if __name__ == '__main__':
    print("开始时间:", datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    asyncio.run(main())
    print("结束时间:", datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
