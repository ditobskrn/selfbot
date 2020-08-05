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
# AKUN UTAMA
cl = LINE("maudyliana666@gmail.com","ditobaskaran123")

cl.log("Auth Token : ESnUFOPlJqnJ6EUY8e43.gD5TSeVN7yElVUvXKIBRuW.5WtDJv3qIG5pUUjSqjEh+ouuqOdiyfWOuedbOWDLVqc=" + str(cl.authToken))
channelToken = cl.getChannelResult()
cl.log("Channel Token : TJvDC9rMp9DZ0il9wq3bnb54lngsoWcewxoPS/JB1wSea5/FTQlFkZNNGqD9bXODQZVUNvB0IHmG4p9IKvf97maTA07cPd6ypnCLqhDsoR8AaRebLj7wMCK8l1okBPIyIojqfbYl3mAv3XkE5uwaDL7bC131BzsktZjvboJ0Coq77+GQ7t0noFnF4+vRD8v95ZacdnbkkaGVCZTraPuzsPvzOawQ+6MjngB9fKsdJo4dBv1BBeSV7A5MklYXI8PrQqN701UONFLdvfESgb1aAiFNPIus0jQMcPvRZrnqNTn0pv3F/GdhLsEdiKe/3gsQrThl3rFWFPaU9rvhrjUAO5LfqpPWMU+iezF3/XM5tPQ=', obsToken='', expiration=1596353476157, refreshToken='ipQg8VgVkYeoesw8xQ9a', channelAccessToken='cYLcbT8iqRUv4plQQiCiQL3aO0QW6REPhUuCFwG9XcfLP7OuJ9cdR03HntyzQwBz1yhWqJ/X3s+645IhECHczUl7+5qmPNFVVwz6b+wEl/6ps0hbgRoMPjsPESwV12z+lB/bRDK3wmUtDDy4phim9VQqTK4DRrqa3GpIq8RE2HdwZil231bU8/I8EWoHOWsV" + str(channelToken))

# AKUN KEDUA
db = LINE("dbscoder88@gmail.com","ditobaskaran123")
db.log("Auth Token : ETPkuxhvptuPQ6ohUjKa.UpTF3EJIZEyHTyUdfmkuIG.Ix31SU8+6jTPfjJxkQ+f3qNUAwmameN7RkG/jmqHaF4=" + str(db.authToken))
channelToken = db.getChannelResult()
db.log("Channel Token :  ChannelToken(token='XLnmEnqlikYIe/eIyQpcraXxe6b18VQthQM8YtRhoxaG6015HXMtGhc+wQlS95hn5yzmIITuFGaWhIdgVvOJGlGGe2X4r44EddtI4ltUJNjN5PxWzxj7+VtOyL9I0HyOEVg2K/rNmynLdCTcj/VJsHD/oJkUHswlrDcrppE2Qyi/SDXYYph6WnSjuxX/AlBeLe02wVA5xqfOo1Tq11qlFu6RarOX1MKeMRCGAiUiUGADD5FHJVi4IrE4UR9YCdj9QqN701UONFLdvfESgb1aAiFNPIus0jQMcPvRZrnqNTnaUNgRMDrTqCl9ywGr44GwPGWhiN77zOCIh/yzuWO4GL6WDn8T1F9zHkEaRa5FxLs=', obsToken='', expiration=1597561731980, refreshToken='fwab8pEJF3io2xd0DaxR', channelAccessToken='HoE33OeXg+3EbpM6sy2It/Skwt32nRbSTeOvB/rZV6h1tw51iTAwXHAYLm9gZx7JoITZ6PYYl0fPLI9BOAnXhw8nz6ZQ9OKFu1mpvcocMUT7XMGHWwLX6ENPAT1ZzPfqTQSo8bGV77KdUfophdc1OlQqTK4DRrqa3GpIq8RE2HdwZil231bU8/I8EWoHOWsV')" + str(channelToken))

# AKUN KETIGA
bs = LINE("coreprojectku@gmail.com","ditobaskaran123")
bs.log("Auth Token : ETPkuxhvptuPQ6ohUjKa.UpTF3EJIZEyHTyUdfmkuIG.Ix31SU8+6jTPfjJxkQ+f3qNUAwmameN7RkG/jmqHaF4=" + str(bs.authToken))
channelToken = bs.getChannelResult()
bs.log("Channel Token :  ChannelToken(token='XLnmEnqlikYIe/eIyQpcraXxe6b18VQthQM8YtRhoxaG6015HXMtGhc+wQlS95hn5yzmIITuFGaWhIdgVvOJGlGGe2X4r44EddtI4ltUJNjN5PxWzxj7+VtOyL9I0HyOEVg2K/rNmynLdCTcj/VJsHD/oJkUHswlrDcrppE2Qyi/SDXYYph6WnSjuxX/AlBeLe02wVA5xqfOo1Tq11qlFu6RarOX1MKeMRCGAiUiUGADD5FHJVi4IrE4UR9YCdj9QqN701UONFLdvfESgb1aAiFNPIus0jQMcPvRZrnqNTnaUNgRMDrTqCl9ywGr44GwPGWhiN77zOCIh/yzuWO4GL6WDn8T1F9zHkEaRa5FxLs=', obsToken='', expiration=1597561731980, refreshToken='fwab8pEJF3io2xd0DaxR', channelAccessToken='HoE33OeXg+3EbpM6sy2It/Skwt32nRbSTeOvB/rZV6h1tw51iTAwXHAYLm9gZx7JoITZ6PYYl0fPLI9BOAnXhw8nz6ZQ9OKFu1mpvcocMUT7XMGHWwLX6ENPAT1ZzPfqTQSo8bGV77KdUfophdc1OlQqTK4DRrqa3GpIq8RE2HdwZil231bU8/I8EWoHOWsV')" + str(channelToken))

readOpen = codecs.open("read.json","r","utf-8")
settingsOpen = codecs.open("temp.json","r","utf-8")

#----- INI LOGIN VIA QR LINK ----- # 
# try:
#     apiKey = "Z6vMBEnkp04n"
#     headers = {
#         "apiKey":apiKey,
#         "appName":"IOSIPAD\t10.10.0\tiPhone 8\t11.2.5",
#         "cert" : None,
#         "server": random.choice(["pool-1","pool-2"]),
#         "sysname": "DBSBOT"
#         }
#     main = json.loads(requests.get("https://api.be-team.me/qrv2",headers=headers).text)
#     print("QR LINK: " + main["result"]["qr_link"])
#     if not headers["cert"]:
#         result = json.loads(requests.get(main["result"]["cb_pincode"],headers=headers).text)
#         print("Your Pincode: " + result["result"])
#     result = json.loads(requests.get(main["result"]["cb_token"],headers=headers).text)
#     if result["status"] != 200:
#         print("[ Error ] "+ result["reason"])
#     db = LINE(result["result"]["token"],appName="IOSIPAD\t10.10.0\tiPhone 8\t11.2.5")
#     print ("===== LOGIN BERHASIL =====")
# except:pass

KAC = [db, bs]

clMID = cl.getProfile().mid
dbMid = db.getProfile().mid
bsMid = bs.getProfile().mid

clProfile = cl.getProfile()
clSettings = cl.getSettings()

dbProfile = db.getProfile()
dbSettings = db.getSettings()

bsProfile = bs.getProfile()
bsSettings = bs.getSettings()

oepoll = OEPoll(cl)
dboepoll = OEPoll(db)
Bots = [clMID, dbMid, bsMid]
read = json.load(readOpen)
settings = json.load(settingsOpen)

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
    "autoAdd": True,
    "autoJoin": True,
    "autoLeave": False,
    "autoRead": True,
    "autoResponPc": False,
    "admin":{
      "uac1ba8808fb332e753101563464fa569":True,
    },
    "bots":{},
    "addbots": False,
    "group":{},
    "blacklist":{},
    "broadcast": False,
    "lang":"JP",
    "commentPost": "HADIR BUAT LIKE STATUS KAMU \n Add my owner ID http://line.me/ti/p/~enaksusumm",
    "detectMention": True,
    "welcomeMessage": "Selamat datang jangan lupa cek note",
    "autoResponMessage": "Ngapain tag gua woy",
    "APIKey": "kPFKrDlvxOZ5EYGYcfJp7oFTt25E7EHO",
    "responsticker": False,
    "changeGroupPicture": [],
    "changePicture": True,
    "autoJoinTicket": True,
    "notifikasi": True,
    "Sider":{},
    "responMsgPc": "Hai, pesan Anda akan segera kami balas.",
    "checkSticker": False,
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
    ],
    "mimic": {
        "copy": False,
        "status": False,
        "target": {}
    }
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

def shutdownBot():
    sys.exit("============= BOT DIMATIKAN =============")

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

def Camera(to, text):
    pilih = ("#FF0000","#E000CD","#57FF00")
    warna = random.choice(pilih)
    data = {
            "type": "flex",
            "altText": "ARIFISTIFIK",
            "contents": {
             "type": "bubble",
             "styles": {
               "header": {
                 "backgroundColor": "#0000FF",
               },
               "body": {
                 "backgroundColor": "#000000",
                 "separator": True,
                 "separatorColor": "#ffffff"
               },
               "footer": {
                 "backgroundColor": "#000080",
                 "separator": True
               }
             },
             "header": {
               "type": "box",
               "layout": "horizontal",
               "contents": [
                 {
                   "type": "text",
                   "text": "  SIDER MEMBERS",
                   "weight": "bold",
                   "color": warna,
                   "size": "xxl"
                 }
               ]
             },
             "hero": {
               "type": "image",
               "url": "https://obs.line-scdn.net/{}".format(cl.getContact(op.param2).pictureStatus),
               "size": "full",
               "aspectRatio": "20:13",
               "aspectMode": "cover",
               "action": {
                 "type": "uri",
                 "uri": "https://line.me/ti/p/~arifistifik"
                 }
               },
                   "type": "bubble",
                   "body": {
                       "type": "box",
                       "layout": "horizontal",
                       "contents": [
                           {
                               "type": "text",
                               "text": "Nama: {}".format(cl.getContact(op.param2).displayName),
                               "wrap": True,
                               "color": warna,
                               "align": "center"
                           }
                       ]
                   },
                   "footer": {
                    "type": "box",
                    "layout": "vertical",
                    "spacing": "sm",
                    "contents": [{
                        "type": "button",
                        "style": "primary",
                        "color": warna,
                        "height": "sm",
                        "action": {
                            "type": "uri",
                            "label": "ADD ID LINE",
                            "uri": "https://line.me/ti/p/"+cl.getUserTicket().id
                            }                         
                        },
                    {
                        "type": "spacer",
                        "size": "sm",
                    }],
                    "flex": 0
                }
            }
        }
    cl.postTemplate(op.param1, data)

def sendTemplates(to, data):
    data = data
    url = "https://api.line.me/message/v3/share"
    headers = {}
    headers['User-Agent'] = 'Mozilla/5.0 (Linux; Android 8.1.0; Redmi Note 5 Build/OPM1.171019.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/67.0.3396.87 Mobile Safari/537.36 Line/8.1.1'  
    headers['Content-Type'] = 'application/json'  
    headers['Authorization'] = 'Bearer eyJhbGciOiJIUzI1NiJ9.5uMcEEHahauPb5_MKAArvGzEP8dFOeVQeaMEUSjtlvMV9uuGpj827IGArKqVJhiGJy4vs8lkkseiNd-3lqST14THW-SlwGkIRZOrruV4genyXbiEEqZHfoztZbi5kTp9NFf2cxSxPt8YBUW1udeqKu2uRCApqJKzQFfYu3cveyk.GoRKUnfzfj7P2uAX9vYQf9WzVZi8MFcmJk8uFrLtTqU'
    sendPost = requests.post(url, data=json.dumps(data), headers=headers)
    print(sendPost)
    return sendPost
def sendTextTemplate(to, text):
  data = {
    "type": "flex",
    "altText": "ADA PESAN",
    "contents": {
      "type": "bubble",
      "body": {
        "type": "box",
        "layout": "horizontal",
        "spacing": "md",
        "contents": [
          {
            "type": "image",
            "url": "https://i.pinimg.com/564x/59/df/b2/59dfb20c927598089a2b80ae86910a44.jpg",
            "size": "full",
            "aspectMode": "cover",
            "margin": "none",
            "position": "absolute"
          },
          {
            "type": "box",
            "layout": "vertical",
            "flex": 2,
            "contents": [
              {
                "type": "text",
                "text": text,
                "size": "sm",
                "weight": "bold",
                "wrap": True,
                "color": "#FFFFFF"
              }
            ]
          }
        ]
      },
      "styles": {
        "body": {
          "backgroundColor": "#222222"
        },
        "header": {
          "backgroundColor": "#03f5f1"
        }
      },
    }
  }
  cl.postTemplate(to, data)

def sendInfoCorona(to, text):
  data = {
    "type": "flex",
    "altText": "INFO CORONA",
    "contents": {
      "type": "bubble",
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "image",
            "url": "https://i.pinimg.com/564x/59/df/b2/59dfb20c927598089a2b80ae86910a44.jpg",
            "aspectMode": "cover",
            "position": "relative",
            "align": "center",
            "size": "full"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "KASUS CORONA INDONESIA",
                "wrap": True,
                "size": "md",
                "weight": "bold",
                "style": "normal",
                "decoration": "none",
                "align": "center",
                "color": "#ffffff"
              }
            ],
            "position": "absolute",
            "offsetTop": "15px",
            "backgroundColor": "#004EFF",
            "paddingTop": "10px",
            "paddingBottom": "10px",
            "width": "100%"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "━━━━━━━━━━━━━━━━━━",
                "color": "#ffffff",
                "align": "center"
              },
              {
                "type": "text",
                "text": text,
                "wrap": True,
                "color": "#ffffff",
                "size": "md",
                "weight": "bold",
                "offsetStart": "35px"
              },
              {
                "type": "text",
                "text": "━━━━━━━━━━━━━━━━━━",
                "color": "#ffffff",
                "align": "center"
              }
            ],
            "position": "absolute",
            "offsetBottom": "100px",
            "spacing": "xs",
            "width": "100%"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "\"MESKI TIDAK MENJADI\n GARDA TERDEPAN\n\nDENGAN DIRUMAH,\nKITA MENJADI PAHLAWAN\"",
                "color": "#FFFC00",
                "size": "sm",
                "weight": "bold",
                "style": "italic",
                "align": "center",
                "wrap": True
              }
            ],
            "position": "absolute",
            "paddingBottom": "10px",
            "offsetEnd": "0px",
            "offsetBottom": "0px",
            "offsetStart": "0px"
          }
        ],
        "position": "relative",
        "margin": "none",
        "paddingAll": "0px",
        "borderWidth": "3px",
        "borderColor": "#000000",
        "cornerRadius": "0px"
      }
    }
  }
  cl.postTemplate(to, data)

