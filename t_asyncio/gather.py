import asyncio
import datetime

"""
gather接收的是列表，结果将是一个由所有返回值聚合而成的列表。结果值的顺序与 aws 中可等待对象的顺序一致。
如果 return_exceptions 为 False (默认)，所引发的首个异常会立即传播给等待 gather() 的任务。
aws 序列中的其他可等待对象 不会被取消 并将继续运行
"""


async def async_test(delay: int, content):
    await asyncio.sleep(delay)
    return content


async def exception_test(delay: int, content):
    await asyncio.sleep(delay)
    raise TimeoutError("超时")
    return content


async def main():
    result_list = await asyncio.gather(exception_test(1, "lady"), async_test(2, "killer"), return_exceptions=True)
    return result_list


if __name__ == '__main__':
    print("开始时间:", datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    res = asyncio.run(main())
    print(res)
    print("结束时间:", datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
