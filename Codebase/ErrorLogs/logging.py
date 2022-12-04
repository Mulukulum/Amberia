#Functions to log errors with other functions
from datetime import datetime
from os.path import dirname
LogPath=dirname(dirname(dirname(__file__)))+("\\LogFiles\\")         #Gets the path of the logs Folder
from inspect import stack
FileConstant=6


def ErrorLog(text=None,FileName=stack()[FileConstant].filename):
    if text==None or type(text) != str :
        return None
    else:
        _WriteToMaster(text,FileName,type='ERROR')
        _WriteToErrors(text,FileName)

def Log(text=None,FileName=stack()[FileConstant].filename):
    if text==None or type(text) != str :
        return None
    else:
        _WriteToMaster(text,FileName,type='LOG')
        _WriteToLogs(text,FileName)

def StartLog(text=None,FileName=stack()[FileConstant].filename):
    if text==None or type(text) != str :
        return None
    else:
        _WriteToMaster(text,FileName,type='STARTUP')
        _WriteToStartLogs(text,FileName)

def DBLog(text=None,FileName=stack()[FileConstant].filename):
    if text==None or type(text) != str :
        return None
    else:
        _WriteToMaster(text,FileName,type='DATABASE')
        _WriteToDBLogs(text,FileName)

def DBOnlyLog(text=None,FileName=stack()[FileConstant].filename):
    if text==None or type(text) != str :
        return None
    else:
        _WriteToDBLogs(text,FileName)

#This function is for testing purposes only
def _Test(text=None,FileName=stack()):
    if text==None or type(text) != str :
        return None
    for i in range(len(FileName)):
        print(i,FileName[i].filename)
    else:
        _WriteToMaster(text,FileName,type='LOG')
        _WriteToLogs(text,FileName)


