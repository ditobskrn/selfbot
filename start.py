# -*- coding: utf-8 -*-
from thrift.transport import TTransport,TSocket,THttpClient,TTransport,TZlibTransport
from thrift.protocol import TCompactProtocol,TMultiplexedProtocol,TProtocol
from thrift.server import THttpServer,TServer,TProcessPoolServer
from linepy import *
from akad.ttypes import *
from multiprocessing import Pool, Process
from time import sleep
from humanfriendly import format_timespan, format_size, format_number, format_length
import pytz, datetime, pafy, time, timeit, random, sys, ast, re, os, json, subprocess, threading, string, codecs, requests, tweepy, ctypes, urllib, wikipedia
from datetime import timedelta, date
from datetime import datetime
from urllib.parse import quote
from bs4 import BeautifulSoup
import youtube_dl
from zalgo_text import zalgo
from threading import Thread,Event
import wikipedia as wiki
requests.packages.urllib3.disable_warnings()
from ttypes import LoginRequest
import json, requests, LineService
from thrift.transport import THttpClient

# ----- INI LOGIN VIA EMAIL ----- # 
botStart = time.time()
# # AKUN UTAMA
# cl = LINE("maudyliana666@gmail.com","ditobaskaran123")

# cl.log("Auth Token : ESnUFOPlJqnJ6EUY8e43.gD5TSeVN7yElVUvXKIBRuW.5WtDJv3qIG5pUUjSqjEh+ouuqOdiyfWOuedbOWDLVqc=" + str(cl.authToken))
# channelToken = cl.getChannelResult()
# cl.log("Channel Token : TJvDC9rMp9DZ0il9wq3bnb54lngsoWcewxoPS/JB1wSea5/FTQlFkZNNGqD9bXODQZVUNvB0IHmG4p9IKvf97maTA07cPd6ypnCLqhDsoR8AaRebLj7wMCK8l1okBPIyIojqfbYl3mAv3XkE5uwaDL7bC131BzsktZjvboJ0Coq77+GQ7t0noFnF4+vRD8v95ZacdnbkkaGVCZTraPuzsPvzOawQ+6MjngB9fKsdJo4dBv1BBeSV7A5MklYXI8PrQqN701UONFLdvfESgb1aAiFNPIus0jQMcPvRZrnqNTn0pv3F/GdhLsEdiKe/3gsQrThl3rFWFPaU9rvhrjUAO5LfqpPWMU+iezF3/XM5tPQ=', obsToken='', expiration=1596353476157, refreshToken='ipQg8VgVkYeoesw8xQ9a', channelAccessToken='cYLcbT8iqRUv4plQQiCiQL3aO0QW6REPhUuCFwG9XcfLP7OuJ9cdR03HntyzQwBz1yhWqJ/X3s+645IhECHczUl7+5qmPNFVVwz6b+wEl/6ps0hbgRoMPjsPESwV12z+lB/bRDK3wmUtDDy4phim9VQqTK4DRrqa3GpIq8RE2HdwZil231bU8/I8EWoHOWsV" + str(channelToken))

# # AKUN KEDUA
# db = LINE("dbscoder88@gmail.com","ditobaskaran123")
# db.log("Auth Token : ETPkuxhvptuPQ6ohUjKa.UpTF3EJIZEyHTyUdfmkuIG.Ix31SU8+6jTPfjJxkQ+f3qNUAwmameN7RkG/jmqHaF4=" + str(db.authToken))
# channelToken = db.getChannelResult()
# db.log("Channel Token :  ChannelToken(token='XLnmEnqlikYIe/eIyQpcraXxe6b18VQthQM8YtRhoxaG6015HXMtGhc+wQlS95hn5yzmIITuFGaWhIdgVvOJGlGGe2X4r44EddtI4ltUJNjN5PxWzxj7+VtOyL9I0HyOEVg2K/rNmynLdCTcj/VJsHD/oJkUHswlrDcrppE2Qyi/SDXYYph6WnSjuxX/AlBeLe02wVA5xqfOo1Tq11qlFu6RarOX1MKeMRCGAiUiUGADD5FHJVi4IrE4UR9YCdj9QqN701UONFLdvfESgb1aAiFNPIus0jQMcPvRZrnqNTnaUNgRMDrTqCl9ywGr44GwPGWhiN77zOCIh/yzuWO4GL6WDn8T1F9zHkEaRa5FxLs=', obsToken='', expiration=1597561731980, refreshToken='fwab8pEJF3io2xd0DaxR', channelAccessToken='HoE33OeXg+3EbpM6sy2It/Skwt32nRbSTeOvB/rZV6h1tw51iTAwXHAYLm9gZx7JoITZ6PYYl0fPLI9BOAnXhw8nz6ZQ9OKFu1mpvcocMUT7XMGHWwLX6ENPAT1ZzPfqTQSo8bGV77KdUfophdc1OlQqTK4DRrqa3GpIq8RE2HdwZil231bU8/I8EWoHOWsV')" + str(channelToken))

