import urllib2
from pyquery import PyQuery
import time,codecs,datetime

def get_votes():
    html=urllib2.urlopen("http://c.student.mynavi.jp/cpf/stu_003/").read()
    query=PyQuery(html)
    charas=[]

    for photo_box in query.find("div.photo_box"):
        votes=PyQuery(photo_box).find("div.votes").text()
        names=PyQuery(photo_box).find("a").text()
        result=dict(name=names,vote=votes)
        charas.append(result)

    return charas

while 1:
    day=datetime.datetime.today()
    fin=codecs.open('vote.log',"a",'utf-8')
    fin.write(str(day.month)+":"+str(day.day)+":"+str(day.hour)+":"+str(day.minute)+"\n")
    charas=get_votes()
    for p in charas:
        fin.write(p["name"]+","+str(p["vote"])+"\n")
    fin.write("----------------------------\n")
    fin.close()
    time.sleep(600)
