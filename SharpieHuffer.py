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

# with open("sibling_words.txt", "r") as sibling_keywords:
#     sibling_words = sibling_keywords.readlines()
# 
# for i in range(len(sibling_words)):
#     sibling_words[i] = sibling_words[i].strip()
# 
# @client.event
# async def on_message(message):
#     has_sent = False
#     channel = message.channel
#     for x in sibling_words:
#         if (message.content.lower().count(x.lower()) > 0 and has_sent == False and message.author.name != "SharpieHuffer" and message.author.name == "Mickey"):
#             await channel.send("Did you know: Mickey has too many siblings to count")
#             has_sent = True
#     has_sent = False
#     if (message.content.lower().count("sharpie" && has_sent == False and message.author.name != "SharpieHuffer"):
#         await channel.send("Mrs. Lefstad is disappointed. No sniffing sharpies!")

with open("token.txt", "r") as token_file:
    token = token_file.read()

client.run(token)
