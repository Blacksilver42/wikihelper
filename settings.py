import pycurl, zlib, discord

WHOAMI="wikihelper"
URL="https://github.com/Blacksilver42/wikihelper"
VERSION="0.1.0"
VERSIONSTRING="Xyzzy!"
PREFIX="&"
USERAGENT = "{whoami}/{bot_version} ({pycurl_version})".format(
	whoami=WHOAMI,
	bot_version=VERSION,
	pycurl_version=pycurl.version
)
CACHEFILE = "cache.json"
ZIP_CACHE = True
ZIP_CACHEFILE = "cache.z"

WIKI = "https://sbwiki.blacksilver.xyz/wiki/{page}"
OKCODE = 200

def embed_version():
	em = discord.Embed(
		title="{i} {v} \"{vs}\"".format(i=WHOAMI, v=VERSION, vs=VERSIONSTRING),
		url=URL
	)
	em.add_field(name="discord.py", value=discord.__version__)
	em.add_field(name="PycURL", value=pycurl.version_info()[1])
	em.add_field(name="zlib", value=zlib.ZLIB_VERSION)
	return em

async def getUserAgent(client, M, argv):
	await client.send_message(M.channel, "```\n{}```\n".format(USERAGENT))
async def getVersion(client, M, argv):
	await client.send_message(M.channel, embed=embed_version())

