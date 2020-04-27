import discord

client = discord.Client()

TOKEN = "" 
PREFIX = ""

@client.event
async def on_ready():
  print("Ready the Bots!")
  game = discord.Game(name="")
  await client.change_presence(status=discord.Status.online,activity=game)

# online 초록색 - 온라인
# idle 노랑색 - 자리비움
# dnd 빨강색 - 다른 용무 중
# offline 회색 - 오프라인
# 어떤 상태든 간에 일단 모두 작동하지만 온라인 이것을 선호합니다.

client.run(TOKEN)
