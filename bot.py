from discord.ext.commands import Bot,Context
from discord import Intents, Message

bot = Bot('>',intents=Intents.all())


# from here you can edit to make more commands


@bot.command()
async def ping(ctx:Context):
    await ctx.send("what the fuck why are you pinging me im tryna sleep")

@bot.event
async def on_message(msg:Message):
    if msg.author.id != bot.user.id:
        if msg.content.lower().startswith("im"):

            await msg.channel.send(f"hi {msg.content[3:]}, i'm dad")
        if msg.content.lower().startswith("i am"):

            await msg.channel.send(f"hi {msg.content[5:]}, i'm dad")
        if msg.content.lower().startswith("i'm"):
            await msg.channel.send(f"hi {msg.content[4:]}, i'm dad")

# do not touch after this
try:
    with open("./token") as f:
        bot.run(f.readline().removesuffix("\n"))
except FileNotFoundError:
    print("No Token has been set")