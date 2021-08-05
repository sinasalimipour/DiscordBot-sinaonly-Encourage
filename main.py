

import discord
import os
import requests
import json

TOKEN= 'token here'

client = discord.Client()

def get_quote():
  resource=requests.get("https://zenquotes.io/api/random")

  json_data = json.loads(resource.text)

  quote= json_data[0]['q']+" -" + json_data[0]['a']
  return(quote)




@client.event
async def on_ready():
  print('we have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('$inspire'):
    quote = get_quote()
    await message.channel.send(quote)

client.run(TOKEN)
