import discord

intents = discord.Intents.default()

client = discord.Client(intents=intents)

#起動時処理

@client.event
async def on_ready():
    for channel in client.get_all_channels():
        print("----------")
        print("channel name:" + str(channel.name))
        print("channel ID:" + str(channel.id))
        print("----------")

# Botのトークンを指定（デベロッパーサイトで確認可能）
client.run("***********************************************")