# # AKUN KETIGA
# bs = LINE("coreprojectku@gmail.com","ditobaskaran123")
# bs.log("Auth Token : ETPkuxhvptuPQ6ohUjKa.UpTF3EJIZEyHTyUdfmkuIG.Ix31SU8+6jTPfjJxkQ+f3qNUAwmameN7RkG/jmqHaF4=" + str(bs.authToken))
# channelToken = bs.getChannelResult()
# bs.log("Channel Token :  ChannelToken(token='XLnmEnqlikYIe/eIyQpcraXxe6b18VQthQM8YtRhoxaG6015HXMtGhc+wQlS95hn5yzmIITuFGaWhIdgVvOJGlGGe2X4r44EddtI4ltUJNjN5PxWzxj7+VtOyL9I0HyOEVg2K/rNmynLdCTcj/VJsHD/oJkUHswlrDcrppE2Qyi/SDXYYph6WnSjuxX/AlBeLe02wVA5xqfOo1Tq11qlFu6RarOX1MKeMRCGAiUiUGADD5FHJVi4IrE4UR9YCdj9QqN701UONFLdvfESgb1aAiFNPIus0jQMcPvRZrnqNTnaUNgRMDrTqCl9ywGr44GwPGWhiN77zOCIh/yzuWO4GL6WDn8T1F9zHkEaRa5FxLs=', obsToken='', expiration=1597561731980, refreshToken='fwab8pEJF3io2xd0DaxR', channelAccessToken='HoE33OeXg+3EbpM6sy2It/Skwt32nRbSTeOvB/rZV6h1tw51iTAwXHAYLm9gZx7JoITZ6PYYl0fPLI9BOAnXhw8nz6ZQ9OKFu1mpvcocMUT7XMGHWwLX6ENPAT1ZzPfqTQSo8bGV77KdUfophdc1OlQqTK4DRrqa3GpIq8RE2HdwZil231bU8/I8EWoHOWsV')" + str(channelToken))


# ----- INI LOGIN VIA QR LINK ----- # 
try:
    apiKey = "Z6vMBEnkp04n"
    headers = {
        "apiKey":apiKey,
        "appName":"IOSIPAD\t10.10.0\tiPhone 8\t11.2.5",
        "cert" : None,
        "server": random.choice(["pool-1","pool-2"]),
        "sysname": "DBSBOT"
        }
    main = json.loads(requests.get("https://api.be-team.me/qrv2",headers=headers).text)
    print("QR LINK: " + main["result"]["qr_link"])
    if not headers["cert"]:
        result = json.loads(requests.get(main["result"]["cb_pincode"],headers=headers).text)
        print("Your Pincode: " + result["result"])
    result = json.loads(requests.get(main["result"]["cb_token"],headers=headers).text)
    if result["status"] != 200:
        print("[ Error ] "+ result["reason"])
    else:
        cl = LINE(result["result"]["token"],appName="IOSIPAD\t10.10.0\tiPhone 8\t11.2.5")
        print ("===== LOGIN BERHASIL =====")
except:
    pass

readOpen = codecs.open("read.json","r","utf-8")
settingsOpen = codecs.open("temp.json","r","utf-8")

clMID = cl.getProfile().mid

clProfile = cl.getProfile()
clSettings = cl.getSettings()

oepoll = OEPoll(cl)
read = json.load(readOpen)
settings = json.load(settingsOpen)

menuHelp = """
╔════════════════════
║            ★MENU HELP★ 
╠════════════════════
╠ ✾ Me
╠ ✾ Mymid
╠ ✾ MyContact
╠ ✾ MyName
╠ ✾ MyBio
╠ ✾ MyPp
╠ ✾ MyCover
╠ ✾ SearchID (ID LINE)
╠ ✾ Invite (ID LINE)
╠ ✾ Kick @
╠ ✾ GetMid @
╠ ✾ GetContact @
╠ ✾ GetPp @
╠ ✾ GetCover @
╠ ✾ Gbc (Text)
╠ ✾ Gname (Text)
╠ ✾ Glist
╠ ✾ Gcreator
╠ ✾ Ginfo
╠ ✾ Gurl
╠ ✾ FriendList
╠ ✾ TagAll
╠ ✾ CancelAll
╠ ✾ ClearChat
╠ ✾ Message
╠ ✾ Speed
╠ ✾ Status
╠ ✾ Runtime
╠ ✾ Settings
╠ ✾ Bye
╚════════════════════
"""

menuSettings = """
╔════════════════════
║            ★ SETTINGS ★
╠════════════════════
╠ ✾ AllStatus On/Off
╠ ✾ AutoJoin On/Off
╠ ✾ AutoJoinTicket On/Off
╠ ✾ AutoRead On/Off
╠ ✾ AutoRespon On/Off
╠ ✾ AutoResponPc On/Off
╠ ✾ Broadcast On/Off
╠ ✾ SetPp On/Off
╠ ✾ GLink On/Off
╠ ✾ SetWelcome (Text)
╠ ✾ SetAutoResponPc (Text)
╠ ✾ SetName (Text)
╠ ✾ SetPpGroup
╠ ✾ SetPp
╚════════════════════
"""

connect1 = 'CHROME'
Headers1 = {
        'User-Agent': "Line/9.22.1",
        'X-Line-Application': "CROMEOS\t2.1.5ARIFISTIFIK\t11.2.5",
        "x-lal": "ja-US_US",
    }
connect2 = 'WIN'
Headers2 = {
        'User-Agent': "Line/9.22.1",
        'X-Line-Application': "DESKTOPWIN\t5.5.5ARIFISTIFIK\t11.2.5",
        "x-lal": "ja-US_US",
    }
connect3 = 'ios'
Headers3 = {
        'User-Agent': "Line/9.22.1",
        'X-Line-Application': "IOSIPAD\t8.14.2\tiPhone OS\t11.2.5",
        "x-lal": "ja-US_US",
    }

settings = {
    "autoJoin": False,
    "autoJoinTicket": False,
    "autoRead": False,
    "autoRespon": False,
    "autoResponPc": False,
    "broadcast": False,
    "changePicture": False,
    "restartPoint": False,
    "welcomeMessage": "Selamat datang",
    "responMsgPc": "Hai, pesan Anda akan segera kami balas.",
    "lang":"JP",
    "group":{},
    "changeGroupPicture": [],
    "userAgent": [
        "Mozilla/5.0 (X11; U; Linux i586; de; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (X11; U; Linux amd64; rv:5.0) Gecko/20100101 Firefox/5.0 (Debian)",
        "Mozilla/5.0 (X11; U; Linux amd64; en-US; rv:5.0) Gecko/20110619 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 FirePHP/0.5",
        "Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux x86_64) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; Linux ppc; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux AMD64) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; FreeBSD amd64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:5.0) Gecko/20110619 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; rv:6.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1.1; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.2; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.1; U; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.1; rv:2.0.1) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.0; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.0; rv:5.0) Gecko/20100101 Firefox/5.0"
    ]
}


