import discord
import json
client = discord.Client()

with open("keywords.json", "r") as keyword_file:
    keyword = json.load(keyword_file)

print(keyword)

def triggered_response(topic, author, message_text):
    has_sent = False
    caller = keyword[topic]["caller"]
    response = ""
    if (caller == any or caller == author):
        caller = True

    for key in keyword[topic]["key"]:
        if (message_text.lower().count(key.lower()) > 0 and has_sent == False and author != "SharpieHuffer" and caller):
            has_sent = True
            response = keyword[topic]["response"]
    return has_sent, response

@client.event
async def on_message(message):
    message_text = message.content
    channel = message.channel
    response = ""
    can_send = False
    for topic in keyword:
        can_send, response = triggered_response(topic, message.author.name, message_text)
        if can_send:
            await channel.send(response)

with open("token.txt", "r") as token_file:
    token = token_file.read()

client.run(token)
