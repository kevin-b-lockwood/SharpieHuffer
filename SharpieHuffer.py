import discord
client = discord.Client()

with open("sibling_words.txt", "r") as sibling_keywords:
    sibling_words = sibling_keywords.readlines()

for i in range(len(sibling_words)):
    sibling_words[i] = sibling_words[i].strip()

@client.event
async def on_message(message):
    has_sent = False
    for x in sibling_words:
        if (message.content.lower().count(x.lower()) > 0 and has_sent == False and message.author.name != "SharpieHuffer" and message.author.name == "Mickey"):
            channel = message.channel
            await channel.send("Did you know: Mickey has too many siblings to count")
            has_sent = True

with open("token.txt", "r") as token_file:
    token = token_file.read()

client.run(token)
