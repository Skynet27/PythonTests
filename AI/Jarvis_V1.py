import os
import discord
import time
import sys

from discord.ext import commands

client = commands.Bot(command_prefix = '.')

turnOff = {"shutdown","takarodj", "aludni","gosleep","sleep","please"}

def checkMSG(msg, channelID):
    msg1 = str(msg.content).lower()
    channel = client.get_channel(468462376455372801)
    for word in msg1.split():
        if word in turnOff:
            print("Turning off!")
            #await channel.send("Megyek aludni.")
            time.sleep(5)
            sys.exit(0)
    else:
        print("ismeretlen történet!")
        #await channel.send("Nem értem!")

@client.event
async def on_ready():
    print('Bot is online: ' f'{client.user}')
    channel = client.get_channel(468462376455372801)
    await channel.send("Szép jónapot kívánok!")

@client.event
async def on_message(msg):
    if msg.author == client.user:
        return
    name = str(msg.author)
    content = msg.content

    file = open("log.txt","a")
    file.write(time.asctime( time.localtime(time.time()) ) + ": " + name + " üzenetet küldött: '" + content + "'" + "\n")
    file.close()
    print(f"{name} küldött egy üzenetet. '{content}' ")
    #checkMSG(msg, msg.channel)
    if content=="Menj aludni!":
        print("Turning off!")
        await msg.channel.send("Rendben, jó éjt! :(")
        time.sleep(5)
        sys.exit(0)

    #await msg.channel.send(f"{msg.author} te LOG-ba vagy véve, amit küldtél!! Eskü, nem figyelünk. ;)")

client.run("NjkyMDIzNjE4MDE1NzIzNTMy.XoD7_A.c2CYQWCRlxH4EjTIdeN7cIm0xrA")
