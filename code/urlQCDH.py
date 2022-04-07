ra = open('output.txt','r')
import urllib
import urllib.parse
import urllib.request
import simplejson

rads = ra.readlines()
list_source_dk= []
for i in range(4):
 list_source_dk.append(''.join(rads[i*25:
(i+1)*25]))
# tao tap macilious gom nhung url doc hai
malicious_count = 0
total_ads = 0
macilious = []
# Su dung VirusTotal API de phan loai quang cao doc hai
for item in list_source_dk:
    parameters = {"resource": item, "apikey": '908259743dd40b4ec78f95178a973b89501f9abf3710913d4bd0c924c2f9151f',
    "scan": '1'}
    data = urllib.parse.urlencode(parameters)
    data = data.encode('utf-8')
    req = urllib.request.Request("https://nhacaiso.top/vua-bai88/", data)
    response = urllib.request.urlopen(req)
    jsonstr = response.read()
    # jsonstr = str(jsonstr).strip("'<>() ").replace('\'', '\"')
    # listjson = {}
    listjson = simplejson.load(jsonstr)
    print (listjson)
    total = 0
    for i in listjson:
        if i.get('positives') > 0:
            macilious.append(i.get('resource').encode('utf-8'))
            malicious_count += 1 