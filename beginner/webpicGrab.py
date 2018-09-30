#basic exercise for garbbing pics from web pages
import re
import urllib.request
req = urllib.request.urlopen('http://www.imooc.com/course/programdetail/pid/52')
buf = req.read()
buf = buf.decode('utf-8')
listurl = re.findall(r'http://.+\.jpg', buf)

i=0
for url in listurl:
    print (url)
    req = urllib.request.urlopen(url)
    buf=req.read()
    print (buf)
    f=open(str(i)+'.jpg','wb')
    f.write(buf)
    f.close()
    i+=1
    if i==7:
        break
