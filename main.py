import discord
from discord.ext import commands

id = 1065713474157690960
bot = commands.Bot(command_prefix="!", intents = discord.Intents.all())
channel = bot.get_channel(id)

@bot.event
async def on_ready():
  print('connected to Discord!')


@bot.event
async def on_message(message):
  if message.content.lower() == "hello":
    await message.channel.send("Hi")


bot.run(
  'MTA3MDY3NjkyODczMTgxMTkxMA.GGgyjF.XXHjUgkM-COjcZSTHeKUPIrKhQK4j9p_Lb9x3A')
