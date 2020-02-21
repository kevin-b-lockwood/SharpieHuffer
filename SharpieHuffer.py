import discord
client = discord.Client()

with open("token.txt", "r") as token_file:
    token = token_file.read()

client.run(token)