read = {
    "readPoint": {},
    "readMember": {},
    "readTime": {},
    "ROM": {}
}

myProfile = {
  "displayName": "",
  "statusMessage": "",
  "pictureStatus": ""
}

cctv = {
    "cyduk":{},
    "point":{},
    "MENTION":{},
    "sidermem":{}
}

myProfile["displayName"] = clProfile.displayName
myProfile["statusMessage"] = clProfile.statusMessage
myProfile["pictureStatus"] = clProfile.pictureStatus

def restart_program(): 
    python = sys.executable
    os.execl(python, python, * sys.argv)

def restartBot():
    print ("[ INFO ] RESTARTING BOT")
    python = sys.executable
    os.execl(python, python, *sys.argv)
    
def logError(text):
    cl.log("[ ERROR ] " + str(text))
    time_ = datetime.now()
    with open("errorLog.txt","a") as error:
        error.write("\n[%s] %s" % (str(time), text))
        
def sendMention(to, mid, firstmessage, lastmessage):
    try:
        arrData = ""
        text = "%s " %(str(firstmessage))
        arr = []
        mention = "@x "
        slen = str(len(text))
        elen = str(len(text) + len(mention) - 1)
        arrData = {'S':slen, 'E':elen, 'M':mid}
        arr.append(arrData)
        text += mention + str(lastmessage)
        cl.sendMessage(to, text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        logError(error)
        cl.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def sendMessage(to, Message, contentMetadata={}, contentType=0):
    mes = Message()
    mes.to, mes._from = to, profile.mid
    mes.text = text
    mes.contentType, mes.contentMetadata = contentType, contentMetadata
    if to not in messageReq:
        messageReq[to] = -1
    messageReq[to] += 1

def RmentionMembers(to, mid):
    try:
        arrData = ""
        textx = "{} mention members\n1.".format(str(len(mid)))
        arr = []
        no = 1
        num = 2
        for i in mid:
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention
            if no < len(mid):
                no += 1
                textx += "%i. " % (num)
                num=(num+1)
            else:
                try:
                    no = "\n[ {} ]".format(str(cl.getGroup(to).name))
                except:
                    no = "\n[ Success ]"
        cl.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        logError(error)

def sendMessageWithMention(to, mid):
    try:
        aa = '{"S":"0","E":"3","M":'+json.dumps(mid)+'}'
        text_ = '@x '
        cl.sendMessage(to, text_, contentMetadata={'MENTION':'{"MENTIONEES":['+aa+']}'}, contentType=0)
    except Exception as error:
        logError(error)

def mentionMembers(to, mid):
    try:
        arrData = ""
        textx = "╔══[Total {} User]\n╠ ".format(str(len(mid)))
        arr = []
        no = 1
        for i in mid:
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention
            if no < len(mid):
                no += 1
                textx += "╠ "
            else:
                try:
                    textx += "╚══[ {} ]".format(str(cl.getGroup(to).name))
                except:
                    pass
        cl.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        logError(error)
        cl.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def backupData():
    try:
        backup = settings
        f = codecs.open('temp.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        backup = read
        f = codecs.open('read.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        return True
    except Exception as error:
        logError(error)
        return False

def sendStickerTemplate(to, text):
    url = "https://game.linefriends.com/jbp-lcs-ranking/lcs/sendMessage"
    to = op.param1
    data = {
        "type": "template",
        "altText": "{} sent a sticker".format(cl.getProfile().displayName),
        "template": {
            "type": "image_carousel",
            "columns": [
                {
                        "imageUrl": text,
                        "size": "full", 
                        "action": {
                            "type": "uri",
                        "uri": "http://line.me/ti/p/~enaksusumm"
                            }                                                
              }
                ]
        }
    }
    cl.postTemplate(to, data)

def clBot(op):
  try:
    if op.type == 0:
        print ("[ 0 ] END OF OPERATION")
        return
    if op.type == 5:
        print ("[ 5 ] NOTIFIED ADD CONTACT")
        if settings["autoAdd"] == True:
            cl.sendMessage(op.param1, "Terimakasih telah menambahkan saya sebagai teman")
            cl.findAndAddContactsByMid(op.param1)
    if op.type == 13 or op.type == 124:
        print ("CL DI INVITE")
        if settings["autoJoin"] == True:
            cl.acceptGroupInvitation(op.param1)
            cl.sendMessage(op.param1, "Hai, salken yaa!")
    if op.type == 25:
        print ("[ 25 ] SEND MESSAGE")
        msg = op.message
        text = msg.text
        msg_id = msg.id
        receiver = msg.to
        sender = msg._from
        if msg.toType == 0:
            if sender != cl.profile.mid:
                to = sender
            else:
                to = receiver
        else:
            to = receiver
        if msg.contentType == 0:
            if text is None:
                return
            if text.lower() == 'help':
                cl.sendMessage(to, menuHelp)
            elif text.lower() == 'settings':
                cl.sendMessage(to, menuSettings)
            elif text.lower() == 'me':
                cl.sendContact(to, clMID)
            elif text.lower() == 'mymid':
                cl.sendMessage(msg.to, "[MY MID]\n" +  clMID)
            elif text.lower() == 'mycontact':
                cl.sendContact(to, clMID)
            elif text.lower() == 'myname':
                me = cl.getContact(clMID)
                cl.sendMessage(msg.to, "[DisplayName]\n" + me.displayName)
            elif text.lower() == 'mybio':
                me = cl.getContact(clMID)
                cl.sendMessage(msg.to, "[StatusMessage]\n" + me.statusMessage)
            elif text.lower() == 'mypp':
                me = cl.getContact(clMID)
                cl.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/" + me.pictureStatus)
            elif text.lower() == 'mycover':
                me = cl.getContact(clMID)
                cover = cl.getProfileCoverURL(clMID)    
                cl.sendImageWithURL(msg.to, cover)
            elif text.lower().startswith("searchid "):
                sep = text.split(" ")
                idline = text.replace(sep[0] + " ","")
                conn = cl.findContactsByUserid(idline)
                try:
                    anu = conn.mid
                    dn = conn.displayName
                    bio = conn.statusMessage
                    sendMention(to, anu, "「 Contact Line ID 」\n• Nama : ", "\n• Nick : "+dn+"\n• Bio : "+bio+"\n• Contact Link : http://line.me/ti/p/~"+idline)
                    cl.sendContact(to, anu)
                except Exception as e:
                    cl.sendMessage(msg.to, "ID LINE tidak ditemukan")
            elif text.lower().startswith("invite "):
                sep = text.split(" ")
                nick = text.replace(sep[0] + " ", "")
                conn = cl.findContactsByUserid(nick)
                cl.findAndAddContactsByMid(conn.mid)
                cl.inviteIntoGroup(msg.to, [conn.mid])
                group = cl.getGroup(msg.to)
                xname = cl.getContact(conn.mid)
                zx = ""
                zxc = ""
                zx2 = []
                xpesan = "「 Sukses Diinvite 」\nNama contact "
                recky = str(xname.displayName)
                pesan = ""
                pesan2 = pesan + "@a\n"
                xlen = str(len(zxc) + len(xpesan))
                xlen2 = str(len(zxc) + len(pesan2) + len(xpesan) - 1)
                zx = {"S": xlen, "E": xlen2, "M": xname.mid}
                zx2.append(zx)
                zxc += pesan2
                text = xpesan + zxc + "ke grup " + str(group.name) + ""
                cl.sendMessage(
                    receiver,
                    text,
                        contentMetadata={
                            "MENTION": str(
                                '{"MENTIONEES":'
                                    + json.dumps(zx2).replace(" ", "")
                                + "}"
                            )
                        },
                    contentType=0,
                )

            elif msg.text.lower().startswith("kick "):
                if 'MENTION' in msg.contentMetadata.keys() != None:
                    names = re.findall(r'@(\w+)', text)
                    mention = ast.literal_eval(
                    msg.contentMetadata['MENTION'])
                    mentionees = mention['MENTIONEES']
                    for mention in mentionees:
                        cl.kickoutFromGroup(msg.to,[mention['M']])
            elif text.lower().startswith("getmid "):
                if 'MENTION' in msg.contentMetadata.keys()!= None:
                  names = re.findall(r'@(\w+)', text)
                  mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                  mentionees = mention['MENTIONEES']
                  lists = []
                  for mention in mentionees:
                      if mention["M"] not in lists:
                          lists.append(mention["M"])
                  ret_ = "[ Mid User ]"
                  for ls in lists:
                      ret_ += "\n" + ls
                  cl.sendMessage(msg.to, str(ret_))
            elif text.lower().startswith("getcontact "):
                if 'MENTION' in msg.contentMetadata.keys()!= None:
                    names = re.findall(r'@(\w+)', text)
                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                    mentionees = mention['MENTIONEES']
                    lists = []
                    for mention in mentionees:
                        if mention["M"] not in lists:
                            lists.append(mention["M"])
                    for ls in lists:
                        contact = cl.getContact(ls)
                        mi_d = contact.mid
                        cl.sendContact(msg.to, mi_d)
            elif text.lower().startswith("getpp "):
                if 'MENTION' in msg.contentMetadata.keys()!= None:
                    names = re.findall(r'@(\w+)', text)
                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                    mentionees = mention['MENTIONEES']
                    lists = []
                    for mention in mentionees:
                        if mention["M"] not in lists:
                            lists.append(mention["M"])
                    for ls in lists:
                        path = "http://dl.profile.line.naver.jp/" + cl.getContact(ls).pictureStatus
                        cl.sendImageWithURL(msg.to, str(path))
            elif text.lower().startswith("getcover "):
                if cl != None:
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        for ls in lists:
                            path = cl.getProfileCoverURL(ls)
                            cl.sendImageWithURL(msg.to, str(path))
            elif text.lower().startswith("gbc "):
                sep = msg.text.split(" ")
                pesan = msg.text.replace(sep[0] + " ","")
                utama = cl.getGroupIdsJoined()
                if settings["broadcast"] == False:
                    cl.sendMessage(to, "Fitur broadcast off")
                elif settings["broadcast"] == True:
                    for group in utama:
                        groups = cl.groups
                        cl.sendMessage(group, str(pesan))
                groups = cl.groups
                cl.sendMessage(to, "[Broadcast] dikirim ke " + format(str(len(groups))) + " group")
            elif text.lower().startswith("gname "):
                if msg.toType == 2:
                    sep = text.split(" ")
                    groupname = text.replace(sep[0] + " ","")
                    if len(groupname) <= 20:
                        group = cl.getGroup(to)
                        group.name = groupname
                        cl.updateGroup(group)
                        cl.sendMessage(to, "「CHANGE GROUP NAME」\nBerhasil mengubah nama group menjadi : {}".format(groupname))
                else:
                    cl.sendMessage(to, "Perintah khusus dalam grup.")

#---------------------------------- START FITUR MEDIA ---------------------------------------#   
            elif text.lower() == 'myip':
                r = requests.get("https://dbspublic.my.id/api/myip.php?apikey=pynjn1CC68wwVue7Psn0MYzbJb88Fj")
                data = r.text
                a = json.loads(data)
                cl.sendMessage(to, "Tunggu sebentar...")
                if a["status"] == True:
                    cl.sendMessage(to, "[MY IP]\n"+str(a['result']))
                else:
                    cl.sendMessage(to, a['message'])
            elif text.lower().startswith("wallpaper "):
                sep = text.split(" ")
                q = text.replace(sep[0] + " ","")
                r = requests.get("https://dbspublic.my.id/api/wallpaper.php?apikey=pynjn1CC68wwVue7Psn0MYzbJb88Fj&q="+str(q))
                data = r.text
                a = json.loads(data)
                cl.sendMessage(to, "Tunggu sebentar...")
                if a["status"] == True:
                    result = a["result"]
                    k = len(result)//5
                    for image in range(k+4):
                      cl.sendImageWithURL(to, result[image])
                    cl.sendMessage(to, "FINISH")
                else:
                    cl.sendMessage(to, "Something error")
            elif text.lower().startswith("tiktok "):
                sep = text.split(" ")
                url = text.replace(sep[0] + " ","")
                r = requests.get("https://dbspublic.my.id/api/tiktok.php?apikey=pynjn1CC68wwVue7Psn0MYzbJb88Fj&url="+str(url))
                data = r.text
                a = json.loads(data)
                cl.sendMessage(to, "Tunggu sebentar...")
                if a["status"] == True:
                    cl.sendVideoWithURL(to, a['result']['vid'])
                    cl.sendMessage(to, "FINISH")
                else:
                    cl.sendMessage(to, a['message'])
            elif text.lower().startswith("ssweb "):
                sep = text.split(" ")
                url = text.replace(sep[0] + " ","")
                r = requests.get("https://dbspublic.my.id/api/ssweb.php?apikey=pynjn1CC68wwVue7Psn0MYzbJb88Fj&url="+str(url))
                data = r.text
                a = json.loads(data)
                cl.sendMessage(to, "Tunggu sebentar...")
                if a["status"] == True:
                    cl.sendImageWithURL(to, a['result'])
                    cl.sendMessage(to, "FINISH")
                else:
                    cl.sendMessage(to, a['message'])
            elif text.lower().startswith("shalat "):
                sep = text.split(" ")
                city = text.replace(sep[0] + " ","")
                r = requests.get("https://dbspublic.my.id/api/shalat.php?apikey=pynjn1CC68wwVue7Psn0MYzbJb88Fj&q="+str(city))
                data = r.text
                a = json.loads(data)
                cl.sendMessage(to, "Tunggu sebentar...")
                if a["status"] == True:
                    cl.sendMessage(to, "╔══[ Jadwal Shalat di "+a['result']['city']+" ]\n╠ Subuh : "+a['result']['subuh']+"\n╠ Dzuhur : "+a['result']['dzuhur']+"\n╠ Ashar : "+a['result']['ashar']+"\n╠ Maghrib : "+a['result']['maghrib']+"\n╠ Isya : "+a['result']['isya']+"\n╚══[ Jadwal Shalat di "+a['result']['city']+ "]")
                else:
                    cl.sendMessage(to, a['message'])
            elif text.lower().startswith("cuaca "):
                sep = text.split(" ")
                city = text.replace(sep[0] + " ","")
                r = requests.get("https://dbspublic.my.id/api/cuaca.php?apikey=pynjn1CC68wwVue7Psn0MYzbJb88Fj&q="+str(city))
                data = r.text
                a = json.loads(data)
                cl.sendMessage(to, "Tunggu sebentar...")
                if a["status"] == True:
                    cl.sendMessage(to, "╔══[ Cuaca di "+a['result']['name'] +"]\n╠ Weather : "+a['result']['weather']+"\n╠ City : "+a['result']['name']+"\n╠ Country : "+a['result']['country']+"\n╚══[ Jadwal Shalat di "+a['result']['name']+ "]")
                else:
                    cl.sendMessage(to, a['message'])

            elif text.lower().startswith("giphy "):
                sep = text.split(" ")
                key = text.replace(sep[0] + " ","")
                r = requests.get("https://dbspublic.my.id/api/gif.php?apikey=pynjn1CC68wwVue7Psn0MYzbJb88Fj&q="+str(key))
                data = r.text
                a = json.loads(data)
                cl.sendMessage(to, "Tunggu sebentar...")
                if a["status"] == True:
                    result = a["result"]
                    k = len(result)//5
                    for image in range(k+4):
                      cl.sendGIFWithURL(to, result[image])
                    cl.sendMessage(to, "════ FINISH ════")
                else:
                    cl.sendMessage(to, "Something error")
            elif text.lower().startswith("redtube "):
                sep = text.split(" ")
                key = text.replace(sep[0] + " ","")
                r = requests.get("https://dbspublic.my.id/api/redtube.php?apikey=pynjn1CC68wwVue7Psn0MYzbJb88Fj&q="+str(key))
                data = r.text
                a = json.loads(data)
                cl.sendMessage(to, "Tunggu sebentar...")
                if a["status"] == True:
                    result = a["result"]
                    k = len(result)//5
                    for data in range(k+4):
                      cl.sendImageWithURL(to, result[data]['thumbnail'])
                      cl.sendMessage(to, "╔══ [ RESULT CONTENT ]\n╠ Title : "+result[data]['title']+"\n╠ Duration : "+result[data]['duration']+"\n╠ URL : "+result[data]['url']+"\n╠ Embed : "+result[data]['embed_url']+"\n╚══[ FINISH ]")
                    cl.sendMessage(to, "════ FINISH ════")
                else:
                    cl.sendMessage(to, "Something error")
            elif text.lower().startswith("eporner "):
                sep = text.split(" ")
                key = text.replace(sep[0] + " ","")
                r = requests.get("https://dbspublic.my.id/api/porn.php?apikey=pynjn1CC68wwVue7Psn0MYzbJb88Fj&q="+str(key))
                data = r.text
                a = json.loads(data)
                cl.sendMessage(to, "Tunggu sebentar...")
                if a["status"] == True:
                    result = a["result"]
                    k = len(result)//5
                    for data in range(k+4):
                      cl.sendImageWithURL(to, result[data]['thumbnail'])
                      cl.sendMessage(to, "╔══ [ RESULT CONTENT ]\n╠ Title : "+result[data]['title']+"\n╠ URL : "+result[data]['url']+"\n╠ Embed : "+result[data]['embed']+"\n╚══[ FINISH ]")
                    cl.sendMessage(to, "════ FINISH ════")
                else:
                    cl.sendMessage(to, "Something error")


#---------------------------------- END FITUR MEDIA ---------------------------------------#  

            elif text.lower() == 'glist':
                cl.sendMessage(to, "Tunggu sebentar...")
                groups = cl.groups
                ret_ = "╔══[ Group List ]"
                no = 0 + 1
                for gid in groups:
                    group = cl.getGroup(gid)
                    ret_ += "\n╠ {}. {} | {}".format(str(no), str(group.name), str(len(group.members)))
                    no += 1
                ret_ += "\n╚══[ Total {} Groups ]".format(str(len(groups)))
                cl.sendMessage(to, str(ret_))
            elif text.lower() == 'gcreator':
                group = cl.getGroup(to)
                GS = group.creator.mid
                cl.sendContact(to, GS)
            elif text.lower() == 'ginfo':
                group = cl.getGroup(to)
                try:
                    gCreator = group.creator.displayName
                except:
                    gCreator = "Tidak ditemukan"
                if group.invitee is None:
                    gPending = "0"
                else:
                    gPending = str(len(group.invitee))
                if group.preventedJoinByTicket == True:
                    gQr = "Tertutup"
                    gTicket = "Tidak ada"
                else:
                    gQr = "Terbuka"
                    gTicket = "https://line.me/R/ti/g/{}".format(str(cl.reissueGroupTicket(group.id)))
                path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                cl.sendImageWithURL(to, path)
                ret_ = "╔══[ Group Info ]"
                ret_ += "\n╠ Nama Group : {}".format(str(group.name))
                ret_ += "\n╠ ID Group : {}".format(group.id)
                ret_ += "\n╠ Pembuat : {}".format(str(gCreator))
                ret_ += "\n╠ Jumlah Member : {}".format(str(len(group.members)))
                ret_ += "\n╠ Jumlah Pending : {}".format(gPending)
                ret_ += "\n╠ Group Qr : {}".format(gQr)
                ret_ += "\n╠ Group Ticket : {}".format(gTicket)
                ret_ += "\n╚══[ Group Info ]"
                cl.sendMessage(to, str(ret_))
            elif text.lower() == 'gurl':
                if msg.toType == 2:
                    group = cl.getGroup(to)
                    if group.preventedJoinByTicket == False:
                        ticket = cl.reissueGroupTicket(to)
                        cl.sendMessage(to, "[ Group Ticket ]\nhttps://line.me/R/ti/g/{}".format(str(ticket)))
                    else:
                        cl.sendMessage(to, "Grup qr tidak terbuka silahkan buka terlebih dahulu dengan perintah {}QR On".format(str(settings["keyCommand"])))
            elif text.lower() == 'friendlist':
                cl.sendMessage(to, "Tunggu sebentar...")
                ma = ""
                a = 0
                gid = cl.getAllContactIds()
                ma = "╔══[ Friend List ]"
                for i in gid:
                    G = cl.getContact(i)
                    a = a + 1
                    end = "\n"
                    ma += ("\n╠ " + str(a) + ". " + G.displayName)
                ma += "\n╚══[ Total {} Friends ]".format(str(len(gid)))
                cl.sendMessage(to, str(ma))
            elif text.lower() == 'tagall':
                if msg.toType == 0:
                    sendMention(to, to, "", "")
                elif msg.toType == 2:
                    group = cl.getGroup(to)
                    midMembers = [contact.mid for contact in group.members]
                    midSelect = len(midMembers)//20
                    for mentionMembers in range(midSelect+1):
                        no = 0
                        ret_ = "╔══[ Mention Members ]"
                        dataMid = []
                        for dataMention in group.members[mentionMembers*20 : (mentionMembers+1)*20]:
                            dataMid.append(dataMention.mid)
                            no += 1
                            ret_ += "\n╠ {}. @!".format(str(no))
                        ret_ += "\n╚══[ Total {} Members]".format(str(len(dataMid)))
                        cl.sendMention(msg.to, ret_, dataMid)
            elif text.lower() == 'cancelall':
                if msg.toType == 2:
                    group = cl.getGroup(to)
                    if group.invitee is None or group.invitee == []:
                        cl.sendReplyMessage(msg.id, to, "Tidak ada yang pending")
                    else:
                        invitee = [contact.mid for contact in group.invitee]
                        for inv in invitee:
                            cl.cancelGroupInvitation(to, [inv])
                        cl.sendMessage(to, "「CANCELALL」\nBerhasil membersihkan {} pendingan".format(str(len(invitee))))
            elif text.lower() == 'clearchat':
                cl.removeAllMessages(op.param2)
                cl.sendMessage(to, "Done")
            elif text.lower() == 'message':
                cl.sendMessage(to,"WELCOME MESSAGE\n" + "━ " + settings["welcomeMessage"] + "\n\nAUTO RESPON PC\n" + "━ " + settings["responMsgPc"])
            elif text.lower() == 'speed':
                start = time.time()
                cl.sendMessage(to, "Tunggu sebentar...")
                elapsed_time = time.time() - start
                cl.sendMessage(to, "[ Speed ]\n{} detik".format(str(elapsed_time)))
            elif text.lower() == 'status':
                try:
                    timeNow = time.time()
                    runtime = timeNow - botStart
                    runtime = format_timespan(runtime)
                    start = time.time()
                    cl.sendMessage(to, "Processing...")
                    elapsed_time = time.time() - start
                    ret_ = "╔══[ STATUS BOT ]"
                    ret_ += "\n╠ Runtime : {}".format(str(runtime))
                    ret_ += "\n╠ Speed : {} detik".format(str(elapsed_time))
                    if settings["autoJoin"] == True: 
                        ret_ += "\n╠ [ ON ] Auto Join"
                    else: 
                        ret_ += "\n╠ [ OFF ] Auto Join"
                    if settings["autoJoinTicket"] == True: 
                        ret_ += "\n╠ [ ON ] Auto Join Ticket"
                    else: 
                        ret_ += "\n╠ [ OFF ] Auto Join Ticket"
                    if settings["autoRead"] == True: 
                        ret_ += "\n╠ [ ON ] Auto Read"
                    else: 
                        ret_ += "\n╠ [ OFF ] Auto Read"
                    if settings["autoRespon"] == True: 
                        ret_ += "\n╠ [ ON ] Auto Respon"
                    else: 
                        ret_ += "\n╠ [ OFF ] Auto Respon"
                    if settings["autoResponPc"] == True: 
                        ret_ += "\n╠ [ ON ] Auto Respon PC"
                    else: 
                        ret_ += "\n╠ [ OFF ] Auto Respon PC"
                    if settings["broadcast"] == True: 
                        ret_ += "\n╠ [ ON ] Broadcast"
                    else: 
                        ret_ += "\n╠ [ OFF ] Broadcast"
                    ret_ += "\n╚══[ STATUS BOT ]"
                    cl.sendMessage(to, str(ret_))
                except Exception as e:
                    cl.sendMessage(msg.to, str(e))
            elif text.lower() == 'runtime':
                timeNow = time.time()
                runtime = timeNow - botStart
                runtime = format_timespan(runtime)
                cl.sendMessage(to, "Bot Aktif Selama {}".format(str(runtime)))
            elif text.lower() == 'settings':
                cl.sendMessage(to, menuSettings)
            # elif text.lower() == 'restart':
            #     cl.sendMessage(to, "Tunggu sebentar...")
            #     os.system("clear")
            #     settings["restartPoint"] = msg.to
            #     restartBot()
            #     cl.sendMessage(to, "Bot berhasil di restart...")
            elif text.lower() == 'bye':
              group = cl.getGroup(to)
              cl.sendMessage(to, "Dadah")
              cl.leaveGroup(to)

            # --- SETTING --- #
            elif text.lower() == 'allstatus on':
                settings["autoJoin"] = True
                settings["autoJoinTicket"] = True
                settings["autoRead"] = True
                settings["autoRespon"] = True
                settings["autoResponPc"] = True
                settings["broadcast"] = True
                settings["changePicture"] = True
                cl.sendMessage(to, "Allstatus aktif")
            elif text.lower() == 'allstatus off':
                settings["autoJoin"] = False
                settings["autoJoinTicket"] = False
                settings["autoRead"] = False
                settings["autoRespon"] = False
                settings["autoResponPc"] = False
                settings["broadcast"] = False
                settings["changePicture"] = False
                cl.sendMessage(to, "Allstatus mati")
            elif text.lower() == 'autojoin on':
                settings["autoJoin"] = True
                cl.sendMessage(to, "Auto join aktif")
            elif text.lower() == 'autojoin off':
                settings["autoJoin"] = False
                cl.sendMessage(to, "Auto join mati")
            elif text.lower() == 'autojointicket on':
                settings["autoJoinTicket"] = True
                cl.sendMessage(to, "Auto join ticket aktif")
            elif text.lower() == 'autojointicket off':
                settings["autoJoinTicket"] = False
                cl.sendMessage(to, "Auto join ticket mati")
            elif text.lower() == 'autoread on':
                settings["autoRead"] = True
                cl.sendMessage(to, "Auto read aktif")
            elif text.lower() == 'autoread off':
                settings["autoRead"] = False
                cl.sendMessage(to, "Auto read mati")
            elif text.lower() == 'autorespon on':
                settings["autoRespon"] = True
                cl.sendMessage(to, "Auto respon aktif")
            elif text.lower() == 'autorespon off':
                settings["autoRespon"] = False
                cl.sendMessage(to, "Auto respon mati")
            elif text.lower() == 'autoresponpc on':
                settings["autoResponPc"] = True
                cl.sendMessage(to, "Auto respon pc aktif")
            elif text.lower() == 'autoresponpc off':
                settings["autoResponPc"] = False
                cl.sendMessage(to, "Auto respon pc mati")
            elif text.lower() == 'broadcast on':
                settings["broadcast"] == True
                cl.sendMessage(to, "Broadcast aktif")
            elif text.lower() == 'broadcast off':
                settings["broadcast"] == False
                cl.sendMessage(to, "Broadcast mati")
            elif text.lower() == 'setpp on':
                settings["changePicture"] == True
                cl.sendMessage(to, "SetPp aktif")
            elif text.lower() == 'setpp off':
                settings["changePicture"] == False
                cl.sendMessage(to, "SetPp mati")
            elif text.lower() == 'glink on':
                if msg.toType == 2:
                    x = cl.getGroup(msg.to)
                    if x.preventedJoinByTicket == True:
                        x.preventedJoinByTicket = False
                        cl.updateGroup(x)
                    gurl = cl.reissueGroupTicket(msg.to)
                    cl.sendMessage(msg.to, "Nama : "+str(x.name)+ "\nUrl grup : http://line.me/R/ti/g/"+gurl)
            elif text.lower() == 'glink off':
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    X.preventedJoinByTicket = True
                    cl.updateGroup(X)
                    cl.sendMessage(msg.to, "Url closed")
                else:
                    cl.sendMessage(to, "Khusus di grup")
            elif msg.text.lower().startswith("setwelcome "):
                sep = text.split(" ")
                pesan = text.replace(sep[0] + " ", "")
                settings["welcomeMessage"] = settings["welcomeMessage"].replace(settings["welcomeMessage"], str(pesan))
                cl.sendMessage(to, "Berhasil diubah")
            elif msg.text.lower().startswith("setautoresponpc "):
                sep = text.split(" ")
                pesan = text.replace(sep[0] + " ", "")
                settings["responMsgPc"] = settings["responMsgPc"].replace(settings["responMsgPc"], str(pesan))
                cl.sendMessage(to, "Berhasil diubah")
            elif msg.text.lower().startswith("setname "):
                sep = text.split(" ")
                string = text.replace(sep[0] + " ", "")
                if len(string) <= 20:
                    profile = cl.getProfile()
                    profile.displayName = string
                    cl.updateProfile(profile)
                    cl.sendMessage(to, "Nama diubah menjadi :\n{}".format(str(string)))
                else:
                    cl.sendMessage(to, "Maksimal 20 karakter")
            elif text.lower() == 'cpgroup':
                if msg.toType == 2:
                    if to not in settings["changeGroupPicture"]:
                        settings["changeGroupPicture"].append(to)
                    cl.sendMessage(to, "Silahkan kirim gambarnya")
                else:
                    cl.sendMessage(to, "Khusus di grup")
            elif text.lower() == 'setpp':
                if msg.toType == 2:
                    cl.sendMessage(to, "Tidak bisa di grup.")
                else:
                    if settings["changePicture"] == False:
                        cl.sendMessage(to, "Setpp tidak aktif")
                    else:
                        cl.sendMessage(to, "Silahkan kirim gambarnya")
        elif msg.contentType == 1:
            if msg.toType == 2:
                if to in settings["changeGroupPicture"]:
                    path = cl.downloadObjectMsg(msg_id)
                    settings["changeGroupPicture"].remove(to)
                    cl.updateGroupPicture(to, path)
                    cl.sendMessage(to, "Berhasil mengubah foto profil grup.")
            else:
                if settings["changePicture"] == True:
                    path1 = cl.downloadObjectMsg(msg_id)
                    cl.updateProfilePicture(path1)
                    cl.sendMessage(to, "Foto profil berhasil diubah")
                else:
                    cl.sendMessage(to, "Setpp belum on")
    if op.type == 26:
        print ("[ 26 ] SEND PUBLIC MESSAGE")
        msg = op.message
        text = msg.text
        msg_id = msg.id
        receiver = msg.to
        sender = msg._from
        if msg.toType == 0:
            if sender != cl.profile.mid:
                to = sender
            else:
                to = receiver
        else:
            to = receiver
        if msg.contentType == 0:
            to = receiver
            if msg.contentType == 0:
                if settings["autoRead"] == True:
                    cl.sendChatChecked(to, msg_id)
                    cl.sendChatChecked(sender, msg_id)
                if settings["autoResponPc"] == True:
                    if msg.toType == 2:
                        print("[ INFO ] PRIVATE MESSAGE")
                    else:
                        cl.sendMessage(sender, settings["responMsgPc"])
            if text is None:
                return
            if "/ti/g/" in msg.text.lower():
                if settings["autoJoinTicket"] == True:
                    link_re = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
                    links = link_re.findall(text)
                    n_links = []
                    for l in links:
                        if l not in n_links:
                            n_links.append(l)
                    for ticket_id in n_links:
                        group = cl.findGroupByTicket(ticket_id)
                        cl.acceptGroupInvitationByTicket(group.id, ticket_id)
                        cl.sendMessage(to, "Berhasil masuk ke group %s" % str(group.name))

    if op.type == 17 or op.type == 130:
        print ("MEMBER JOIN TO GROUP")
        if settings["autoRespon"] == True:
            if op.param2 in clMID:
                return
            ginfo = cl.getGroup(op.param1)
            name = cl.getContact(op.param2).displayName
            mid = cl.getContact(op.param2).mid
            cl.sendContact(op.param1, mid)
            sendMention(op.param1, mid, "", settings["welcomeMessage"])
    if op.type == 15 or op.type == 61:
        print ("MEMBER LEAVE TO GROUP")
        if settings["autoRespon"] == True:
            if op.param2 in clMID:
                return
            ginfo = cl.getGroup(op.param1)
            name = cl.getContact(op.param2).displayName
            mid = cl.getContact(op.param2).mid
            cl.sendContact(op.param1, mid)
            sendMention(op.param1, mid, "", " Yah dia pergi:(")
    if op.type == 55:
        print ("[ 55 ] NOTIFIED READ MESSAGE")
        try:
          if cctv['cyduk'][op.param1]==True:
            if op.param1 in cctv['point']:
              Name = cl.getContact(op.param2).displayName
              if Name in cctv['sidermem'][op.param1]:
                  pass
              else:
                cctv['sidermem'][op.param1] += "\nâ¢ " + Name
                if " " in Name:
                  nick = Name.split(' ')
                  if len(nick) == 2:
                    Camera(op.param1, Name)
                    time.sleep(0.2)
                  else:
                    Camera(op.param1, Name)
                    time.sleep(0.2)
                else:
                  Camera(op.param1, Name)
                  time.sleep(0.2)
            else:
              pass
          else:
            pass
        except:
            pass
    if op.type == 55:
        print ("[ 55 ] NOTIFIED READ MESSAGE")
        try:
            if op.param1 in read['readPoint']:
                if op.param2 in read['readMember'][op.param1]:
                    pass
                else:
                    read['readMember'][op.param1] += op.param2
                read['ROM'][op.param1][op.param2] = op.param2
                backupData()
            else:
               pass
        except:
              pass
  except Exception as error:
      logError(error)

while True:
    try:
        ops = oepoll.singleTrace(count=50)
        if ops is not None:
            for op in ops:
                clBot(op)
                oepoll.setRevision(op.revision)
    except Exception as e:
        E = str(E)
        if "reason=None" in E:
          print (E)
          time.sleep(60)
          restart_program()
