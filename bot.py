from discord.ext.commands import Bot,Context
from discord import Intents

bot = Bot('>',intents=Intents(messages=True))


# from here you can edit to make more commands


@bot.command()
async def ping(ctx:Context):
    await ctx.send("pong")


# do not touch after this
try:
    with open("./token") as f:
        bot.run(f.readline().removesuffix("\n"))
except FileNotFoundError:
    print("No Token has been set")