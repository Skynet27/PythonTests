import asyncio
import websockets

name = input("Adj meg egy nevet: ")
age = input("Add meg az életkorod: ")


async def main():
    uri = "ws://localhost:8765"
    async with websockets.connect(uri) as websocket:
        msg = input("Üzeneted: ")
        if msg == "":
            msgTo = f"{name}|{age}"
        else:
            msgTo = f"{name}|{age}|{msg}"
        await websocket.send(msgTo)

        while True:
            recv_msg = await websocket.recv()
            if not (recv_msg):
                return False
            msgR = recv_msg.split("|")
            msgFrom = ""
            if msgR[0] == name:
                if len(recv_msg) < 3:
                    msgFrom = f"{msgR[0]}({msgR[1]}) csatlakozott a chathez."
                elif len(recv_msg) == 3:
                    msgFrom = f"{msgR[0]}({msgR[1]}) üzenete > {msgR[2]}"
                print(msgFrom)
            else:
                continue

asyncio.get_event_loop().run_until_complete(main())
asyncio.get_event_loop().run_forever()
