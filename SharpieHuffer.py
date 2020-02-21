import discord
client = discord.Client()

with open("sibling_words.txt", "r") as keywords:
    sibling_words = keywords.readlines()

for i in range(len(keywords)):
    keywords[i] = keywords[i].strip()

@client.event
async def on_message(message):
    has_sent = False
    for x in keywords:
        if(message.content.lower().count(x.lower()) > 0 and has_sent == False and message.author.name != "SharpieHuffer" and message.author.name == "Mickey")
            channel = message.channel
            await channel.send("Did you know: Mickey has too many siblings to count")
            has_sent = True

with open("token.txt", "r") as token_file:
    token = token_file.read()

client.run(token)
