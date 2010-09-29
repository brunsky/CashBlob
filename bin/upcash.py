import MultipartPostHandler, urllib2, cookielib

res = urllib2.urlopen('http://sharping-1.appspot.com/get_u_path')
cookies = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookies),MultipartPostHandler.MultipartPostHandler)
params = { "file" : open("/home/will/Documents/cash/mycash", "rb"),"submit" : "Submit" }
opener.open(res.read(), params)
