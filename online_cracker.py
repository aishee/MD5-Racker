import urllib, urllib2, re
def on_crack(MD5Hash):
    site = "http://md5.my-addr.com/md5_decrypt-md5_cracker_online/md5_decoder_tool.php"
    data = urllib.urlencode({"md5":MD5Hash})
    request = urllib2.Request(site)
    response = urllib2.urlopen(request, data)
    payload = response.read()
    results = re.findall("Hashed string</span>: (.*?)</div>",payload)
    for result in results:
        print result
