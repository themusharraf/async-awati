import asyncio

# async def my_async_function():
#     print("Started")
#     await asyncio.sleep(1)
#     print("Finished")
#
#
# async def main():
#     print("Before")
#     await my_async_function()
#     print("After")
#
#
# asyncio.run(main())
#
# import asyncio
#
#
# async def my_async_function():
#     print("Started")
#     await asyncio.sleep(1)
#     print("Finished")
#
#
# async def main():
#     await my_async_function()
#
#
# asyncio.run(main())

import asyncio


async def function_1():
    await asyncio.sleep(2)
    print("Function 1 finished")


async def function_2():
    await asyncio.sleep(1)
    print("Function 2 finished")


async def main():
    task1 = asyncio.create_task(function_1())
    task2 = asyncio.create_task(function_2())
    await task1
    await task2


asyncio.run(main())
