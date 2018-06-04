import pycurl, cache

def blind_try(url, opts={}):
	"""Blindly return the http code for a url. Don't ask any questions."""
	curl = pycurl.Curl()
	
	curl.setopt(curl.NOBODY, True)
	curl.setopt(curl.URL, url)
	
	curl.setopt(curl.FOLLOWLOCATION, opts.get("follow", False))
	
	curl.setopt(curl.USERAGENT, opts.get("useragent", pycurl.version_info()[1]))
	
	curl.perform()
	
	code = curl.getinfo(pycurl.HTTP_CODE)
	print("> HEAD   {url:40}:{code}".format(url=url, code=code))
	return code

def blind_try_cached(url, C, opts={}):
	"""Blindly look up the url, respecting the cache.
	Pass cache as cache.fake if you don't want me to look up in the cache."""
	
	response = C.get(url)
	if(response == None):
		response = blind_try(url, opts=opts)
		C.add(url, response)
	else:
		print("(CACHED) {url:40}:{code}".format(url=url, code=response))
	
	return response

def try_url(url, opts={}):
	"""Actually use this function"""
	
	if(opts.get("nocache", False) == True):
		arg_cache = cache.fake
	else:
		arg_cache = cache.cache
	return blind_try_cached(url, arg_cache, opts=opts)
