# server.py
import asyncio
import websockets
from websockets.exceptions import ConnectionClosedError

async def echo(websocket):
    try:
        async for message in websocket:
            print(f"Received message: {message}")
            await websocket.send(f"Echo: {message}")
    except ConnectionClosedError:
        print("Client connection closed")
    except Exception as e:
        print(f"Error occurred: {e}")

async def main():
    # 设置 ping_interval 和 ping_timeout 参数来控制心跳检测
    async with websockets.serve(
        echo,
        "localhost",
        8765,
        ping_interval=20,    # 每20秒发送一次ping
        ping_timeout=20,     # ping超时时间为20秒
        close_timeout=10     # 关闭连接的超时时间为10秒
    ):
        print("WebSocket server started on ws://localhost:8765")
        await asyncio.Future()  # run forever

if __name__ == "__main__":
    asyncio.run(main())