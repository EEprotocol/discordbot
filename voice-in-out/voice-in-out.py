import discord

intents = discord.Intents.default()

client = discord.Client(intents=intents)

# チャンネル入退室時の通知処理
@client.event
async def on_voice_state_update(member, before, after):

    # チャンネルへの入室ステータスが変更されたとき（ミュートON、OFFに反応しないように分岐）
    if before.channel != after.channel:
        # 通知メッセージを書き込むテキストチャンネル（チャンネルIDを指定）
        botRoom = client.get_channel("***********************")

        # 入退室を監視する対象のボイスチャンネル（チャンネルIDを指定）
        # 複数選択が可能
        announceChannelIds = ["****************","+++++++++++++++++++"]

        # 退室通知
        if before.channel is not None and before.channel.id in announceChannelIds:
            await botRoom.send("**" + before.channel.name + "** から、__" + member.name + "__  が抜けました！")
        # 入室通知
        if after.channel is not None and after.channel.id in announceChannelIds:
            await botRoom.send("**" + after.channel.name + "** に、__" + member.name + "__  が参加しました！")

# Botのトークンを指定（デベロッパーサイトで確認可能）
client.run("*************************************************************")
