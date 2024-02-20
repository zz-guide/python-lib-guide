import asyncio
import datetime
"""
认识协程
"""


async def task():
    print("=== task START ===")
    await asyncio.sleep(5)
    print("=== task END ===")


async def task1():
    print("=== task1 START ===")
    await asyncio.sleep(3)
    print("=== task1 END ===")


async def main():
    print("=== main START ===")
    """
    需要并发的话，先create_task，后await
    """
    _task = asyncio.create_task(task())
    _task1 = asyncio.create_task(task1())

    await _task
    await _task1  # 没执行完是不会继续向下的
    print("干扰代码")

    print("=== main END ===")


if __name__ == '__main__':
    print("开始时间:", datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    asyncio.run(main())
    print("结束时间:", datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
