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

