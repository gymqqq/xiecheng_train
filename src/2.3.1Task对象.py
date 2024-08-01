import asyncio


async def func():
    print(1)
    await asyncio.sleep(2)
    print(2)
    return '返回值'

async def main():
    print("main开始")

    # 创建Task对象，将当前执行func函数任务添加到事件循环
    task1 = asyncio.create_task(func())
    # 创建Task对象，将当前执行func函数任务添加到事件循环
    task2 = asyncio.create_task(func())
    print("main结束")
    # 当执行某协程遇到I0操作时，会自动化切换执行其他任务。
    # 此处的await是等待相对应的协程全都执行完毕并获取结果
    ret1 = await task1
    ret2 = await task2
    print(ret1, ret2)
asyncio.run(main())