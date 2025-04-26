# client.py
import asyncio
import websockets

async def test():
    uri = "ws://localhost:8765"
    while True:
        try:
            async with websockets.connect(uri) as websocket:
                while True:
                    message = input("请输入要发送的消息 (输入 'exit' 退出): ")
                    if message.lower() == 'exit':
                        print("退出程序")
                        return
                    print(f"发送消息: {message}")
                    await websocket.send(message)

                    response = await websocket.recv()
                    print(f"收到响应: {response}")
        except (websockets.exceptions.ConnectionClosedError, asyncio.TimeoutError) as e:
            print(f"连接断开或超时，尝试重新连接: {e}")
            await asyncio.sleep(5)  # 等待5秒后重试连接

if __name__ == "__main__":
    asyncio.run(test())