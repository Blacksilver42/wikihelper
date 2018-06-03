#!/usr/bin/python3
import discord, json, pycurl
import parse, cache, settings



with open("token", "r") as f:
	TOKEN = f.read().rstrip()


client = discord.Client()

cmds = {
	"getcache" : cache.getcache,
	"agent"	: misc.getUserAgent,
	"version" : misc.getVersion
}

@client.event
async def on_ready():
	print("Connected!")
	print("----------\n")

@client.event
async def on_message(M):
	if(M.author == client.user):
		return
	for key, value in cmds.items():
		if(M.content.startswith(settings.PREFIX + key)):
			argv = M.content.split()
			await value(client, M, argv)
			return
	await parse.parse(client, M)

client.run(TOKEN)
