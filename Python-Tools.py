import discord # 기본 디스코드을 셋팅해 주는 것이며 인스톨해주셔야 합니다.
# pip install discord

client = discord.Client()

# TOKEN(토큰), PREFIX(접두사)에 각각 PREFIX(접두사)나 TOKEN(토큰) 넣으주시면 되요.
TOKEN = "" 
PREFIX = ""

@client.event
async def on_ready(): #이것은 봇이 온라인 상태 즉 준비되었을때
  print("Ready the Bots!") # Console 창에 "Ready to the Bots" 이라고 띄어주는 겁니다. 원하는대로 바꿔 주셔서 쓰셔도 무관합니다.
  game = discord.Game(name="") # 이곳은 플레이중을 어떻게 표시할지을 이야기하는거예요
  await client.chage_persence(status=discord.Status.online,activity=game) #discord.Status 이거는 봇의 상태을 예기 해요

# online 초록색 - 온라인
# idle 노랑색 - 자리비움
# dnd 빨강색 - 다른 용무 중
# offline 회색 - 오프라인
# 어떤 상태든 간에 일단 모두 작동하지만 온라인 이것을 선호합니다.

client.run(TOKEN)
