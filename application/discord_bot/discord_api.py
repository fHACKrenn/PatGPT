from dotenv import load_dotenv
from discord.ext import commands
import discord
import os
from application.chatgpt_ai.openai import chatgpt_response

load_dotenv()

discord_token = os.getenv('BOT_TOKEN')

class MyClient(discord.Client):
    async def on_ready(self):
      print("Successfully logged in as: ", self.user)

    async def on_message(self, message):
      print(f"{message.author} : {message.content}")
      if message.author == self.user:
        return

      if message == 'checkservers':
        if message.author.id == 710315085414924288:
          await message.channel.send('\n'.join(guild.name for guild in discord.Client.guilds))
          
      command, user_message=None, None

      for text in ['patgpt', 'Patgpt', 'PatGPT', 'patGPT']:
        if message.content.startswith(text):
          command=message.content.split(' ')[0]
          user_message=message.content.replace(text, '')
          print(command, user_message)

      match command:
        case 'patgpt':
          # if len(command) <=6:
          #   bot_response = f"Please include request texts after the prefix!!"
          #   await message.channel.send(bot_response, reference=message)
          # else:
            bot_response = chatgpt_response(prompt=user_message)
            await message.channel.send(bot_response, reference=message)
        case 'Patgpt':
          # if len(command) <=6:
          #   bot_response = f"Please include request texts after the prefix!!"
          #   await message.channel.send(bot_response, reference=message)
          # else:
            bot_response = chatgpt_response(prompt=user_message)
            await message.channel.send(bot_response, reference=message)
        case 'patGPT':
          # if len(command) <=6:
          #   bot_response = f"Please include request texts after the prefix!!"
          #   await message.channel.send(bot_response, reference=message)
          # else:
            bot_response = chatgpt_response(prompt=user_message)
            await message.channel.send(bot_response, reference=message)
        case 'PatGPT':
          # if len(command) <=6:
          #   bot_response = f"Please include request texts after the prefix!!"
          #   await message.channel.send(bot_response, reference=message)
          # else:
            bot_response = chatgpt_response(prompt=user_message)
            await message.channel.send(bot_response, reference=message)
          
            
        

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)