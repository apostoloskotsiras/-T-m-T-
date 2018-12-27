import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import random
from discord import Game

TOKEN = 'NTI3Nzk5OTkzNDQxMDU4ODI3.DwZAkg.MjCKRgVOk-JyNiuM9L419CCaX-M'

Client = discord.client
client = commands.Bot(command_prefix = '.')
client.remove_command('help')
Clientdiscord = discord.Client()


@client.event
async def on_ready():
    await client.change_presence(game=Game(name='.help'))
    print('Bot Is Ready')

@client.event
async def on_reaction_add(reaction, user):
    channel = reaction.message.channel
    await client.send_message(channel, '{} has added {} to the message: {}'.format(user.name, reaction.emoji, reaction.message.content,))

@client.event
async def on_reaction_remove(reaction, user):
    channel = reaction.message.channel
    await client.send_message(channel, '{} has removed {} from the message: {}'.format(user.name, reaction.emoji, reaction.message.content))

@client.command(pass_context=True)
async def clear(ctx, amount=100):
    channel = ctx.message.channel
    messages = []
    async for message in client.logs_from(channel, limit=int(amount) + 1):
        messages.append(message)
    await client.delete_messages(messages)

@client.command()
async def ping():
    await client.say('pong!')

@client.command(pass_context=True)
async def help(ctx):
    author = ctx.message.author

    embed = discord.Embed(
        colour = discord.Colour.orange()
    )

    embed.set_author(name='Help')
    embed.add_field(name='.ping', value='returns pong!', inline=False)

    await client.send_message(author, embed=embed)

@client.command()
async def echo(*args):
    output = ''
    for word in args:
        output += word
        output += ' '
    await client.say(output)

@client.command(pass_context=True)
async def info(ctx, user: discord.Member):
    await client.say("The users name is: {}".format(user.name))
    await client.say("The users ID is: {}".format(user.id))
    await client.say("The users status is: {}".format(user.status))
    await client.say("The users highest role is: {}".format(user.top_role))
    await client.say("The user joined at: {}".format(user.joined_at))

@client.command(pass_context=True)
@commands.has_permissions(kick_members=True)
async def kick(ctx, user: discord.Member):
    await client.say(":boot: Cya, {}.".format(user.name))
    await client.kick(user)
    print (".kick on {}".format(user.name))

@client.command(pass_context=True)
@commands.has_permissions(ban_members=True)
async def ban(ctx, user: discord.Member):
    await client.say(":boot: Cya, {}.".format(user.name))
    await client.ban(user)
    print (".ban on {}".format(user.name))


client.run(TOKEN)
