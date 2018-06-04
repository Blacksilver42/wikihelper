import settings, try_url


start = "[["
end = "]]"

def xyzzy(s, start, end):
	finds = []
	for i, c in enumerate(s):
		if(s[i:i+len(start)] == start):
			find = ""
			after = s[i+2:]
			for i2, c2 in enumerate(after):
				i+=1
				if(after[i2:i2+len(end)] == end):
					break
				find = find + c2
			if(find):
				finds.append(find)
	return finds

async def parse(client, M):
	finds = xyzzy(M.content, start, end)
	pages = []
	errs = []
	for find in finds:
		find = find.replace(" ", "_")
		opts, find = parse_find(find)
		url = settings.WIKI.format(page=find)
		try:
			code = try_url.try_url(url, opts=opts)
		except try_url.pycurl.error as e:
			errs.append((repr(find),e.args[1]))
			continue
		except:
			errs.append((repr(find),"<Unknown Error: {}>".format(str(e))))
		else:
			if(code == 200):
				pages.append(url)
	if(pages):
		pages = list(set(pages))
		await client.send_message(M.channel, " | ".join(pages))
	if(errs):
		errs = [("`"+e[0][1:len(e[0])-1]+"`",e[1]) for e in errs]
		await client.send_message(M.channel, "\n".join(["{e[0]}: {e[1]}".format(e=e) for e in errs]))
	try_url.cache.cache.save()


def parse_find(find):
	opts = {}
	opts["follow"] = True
	if(find[0] == "*"):
		opts["nocache"] = True
		find = find[1:]
	
	return opts, find
