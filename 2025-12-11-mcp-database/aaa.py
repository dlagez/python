from toolbox_core import ToolboxClient
import asyncio

async def main():
    async with ToolboxClient("http://74.48.1.91:5001") as client:
        tools = await client.load_toolset("toolset_name")
        print(tools)

# 执行异步函数
asyncio.run(main())
