from application.discord_bot.discord_api import client, discord_token
from keep_alive import keep_alive
import os
import discord

@client.event
async def on_ready():
  print("Your bot is ready")

keep_alive()

try:
  client.run(discord_token)
except discord.errors.HTTPException:
  print("\n\n\nBlocked by rate limits\nRestarting...\n\n\n")
  os.system("kill 1")
  os.system("python restarter.py")