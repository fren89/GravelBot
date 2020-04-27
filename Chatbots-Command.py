import discord

client = discord.Client()

TOKEN = "" 
PREFIX = ""

@client.event
async def on_ready():
  print("Ready the Bots!")
  game = discord.Game(name="")
  await client.chage_persence(status=discord.Status.online,activity=game)

@client.event
async def on_message(message):
  if message.content.startswith(PREFIX + "안녕"):
    return await message.channel.send("안녕") # 이걸 복사해서 채팅봇을 만들 수 있습니다.


client.run(TOKEN)
