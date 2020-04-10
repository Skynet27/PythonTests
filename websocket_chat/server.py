import asyncio
import websockets


async def hello(websocket, path):
    recv_msg = (await websocket.recv()).split("|")

    if len(recv_msg) < 3:
        msg = f"{recv_msg[0]}({recv_msg[1]}) csatlakozott a chathez."
    elif len(recv_msg) == 3:
        msg = f"{recv_msg[0]}({recv_msg[1]}) üzenete > {recv_msg[2]}"
    print(msg)
    await websocket.send(recv_msg)

start_server = websockets.serve(hello, "localhost", 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