'''
B7^:::~7Y55J?5GGGPB#B#####B#BBBB&&#&@&&&&@@@@@@&#GB#&@@&&&&#&&&&&@@@@@@@@@@&&&&&@@@@@@@&&@@@&@@@@&@@
B?5!~^~?PP5JJPBGGB####&&##BBGG#GB&####&&@&@@@@@@&B#&##&&@@@&&&&&&&&@@@@@@@&@@&&&&&&@@@@&@@@@@@@&@@@@
#5PY77~^!?PBGB##&&BB#BBGG#GB#GB#B#BBB##&&&&&&#&&@&&&&&&&&@@&&&##&#&&@&&&&@@@@&@@@&&&@@@@@@@@@@@@@&G!
BJ7^!~J5BB######G##&###BB#G##BG#B###BG#GPGBGG#&BGGPPB&&&&@@@@&&##&@&&&&&&&@@@@@@@@@@@@@@@@@@@@@@@G5~
#GY?JYG#BGG5?~^7???YPPG7~YB#GBB#&&&#BPGP555YP#B5PYY55B#B#&@&&&&&&&@@@&&@@@@@@@&@&@@@@@@@@@@@##GJB!?#
&BPG##BB&B?J?7~.::.:7?P?:^J#?5#P?BB&#GPYJ?Y5PGP555YY5GGPPBB#&@@@&&&&&&&&@&&&&&&@&@@@@@&&BYP5~~^~5YJ5
&###&#&B5!!7?Y7!!:.:^::^~:~G7Y##JPJYY?Y?????JJJYJYYJYYYYPPG#&&&#&@@&&@@&@@&&&&@@@@@&B55P#5J!!P#####B
B?Y5PJY7..^~:~~^~^:~..:.~^^?7J5B5J!^!^7~!7~7!~?77!7?!77J55PG&B5GGBBB&&@@@@@&&&#&@&#GPPY5B#BJ^J!!BJY!
G7!!!!~^^~^::~!7!!^?^:::^7^~!J?JJ77J?!~~~~~!~~!~~^?!~!JYYYPBB55PPPB#&&&&@@@@@&&BP?~~?PP5Y7G5!^^~GY:^
B?7!YJ7!!JJ~..:~::~!!~.:^?^:75J!??J?5PY?7!7~~^~^~~7~~JYJ55G#GB##&&##BB#&@@@@@@@&!^^^^^^~?JPGBJ^!7J5G
#Y5YJYJ7YG:.:!^:....~JYYJ7:^G5PJ5&&#B###BPGPJ!^~7~7!7YY5PB#&&&&@@@&&&#&@&&&@@@@#~^^^^~^JB#BPB#B#&&&@
#PGG5Y5?J!:.:755?7~7JP55Y!:^PBG&&&&&&&@@@&&&&B?!!~77?Y5GB&@@@@@@@@@@@@@@&#&&@@&&BJ7?!GPB&&B#&&&&&&#&
&GGGP55Y?!7777PP5GPGGY57~:^!5&&&GG##&&B&@@@@&&#7!?77JG#@@@@@@@&&@@@@@@@@&&&&@@@&B#&&B#GBBBB#BG&@#B&&
BJY5GGB##GPYY55B&&BB#GY!::~JB&@#B&P7P#Y7B&&@@@&5??7JG&@@@@&5P#Y?#@@@@@@@@&&&#B#&&&##BGB#BBB#BB&@@@@&
G:.:~^!?Y??J5GYG&#BG##!:~~5#GB##BBGG5GBB#&@&&&#Y?!!?B@@@@@&#BGGB&&@@@@&&BBGBGBPG&###BB#BGBB&#&@@@@@&
G!~!?7YPJ~?~^!~^?5##BBJ:75GGPG5PB#BB&&&&&@&&&&P?!~~!G&@@@&&&&&&@&&&&&#GB55PGBGGGG#####&###B#&@@@&@@@
Y.:.:^~!^!!!?~~^^.^P#G~^!J5JP5YYYPB##B#####BBP77~^^!PBB#&@&&&##&&&&##BPPBBB#&B###&&&BB#B&&&&@@@@&@@@
Y.:^~!7~7!~^!7YJYJ^:JY^^7JJ?55PP5JGYYP5JYJJJ??!~~^!!5#BB&&&&#GGGGGB#&BB##&&&&&&@&&&BGB#B&##@@@@@@@@@
P^!!~~!~?!7?!?57~~!?7!~~7YGG5G??YYPJ5J77!7J55YJ7~!!?Y##&&&&#GPYPPPPG##B####&@&&&##&BB##B&@@@@@@@PPB&
G!7777!7??JJ?YP!JJ?!7^:7YYJ!!!~JY5JJJ!?7J5B&#G57!77J5B#&&&&##GPPPP5PB&&#&@&@@@&B###&&&&&@@@@@@@@&#&&
P~~!Y5J?7J????77YYJ~!^~?JJJ!^^~YYY5JY5G#&&##GP5?77Y5PB##&&&&&&#GBGGB#&&#B#&BB&#&#&&@&#@@@@@@@@@@@&&@
5^~!?PJ7JY??YPYYYJ??J~~7JJ?YJJ?YY5G#&&@@&5!J55Y!~?GYYB#B#&B&#&@&B###&BBB#&&B&###&&#&&##&&@@@@@@@@@@@
G!7Y!~!!75JYP5PG5YYYY!~J7?77??YPG#&@@@&&5??PJJ~^^JPJ?YBBBBB#B&@@@&&#&&&&&&@&##&##@@&&&#GB&@@@@@@@@@@
G!!~~7J?!7?YPPBPPGGYY~!Y!!7?Y5BB&@@&&#B&&B5GGJ7!~~??JPGBBB#&@@@@@@&&##&&&@&#&#@&&&@@&&##&@@@@@@@@&&@
P7J??Y5JY??Y55J55PPPG~??!7J5PB#@@@#B#GB&@@@@@&&BGGBBB##&&@@@@@@@@@@&#GG&@&&#&&@@@@&&&##&@@@@@@&&@#&@
#JGP5PP?YP5Y5PJ!77YP??Y!!J5GB&&@&#GPGGP#&&&@@@@@@@@@&&@@@@@@@@@&@&@@&&#&&&&&@@@&@@@@@@@@@@@@@@&#&#&@
#YG5YY577YJ??Y7??~7J?5!^7YP#&@@@&BP55JJGBB##&&&@@@@@@@@@@@@@@&@&&@&&@@&&&###&@@&@@@@@@@@@@@@@&#&#B&@
&GY55JY7!7J!?77^!?77Y?!77YG#&@@&#B55??Y5YPBPGG#&#&&&&&&&@@@@&&@&&&@&&@@&&&&&#&&@@@@@@@@@@@@@@&#&&#&&
#PJYYJPPGY777Y7~?G5J5?!?P5P&&&@&BBGBPP55JJP?YJPY5YB#5B#B#&&&&&&&@&@@@@@@@&&&&#~~7J5PGB#&&&&@@@&&&&&#
&GG5GGGGP#PJ7?PGG5YJYY5PB?YPPGB#&#&&&##BG55JJ?77?7YY75BB###&&@@@@@@@@@@@@@&&&&^^^^:::^^^^~~!JG&&@&&&
&B#GB#B##BP5P5BBPJJYPGG#Y5PY?BBBB&&&&@@@@@@@@&&&&&&&&&@&@@@@@@@@@@@@@@@@@@&&&&Y????~^^^^^^^^^^~?G#&&
&&#PG#BGP5P5GP5PGGGGYYGBYGGPY5GP5G&BBBP##GGB##&&##&&#&&&&&&&&&&@@@@@@@@@@@&&&@P5GGG5J~^^^^^^~~~^^~!~
&PPYGB##GGBB###B#&&#BB55PJP##5PPGGPB#B5##5YJYJJ??JJJ?YYBBB#&&&&&&&&&&&&&&&@@&&#&&###G7^~~^~~~~~~~~~~
&JJYYGGB&#####&&#&##G5BPP#P#GPPG#B#&&&##&BBBGGP5YGGGGBB&&&@@@@@&@&@&&&&&&&@&#&&#&&#P?!?!~^~~~~~~~~~~
&P#GB&##&##&BB&&&&#&G##5YBPP##&@&@@@@@@@@@@&@@@@@@@@@@@@@@@@@@@@@@@&@@@@&@&&&&&&##BBGPP5Y?!~~~~~~~~~
@&&&###&#&#&&&@&&&&&&&&BGBGB@&&&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&@@@@@@@@&#&##&B##BBPY!~~~~~~~~~
@&###&&&&&@&&&&&&##B&&####&&@&##&&@@@@@@@@@@@&@@@@@@@@@@@@@@@@@@@@&@&@@@&&@@@&&&##BG5JJPY~~!!!!!!!!~
@BBB&B#BB##&&&B#&&#B##GPG#@@@&&&&&&@@@@@@@@&&#&&@@@@&&&@&&@&&@@@&&&@@@@@&@@@@@@@#57!~!!~~~!!!!!!!!!!
&GG#&#G#&BG###G&##&##BBGBB#&&&&&&&&@@@@@@@&##&#&&&&#G#########&&@@@@@@@@@@@@@@@&BJ!!!!!!!!!!!!!!!!!!
@&#####&&#&&B##&&&&&GB#BG##&&B##&&&@&@@@@@&####@@@#&B&&B#B#&&&&&&@&@@@@@@@@@@@@&&?!7777!!!!!!!!!!!!!
&#BB#&&#&&&&&##B#&@&PG&@&&&######&&@&@@@@@&&&&@&&&###&&&&&@@&@&&&@&@@@@@@@@@@@&#&P~77777777777777777
@&&##&@&&&&&#&&#&&&#&&@@&&&######&&&@@@@@@@@@@@&##&#&&&&&&&&@@@&&@@@&&@@@@@@@@@&&&Y?????????????????
#B##&&&@@&#@&&BB&&&&@@&&BB#BBB##&#&&&@&&@@@@@@@@@@@@@&&@&##&&&&@@@@@@@@@@@@@@@@@&&&JJJJJJJJJJJJ5YJJP
BYPB###&&#B&&@&#&@&&###GGBB#BB#&&&&&#&&&@@@@@@@@@@@@@@@@&@&&&&&&&@@@@@@@@@@@@@@@&&&BJYYYYYYYYY55PPPP
BJJYY5#B&&GG&@@&&&##BBBPB###B##&&@&#&&&@@@@@@@@@@@@@@@@@@&@@@@@@@@@@@@@@@@@@@@@@@&&&B555555YY55PBBBB
#YYYY5##&&B#&@@&&BBBB##BB#####&#&&&##&&@@@@@@@@@@@@@@@@@@&@@@@@@@@@@&@@@@@@@@@@@@@@&&#PPP555Y5BB#&&&
#55555G#5PBBPBGGGB##&&&###&###&#&&#&&&&&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#BBBGB#B#&&&@&
'''

