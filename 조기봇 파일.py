Python 3.9.6 (tags/v3.9.6:db3ff76, Jun 28 2021, 15:26:21) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import discord
>>> import asyncio
>>> 
>>> client = discord.Client()
>>> 
>>> @client.event
async def on_ready(): 
    print("디스코드 봇 로그인이 완료되었습니다.")
    print("디스코드봇 이름:" + client.user.name)
    print("디스코드봇 ID:" + str(client.user.id))
    print("디스코드봇 버전:" + str(discord.__version__))
    print('------')
    await client.change_presence(status=discord.Status.online, activity=discord.Game("!조기온라인해보세요"))

    
>>> @client.event
async def on_message(message): 
    content = message.content 
    guild = message.guild 
    author = message.author 
    channel = message.channel 
    if content.startswith("!조기온라인"): 
        await message.channel.send("안알려줄건데 ㅋ" + message.content) 
    if content == "!좆기": 
        await message.channel.send("ㄹㅇ!")

        
>>> client.run('ODc0NTMzMTEwMTkxMDk5OTQ0.YRIWbQ.mm0RjdOh-KhCbgjNgzem8djU1Sg')
디스코드 봇 로그인이 완료되었습니다.
디스코드봇 이름:조기봇
디스코드봇 ID:874533110191099944
디스코드봇 버전:1.7.3
------

