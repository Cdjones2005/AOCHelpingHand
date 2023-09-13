import discord
from discord import app_commands
from discord.ext import commands
from bs4 import BeautifulSoup
import requests
import random

URL = "https://www.pathways.me/career-roadmaps"
r = requests.get(URL)

soup = BeautifulSoup(
  r.content, 'html5lib'
)  # If this line causes an error, run 'pip install html5lib' or install html5lib
art = soup.find('fluid-columns-repeater',
                attrs={'container-id': 'comp-ldvz0g16_wrapper'})
business = soup.find('fluid-columns-repeater',
                     attrs={'container-id': 'comp-ldwbo63e4_wrapper'})
businessID = 'comp-ldwbo63p4'
health = soup.find('fluid-columns-repeater',
                   attrs={'container-id': 'comp-ldwc9qtu2_wrapper'})
healthID = 'comp-ldwc9qud4'
humanities = soup.find('fluid-columns-repeater',
                       attrs={'container-id': 'comp-ldwcbark5_wrapper'})
humanitiesID = 'comp-ldwcbas8'
law = soup.find('fluid-columns-repeater',
                attrs={'container-id': 'comp-ldwh9not3_wrapper'})
lawID = 'comp-ldwh9npl'
math = soup.find('fluid-columns-repeater',
                 attrs={'container-id': 'comp-ldwihzvg3_wrapper'})
mathID = 'comp-ldwihzwd4'
engineering = soup.find('fluid-columns-repeater',
                        attrs={'container-id': 'comp-ldwitifj_wrapper'})
engineeringID = 'comp-ldwitign4'
social = soup.find('fluid-columns-repeater',
                   attrs={'container-id': 'comp-ldwj3yx91_wrapper'})
socialID = 'comp-ldwj3yyi2'
environment = soup.find('fluid-columns-repeater',
                        attrs={'container-id': 'comp-ldwjtiv93_wrapper'})
environmentID = 'comp-ldwjtiwl'

names = []
imgs = []

for row in art.find_all_next(
    'div', attrs={'class': 'comp-ldvz0g3z1 YzqVVZ wixui-repeater__item'}):

  names.append(
    art.find('div',
             attrs={
               'data-mesh-id': row['id'] + 'inlineContent-gridContainer'
             }).h6.text)
  imgs.append(
    art.find('div',
             attrs={
               'data-mesh-id': row['id'] + 'inlineContent-gridContainer'
             }).img["src"])

for row in business.find_all_next(
    'div', attrs={'class': businessID + 'YzqVVZ wixui-repeater__item'}):

  names.append(
    business.find('div',
                  attrs={
                    'data-mesh-id': row['id'] + 'inlineContent-gridContainer'
                  }).h6.text)
  imgs.append(
    business.find('div',
                  attrs={
                    'data-mesh-id': row['id'] + 'inlineContent-gridContainer'
                  }).img["src"])

for row in health.find_all_next(
    'div', attrs={'class': healthID + ' YzqVVZ wixui-repeater__item'}):

  names.append(
    health.find('div',
                attrs={
                  'data-mesh-id': row['id'] + 'inlineContent-gridContainer'
                }).h6.text)
  imgs.append(
    health.find('div',
                attrs={
                  'data-mesh-id': row['id'] + 'inlineContent-gridContainer'
                }).img["src"])

for row in humanities.find_all_next(
    'div', attrs={'class': humanitiesID + ' YzqVVZ wixui-repeater__item'}):

  names.append(
    humanities.find('div',
                    attrs={
                      'data-mesh-id': row['id'] + 'inlineContent-gridContainer'
                    }).h6.text)
  imgs.append(
    humanities.find('div',
                    attrs={
                      'data-mesh-id': row['id'] + 'inlineContent-gridContainer'
                    }).img["src"])

for row in law.find_all_next(
    'div', attrs={'class': lawID + ' YzqVVZ wixui-repeater__item'}):

  names.append(
    law.find('div',
             attrs={
               'data-mesh-id': row['id'] + 'inlineContent-gridContainer'
             }).h6.text)
  imgs.append(
    law.find('div',
             attrs={
               'data-mesh-id': row['id'] + 'inlineContent-gridContainer'
             }).img["src"])

for row in math.find_all_next(
    'div', attrs={'class': mathID + ' YzqVVZ wixui-repeater__item'}):

  names.append(
    math.find('div',
              attrs={
                'data-mesh-id': row['id'] + 'inlineContent-gridContainer'
              }).h6.text)
  imgs.append(
    math.find('div',
              attrs={
                'data-mesh-id': row['id'] + 'inlineContent-gridContainer'
              }).img["src"])

for row in engineering.find_all_next(
    'div', attrs={'class': engineeringID + ' YzqVVZ wixui-repeater__item'}):

  names.append(
    engineering.find('div',
                     attrs={
                       'data-mesh-id':
                       row['id'] + 'inlineContent-gridContainer'
                     }).h6.text)
  imgs.append(
    engineering.find('div',
                     attrs={
                       'data-mesh-id':
                       row['id'] + 'inlineContent-gridContainer'
                     }).img["src"])

for row in social.find_all_next(
    'div', attrs={'class': socialID + ' YzqVVZ wixui-repeater__item'}):

  names.append(
    social.find('div',
                attrs={
                  'data-mesh-id': row['id'] + 'inlineContent-gridContainer'
                }).h6.text)
  imgs.append(
    social.find('div',
                attrs={
                  'data-mesh-id': row['id'] + 'inlineContent-gridContainer'
                }).img["src"])

for row in environment.find_all_next(
    'div', attrs={'class': environmentID + ' YzqVVZ wixui-repeater__item'}):

  names.append(
    environment.find('div',
                     attrs={
                       'data-mesh-id':
                       row['id'] + 'inlineContent-gridContainer'
                     }).h6.text)
  imgs.append(
    environment.find('div',
                     attrs={
                       'data-mesh-id':
                       row['id'] + 'inlineContent-gridContainer'
                     }).img["src"])

id = 1065713474157690960
bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())
channel = bot.get_channel(id)


@bot.event
async def on_ready():
  print('connected to Discord!')
  try:
    synced = await bot.tree.sync()
    print(f"synced {len(synced)} commands")
  except Exception as e:
    print(e)


@bot.event
async def on_message(message):
  if message.content.lower() == "help":
    await message.channel.send("please use /")


@bot.tree.command(name="test")
async def test(interaction: discord.Interaction):
  tester = random.randint(0, len(names) + 1)
  embed = discord.Embed(title="Bot Commands")
  embed.set_thumbnail(url=imgs[tester])
  #await interaction.response.send_message(imgs[tester] + " " + names[tester], ephemeral=False)
  await interaction.response.send_message(embed=embed, ephemeral=False)


bot.run(
  'MTA3MDY3NjkyODczMTgxMTkxMA.GGgyjF.XXHjUgkM-COjcZSTHeKUPIrKhQK4j9p_Lb9x3A')