#Don't worry about any of these functions they're all perfectly tested
def _WriteToMaster(text,file,type):
    with open(LogPath+'Master.log','a') as Master: #Opens the file in an appropriate filepath in append mode
        Master.write(f"{type} : at {datetime.now().strftime('%H:%M:%S %d-%m-%Y')} from {file} \n") 
        #This code is just formatting stuff don't even worry about it
        Master.write(text+'\n')

def _WriteToErrors(text,file):
    with open(LogPath+'Errors.log','a') as Errors:
        Errors.write(f"ERROR : at {datetime.now().strftime('%H:%M:%S %d-%m-%Y')} from {file} \n")
        Errors.write(text+'\n')

def _WriteToLogs(text,file):
    with open(LogPath+'Logs.log','a') as Logs:
        Logs.write(f"LOG : at {datetime.now().strftime('%H:%M:%S %d-%m-%Y')} from {file} \n")
        Logs.write(text+'\n')

def _WriteToStartLogs(text,file):
    with open(LogPath+'Start.log','a') as Startup:
        Startup.write(f"STARTUP : at {datetime.now().strftime('%H:%M:%S %d-%m-%Y')} from {file} \n")
        Startup.write(text+'\n')
    
def _WriteToDBLogs(text,file):
    with open(LogPath+'DB.log','a') as Startup:
        Startup.write(f"DATABASE : at {datetime.now().strftime('%H:%M:%S %d-%m-%Y')} from {file} \n")
        Startup.write(text+'\n')