def sendTextTemplateMaster(to, text):
    data = {
      "type": "flex",
      "altText": "ADA PESAN",
      "contents": {
        "type": "bubble",
        "body": {
          "type": "box",
          "layout": "horizontal",
          "spacing": "md",
          "contents": [
            {
              "type": "image",
              "url": "https://i.pinimg.com/564x/59/df/b2/59dfb20c927598089a2b80ae86910a44.jpg",
              "size": "full",
              "aspectMode": "cover",
              "margin": "none",
              "position": "absolute"
            },
            {
              "type": "box",
              "layout": "vertical",
              "flex": 2,
              "contents": [
                {
                  "type": "text",
                  "text": text,
                  "size": "sm",
                  "weight": "bold",
                  "wrap": True,
                  "color": "#FFFFFF"
                }
              ]
            }
          ]
        },
        "styles": {
          "body": {
            "backgroundColor": "#222222"
          },
          "header": {
            "backgroundColor": "#03f5f1"
          }
        },
      }
    }
    cl.postTemplate(to, data)

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
              cl.sendMessage(op.param1, "Terimakasih telah menambahkan saya sebagai teman :D")
              cl.findAndAddContactsByMid(op.param1)
        if op.type == 24:
            print ("[ 24 ] NOTIFIED LEAVE ROOM")
            if settings["autoLeave"] == True:
              cl.leaveRoom(op.param1)
        if op.type == 19: 
          if op.param3 in clMID: #Kalo Admin ke Kick
            if op.param2 in Bots:
              pass
            else:
              random.choice(KAC).kickoutFromGroup(op.param1, [op.param2])
              random.choice(KAC).inviteIntoGroup(op.param1,[op.param3])
          if op.param3 in dbMid: # kalo db ke kick
            if op.param2 in Bots:
              pass
            else:
              cl.kickoutFromGroup(op.param1, [op.param2])
              cl.sendMessage(op.param1,"In")
          if op.param3 in bsMid: # kalo db ke kick
            if op.param2 in Bots:
              pass
            else:
              cl.kickoutFromGroup(op.param1, [op.param2])
              cl.sendMessage(op.param1,"In")
        if op.type == 13:
          if clMID in op.param3:
            print ("CL DI INVITE")
            if settings["autoJoin"] == True:
              if op.param2 in Bots and op.param2 in clMID and op.param2 in dbMid:
                cl.acceptGroupInvitation(op.param1)
                cl.sendMessage(op.param1,"In")
              else:
                cl.acceptGroupInvitation(op.param1)
                cl.sendMessage(op.param1,"In")
          elif dbMid in op.param3:
            print ("DB DI INVITE")
            if settings["autoJoin"] == True:
              if op.param2 in Bots and op.param2 in clMID and op.param2 in dbMid:
                db.acceptGroupInvitation(op.param1)
              else:
                db.acceptGroupInvitation(op.param1)
          elif bsMid in op.param3:
            print ("BS DI INVITE")
            if settings["autoJoin"] == True:
              if op.param2 in Bots and op.param2 in clMID and op.param2 in dbMid:
                bs.acceptGroupInvitation(op.param1)
              else:
                bs.acceptGroupInvitation(op.param1)
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
                  helpMessage = {
                    "type": "carousel",
                    "contents": [
                      {
                        "type": "bubble",
                        "body": {
                          "type": "box",
                          "layout": "vertical",
                          "contents": [
                            {
                              "type": "image",
                              "url": "https://i.pinimg.com/originals/ab/6c/ec/ab6ceca46ed88fccb12154f739a44b4d.jpg",
                              "size": "full",
                              "aspectMode": "cover",
                              "aspectRatio": "1280:1920"
                            },
                            {
                              "type": "box",
                              "layout": "vertical",
                              "contents": [
                                {
                                  "type": "text",
                                  "text": "HELP MENU",
                                  "color": "#ffffff",
                                  "align": "center",
                                  "size": "lg",
                                  "offsetTop": "3px",
                                  "weight": "bold"
                                }
                              ],
                              "position": "absolute",
                              "offsetTop": "18px",
                              "backgroundColor": "#004EFF",
                              "width": "100%",
                              "borderColor": "#ffffff",
                              "paddingAll": "10px"
                            },
                            {
                              "type": "box",
                              "layout": "vertical",
                              "contents": [
                                {
                                  "type": "text",
                                  "text": " ✦ Runtime\n ✦ Speed\n ✦ Status\n ✦ AllStatus 「On/Off」\n ✦ Broadcast 「On/Off」\n ✦ AutoAdd 「On/Off」\n ✦ AutoJoin 「On/Off」\n ✦ AutoJoinTicket 「On/Off」\n ✦ AutoLeave 「On/Off」\n ✦ AutoRead 「On/Off」\n ✦ AutoResponPC 「On/Off」\n ✦ Notif 「On/Off」\n",
                                  "color": "#ffffff",
                                  "size": "md",
                                  "weight": "bold",
                                  "wrap": True
                                }
                              ],
                              "offsetBottom": "300px",
                              "offsetStart": "15px"
                            }
                          ],
                          "paddingAll": "0px",
                          "height": "400px",
                          "borderWidth": "3px",
                          "borderColor": "#000000"
                        }
                      },
                      {
                        "type": "bubble",
                        "body": {
                          "type": "box",
                          "layout": "vertical",
                          "contents": [
                            {
                              "type": "image",
                              "url": "https://i.pinimg.com/originals/ab/6c/ec/ab6ceca46ed88fccb12154f739a44b4d.jpg",
                              "size": "full",
                              "aspectMode": "cover",
                              "aspectRatio": "1280:1920"
                            },
                            {
                              "type": "box",
                              "layout": "vertical",
                              "contents": [
                                {
                                  "type": "text",
                                  "text": "HELP MENU",
                                  "color": "#ffffff",
                                  "align": "center",
                                  "size": "lg",
                                  "offsetTop": "3px",
                                  "weight": "bold"
                                }
                              ],
                              "position": "absolute",
                              "offsetTop": "18px",
                              "backgroundColor": "#004EFF",
                              "width": "100%",
                              "borderColor": "#ffffff",
                              "paddingAll": "10px"
                            },
                            {
                              "type": "box",
                              "layout": "vertical",
                              "contents": [
                                {
                                  "type": "text",
                                  "text": " ✦ CheckSticker 「On/Off」\n ✦ Mimic 「On/Off」\n ✦ Cname 「Your name」\n ✦ Setpp\n ✦ Me\n ✦ MyMid\n ✦ MyName\n ✦ MyBio\n ✦ MyPicture\n ✦ MyVideoProfile\n ✦ MyCover\n ✦ StealContact 「Mention」\n",
                                  "color": "#ffffff",
                                  "size": "md",
                                  "weight": "bold",
                                  "wrap": True
                                }
                              ],
                              "offsetBottom": "300px",
                              "offsetStart": "15px"
                            }
                          ],
                          "paddingAll": "0px",
                          "height": "400px",
                          "borderWidth": "3px",
                          "borderColor": "#000000"
                        }
                      },
                      {
                        "type": "bubble",
                        "body": {
                          "type": "box",
                          "layout": "vertical",
                          "contents": [
                            {
                              "type": "image",
                              "url": "https://i.pinimg.com/originals/ab/6c/ec/ab6ceca46ed88fccb12154f739a44b4d.jpg",
                              "size": "full",
                              "aspectMode": "cover",
                              "aspectRatio": "1280:1920"
                            },
                            {
                              "type": "box",
                              "layout": "vertical",
                              "contents": [
                                {
                                  "type": "text",
                                  "text": "HELP MENU",
                                  "color": "#ffffff",
                                  "align": "center",
                                  "size": "lg",
                                  "offsetTop": "3px",
                                  "weight": "bold"
                                }
                              ],
                              "position": "absolute",
                              "offsetTop": "18px",
                              "backgroundColor": "#004EFF",
                              "width": "100%",
                              "borderColor": "#ffffff",
                              "paddingAll": "10px"
                            },
                            {
                              "type": "box",
                              "layout": "vertical",
                              "contents": [
                                {
                                  "type": "text",
                                  "text": " ✦ StealMid 「Mention」\n ✦ StealName 「Mention」\n ✦ StealBio 「Mention」\n ✦ StealPicture 「Mention」\n ✦ StealVideoProfile 「Mention」\n ✦ StealCover 「Mention」\n ✦ Broadcast 「Text」\n ✦ Invite 「ID Line」\n ✦ Friendlist\n ✦ CGname 「Text」\n ✦ CPgroup\n ✦ Gcreator\n",
                                  "color": "#ffffff",
                                  "size": "md",
                                  "weight": "bold",
                                  "wrap": True
                                }
                              ],
                              "offsetBottom": "300px",
                              "offsetStart": "15px"
                            }
                          ],
                          "paddingAll": "0px",
                          "height": "400px",
                          "borderWidth": "3px",
                          "borderColor": "#000000"
                        }
                      },
                      {
                        "type": "bubble",
                        "body": {
                          "type": "box",
                          "layout": "vertical",
                          "contents": [
                            {
                              "type": "image",
                              "url": "https://i.pinimg.com/originals/ab/6c/ec/ab6ceca46ed88fccb12154f739a44b4d.jpg",
                              "size": "full",
                              "aspectMode": "cover",
                              "aspectRatio": "1280:1920"
                            },
                            {
                              "type": "box",
                              "layout": "vertical",
                              "contents": [
                                {
                                  "type": "text",
                                  "text": "HELP MENU",
                                  "color": "#ffffff",
                                  "align": "center",
                                  "size": "lg",
                                  "offsetTop": "3px",
                                  "weight": "bold"
                                }
                              ],
                              "position": "absolute",
                              "offsetTop": "18px",
                              "backgroundColor": "#004EFF",
                              "width": "100%",
                              "borderColor": "#ffffff",
                              "paddingAll": "10px"
                            },
                            {
                              "type": "box",
                              "layout": "vertical",
                              "contents": [
                                {
                                  "type": "text",
                                  "text": " ✦ GId\n ✦ GName\n ✦ GPict\n ✦ GList\n ✦ GMemberList\n ✦ GInfo\n ✦ QR\n ✦ QR 「On/Off」\n ✦ Tagall\n ✦ Cancelall\n ✦ Keluar\n ✦ Kick 「Mention」",
                                  "color": "#ffffff",
                                  "size": "md",
                                  "weight": "bold",
                                  "wrap": True
                                }
                              ],
                              "offsetBottom": "300px",
                              "offsetStart": "15px"
                            }
                          ],
                          "paddingAll": "0px",
                          "height": "400px",
                          "borderWidth": "3px",
                          "borderColor": "#000000"
                        }
                      },
                      {
                        "type": "bubble",
                        "body": {
                          "type": "box",
                          "layout": "vertical",
                          "contents": [
                            {
                              "type": "image",
                              "url": "https://i.pinimg.com/originals/ab/6c/ec/ab6ceca46ed88fccb12154f739a44b4d.jpg",
                              "size": "full",
                              "aspectMode": "cover",
                              "aspectRatio": "1280:1920"
                            },
                            {
                              "type": "box",
                              "layout": "vertical",
                              "contents": [
                                {
                                  "type": "text",
                                  "text": "HELP MENU",
                                  "color": "#ffffff",
                                  "align": "center",
                                  "size": "lg",
                                  "offsetTop": "3px",
                                  "weight": "bold"
                                }
                              ],
                              "position": "absolute",
                              "offsetTop": "18px",
                              "backgroundColor": "#004EFF",
                              "width": "100%",
                              "borderColor": "#ffffff",
                              "paddingAll": "10px"
                            },
                            {
                              "type": "box",
                              "layout": "vertical",
                              "contents": [
                                {
                                  "type": "text",
                                  "text": " ✦ Message\n ✦ Autorespontext [text]\n ✦ Wctext [Text]",
                                  "color": "#ffffff",
                                  "size": "md",
                                  "weight": "bold",
                                  "wrap": True
                                }
                              ],
                              "offsetBottom": "300px",
                              "offsetStart": "15px"
                            }
                          ],
                          "paddingAll": "0px",
                          "height": "400px",
                          "borderWidth": "3px",
                          "borderColor": "#000000"
                        }
                      }
                    ]
                  }                  
                  cl.postFlex(to, helpMessage)
                elif msg.text.lower().startswith("scall "):
                  if msg.toType == 2:
                      sep = text.split(" ")
                      strnum = text.replace(sep[0] + " ","")
                      num = int(strnum)
                      cl.sendMessage(to, "Succesfully Spam Call to Group")
                      for var in range(0,num):
                         group = cl.getGroup(to)
                         members = [mem.mid for mem in group.members]
                         cl.acquireGroupCallRoute(to)
                         cl.inviteIntoGroupCall(to, contactIds=members)
                elif msg.text.lower().startswith("smule "):
                  proses = text.split(" ")
                  urutan = text.replace(proses[0] + " ","")
                  count = urutan.split("-")
                  search = str(count[0])
                  r = requests.get("https://www.smule.com/"+search+"/performances/json")
                  data = json.loads(r.text)
                  if len(count) == 1:
                      no = 0
                      ret_ = "DAFTAR OC\n"
                      for aa in data["list"]:
                          no += 1
                          ret_ += "\n" + str(no) + ". " + str(aa["title"])
                      ret_ += "\n\nSelanjutnya ketik: smule {}-nomor\nuntuk melihat detailnya. ".format(str(search))
                      sendTextTemplate(msg.to,ret_)
                  elif len(count) == 2:
                      try:
                          num = int(count[1])
                          b = data["list"][num - 1]
                          smule = str(b["web_url"])
                          c = "Judul Oc: "+str(b["title"])
                          c += "\nPembuat: "+str(b["owner"]["handle"])
                          c += "\nTotal like: "+str(b["stats"]["total_loves"])+" like"
                          c += "\nTotal comment: "+str(b["stats"]["total_comments"])+" comment"
                          c += "\nStatus VIP: "+str(b["owner"]["is_vip"])
                          c += "\nStatus Oc: "+str(b["message"])
                          c += "\nCreated Oc: {}".format(b["created_at"][:10])
                          c += "\nDidengarkan: {}".format(b["stats"]["total_listens"])+" orang"
                          hasil = "Detail Record\n\n"+str(c)
                          dl = str(b["cover_url"])
                          cl.sendImageWithURL(msg.to,dl)
                          cl.sendMessage(msg.to, hasil, {'AGENT_NAME': ' URL Smule','AGENT_LINK': 'https://www.smule.com/{}'.format(str(b['owner']['handle'])),'AGENT_ICON': 'https://png.icons8.com/color/50/000000/speaker.png' })
                          with requests.session() as s:
                              s.headers['user-agent'] = 'Mozilla/5.0'
                              r = s.get("https://sing.salon/smule-downloader/?url=https://www.smule.com{}".format(urllib.parse.quote(smule)))
                              data = BeautifulSoup(r.content, 'html5lib')
                              get = data.select("a[href*=https://www.smule.com/redir?]")[0]
                              title = data.findAll('h2')[0].text
                              imag = data.select("img[src*=https://www.smule.com/redir?]")[0]
                              if 'Smule.m4a' in get['download']:
                                  sendTextTemplate(msg.to,"Type: Audio\n\nPlease wait for audio...")
                                  cl.sendAudioWithURL(msg.to, get['href'])
                              else:
                                  sendTextTemplate(msg.to,"Type: Video\n\nPlease wait for video...")
                                  cl.sendVideoWithURL(msg.to, get['href'])
                      except Exception as e:
                          cl.sendMessage(msg.to,"DONE")
                elif "hbd" in msg.text.lower():
                  if settings["responsticker"] == True:
                    url = "https://game.linefriends.com/jbp-lcs-ranking/lcs/sendMessage"
                    to = msg.to
                    data = {
                      "type": "template",
                      "altText": "{} sent a sticker".format(cl.getProfile().displayName),
                      "template": {
                        "type": "image_carousel",
                        "columns": [
                          {
                            "imageUrl": "https://3.bp.blogspot.com/-Tjdw2KiP9Bg/Wfnb6krqnbI/AAAAAAAMKF4/LOZXghvCTkcaTmfSe0Fwe8CnTdOdCPj-ACLcBGAs/s1600/AW601285_21.gif",
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
                elif "halo" in msg.text.lower():
                  url = "https://game.linefriends.com/jbp-lcs-ranking/lcs/sendMessage"
                  to = msg.to
                  data = {
                    "type": "template",
                    "altText": "{} sent a sticker".format(cl.getProfile().displayName),
                    "template": {
                      "type": "image_carousel",
                      "columns": [
                        {
                          "imageUrl": "https://3.bp.blogspot.com/--HP9EeBMlC8/W8qMOk-ejkI/AAAAAAAB53o/7wHOJVUoQBoTLF78hI5I4HhIols6XDNNwCLcBGAs/s1600/AW2065640_00.gif",
                          "size": "full", 
                          "action": {
                            "type": "uri",
                            "uri": "https://google.com/"
                          }
                        }
                      ]
                    }
                  }
                  cl.postTemplate(to, data)
                elif text.lower() == 'meow':
                  cl.sendMessage(to, "Tunggu sebentar...")
                  with requests.session() as web:
                    r = web.get("https://aws.random.cat/meow")
                    data = r.text
                    data = json.loads(data)
                    cl.sendImageWithURL(to, data["file"])
                elif text.lower() == 'absen':
                  cl.sendMessage(to, "HADIR")
                  db.sendMessage(to, "HADIR")
                  bs.sendMessage(to, "HADIR")
                elif text.lower() == 'botlist':
                  cl.sendContact(to, clMID)
                  cl.sendContact(to, dbMid)
                  cl.sendContact(to, bsMid)
                elif text.lower() == 'in':
                  if sender in clMID:
                    G = cl.getGroup(msg.to)
                    ginfo = cl.getGroup(msg.to)
                    G.preventedJoinByTicket = False
                    cl.updateGroup(G)
                    invsend = 0
                    Ticket = cl.reissueGroupTicket(msg.to)
                    db.acceptGroupInvitationByTicket(msg.to,Ticket)
                    bs.acceptGroupInvitationByTicket(msg.to,Ticket)
                  elif sender in dbMid:
                    G = db.getGroup(msg.to)
                    ginfo = db.getGroup(msg.to)
                    G.preventedJoinByTicket = False
                    db.updateGroup(G)
                    invsend = 0
                    Ticket = db.reissueGroupTicket(msg.to)
                    cl.acceptGroupInvitationByTicket(msg.to,Ticket)
                elif text.lower() == 'creator':
                  dataProfile = [
                    {
                      "type": "bubble",
                      "body": {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                          {
                            "type": "button",
                            "action": {
                              "type": "message",
                              "label": "TEST",
                              "text": "haloo"
                            }
                          }
                        ]
                      }
                    }
                  ]
                  main = {
                    "type": "flex",
                    "altText": "Yow",
                    "contents": {
                        "type": "carousel",
                        "contents": dataProfile
                    }
                  }
                  cl.postTemplate(to, main)
                elif text.lower() == "info corona":
                  cl.sendMessage(to, "Tunggu sebentar...")
                  with requests.session() as web:
                    r = web.get("https://api.kawalcorona.com/indonesia/")
                    data = r.text
                    data = json.loads(data)
                    ret_ = "Positif : " + data[0]["positif"] + " Orang"
                    ret_ += "\nSembuh : " + data[0]["sembuh"] + " Orang"
                    ret_ += "\nDirawat : " + data[0]["dirawat"] + " Orang"
                    ret_ += "\nMeninggal : " + data[0]["meninggal"] + " Orang"
                    sendInfoCorona(to, str(ret_))
                elif text.lower() == 'dell':
                  cl.removeAllMessages(op.param2)
                  db.removeAllMessages(op.param2)
                  bs.removeAllMessages(op.param2)
                  cl.sendMessage(to, "Chat dibersihkan")
                elif text.lower().startswith("cname"):
                  sep = text.split(" ")
                  string = text.replace(sep[0] + " ", "")
                  if len(string) <= 20:
                      profile = cl.getProfile()
                      profile.displayName = string
                      cl.updateProfile(profile)
                      cl.sendMessage(to, "Nama diubah menjadi :\n{}".format(str(string)))
                elif text.lower().startswith("botname1"):
                  sep = text.split(" ")
                  string = text.replace(sep[0] + " ", "")
                  if len(string) <= 20:
                    profile = db.getProfile()
                    profile.displayName = string
                    db.updateProfile(profile)
                    db.sendMessage(to, "Nama diubah menjadi :\n{}".format(str(string)))
                elif text.lower().startswith("botname2"):
                  sep = text.split(" ")
                  string = text.replace(sep[0] + " ", "")
                  if len(string) <= 20:
                    profile = bs.getProfile()
                    profile.displayName = string
                    bs.updateProfile(profile)
                    bs.sendMessage(to, "Nama diubah menjadi :\n{}".format(str(string)))
                elif text.lower().startswith("cgname "):
                  if msg.toType == 2:
                    sep = text.split(" ")
                    groupname = text.replace(sep[0] + " ","")
                    if len(groupname) <= 20:
                      group = cl.getGroup(to)
                      group.name = groupname
                      cl.updateGroup(group)
                      cl.sendMessage(to, "「CHANGE GROUP NAME」\nBerhasil mengubah nama group menjadi : {}".format(groupname))
                elif text.lower().startswith("invmeto "):
                  sep = text.split(" ")
                  gid = text.replace(sep[0] + " ", "")
                  if gid == "":
                    cl.sendMessage(msg.to,"ID grup salah")
                  else:
                    try:
                      db.inviteIntoGroup(gid,[msg.from_])
                    except:
                      cl.sendMessage(msg.to,"Mungkin Saya Tidak Di Dalam Grup Itu")
                elif text.lower().startswith("ssweb"):
                  if sender in admin:
                    sep = text.split(" ")
                    query = text.replace(sep[0] + " ","")
                    cl.sendMessage(to, "Tunggu sebentar...")
                    print("[ INFO ] TAKING SCREENSHOT WEBSITE")
                    with requests.session() as web:
                      r = web.get("https://api.apiflash.com/v1/urltoimage?access_key=c7a5ef95f56c4b8ea0a9ec8d6079e01a&response_type=json&url="+str(query))
                      data = r.text
                      data = json.loads(data)
                      if data["url"] == '["Invalid URL."]':
                        cl.sendMessage(to, "URL website tidak valid")
                      else:
                        cl.sendImageWithURL(to, data["url"])
                        cl.sendMessage(to, "╚══ Screenshot Done ══╝")
                elif text.lower().startswith("cancelall"):
                  if msg.toType == 2:
                    group = cl.getGroup(to)
                    if group.invitee is None or group.invitee == []:
                      cl.sendReplyMessage(msg.id, to, "Tidak ada yang pending")
                    else:
                      invitee = [contact.mid for contact in group.invitee]
                      for inv in invitee:
                        cl.cancelGroupInvitation(to, [inv])
                      cl.sendMessage(to, "「CANCELALL」\nBerhasil membersihkan {} pendingan".format(str(len(invitee))))
                elif text.lower().startswith("google"):
                  sep = text.split(" ")
                  a = text.replace(sep[0] + " ","")
                  b = urllib.parse.quote(a)
                  cl.sendMessage(msg.to,"Sedang Mencari...")
                  cl.sendMessage(msg.to, "https://www.google.com/search?q="+a+"&oq="+a+"&aqs=chrome..69i57j35i39j0l3j69i60l3.1622j0j7&sourceid=chrome&ie=UTF-8")
                  cl.sendMessage(msg.to,"Itu Dia Linknya. . .")   
                elif text.lower() == "glistid":
                  gruplist = cl.getGroupIdsJoined()
                  kontak = cl.getGroups(gruplist)
                  num = 1
                  msgs = "╔══[ List ID Grup ]"
                  for ids in kontak:
                      msgs+="\n%i. %s" % (num, ids.id)
                      num=(num+1)
                  msgs+="\n╚══[ Finish ]\nTotal Grup : %i" % len(kontak)
                  cl.sendMessage(msg.to, msgs)
                elif text.lower() == "keluar":
                  if msg.toType == 2:
                    group = cl.getGroup(to)
                    cl.sendMessage(to, "Dadah guys!")
                    cl.leaveGroup(to)
                elif text.lower() == "bye":
                  group = cl.getGroup(to)
                  cl.leaveGroup(to)
                elif text.lower() == ".bye":
                  group = db.getGroup(to)
                  db.sendMessage(to, "Dadah")
                  db.leaveGroup(to)
                  bs.leaveGroup(to)
                elif text.lower() == "message":
                  sendTextTemplate(to,"WELCOME MESSAGE\n" + "━ " + settings["welcomeMessage"] + "\n\nAUTO RESPON MESSAGE\n" + "━ " + settings["responMsgPc"])
                elif msg.text.lower().startswith("wctext "):
                  sep = text.split(" ")
                  pesan = text.replace(sep[0] + " ", "")
                  settings["welcomeMessage"] = settings["welcomeMessage"].replace(settings["welcomeMessage"], str(pesan))
                  cl.sendMessage(to, "Welcome message berhasil diubah")
                elif msg.text.lower().startswith("autorespontext "):
                  sep = text.split(" ")
                  pesan = text.replace(sep[0] + " ", "")
                  settings["responMsgPc"] = settings["responMsgPc"].replace(settings["responMsgPc"], str(pesan))
                  cl.sendMessage(to, "Auto respon pc berhasil diubah")
                elif msg.text.lower().startswith("setapikey "):
                  sep = text.split(" ")
                  key = text.replace(sep[0] + " ", "")
                  settings["APIKey"] = settings["APIKey"].replace(settings["APIKey"], str(key))
                  cl.sendMessage(to, "API key berhasil diubah")
                elif msg.text.lower().startswith("invite "):
                  sep = text.split(" ")
                  nick = text.replace(sep[0] + " ", "")
                  conn = random.choice(KAC).findContactsByUserid(nick)
                  random.choice(KAC).findAndAddContactsByMid(conn.mid)
                  random.choice(KAC).inviteIntoGroup(msg.to, [conn.mid])
                  group = random.choice(KAC).getGroup(msg.to)
                  xname = random.choice(KAC).getContact(conn.mid)
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
                  random.choice(KAC).sendMessage(
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
                elif msg.text.lower().startswith("idline "):
                  sep = text.split(" ")
                  user = text.replace(sep[0] + " ","")
                  conn = cl.findContactsByUserid(user)
                  try:
                    anu = conn.mid
                    dn = conn.displayName
                    bio = conn.statusMessage
                    sendMention(to, anu, "「 Contact Line ID 」\n• Nama : ", "\n• Nick : "+dn+"\n• Bio : "+bio+"\n• Contact Link : http://line.me/ti/p/~"+user)
                    cl.sendContact(to, anu)
                  except Exception as e:
                    cl.sendMessage(msg.to, "ID LINE tidak ditemukan")
                elif msg.text.lower().startswith("ban "):
                  targets = []
                  key = eval(msg.contentMetadata["MENTION"])
                  key["MENTIONEES"][0]["M"]
                  for x in key["MENTIONEES"]:
                    targets.append(x["M"])
                  for target in targets:
                    try:
                        settings["blacklist"][target] = True
                        cl.sendMessage(msg.to,"Target ditambahkan!")
                        break
                    except:
                        cl.sendMessage(msg.to,"Added Target Fail !")
                        break
                elif msg.text.lower().startswith("banlist"):
                  if settings["blacklist"] == {}:
                    cl.sendMessage(msg.to,"Blacklist kosong")
                  else:
                    mc = "╔══[ Ban List ]"
                    for mi_d in settings["blacklist"]:
                      mc += "\n╠ " +cl.getContact(mi_d).displayName
                    cl.sendMessage(msg.to,mc + "\n╚══[ Finish ]")
                elif msg.text.lower().startswith("pranksms "):
                  sep = msg.text.split(" ")
                  nomor = text.replace(sep[0] + " ","")
                  r = requests.get("http://apisora2.herokuapp.com/prank/sms/?no={}".format(urllib.parse.quote(nomor)))
                  data = r.text
                  data = json.loads(data)
                  ret_ = "「 Pranked Sms 」"
                  ret_ += "\n• Status : {}".format(str(data["status"]))
                  ret_ += "\n• Tujuan "+str(data["result"])
                  cl.sendMessage(msg.to, str(ret_))
                elif text.lower() == 'speed':
                  start = time.time()
                  cl.sendMessage(to, "Tunggu sebentar...")
                  elapsed_time = time.time() - start
                  cl.sendMessage(to, "[ Speed ]\n{} detik".format(str(elapsed_time)))
                elif text.lower() == 'restart':
                  cl.sendMessage(to, "Sedang memulai ulang...")
                  restartBot()
                elif text.lower() == 'shutdown':
                  cl.sendMessage(to, "Bot dimatikan")
                  shutdownBot()
                elif text.lower() == 'runtime':
                  timeNow = time.time()
                  runtime = timeNow - botStart
                  runtime = format_timespan(runtime)
                  cl.sendMessage(to, "Bot Aktif Selama {}".format(str(runtime)))
                elif text.lower() == 'about':
                  try:
                      arr = []
                      owner = "u4669d4ad77f131a3fb4219a939fba991"
                      creator = cl.getContact(owner)
                      contact = cl.getContact(clMID)
                      grouplist = cl.getGroupIdsJoined()
                      contactlist = cl.getAllContactIds()
                      blockedlist = cl.getBlockedContactIds()
                      timeNow = time.time()
                      runtime = timeNow - botStart
                      runtime = format_timespan(runtime)
                      ret_ = "╔ Country : INDONESIA "
                      ret_ += "\n╠ My Name : {}".format(contact.displayName)
                      ret_ += "\n╠ Group : {}".format(str(len(grouplist)))
                      ret_ += "\n╠ Friend : {}".format(str(len(contactlist)))
                      ret_ += "\n╠ Blocked : {}".format(str(len(blockedlist)))
                      ret_ += "\n╚ Runtime : {}".format(str(runtime))
                      sendTextTemplateMaster(to, str(ret_))
                  except Exception as e:
                      cl.sendMessage(msg.to, str(e))
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
                      if settings["autoAdd"] == True: ret_ += "\n╠ [ ON ] Auto Add"
                      else: ret_ += "\n╠ [ OFF ] Auto Add"
                      if settings["autoJoin"] == True: ret_ += "\n╠ [ ON ] Auto Join"
                      else: ret_ += "\n╠ [ OFF ] Auto Join"
                      if settings["autoJoinTicket"] == True: ret_ += "\n╠ [ ON ] Auto Join Ticket"
                      else: ret_ += "\n╠ [ OFF ] Auto Join Ticket"
                      if settings["autoLeave"] == True: ret_ += "\n╠ [ ON ] Auto Leave"
                      else: ret_ += "\n╠ [ OFF ] Auto Leave"
                      if settings["autoRead"] == True: ret_ += "\n╠ [ ON ] Auto Read"
                      else: ret_ += "\n╠ [ OFF ] Auto Read"
                      if settings["notifikasi"] == True: ret_ += "\n╠ [ ON ] Notif"
                      else: ret_ += "\n╠ [ OFF ] Notif"
                      if settings["detectMention"] == True: ret_ += "\n╠ [ ON ] Detect Mention"
                      else: ret_ += "\n╠ [ OFF ] Detect Mention"
                      if settings["broadcast"] == True: ret_ += "\n╠ [ ON ] Group Broadcast"
                      else: ret_ += "\n╠ [ OFF ] Group Broadcast"
                      if settings["autoResponPc"] == True: ret_ += "\n╠ [ ON ] Auto Respon Chat"
                      else: ret_ += "\n╠ [ OFF ] Auto Respon Chat"
                      if settings["changePicture"] == True: ret_ += "\n╠ [ ON ] Change PP"
                      else: ret_ += "\n╠ [ OFF ] Change PP"
                      ret_ += "\n╚══[ STATUS BOT ]"
                      cl.sendMessage(to, str(ret_))
                  except Exception as e:
                      cl.sendMessage(msg.to, str(e))
                elif text.lower() == 'autoadd on':
                  settings["autoAdd"] = True
                  cl.sendMessage(to, "Mengaktifkan Auto Add")
                elif text.lower() == 'autoadd off':
                  settings["autoAdd"] = False
                  cl.sendMessage(to, "Menonaktifkan Auto Add")
                elif text.lower() == 'autojoin on':
                  settings["autoJoin"] = True
                  cl.sendMessage(to, "Mengaktifkan Auto Join")
                elif text.lower() == 'autojoin off':
                  settings["autoJoin"] = False
                  cl.sendMessage(to, "Menonaktifkan Auto Join")
                elif text.lower() == 'autoresponpc on':
                  settings["autoResponPc"] = True
                  cl.sendMessage(to, "Auto Respon PC On")
                elif text.lower() == 'autoresponpc off':
                  settings["autoResponPc"] = False
                  cl.sendMessage(to, "Auto Respon PC Off")
                elif text.lower() == 'broadcast on':
                  settings["broadcast"] = True
                  cl.sendMessage(to, "Mengaktifkan Group Broadcast")
                elif text.lower() == 'addbot on':
                  settings["addbots"] = True
                  cl.sendMessage(msg.to,"Please send to contact...")
                elif text.lower() == 'addbot off':
                  settings["addbots"] = False
                  cl.sendMessage(to, "Menonaktifkan Add Bot")
                elif text.lower() == 'broadcast off':
                  settings["broadcast"] = False
                  cl.sendMessage(to, "Menonaktifkan Group Broadcast")
                elif text.lower() == 'autoleave on':
                  settings["autoLeave"] = True
                  cl.sendMessage(to, "Mengaktifkan Auto Leave")
                elif text.lower() == 'autoleave off':
                  settings["autoLeave"] = False
                  cl.sendMessage(to, "Menonaktifkan Auto Leave")
                elif text.lower() == 'autojoin off':
                  settings["autoLeave"] = False
                  cl.sendMessage(to, "Menonaktifkan Auto Leave")
                elif text.lower() == 'autoread on':
                  settings["autoRead"] = True
                  cl.sendMessage(to, "Mengaktifkan Auto Read")
                elif text.lower() == 'autoread off':
                  settings["autoRead"] = False
                  cl.sendMessage(to, "Menonaktifkan Auto Read")
                elif text.lower() == 'checksticker on':
                  settings["checkSticker"] = True
                  cl.sendMessage(to, "Mengaktifkan Check Details Sticker")
                elif text.lower() == 'checksticker off':
                  settings["checkSticker"] = False
                  cl.sendMessage(to, "Menonaktifkan Check Details Sticker")
                elif text.lower() == 'responsticker on':
                  settings["responsticker"] = True
                  cl.sendMessage(to, "Mengaktifkan Template Sticker")
                elif text.lower() == 'responsticker off':
                  settings["responsticker"] = False
                  cl.sendMessage(to, "Menonaktifkan Template Sticker")
                elif text.lower() == 'detectmention on':
                  settings["datectMention"] = True
                  cl.sendMessage(to, "Mengaktifkan Detect Mention")
                elif text.lower() == 'detectmention off':
                  settings["datectMention"] = False
                  cl.sendMessage(to, "Menonaktifkan Detect Mention")
                elif text.lower() == 'setpp on':
                  settings["changePicture"] = True
                  cl.sendMessage(to, "Change Picture Profile On")
                elif text.lower() == 'setpp off':
                  settings["changePicture"] = False
                  cl.sendMessage(to, "Change Picture Profile Off")
                elif text.lower() == 'allstatus on':
                  settings["notifikasi"] = True
                  settings["autoAdd"] = True
                  settings["autoJoin"] = True
                  settings["autoLeave"] = True
                  settings["autoRead"] = True
                  settings["datectMention"] = True
                  settings["broadcast"] = True
                  settings["autoJoinTicket"] = True
                  settings["autoResponPc"] = True
                  settings["changePicture"] = True
                  cl.sendMessage(to, "Allstatus bot mode on")
                  db.sendMessage(to, "Allstatus bot mode on")
                elif text.lower() == 'allstatus off':
                  settings["notifikasi"] = False
                  settings["autoAdd"] = False
                  settings["autoJoin"] = False
                  settings["autoLeave"] = False
                  settings["autoRead"] = False
                  settings["datectMention"] = False
                  settings["broadcast"] = False
                  settings["autoJoinTicket"] = False
                  settings["autoResponPc"] = False
                  settings["changePicture"] = False
                  cl.sendMessage(to, "Allstatus bot mode on")
                elif text.lower() == 'mycontact':
                  sendMessageWithMention(to, clMID)
                  cl.sendContact(to, clMID)
                elif text.lower() == 'mymid':
                  cl.sendMessage(msg.to,"[MID]\n" +  clMID)
                elif text.lower() == 'myname':
                  me = cl.getContact(clMID)
                  cl.sendMessage(msg.to,"[DisplayName]\n" + me.displayName)
                elif text.lower() == 'mybio':
                  me = cl.getContact(clMID)
                  sendTextTemplate(msg.to,"[StatusMessage]\n" + me.statusMessage)
                elif text.lower() == 'mypicture':
                  me = cl.getContact(clMID)
                  cl.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/" + me.pictureStatus)
                elif text.lower() == 'myvideoprofile':
                  me = cl.getContact(clMID)
                  cl.sendVideoWithURL(msg.to,"http://dl.profile.line-cdn.net/" + me.pictureStatus + "/vp")
                elif text.lower() == 'mycover':
                  me = cl.getContact(clMID)
                  cover = cl.getProfileCoverURL(clMID)    
                  cl.sendImageWithURL(msg.to, cover)
                elif msg.text.lower().startswith("stealcontact "):
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
                elif msg.text.lower().startswith("mtoh "):
                  sep = text.split(" ")
                  txt = text.replace(sep[0] + " ","")
                  url = requests.get("http://api.aladhan.com/v1/gToH?date={}".format(txt))
                  data = url.json()
                  result = "~ Hijriah ~ = {}".format(str(data["data"]["hijri"]["date"]))
                  result += "\n~ Masehi ~ = {}".format(str(data["data"]["gregorian"]["date"]))
                  sendTextTemplate(to, result)

                elif msg.text.lower().startswith("asmaulhusna "):
                  sep = text.split(" ")
                  txt = text.replace(sep[0] + " ","")
                  url = requests.get("http://api.aladhan.com/asmaAlHusna/{}".format(txt))
                  data = url.json()
                  result = "~ Asma Allah ke {} = ~ {} ~".format(txt,data["data"][0]["name"])
                  result += "\n~Artinya =~ {} ~".format(data["data"][0]["en"]["meaning"])
                  sendTextTemplate(to, result)

                elif msg.text.lower().startswith("al-quran "):
                  sep = text.split(" ")
                  txt = text.replace(sep[0] + " ","")
                  web = requests.get("http://api.alquran.cloud/surah/{}".format(txt))
                  data = web.json()
                  result = "~[~{}~]~".format(data["data"]["englishName"])
                  quran = data["data"]
                  result += "\n~ Surah ke {} ~".format(quran["number"])
                  result += "\n~ Nama Surah ~ {} ~".format(quran["name"])
                  result += "\n~ {} Ayat ~".format(quran["numberOfAyahs"])
                  result += "\n~ {} ~".format(quran["name"])
                  result += "\n~ Ayat Sajadah = {} ~".format(quran["ayahs"][0]["sajda"])
                  result += "\n==================\n"
                  no = 0
                  for ayat in data["data"]["ayahs"]:
                      no += 1
                      result += "\n{}. {}".format(no,ayat['text'])
                  k = len(result)//10000
                  for aa in range(k+1):
                      sendTextTemplate(to,'{}'.format(result[aa*10000 : (aa+1)*10000]))

                elif msg.text.lower().startswith("ayat sajadah"):
                  url = requests.get("http://api.alquran.cloud/sajda/quran-uthmani")
                  data = url.json()
                  result = "~[Ayat Sajadah]~"
                  for ayat in data["data"]["ayahs"]:
                      ayatnya = ayat["text"]
                      result += "\n{}".format(ayatnya)
                      result += "\n Surah {}".format(ayat["surah"]["englishName"])
                  result += "\n ~~~~~~ Juz {} ~~~~~~".format(ayat["juz"])
                  sendTextTemplate(to, result)
                elif msg.text.lower().startswith("stealmid "):
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
                elif msg.text.lower().startswith("stealname "):
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
                      cl.sendMessage(msg.to, "[ Display Name ]\n" + contact.displayName)
                elif msg.text.lower().startswith("stealbio "):
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
                      sendTextTemplate(msg.to, "[ Status Message ]\n{}" + contact.statusMessage)
                elif msg.text.lower().startswith("stealpicture "):
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
                elif msg.text.lower().startswith("stealvideoprofile "):
                  if 'MENTION' in msg.contentMetadata.keys()!= None:
                    names = re.findall(r'@(\w+)', text)
                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                    mentionees = mention['MENTIONEES']
                    lists = []
                    for mention in mentionees:
                      if mention["M"] not in lists:
                        lists.append(mention["M"])
                    for ls in lists:
                      path = "http://dl.profile.cl.naver.jp/" + cl.getContact(ls).pictureStatus + "/vp"
                      cl.sendImageWithURL(msg.to, str(path))
                elif msg.text.lower().startswith("stealcover "):
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
                elif msg.text.lower().startswith("cloneprofile "):
                  if 'MENTION' in msg.contentMetadata.keys()!= None:
                    names = re.findall(r'@(\w+)', text)
                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                    mentionees = mention['MENTIONEES']
                    for mention in mentionees:
                      contact = mention["M"]
                      break
                    try:
                      cl.cloneContactProfile(contact)
                      sendTextTemplate(msg.to, "clone member ")
                    except:
                      sendTextTemplate(msg.to, "Gagal clone member")
                elif text.lower() == 'restoreprofile':
                  try:
                    clProfile.displayName = str(myProfile["displayName"])
                    clProfile.statusMessage = str(myProfile["statusMessage"])
                    clProfile.pictureStatus = str(myProfile["pictureStatus"])
                    cl.updateProfileAttribute(8, clProfile.pictureStatus)
                    cl.updateProfile(clProfile)
                    sendTextTemplate(msg.to, "restore profile ")
                  except:
                    sendTextTemplate(msg.to, "Gagal restore profile")

                elif msg.text.lower().startswith("mimicadd "):
                  targets = []
                  key = eval(msg.contentMetadata["MENTION"])
                  key["MENTIONEES"][0]["M"]
                  for x in key["MENTIONEES"]:
                    targets.append(x["M"])
                  for target in targets:
                    try:
                      settings["mimic"]["target"][target] = True
                      sendTextTemplate(msg.to,"Target ditambahkan!")
                      break
                    except:
                      sendTextTemplate(msg.to,"Added Target Fail !")
                      break
                elif msg.text.lower().startswith("mimicdel "):
                  targets = []
                  key = eval(msg.contentMetadata["MENTION"])
                  key["MENTIONEES"][0]["M"]
                  for x in key["MENTIONEES"]:
                    targets.append(x["M"])
                  for target in targets:
                    try:
                      del settings["mimic"]["target"][target]
                      sendTextTemplate(msg.to,"Target dihapuskan!")
                      break
                    except:
                      sendTextTemplate(msg.to,"Deleted Target Fail !")
                      break
                elif text.lower() == 'mimiclist':
                  if settings["mimic"]["target"] == {}:
                    sendTextTemplate(msg.to,"Tidak Ada Target")
                  else:
                    mc = "╔══[ Mimic List ]"
                    for mi_d in settings["mimic"]["target"]:
                      mc += "\n╠ "+cl.getContact(mi_d).displayName
                    sendTextTemplate(msg.to,mc + "\n╚══[ Finish ]")
                elif text.lower() == 'me':
                  if msg.toType == 2:
                    contact = cl.getProfile()
                    mids = [contact.mid]
                    status = cl.getContact(sender)                              
                    data = {
                      "contents": [
                        {
                          "hero": {
                            "aspectMode": "cover",
                            "aspectRatio": "4:4",
                            "type": "image",
                            "url": "https://obs.line-scdn.net/{}".format(cl.getContact(sender).pictureStatus),
                            "size": "full",
                            "align": "center",
                          },
                          "styles": {
                            "body": {
                              "backgroundColor": "#222222"
                            },
                            "footer": {
                              "backgroundColor": "#222222"
                            },
                            "header": {
                              "backgroundColor": "#222222"
                            }
                          },
                          "type": "bubble",
                          "body": {
                            "contents": [
                              {
                                "contents": [
                                  {
                                    "contents": [
                                      {
                                        "type": "text",
                                        "text": "{}".format(status.displayName),
                                        "size": "xl",
                                        "wrap": True,
                                        "weight": "bold",
                                        "color": "#FFAD00",
                                        "align": "center"               
                                      }
                                    ],
                                    "type": "box",
                                    "layout": "baseline"
                                  }
                                ],
                                "type": "box",
                                "spacing": "xs",
                                "layout": "vertical"
                              }
                            ],
                            "type": "box",
                            "spacing": "xs",
                            "layout": "vertical"
                          }, 
                        }
                      ],
                      "type": "carousel"
                    }
                    cl.postFlex(to, data)
                elif text.lower() == '1cak':
                  r = requests.get("https://beta.moe.team/api/1cak/?apikey=IUV3RXZcPJ2L1HqTKSICmOhTqxlVrwDWkG8eu2ywvYy1UAjIHClvvFkChcAkXE6P")
                  data = r.text
                  a = json.loads(data)                            
                  cl.sendMessage(to, a["result"]["title"])       
                  cl.sendImageWithURL(to, a["result"]["image"])
                elif "mimic" in msg.text.lower():
                  sep = text.split(" ")
                  mic = text.replace(sep[0] + " ","")
                  if mic == "on":
                    if settings["mimic"]["status"] == False:
                      settings["mimic"]["status"] = True
                      sendTextTemplate(msg.to,"Reply Message on")
                  elif mic == "off":
                    if settings["mimic"]["status"] == True:
                      settings["mimic"]["status"] = False
                      sendTextTemplate(msg.to,"Reply Message off")
                elif "youtube" in msg.text.lower():
                  if msg.toType == 2:
                    try:
                      sep = msg.text.split(" ")
                      textToSearch = msg.text.replace(sep[0] + " ","")
                      query = urllib.parse.quote(textToSearch)
                      search_url="https://www.youtube.com/results?search_query="
                      mozhdr = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'}
                      sb_url = search_url + query
                      sb_get = requests.get(sb_url, headers = mozhdr)
                      soupeddata = BeautifulSoup(sb_get.content, "html.parser")
                      yt_links = soupeddata.find_all("a", class_ = "yt-uix-tile-link")
                      x = (yt_links[1])
                      yt_href =  x.get("href")
                      yt_href = yt_href.replace("watch?v=", "")
                      qx = "https://youtu.be" + str(yt_href)
                      vid = pafy.new(qx)
                      stream = vid.streams
                      best = vid.getbest()
                      best.resolution, best.extension
                      for s in stream:
                        me = best.url
                        data = {
                          "type": "flex",
                          "altText": "YOUTUBE",
                          "contents": {
                            "styles": {
                              "body": {
                                "backgroundColor": "#FFFFFF"
                              },
                              "footer": {
                                "backgroundColor": "#FF0000"
                              }
                            },
                            "type": "bubble",
                            "body": {
                              "contents": [
                                {
                                  "contents": [
                                    {
                                      "url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSgekIeIdfny8Bgr-WBIhhZgecUBZKyE89-u_SdB6Z2P-XNPdaVXhrSL1o",
                                      "type": "image"
                                    },
                                    {
                                      "type": "separator",
                                      "color": "#C0C0C0"
                                    },
                                    {
                                      "text": "YOUTUBE\nVIDEOS\nLOADING...\n\nPLAY",
                                      "size": "sm",
                                      "color": "#222222",
                                      "wrap": True,
                                      "weight": "bold",
                                      "type": "text"
                                    }
                                  ],
                                  "type": "box",
                                  "spacing": "md",
                                  "layout": "horizontal"
                                },
                                {
                                  "type": "separator",
                                  "color": "#C0C0C0"
                                },
                                {
                                  "contents": [
                                    {
                                      "text": "JUDUL\n "+vid.title+" ?",
                                      "size": "xs",
                                      "align": "center",
                                      "color": "#222222",
                                      "wrap": True,
                                      "weight": "bold",
                                      "type": "text"
                                    }
                                  ],
                                  "type": "box",
                                  "spacing": "md",
                                  "layout": "vertical"
                                },
                                {
                                  "type": "separator",
                                  "color": "#C0C0C0"
                                },
                                {
                                  "contents": [
                                    {
                                      "contents": [
                                        {
                                          "url": "https://media2.giphy.com/media/13Nc3xlO1kGg3S/100.webp?cid=19f5b51a5c7364c358654a44730cc489",
                                          "type": "icon",
                                          "size": "md"
                                        },
                                        {
                                          "text": "Author : "+str(vid.author),
                                          "size": "sm",
                                          "margin": "none",
                                          "color": "#6F00FF",
                                          "wrap": True,
                                          "weight": "regular",
                                          "type": "text"
                                        }
                                      ],
                                      "type": "box",
                                      "layout": "baseline"
                                    },
                                    {
                                      "contents": [
                                        {
                                          "url": "https://media2.giphy.com/media/13Nc3xlO1kGg3S/100.webp?cid=19f5b51a5c7364c358654a44730cc489",
                                          "type": "icon",
                                          "size": "md"
                                        },
                                        {
                                          "text": "Duration : "+str(vid.duration),
                                          "size": "sm",
                                          "margin": "none",
                                          "color": "#6F00FF",
                                          "wrap": True,
                                          "weight": "regular",
                                          "type": "text"
                                        }
                                      ],
                                      "type": "box",
                                      "layout": "baseline"
                                    },
                                    {
                                      "contents": [
                                        {
                                          "url": "https://media2.giphy.com/media/13Nc3xlO1kGg3S/100.webp?cid=19f5b51a5c7364c358654a44730cc489",
                                          "type": "icon",
                                          "size": "md"
                                        },
                                        {
                                          "text": "Likes : "+str(vid.likes),
                                          "size": "sm",
                                          "margin": "none",
                                          "color": "#6F00FF",
                                          "wrap": True,
                                          "weight": "regular",
                                          "type": "text"
                                        }
                                      ],
                                      "type": "box",
                                      "layout": "baseline"
                                    },
                                    {
                                      "contents": [
                                        {
                                          "url": "https://media2.giphy.com/media/13Nc3xlO1kGg3S/100.webp?cid=19f5b51a5c7364c358654a44730cc489",
                                          "type": "icon",
                                          "size": "md"
                                        },
                                        {
                                          "text": "Rating : "+str(vid.rating),
                                          "size": "sm",
                                          "margin": "none",
                                          "color": "#6F00FF",
                                          "wrap": True,
                                          "weight": "regular",
                                          "type": "text"
                                        }
                                      ],
                                      "type": "box",
                                      "layout": "baseline"
                                    }
                                  ],
                                  "type": "box",
                                  "layout": "vertical"
                                }
                              ],
                              "type": "box",
                              "spacing": "md",
                              "layout": "vertical"
                            },
                            "footer": {
                              "type": "box",
                              "layout": "vertical",
                              "contents": [
                                {
                                  "type": "box",
                                  "layout": "horizontal",
                                  "contents": [
                                    {
                                      "type": "button",
                                      "flex": 2,
                                      "style": "primary",
                                      "color": "#800000",
                                      "height": "sm",
                                      "action": {
                                        "type": "uri",
                                        "label": "PLAY",
                                        "uri": me
                                      }
                                    },
                                    {
                                      "flex": 3,
                                      "type": "button",
                                      "style": "primary",
                                      "color": "#800000",
                                      "margin": "sm",
                                      "height": "sm",
                                      "action": {
                                        "type": "uri",
                                        "label": "YOUTUBE",
                                        "uri": search_url
                                      }
                                    }
                                  ]
                                }
                              ]
                            }
                          }
                        }
                        cl.postTemplate(to, data)
                        cl.sendVideoWithURL(msg.to, me)
                    except Exception as e:
                        cl.sendMessage(msg.to,str(e))
                elif "mp4" in msg.text.lower():
                  if msg.toType == 2:
                    try:
                      sep = msg.text.split(" ")
                      textToSearch = msg.text.replace(sep[0] + " ","")
                      query = urllib.parse.quote(textToSearch)
                      search_url="https://www.youtube.com/results?search_query="
                      mozhdr = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'}
                      sb_url = search_url + query
                      sb_get = requests.get(sb_url, headers = mozhdr)
                      soupeddata = BeautifulSoup(sb_get.content, "html.parser")
                      yt_links = soupeddata.find_all("a", class_ = "yt-uix-tile-link")
                      x = (yt_links[1])
                      yt_href =  x.get("href")
                      yt_href = yt_href.replace("watch?v=", "")
                      qx = "https://youtu.be" + str(yt_href)
                      vid = pafy.new(qx)
                      stream = vid.streams
                      best = vid.getbest()
                      best.resolution, best.extension
                      for s in stream:
                          me = best.url
                      cl.sendVideoWithURL(msg.to, me)
                    except Exception as e:
                      cl.sendMessage(msg.to,str(e))
                elif "mp3" in msg.text.lower():
                  if msg.toType == 2:
                    try:
                      sep = msg.text.split(" ")
                      textToSearch = msg.text.replace(sep[0] + " ","")
                      query = urllib.parse.quote(textToSearch)
                      search_url="https://www.youtube.com/results?search_query="
                      mozhdr = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'}
                      sb_url = search_url + query
                      sb_get = requests.get(sb_url, headers = mozhdr)
                      soupeddata = BeautifulSoup(sb_get.content, "html.parser")
                      yt_links = soupeddata.find_all("a", class_ = "yt-uix-tile-link")
                      x = (yt_links[1])
                      yt_href =  x.get("href")
                      yt_href = yt_href.replace("watch?v=", "")
                      qx = "https://youtu.be" + str(yt_href)
                      vid = pafy.new(qx)
                      stream = vid.streams
                      best = vid.getbest()
                      best.resolution, best.extension
                      for s in stream:
                          me = best.url
                      cl.sendAudioWithURL(msg.to, me)
                    except Exception as e:
                        cl.sendMessage(msg.to,str(e))
                elif msg.text.lower().startswith("bye "):
                  separate = msg.text.split(" ")
                  number = msg.text.replace(separate[0] + " "," ")
                  groups = cl.getGroupIdsJoined()
                  gid = groups[int(number)-1]
                  group = cl.getGroup(gid)  
                  for i in group:
                    ginfo = cl.getGroup(i)
                    cl.sendMessage(to, "Ini : " + str(ginfo.name ))
                    if ginfo == group:
                      cl.leaveGroup(i)
                      cl.sendMessage(msg.to,"Berhasil keluar dari grup "+ str(ginfo.name))                     
                elif msg.text.lower().startswith("tagremot: "):
                  separate = msg.text.split(":")
                  number = msg.text.replace(separate[0] + ":"," ")
                  groups = cl.getGroupIdsJoined()
                  gid = groups[int(number)-1]                                                            
                  group = cl.getGroup(gid)                                                            
                  nama = [contact.mid for contact in group.members]
                  k = len(nama)//19
                  for a in range(k+1):
                    txt = u''
                    s=0
                    b=[]
                    for i in group.members[a*19 : (a+1)*19]:
                      b.append(i.mid)
                    RmentionMembers(gid, b)                            
                    sendTextTemplate(msg.to, "Berhasil Mention Member di Group: \n " + str(group.name))
                elif "memberpicture" in msg.text.lower():
                  if msg.toType == 2:
                    kontak = cl.getGroup(to)
                    group = kontak.members
                    picall = []
                    for ids in group:
                      if len(picall) >= 400:
                        pass
                      else:
                        picall.append({
                          "imageUrl": "https://os.line.naver.jp/os/p/{}".format(ids.mid),
                          "action": {
                            "type": "uri",
                            "uri": "http://line.me/ti/p/~enaksusumm"
                            }
                          }
                        )
                    k = len(picall)//10
                    for aa in range(k+1):
                      data = {
                        "type": "template",
                        "altText": "{}".format(cl.getProfile().displayName),
                        "template": {
                          "type": "image_carousel",
                          "columns": picall[aa*10 : (aa+1)*10]
                        }
                      }
                      cl.postTemplate(to, data)
                elif "gettoken" in msg.text.lower():
                  if msg.toType == 2:
                    lists = {"result": [{"name": "Chrome 1\n(CHROMEOS)",},{"name": "Ios 1\n(ISOPAD)",},{"name": "Win 1\n(DESKTOPWIN)",}]}
                    if lists["result"] != []:
                      ret_ = []
                      for fn in lists["result"]:
                        if len(ret_) >= 20:
                          pass
                        else:
                          ret_.append({
                                  "title": "{}".format(fn["name"]),
                                  "text": "ketik Sesuai ketikan di atas",
                                  "actions": [
                                      {
                                          "type": "uri",
                                          "label": "CREATOR",
                                          "uri": "http://line.me/ti/p/~enaksusumm",
                                      }
                                  ]
                              }
                          )
                      k = len(ret_)//10
                      for aa in range(k+1):
                        data = {
                            "type": "template",
                            "altText": "Token",
                            "template": {
                                "type": "carousel",
                                "columns": ret_[aa*10 : (aa+1)*10]
                            }
                        }
                      cl.postTemplate(to, data)

                elif msg.text.lower().startswith("chrome"):
                  separate = msg.text.split(" ")
                  jmlh = int(separate[1])
                  for x in range(jmlh):
                    Headers1.update({'x-lpqs' : '/api/v4/TalkService.do'})
                    transport = THttpClient.THttpClient('https://gd2.line.naver.jp/api/v4/TalkService.do')
                    transport.setCustomHeaders(Headers1)
                    protocol = TCompactProtocol.TCompactProtocol(transport)
                    client = LineService.Client(protocol)
                    qr = client.getAuthQrcode(keepLoggedIn=1, systemName=connect1)
                    link = "line://au/q/" + qr.verifier
                    print(link)
                    sendTextTemplate(msg.to,"Starting white true")
                    sendTextTemplate(msg.to,"Except")
                    cl.sendMessage(msg.to,str(link))
                    Headers1.update({"x-lpqs" : '/api/v4/TalkService.do', 'X-Line-Access': qr.verifier})
                    json.loads(requests.session().get('https://gd2.line.naver.jp/Q', headers=Headers1).text)
                    Headers1.update({'x-lpqs' : '/api/v4p/rs'})
                    transport = THttpClient.THttpClient('https://gd2.line.naver.jp/api/v4p/rs')
                    transport.setCustomHeaders(Headers1)
                    protocol = TCompactProtocol.TCompactProtocol(transport)
                    client = LineService.Client(protocol)
                    req = LoginRequest()
                    req.type = 1
                    req.verifier = qr.verifier
                    req.e2eeVersion = 1
                    res = client.loginZ(req)
                    print('\n')
                    print(res.authToken)
                  else:
                    sendTextTemplate(msg.to, "The bot has been mmade with DPKheaders")
                    cl.sendMessage(msg.to,str(res.authToken))
                elif msg.text.lower().startswith("win"):
                  separate = msg.text.split(" ")
                  jmlh = int(separate[1])
                  for x in range(jmlh):
                    Headers2.update({'x-lpqs' : '/api/v4/TalkService.do'})
                    transport = THttpClient.THttpClient('https://gd2.line.naver.jp/api/v4/TalkService.do')
                    transport.setCustomHeaders(Headers2)
                    protocol = TCompactProtocol.TCompactProtocol(transport)
                    client = LineService.Client(protocol)
                    qr = client.getAuthQrcode(keepLoggedIn=1, systemName=connect2)
                    link = "line://au/q/" + qr.verifier
                    print(link)
                    sendTextTemplate(msg.to,"Starting white true")
                    sendTextTemplate(msg.to,"Except")
                    cl.sendMessage(msg.to,str(link))
                    Headers2.update({"x-lpqs" : '/api/v4/TalkService.do', 'X-Line-Access': qr.verifier})
                    json.loads(requests.session().get('https://gd2.line.naver.jp/Q', headers=Headers2).text)
                    Headers2.update({'x-lpqs' : '/api/v4p/rs'})
                    transport = THttpClient.THttpClient('https://gd2.line.naver.jp/api/v4p/rs')
                    transport.setCustomHeaders(Headers2)
                    protocol = TCompactProtocol.TCompactProtocol(transport)
                    client = LineService.Client(protocol)
                    req = LoginRequest()
                    req.type = 1
                    req.verifier = qr.verifier
                    req.e2eeVersion = 1
                    res = client.loginZ(req)
                    print('\n')
                    print(res.authToken)
                  else:
                    sendTextTemplate(msg.to, "The bot has been mmade with ARIFISTIFIKheaders")
                    cl.sendMessage(msg.to,str(res.authToken))
                elif msg.text.lower().startswith("ios"):
                  separate = msg.text.split(" ")
                  jmlh = int(separate[1])
                  for x in range(jmlh):
                    Headers3.update({
                      'x-lpqs': '/api/v4/TalkService.do'
                    })
                    transport = THttpClient.THttpClient('https://gd2.line.naver.jp/api/v4/TalkService.do')
                    transport.setCustomHeaders(Headers3)
                    protocol = TCompactProtocol.TCompactProtocol(transport)
                    client = LineService.Client(protocol)
                    qr = client.getAuthQrcode(keepLoggedIn = 1, systemName = connect3)
                    link = "line://au/q/" + qr.verifier
                    print(link)
                    sendTextTemplate(msg.to, "Starting white true")
                    sendTextTemplate(msg.to, "Except")
                    cl.sendMessage(msg.to, str(link))
                    Headers3.update({
                      "x-lpqs": '/api/v4/TalkService.do',
                      'X-Line-Access': qr.verifier
                    })
                    json.loads(requests.session().get('https://gd2.line.naver.jp/Q', headers = Headers3).text)
                    Headers3.update({
                      'x-lpqs': '/api/v4p/rs'
                    })
                    transport = THttpClient.THttpClient('https://gd2.line.naver.jp/api/v4p/rs')
                    transport.setCustomHeaders(Headers3)
                    protocol = TCompactProtocol.TCompactProtocol(transport)
                    client = LineService.Client(protocol)
                    req = LoginRequest()
                    req.type = 1
                    req.verifier = qr.verifier
                    req.e2eeVersion = 1
                    res = client.loginZ(req)
                    print('\n')
                    print(res.authToken)
                  else :
                    sendTextTemplate(msg.to, "The bot has been mmade with DPKTEAMheader")
                    cl.sendMessage(msg.to, str(res.authToken))
                elif msg.text.lower().startswith("wallpaper "):
                  sep = text.split(" ")
                  search = text.replace(sep[0] + " ","")
                  r = requests.get("https://wall.alphacoders.com/api2.0/get.php?auth=e0c40357f688caecbe101d0e8cad309d&method=search&term="+str(search))
                  data = r.text
                  a = json.loads(data)
                  if a["success"] == True:
                    result = a["wallpapers"]
                    k = len(result)//5
                    for image in range(k+1):
                      cl.sendImageWithURL(to, result[image]["url_image"])
                    cl.sendMessage(to, "FINISH")
                  else:
                    cl.sendMessage(to, "Error")
                elif msg.text.lower().startswith("tiktokdown "):
                  sep = text.split(" ")
                  link = text.replace(sep[0] + " ","")
                  print(str(link))
                  r = requests.post("https://tools.coreproject.my.id/test.php?url="+str(link))
                  print(r)
                  data = r.text
                  a = json.loads(data)
                  cl.sendMessage(to, a)
                  if a["result"] == False:
                    cl.sendMessage(to, "Gagal")
                  else:
                    cl.sendMessage(to, "Processing...")
                    cl.sendVideoWithURL(to, a["data"]["video"]["source"]["vid"])
                    cl.sendMessage(to, "[ FINISH ]")
                elif msg.text.lower().startswith("red "):
                  if msg.toType == 2:
                    cl.sendMessage(to, "Processing...")
                    sep = text.split(" ")
                    search = text.replace(sep[0] + " ","")
                    r = requests.get("https://beta.moe.team/api/redtube/?apikey=IUV3RXZcPJ2L1HqTKSICmOhTqxlVrwDWkG8eu2ywvYy1UAjIHClvvFkChcAkXE6P&type=search&q="+str(search))
                    data = r.text
                    a = json.loads(data)
                    if a["code"] == 200:
                      result = a["result"]
                      k = len(result)//5
                      for thumb in range(k+1):
                        data = [
                          {
                            "type": "bubble",
                            "hero": {
                              "type": "image",
                              "url": result[thumb]["video"]["thumb"],
                              "size": "full",
                              "aspectRatio": "20:13",
                              "aspectMode": "cover",
                              "action": {
                                "type": "uri",
                                "uri": result[thumb]["video"]["url"]
                              }
                            },
                            "body": {
                              "type": "box",
                              "layout": "vertical",
                              "contents": [
                                {
                                  "type": "text",
                                  "text": result[thumb]["video"]["title"],
                                  "weight": "bold",
                                  "size": "xl"
                                },
                                {
                                  "type": "box",
                                  "layout": "vertical",
                                  "margin": "lg",
                                  "spacing": "sm",
                                  "contents": [
                                    {
                                      "type": "box",
                                      "layout": "baseline",
                                      "spacing": "sm",
                                      "contents": [
                                        {
                                          "type": "text",
                                          "text": "URL",
                                          "color": "#aaaaaa",
                                          "size": "sm",
                                          "flex": 1
                                        },
                                        {
                                          "type": "text",
                                          "text": result[thumb]["video"]["url"],
                                          "wrap": True,
                                          "color": "#666666",
                                          "size": "sm",
                                          "flex": 5
                                        }
                                      ]
                                    }
                                  ]
                                }
                              ]
                            }
                          }
                        ]
                        result = {
                          "type": "flex",
                          "altText": "Ada pesan",
                          "contents": {
                              "type": "carousel",
                              "contents": data
                          }
                        }
                        cl.postTemplate(to, result)
                      cl.sendMessage(to, "════ FINISH ════")
                    else :
                      cl.sendMessage(to, "GAGAL")
                elif text.lower() == 'gcreator':
                    group = cl.getGroup(to)
                    GS = group.creator.mid
                    cl.sendContact(to, GS)
                elif text.lower() == 'gid':
                    gid = cl.getGroup(to)
                    cl.sendMessage(to, "[ID Group : ]\n" + gid.id)
                elif text.lower() == 'grouppicture':
                    group = cl.getGroup(to)
                    path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                    cl.sendImageWithURL(to, path)
                elif text.lower() == 'gname':
                    gid = cl.getGroup(to)
                    cl.sendMessage(to, "[Nama Group : ]\n" + gid.name)
                elif text.lower() == 'qr':
                    if msg.toType == 2:
                        group = cl.getGroup(to)
                        if group.preventedJoinByTicket == False:
                            ticket = cl.reissueGroupTicket(to)
                            cl.sendMessage(to, "[ Group Ticket ]\nhttps://line.me/R/ti/g/{}".format(str(ticket)))
                        else:
                            cl.sendMessage(to, "Grup qr tidak terbuka silahkan buka terlebih dahulu dengan perintah {}openqr".format(str(settings["keyCommand"])))
                elif text.lower() == 'qr on':
                    if msg.toType == 2:
                        group = cl.getGroup(to)
                        if group.preventedJoinByTicket == False:
                            cl.sendMessage(to, "Grup qr sudah terbuka")
                        else:
                            group.preventedJoinByTicket = False
                            cl.updateGroup(group)
                            cl.sendMessage(to, "membuka grup qr")
                elif text.lower() == 'qr off':
                    if msg.toType == 2:
                        group = cl.getGroup(to)
                        if group.preventedJoinByTicket == True:
                            cl.sendMessage(to, "Grup qr sudah tertutup")
                        else:
                            group.preventedJoinByTicket = True
                            cl.updateGroup(group)
                            cl.sendMessage(to, "menutup grup qr")
                elif text.lower() == "autojointicket on":
                  settings["autoJoinTicket"] = True
                  cl.sendMessage(to, "Berhasil mengaktifkan auto join by ticket")
                elif text.lower() == "autojointicket off":
                  settings["autoJoinTicket"] = False
                  cl.sendMessage(to, "Berhasil menonaktifkan auto join by ticket")
                elif msg.text.lower().startswith("kick "):
                  if 'MENTION' in msg.contentMetadata.keys() != None:
                    names = re.findall(r'@(\w+)', text)
                    mention = ast.literal_eval(
                    msg.contentMetadata['MENTION'])
                    mentionees = mention['MENTIONEES']
                    for mention in mentionees:
                        cl.kickoutFromGroup(msg.to,[mention['M']])
                elif text.lower().startswith("adminadd "):
                  key = eval(msg.contentMetadata["MENTION"])
                  key["MENTIONEES"][0]["M"]
                  targets = []
                  for x in key["MENTIONEES"]:
                    targets.append(x["M"])
                  for target in targets:
                    try:
                      settings["admin"][target] = True
                      sendTextTemplate(msg.to,"Berhasil menambahkan admin ")
                      break
                    except:
                      sendTextTemplate(msg.to,"Gagal menambahkan admin ")
                      break
                elif text.lower().startswith("admindel "):
                  targets = []
                  key = eval(msg.contentMetadata["MENTION"])
                  key["MENTIONEES"][0]["M"]
                  for x in key["MENTIONEES"]:
                    targets.append(x["M"])
                  for target in targets:
                    try:
                      del settings["admin"][target]
                      sendTextTemplate(msg.to,"Admin dihapuskan!")
                      break
                    except:
                      sendTextTemplate(msg.to,"Deleted Target Fail !")
                      break
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
                    cl.sendImageWithURL(to, path)
                elif msg.text.lower().startswith("broadcast "):
                  sep = msg.text.split(" ")
                  pesan = msg.text.replace(sep[0] + " ","")
                  utama = cl.getGroupIdsJoined()
                  kedua = db.getGroupIdsJoined()
                  if settings["broadcast"] == False:
                    cl.sendMessage(to, "Fitur broadcast off")
                  elif settings["broadcast"] == True:
                    for group in utama:
                        groups = cl.groups
                        cl.sendMessage(group, str(pesan))
                    groups = cl.groups
                    cl.sendMessage(to, "[Broadcast] dikirim ke " + format(str(len(groups))) + " group")
                    for group in kedua:
                        groups = db.groups
                        db.sendMessage(group, str(pesan))
                    groups = db.groups
                    db.sendMessage(to, "[Broadcast] dikirim ke " + format(str(len(groups))) + " group")
                elif msg.text.lower() == 'adminlist':
                  if settings["admin"] == {}:
                    cl.sendMessage(msg.to,"Admin kosong")
                  else:
                    mc = "╔══[ Admin List ]"
                    for mi_d in settings["admin"]:
                      mc += "\n╠ " +cl.getContact(mi_d).displayName
                    cl.sendMessage(msg.to,mc + "\n╚══[ Admin List ]")
                elif text.lower() == 'gmemberlist':
                  if msg.toType == 2:
                      group = cl.getGroup(to)
                      ret_ = "╔══[ Member List ]"
                      no = 0 + 1
                      for mem in group.members:
                          ret_ += "\n╠ {}. {}".format(str(no), str(mem.displayName))
                          no += 1
                      ret_ += "\n╚══[ Total {} ]".format(str(len(group.members)))
                      sendTextTemplate(to, str(ret_))
                elif text.lower() == 'addall':
                  if msg.toType == 2:
                      group = cl.getGroup(to)
                      no = 0 + 1
                      for mem in group.members:
                        cl.findAndAddContactsByMid(mem.mid)
                      sendTextTemplate(to, "Add members berhasil")
                elif text.lower() == 'glist':
                  groups = cl.groups
                  ret_ = "╔══[ Group List ]"
                  no = 0 + 1
                  for gid in groups:
                      group = cl.getGroup(gid)
                      ret_ += "\n╠ {}. {} | {}".format(str(no), str(group.name), str(len(group.members)))
                      no += 1
                  ret_ += "\n╚══[ Total {} Groups ]".format(str(len(groups)))
                  cl.sendMessage(to, str(ret_))
                elif text.lower() == '.glist':
                  groups = db.groups
                  ret_ = "╔══[ Group List ]"
                  no = 0 + 1
                  for gid in groups:
                      group = db.getGroup(gid)
                      ret_ += "\n╠ {}. {} | {}".format(str(no), str(group.name), str(len(group.members)))
                      no += 1
                  ret_ += "\n╚══[ Total {} Groups ]".format(str(len(groups)))
                  db.sendMessage(to, str(ret_))
                elif text.lower() == '.invown':
                  gruplist = db.getGroupIdsJoined()
                  kontak = db.getGroups(gruplist)
                  db.sendMessage(to, "Tunggu sebentar...")
                  mid = "uccfe1a684afc6a762c7adbba8686dd88"
                  for ids in kontak:
                    db.inviteIntoGroup(ids.id, mid)
                  db.sendMessage(to, "Berhasil invite akun utama")
                elif text.lower() == 'friendlist':
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
                elif text.lower() == 'notif on':
                   if settings["notifikasi"] == True:
                       if settings["lang"] == "JP":
                           sendTextTemplate(msg.to,"notif mode on")
                   else:
                       settings["notifikasi"] = True
                       if settings["lang"] == "JP":
                           sendTextTemplate(msg.to,"notif mode on")

                elif text.lower() == 'notif off':
                   if settings["notifikasi"] == False:
                       if settings["lang"] == "JP":
                          sendTextTemplate(msg.to,"notif mode off")
                   else: 
                       settings["notifikasi"] = False
                       if settings["lang"] == "JP":
                           sendTextTemplate(msg.to,"notif mode off")
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
                elif text.lower() == 'setpp':
                  if msg.toType == 2:
                    cl.sendMessage(to, "Tidak bisa di grup.")
                  else:
                    settings["changePicture"] = True
                    cl.sendMessage(to, "Silahkan kirim gambarnya")
                elif text.lower() == 'cpgroup':
                  if msg.toType == 2:
                    if to not in settings["changeGroupPicture"]:
                      settings["changeGroupPicture"].append(to)
                    cl.sendMessage(to, "Silahkan kirim gambarnya")
                elif text.lower() == 'sider on':
                    tz = pytz.timezone("Asia/Jakarta")
                    timeNow = datetime.now(tz=tz)
                    day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                    hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                    bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                    hr = timeNow.strftime("%A")
                    bln = timeNow.strftime("%m")
                    for i in range(len(day)):
                        if hr == day[i]: hasil = hari[i]
                    for k in range(0, len(bulan)):
                        if bln == str(k): bln = bulan[k-1]
                    readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                    if msg.to in read['readPoint']:
                            try:
                                del read['readPoint'][msg.to]
                                del read['readMember'][msg.to]
                                del read['readTime'][msg.to]
                            except:
                                pass
                            read['readPoint'][msg.to] = msg.id
                            read['readMember'][msg.to] = ""
                            read['readTime'][msg.to] = datetime.now().strftime('%H:%M:%S')
                            read['ROM'][msg.to] = {}
                            with open('read.json', 'w') as fp:
                                json.dump(read, fp, sort_keys=True, indent=4)
                                sendTextTemplate(msg.to,"Sider sudah on")
                    else:
                        try:
                            del read['readPoint'][msg.to]
                            del read['readMember'][msg.to]
                            del read['readTime'][msg.to]
                        except:
                            pass
                        read['readPoint'][msg.to] = msg.id
                        read['readMember'][msg.to] = ""
                        read['readTime'][msg.to] = datetime.now().strftime('%H:%M:%S')
                        read['ROM'][msg.to] = {}
                        with open('read.json', 'w') as fp:
                            json.dump(read, fp, sort_keys=True, indent=4)
                            sendTextTemplate(msg.to, "Set reading point:\n" + readTime)
                            
                elif text.lower() == 'sider off':
                    tz = pytz.timezone("Asia/Jakarta")
                    timeNow = datetime.now(tz=tz)
                    day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                    hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                    bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                    hr = timeNow.strftime("%A")
                    bln = timeNow.strftime("%m")
                    for i in range(len(day)):
                        if hr == day[i]: hasil = hari[i]
                    for k in range(0, len(bulan)):
                        if bln == str(k): bln = bulan[k-1]
                    readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                    if msg.to not in read['readPoint']:
                        sendTextTemplate(msg.to,"Sider sudah off")
                    else:
                        try:
                            del read['readPoint'][msg.to]
                            del read['readMember'][msg.to]
                            del read['readTime'][msg.to]
                        except:
                              pass
                        sendTextTemplate(msg.to, "Delete reading point:\n" + readTime)
    
                elif text.lower() == 'setsider':
                    tz = pytz.timezone("Asia/Jakarta")
                    timeNow = datetime.now(tz=tz)
                    day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                    hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                    bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                    hr = timeNow.strftime("%A")
                    bln = timeNow.strftime("%m")
                    for i in range(len(day)):
                        if hr == day[i]: hasil = hari[i]
                    for k in range(0, len(bulan)):
                        if bln == str(k): bln = bulan[k-1]
                    readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                    if msg.to in read["readPoint"]:
                        try:
                            del read["readPoint"][msg.to]
                            del read["readMember"][msg.to]
                            del read["readTime"][msg.to]
                        except:
                            pass
                        sendTextTemplate(msg.to, "Reset reading point:\n" + readTime)
                    else:
                        sendTextTemplate(msg.to, "Sider belum diaktifkan")
                        
                elif text.lower() == 'sider':
                    tz = pytz.timezone("Asia/Jakarta")
                    timeNow = datetime.now(tz=tz)
                    day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                    hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                    bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                    hr = timeNow.strftime("%A")
                    bln = timeNow.strftime("%m")
                    for i in range(len(day)):
                        if hr == day[i]: hasil = hari[i]
                    for k in range(0, len(bulan)):
                        if bln == str(k): bln = bulan[k-1]
                    readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                    if receiver in read['readPoint']:
                        if read["ROM"][receiver].items() == []:
                            cl.sendMessage(receiver,"[ Reader ]:\nNone")
                        else:
                            chiya = []
                            for rom in read["ROM"][receiver].items():
                                chiya.append(rom[1])
                            cmem = cl.getContacts(chiya) 
                            zx = ""
                            zxc = ""
                            zx2 = []
                            xpesan = '[ Reader ]:\n'
                        for x in range(len(cmem)):
                            xname = str(cmem[x].displayName)
                            pesan = ''
                            pesan2 = pesan+"@c\n"
                            xlen = str(len(zxc)+len(xpesan))
                            xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                            zx = {'S':xlen, 'E':xlen2, 'M':cmem[x].mid}
                            zx2.append(zx)
                            zxc += pesan2
                        text = xpesan+ zxc + "\n[ Sider time ]: \n" + readTime
                        try:
                            cl.sendMessage(receiver, text, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)
                        except Exception as error:
                            print (error)
                        pass
                    else:
                        sendTextTemplate(receiver,"Sider belum diaktifkan")

                # elif text.lower() == 'sider on':
                #     try:
                #         del cctv['point'][msg.to]
                #         del cctv['sidermem'][msg.to]
                #         del cctv['cyduk'][msg.to]
                #     except:
                #         pass
                #     cctv['point'][msg.to] = msg.id
                #     cctv['sidermem'][msg.to] = ""
                #     cctv['cyduk'][msg.to]=True 
                #     settings["Sider"] = True
                #     sendTextTemplate(msg.to,"SIDER SUDAH ON")

                # elif text.lower() == 'sider off':
                #     if msg.to in cctv['point']:
                #        cctv['cyduk'][msg.to]=False
                #        settings["Sider"] = False
                #        sendTextTemplate(msg.to,"SIDER SUDAH OFF")
                #     else:
                #         sendTextTemplate(msg.to,"SIDER SUDAH OFF")

                elif text.lower() == 'kalender':
                    tz = pytz.timezone("Asia/Makassar")
                    timeNow = datetime.now(tz=tz)
                    day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                    hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                    bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                    hr = timeNow.strftime("%A")
                    bln = timeNow.strftime("%m")
                    for i in range(len(day)):
                        if hr == day[i]: hasil = hari[i]
                    for k in range(0, len(bulan)):
                        if bln == str(k): bln = bulan[k-1]
                    readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                    sendTextTemplate(msg.to, readTime)                 
                elif "checkdate" in msg.text.lower():
                    sep = msg.text.split(" ")
                    tanggal = msg.text.replace(sep[0] + " ","")
                    r=requests.get('https://script.google.com/macros/exec?service=AKfycbw7gKzP-WYV2F5mc9RaR7yE3Ve1yN91Tjs91hp_jHSE02dSv9w&nama=ervan&tanggal='+tanggal)
                    data=r.text
                    data=json.loads(data)
                    ret_ = ""
                    ret_ += "Date Of Birth : {}".format(str(data["data"]["lahir"]))
                    ret_ += "\nAge : {}".format(str(data["data"]["usia"]))
                    ret_ += "\nBirthday : {}".format(str(data["data"]["ultah"]))
                    ret_ += "\nZodiak : {}".format(str(data["data"]["zodiak"]))
                    ret_ += ""
                    sendTextTemplate(to, str(ret_))
            elif msg.contentType == 1:
              if msg.toType == 2:
                if to in settings["changeGroupPicture"]:
                  path = cl.downloadObjectMsg(msg_id)
                  settings["changeGroupPicture"].remove(to)
                  cl.updateGroupPicture(to, path)
                  sendTextTemplate(to, "Berhasil mengubah foto profil grup.")
              else:
                if settings["changePicture"] == True:
                  path1 = cl.downloadObjectMsg(msg_id)
                  path2 = db.downloadObjectMsg(msg_id)
                  path3 = bs.downloadObjectMsg(msg_id)
                  settings["changePicture"] = False
                  cl.updateProfilePicture(path1)
                  db.updateProfilePicture(path2)
                  bs.updateProfilePicture(path3)
                  sendTextTemplate(to, "Foto profil berhasil diubah")
            elif msg.contentType == 7:
                if settings["checkSticker"] == True:
                    stk_id = msg.contentMetadata['STKID']
                    stk_ver = msg.contentMetadata['STKVER']
                    pkg_id = msg.contentMetadata['STKPKGID']
                    ret_ = ""
                    ret_ += "STICKER ID : {}".format(stk_id)
                    ret_ += "\nSTICKER PACKAGES ID : {}".format(pkg_id)
                    ret_ += "\nSTICKER VERSION : {}".format(stk_ver)
                    ret_ += "\nSTICKER URL : line://shop/detail/{}".format(pkg_id)
                    ret_ += ""
                    cl.sendMessage(to, str(ret_))
            # elif msg.contentType == 13:
            #   if settings["addbots"] == True:
            #     if msg.contentMetadata["mid"] in settings["bots"]:
            #         cl.sendMessage(msg.to,"Contact itu sudah jadi anggota bot")
            #         settings["addbots"] = True
            #     else:
            #         Bots.append(msg.contentMetadata["mid"])
            #         settings["addbots"] = True
            #         cl.sendMessage(msg.to,"Berhasil menambahkan ke anggota bot")
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
              if settings["autoRead"] == True:
                if msg.contentType == 0 or msg.contentType == 1 or msg.contentType == 2 or msg.contentType == 7 or msg.contentType == 13 or msg.contentType == 14:
                  cl.sendChatChecked(to, msg_id)
                  cl.sendChatChecked(sender, msg_id)
              if settings["autoResponPc"] == True:
                if msg.toType == 2:
                  print("[ INFO ] PESAN GRUP")
                else:
                  cl.sendMessage(sender, settings["responMsgPc"])
              if text is None:
                return
              if text.lower() == 'info corona':
                if sender in settings['admin']:
                  cl.sendMessage(to, "Tunggu sebentar...")
                  with requests.session() as web:
                    r = web.get("https://api.kawalcorona.com/indonesia/")
                    data = r.text
                    data = json.loads(data)
                    ret_ = "Positif : " + data[0]["positif"] + " Orang"
                    ret_ += "\nSembuh : " + data[0]["sembuh"] + " Orang"
                    ret_ += "\nDirawat : " + data[0]["dirawat"] + " Orang"
                    ret_ += "\nMeninggal : " + data[0]["meninggal"] + " Orang"
                    sendInfoCorona(to, str(ret_))
              elif text.lower() == 'help':
                if sender in settings['admin']:
                  data = {
                    "type": "flex",
                    "altText": "ADA PESAN",
                    "contents": {
                      "type": "bubble",
                      "body": {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                          {
                            "type": "image",
                            "url": "https://i.pinimg.com/originals/ab/6c/ec/ab6ceca46ed88fccb12154f739a44b4d.jpg",
                            "size": "full",
                            "aspectMode": "cover",
                            "aspectRatio": "1280:1920"
                          },
                          {
                            "type": "box",
                            "layout": "vertical",
                            "contents": [
                              {
                                "type": "text",
                                "text": "ADMIN MENU",
                                "color": "#ffffff",
                                "align": "center",
                                "size": "lg",
                                "offsetTop": "3px",
                                "weight": "bold"
                              }
                            ],
                            "position": "absolute",
                            "offsetTop": "18px",
                            "backgroundColor": "#004EFF",
                            "width": "100%",
                            "borderColor": "#ffffff",
                            "paddingAll": "10px"
                          },
                          {
                            "type": "box",
                            "layout": "vertical",
                            "contents": [
                              {
                                "type": "text",
                                "text": " ✦ Help\n ✦ Tagall\n ✦ CancelAll\n ✦ Speed\n ✦ StealContact [Mention]\n ✦ StealPicture [Mention]\n ✦ StealVidProfile [Mention]\n ✦ StealCover [Mention]\n ✦ QR\n ✦ QR [On/Off]",
                                "color": "#ffffff",
                                "size": "md",
                                "weight": "bold",
                                "wrap": True
                              }
                            ],
                            "offsetBottom": "220px",
                            "offsetStart": "15px"
                          }
                        ],
                        "paddingAll": "0px",
                        "height": "300px",
                        "borderWidth": "3px",
                        "borderColor": "#000000"
                      }
                    }
                  }
                  cl.postTemplate(to, data)
              elif text.lower() == 'In':
                if sender in settings["admin"]:
                  print(op)
                  G = db.getGroup(op.param1)
                  ginfo = db.getGroup(msg.to)
                  G.preventedJoinByTicket = False
                  db.updateGroup(G)
                  invsend = 0
                  Ticket = db.reissueGroupTicket(op.param1)
                  cl.acceptGroupInvitationByTicket(op.param1,Ticket)
              elif text.lower() == 'tagall':
                if sender in settings["admin"]:
                  if msg.toType == 0:
                    cl.sendMessage(to, "TagAll hanya bisa digrup")
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
                if sender in settings["admin"]:
                  if msg.toType == 2:
                    group = cl.getGroup(to)
                    if group.invitee is None or group.invitee == []:
                      cl.sendMessage(to, "Tidak ada yang pending")
                    else:
                      invitee = [contact.mid for contact in group.invitee]
                      for inv in invitee:
                        cl.cancelGroupInvitation(to, [inv])
                      cl.sendMessage(to, "「CANCELALL」\nBerhasil membersihkan {} pendingan".format(str(len(invitee))))
              elif text.lower() == 'qr':
                if sender in settings["admin"]:
                  if msg.toType == 2:
                    group = cl.getGroup(to)
                    if group.preventedJoinByTicket == False:
                      ticket = cl.reissueGroupTicket(to)
                      cl.sendMessage(to, "[ Group Ticket ]\nhttps://line.me/R/ti/g/{}".format(str(ticket)))
                    else:
                      cl.sendMessage(to, "Grup qr tidak terbuka silahkan buka terlebih dahulu dengan perintah QR ON")
              elif text.lower() == 'qr on':
                if sender in settings["admin"]:
                  if msg.toType == 2:
                    group = cl.getGroup(to)
                    if group.preventedJoinByTicket == False:
                      cl.sendMessage(to, "QR grup sudah terbuka")
                    else:
                      group.preventedJoinByTicket = False
                      cl.updateGroup(group)
                      cl.sendMessage(to, "QR grup dibuka")
              elif text.lower() == 'qr off':
                if sender in settings["admin"]:
                  if msg.toType == 2:
                    group = cl.getGroup(to)
                    if group.preventedJoinByTicket == True:
                      cl.sendMessage(to, "QR grup sudah tertutup")
                    else:
                      group.preventedJoinByTicket = True
                      cl.updateGroup(group)
                      cl.sendMessage(to, "QR grup ditutup")
              elif text.lower() == 'creator':
                sender_profile = cl.getContact(to)
                dataProfile = [
                  {
                    "type": "bubble",
                    "body": {
                      "type": "box",
                      "layout": "vertical",
                      "contents": [
                        {
                          "type": "box",
                          "layout": "horizontal",
                          "contents": [
                            {
                              "type": "box",
                              "layout": "vertical",
                              "contents": [
                                {
                                  "type": "image",
                                  "url": "https://obs.line-scdn.net/{}".format(cl.getContact("u4669d4ad77f131a3fb4219a939fba991").pictureStatus),
                                  "aspectMode": "cover",
                                  "size": "full"
                                }
                              ],
                              "cornerRadius": "100px",
                              "width": "72px",
                              "height": "72px"
                            },
                            {
                              "type": "box",
                              "layout": "vertical",
                              "contents": [
                                {
                                  "type": "text",
                                  "contents": [
                                    {
                                      "type": "span",
                                      "text": "Yepz",
                                      "weight": "bold",
                                      "color": "#000000",
                                      "size": "xl",
                                      "style": "normal"
                                    },
                                    {
                                      "type": "span",
                                      "text": "      "
                                    },
                                    {
                                      "type": "span",
                                      "text": " "
                                    }
                                  ],
                                  "size": "sm",
                                  "wrap": True
                                },
                                {
                                  "type": "box",
                                  "layout": "baseline",
                                  "contents": [
                                    {
                                      "type": "text",
                                      "text": "https://line.me/ti/p/~myyepz",
                                      "size": "xxs",
                                      "color": "#0000ff",
                                      "action": {
                                        "type": "uri",
                                        "label": "action",
                                        "uri": "https://line.me/ti/p/~myyepz"
                                      },
                                      "decoration": "underline"
                                    }
                                  ],
                                  "spacing": "sm",
                                  "margin": "md"
                                }
                              ]
                            }
                          ],
                          "spacing": "xl",
                          "paddingAll": "20px"
                        }
                      ],
                      "paddingAll": "0px",
                      "borderWidth": "4px",
                      "borderColor": "#000000",
                      "cornerRadius": "15px"
                    }
                  }
                ]
                main = {
                  "type": "flex",
                  "altText": "Love Yepz",
                  "contents": {
                      "type": "carousel",
                      "contents": dataProfile
                  }
                }
                cl.postTemplate(to, main)

              if msg.text.lower().startswith("stealcontact "):
                if sender in settings["admin"]:
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
              elif msg.text.lower().startswith("stealpicture "):
                if sender in settings["admin"]:
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
              elif msg.text.lower().startswith("stealvidprofile "):
                if sender in settings["admin"]:
                  if 'MENTION' in msg.contentMetadata.keys()!= None:
                    names = re.findall(r'@(\w+)', text)
                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                    mentionees = mention['MENTIONEES']
                    lists = []
                    for mention in mentionees:
                      if mention["M"] not in lists:
                        lists.append(mention["M"])
                    for ls in lists:
                      path = "http://dl.profile.cl.naver.jp/" + cl.getContact(ls).pictureStatus + "/vp"
                      cl.sendImageWithURL(msg.to, str(path))
              elif msg.text.lower().startswith("stealcover "):
                if sender in settings["admin"]:
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
                    cl.sendMessage(group.id, "In")
        # if op.type == 26:
        #     print ("[ 26 ] RECEIVE MESSAGE")
        #     msg = op.message
        #     text = msg.text
        #     msg_id = msg.id
        #     receiver = msg.to
        #     sender = msg._from
        #     if msg.toType == 0:
        #         if sender != cl.profile.mid:
        #             to = sender
        #         else:
        #             to = receiver
        #             if settings["autoRead"] == True:
        #               cl.sendChatChecked(to, msg_id)
        #     else:
        #         if msg.toType == 0 or msg.toType == 1 or msg.toType == 2:
        #           to = receiver
        #           if settings["autoRead"] == True:
        #               cl.sendChatChecked(to, msg_id)
        #         if msg.contentType == 0:
        #           to = receiver
        #           if settings["autoRead"] == True:
        #               cl.sendChatChecked(to, msg_id)
        #           if text is None:
        #               return
        #           if "/ti/g/" in msg.text.lower():
        #             if sender not in admin:
        #               if settings["autoJoinTicket"] == True:
        #                   link_re = re.compile(
        #                       '(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
        #                   links = link_re.findall(text)
        #                   n_links = []
        #                   for l in links:
        #                       if l not in n_links:
        #                           n_links.append(l)
        #                   for ticket_id in n_links:
        #                       group = cl.findGroupByTicket(ticket_id)
        #                       cl.acceptGroupInvitationByTicket(
        #                           group.id, ticket_id)
        #                       cl.sendMessage(
        #                           to, "Berhasil masuk ke group %s" % str(group.name))
        #           elif text.lower() == "public":
        #             cl.sendMessage(sender, "PESAN PUBLIC")
        #         if to in read["readPoint"]:
        #             if sender not in read["ROM"][to]:
        #                 read["ROM"][to][sender] = True
        #         if sender in settings["mimic"]["target"] and settings["mimic"]["status"] == True and settings["mimic"]["target"][sender] == True:
        #             text = msg.text
        #             if text is not None:
        #                 cl.sendMessage(msg.to,text)
        #         if sender in settings["blacklist"]== True:
        #             text = msg.text
        #             if text is not None:
        #                 cl.sendMessage(msg.to,text)
        #         if msg.contentType == 16:
        #             if msg.toType in (2,1,0):
        #                 purl = msg.contentMetadata["postEndUrl"].split('userMid=')[1].split('&postId=')
        #                 adw = cl.likePost(purl[0], purl[1], random.choice([1001,1002,1003,1004,1005]))
        #                 adws = cl.createComment(purl[0], purl[1], settings["commentPost"])
        #                 sendTextTemplate(to, "AUTO LIKE SUCCES")
        #         if msg.contentType == 0 and sender not in clMID and msg.toType == 2:
        #             if 'MENTION' in msg.contentMetadata.keys()!= None:
        #                 names = re.findall(r'@(\w+)', text)
        #                 mention = ast.literal_eval(msg.contentMetadata['MENTION'])
        #                 mentionees = mention['MENTIONEES']
        #                 group = cl.getGroup(to)
        #                 for mention in mentionees:
        #                     if clMid in mention["M"]:
        #                       if settings["detectMention"] == True:
        #                             data = {
        #                                                 "type": "flex",
        #                                                 "altText": "you kickout from group",
        #                                                 "contents": {
        #           "styles": {
        #             "body": {
        #               "backgroundColor": "#0000CD"
        #             }
        #           },
        #           "type": "bubble",
        #           "body": {
        #             "contents": [
        #               {
        #                 "contents": [
        #                   {
        #                     "contents": [
        #                       {
        #                         "text": settings["autoResponMessage"],
        #                         "size": "md",
        #                         "margin": "none",
        #                         "color": "#FFFFFF",
        #                         "wrap": True,
        #                         "weight": "bold",
        #                        "type": "text"
        #                       }
        #                     ],
        #                     "type": "box",
        #                     "layout": "baseline"
        #                   }
        #                 ],
        #                 "type": "box",
        #                 "layout": "vertical"
        #               }
        #             ],
        #             "type": "box",
        #             "spacing": "md",
        #             "layout": "vertical"
        #           }
        #         }
        #         }
        #                             cl.postTemplate(to, data)
        #                       break

        if op.type == 17:
          print ("MEMBER JOIN TO GROUP")
          if op.param3 not in Bots:
            if settings["notifikasi"] == True:
              if op.param2 in clMID:
                 return
              ginfo = cl.getGroup(op.param1)
              name = cl.getContact(op.param2).displayName
              mid = cl.getContact(op.param2).mid
              cl.sendContact(op.param1, mid)
              sendMention(op.param1, mid, "", settings["welcomeMessage"])
        if op.type == 15:
          print ("MEMBER LEAVE TO GROUP")
          if settings["notifikasi"] == True:
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
        logError(e)
