import urllib, urllib2

params = urllib.urlencode(dict(account='will.lien@gmail.com'))
f = urllib2.urlopen('http://sharping-1.appspot.com/download', params)
data = f.read()
f.close()
file = open('/home/will/Documents/cash/mycash', 'w')
file.write(data)
file.close()
