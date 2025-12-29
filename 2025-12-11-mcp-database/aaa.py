from toolbox_core import ToolboxClient
import asyncio

async def main():
    async with ToolboxClient("http://74.48.1.91:5000") as client:
        # 使用正确的 toolset 名称
        tools = await client.load_toolset("my-toolset")
        print(tools)

asyncio.run(main())
