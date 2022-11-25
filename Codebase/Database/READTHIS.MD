**This doc contains a list of all tables and their attributes**

**Adding or modifying table structure:**

If an attribute should exist, then **explicitly** declare a *NOT NULL*

Give all Attributes and TableNames in lowercase and always declare types

Only add attributes if you absolutely need to, more instrucutions are at the end of this 

If you need to store something that would require multiple attributes,
then use the #func-requests channel on discord because,

It might be a better idea to write [an adapter](https://docs.python.org/3/library/sqlite3.html#default-adapters-and-converters)
Check if what you're trying to store has an adapter already
According to the python docs:
*The default converters are registered under the name “date” for datetime.date and under the name “timestamp” for datetime.datetime*
I've attached sample code [here](./Data/CODESAMPLE.py)
      **IMPORTANT: Avoid using [sqlite3.PARSE_DECLTYPES](https://docs.python.org/3/library/sqlite3.html#sqlite3.PARSE_DECLTYPES)**
      **Declare it explicitly with [sqlite3.PARSE_COLNAMES](https://docs.python.org/3/library/sqlite3.html#sqlite3.PARSE_COLNAMES)**

Otherwise it might even be a better idea to just make a new table altogether.
If you do, remember to update [Initialize.py](./Initialize.py)

**ADDING ATTRIBUTES AND TABLES:**

Add the *tablename* to the tuple called checklist
and add the *tablename*:*attributelist* entry to the 'AttribDict' Variable

For just adding attributes, modify the dictionary value for the corresponding table

**TABLE INDEX:**

The following is a list of all tables and their attributes that should be present in the Database

projects
Attributes :-
project_id INTEGER PRIMARY KEY
project_title TEXT NOT NULL
project_color INTEGER NOT NULL
project_sectioncount INTEGER NOT NULL

labels 
Attributes:-
label_id INTEGER PRIMARY KEY
label_title TEXT UNIQUE
label_color INTEGER NOT NULL
label_taskcount INTEGER NOT NULL                          

tasks
Attributes:-
task_id INTEGER PRIMARY KEY
task_title TEXT NOT NULL
task_description TEXT
task_projectid INTEGER NOT NULL
task_sectionid INTEGER NOT NULL
task_priority INTEGER NOT NULL
task_completed INTEGER NOT NULL
task_duedate DATE
task_completed_date DATE

texttasks
Attributes:-
texttask_id INTEGER PRIMARY KEY
texttask_text TEXT NOT NULL
texttask_sectionid INTEGER NOT NULL
texttask_projectid INTEGER NOT NULL

sections
Attributes:-
section_id INTEGER PRIMARY KEY
section_parentprojectid INTEGER NOT NULL
section_title TEXT NOT NULL
section_taskcount INTEGER NOT NULL
section_activetaskcount INTEGER NOT NULL 
section_texttaskcount INTEGER NOT NULL

prcolors
Attributes:-
level INTEGER PRIMARY KEY
clrvalue INTEGER NOT NULL

labelsfortasks
Attributes:-
task INTEGER NOT NULL
label INTEGER NOT NULL

REMEMBER TO ALSO CHANGE THE CORRESPONDING VALUES IN [INITIALIZE.PY](./Initialize.py) BOTH IN THE DICTIONARY AND IN THE TUPLE




































&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&#BBBGGGGGPPP555555555555YYYYJJJJJ?????????????JJJJJJ??????????JJJJJJ????777777777777777777777
&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&#BBBGGGGGPP555555YYYYYYYYYYJJJJJJ?????77??????JJJJJJ??????????JJJJJJ???7777777777777777777777
&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&##BBBBGGGPP5555YYYYYYYYYYYJJJJJJ?????77777????JJJJJJJ?????????JJJJJJJ??77777777777777777777777
&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&###BBGPPP55555YYYYYYYYYYJJJJJJ?????777777?????JJJJJJJ?????????JJJJJJ??77777777777777777777777
##############&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&##BGP55555YYYYYYYYYYYYJJJJJ????7777777????JJJJJJJ??????????JJJJJJ?777777777777777777777777
GGGGGGGGGGGGGBBBBBBBB###########&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&@@@@@@@@@@@@&&&&&&&&&#GP555555PPPPPPPPP55YJJJJ???7777777??JJJJJJJJ???????????JJJJ?J?777777777777777777777777
PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPGGGGGGBBBBBBBBB########&&&&&&&&&&&&&&&@@@@@@@@@@@@@@@@@@&&&&&&&&&##BBBB##########BBGGP5YJ???777!!7??JJJJJJJJJJJJJJJJ???JJJJJJ?777777777777777777777777
PPPPPPPPPPPPPPPPP5P55555PPPPP555555YYYY5YYYYYY5555555PPPGGGGGB#&&&@@@@@@@@@@@@@@@@@@@@@@@@&&&&@@@&&&&&&&&&&&&&&##BGGGP5YJ?777!!????JJJJJJJJJJJJJJJJJJJJJJJJ?777!77777777777777777777
GGGGPPPPPPPPPPPPPPPPPPPGBBBBGP5555PGBGP55YYYYJJJJJJJ???????J5B&&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&&&&&&&&&&&&&#G5JJ?7!!!!7??JJJJJJJJJJJJJJJJJJJJJJJJJ777!!!7777777777777777777
GGGGGGGGGGGGGGPPPPGGB####BGPPPPP55PB&&#GP5PP5555PPPPPP5555PB&&@@@@@@@@@@@@@@@@@@@@@@@@@@@@&&&@@@@@@@@@@@&&&&&&&&&&&&&&#B5?7!!~~7??JJJJJJJJJJJJJJJJJJJJJJJJ?777!!!777777777777!!!!!!!
55555555PPPPPPPPGB###BBGGGGGPGGGGGGGB#BBGGGGGGBBBBBBGGPGB#&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&&&&@@&&&&&&&&&&BPJ~^^7???JJJJJJJJJJJJJJJJJJJJJJJ?777!!!77777!777777!!!!!!!
JJJJJJJJJJJJJJJJY55YYYY555555PPPPPGGGGBBBBBB###BBGPP555G&&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&&&&&&&&#5~:7??JJJJJJJJJJJJJJJJJJJJJJJJ?7777!!!!!!!!!!!!!!!!!!!!!
JJJJJJJJJ?????????JJJJJJJJJJJJYYYYY555PPGGGBBBGPP55555G#&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&&&&&&&&GJ?JJJJJJJJJJJJJJJJJJJJJJJJJJ?777!!!!!!!!!!!!!!!!!!!!!!
JJJJJ?????????????????????JJJJJJJYYYY5555PPPGPP555555G#&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&&&&&&&&#GYJJJJJJJJJJJJJJJJJJJJJJJJJ?7!!!!!!!!!!!!!!!!!!!!!!!!
??????????????????????????????JJJJJYYYY555PPPP555555G#&&&&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&&&&&&&&&B5JJJJJJJJJJJJJJJJJJJJJJJJ?7!!!!!!!!!!!!!!!!!!!!!!!!
????????????????????????????????JJJJJYYY555PPP55555P#&&&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&&&&&&&&&&#5JJJJJJJJJJJJJJJJJJJJJJJ?7!!!!!!!!!!!!!!!!!!!!!!!!
????????????7??????????7777???????JJJJYY5555555YYYPB&&&&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&&&&&&&&&&&B5YJJJJJJJJJJJJJJJJJJJJJ?7!!!!!!!!!!!!!!!!!!!!!!!!
????????7777777777777777777777??????JJJYYY55555Y5P#&&&&&@@&&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&&&&&&&&&&&B5YJJJJJJJJJJJJJJJJJJJJ7777!!!!!!!!!!!!!!!!!!!!!!
7?77777777777777777777777777777?????JJJJJY55555Y5B&&&&&@@@@&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&&&&&&&&&&&#PYJJJJJJJJJJJJJJJJJJJ?777777!!!!!!!!!!!!!!!!!!!!
777777777777777777777777777777777?????JJJYY55555G&&&&&&@&@&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&&@@&&&&&&#GYJJJJJJJJJJJJJJJJJJJ?77777!!!!!!!!!!!!!!!!!!!!!
77777777777777777777777777777777777?????JJYY55Y5B&&&&&&&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&&&&@&&&&&&B5JJJJJJJJJJJJJJJJJJJ?77!!!!!!!!!!!!!!!!!!!!!!!!
777777777777777!!!!!!!!!7777777777777????JJYY55G#&&&&&&&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&&&&&&&&&&&&#PYYJJJJJJJJJJJJJJJJJ?7!!!!!!!!!!!!!!!!!!!!!!!!!
777777777777!!!!!!!!!!!!!!!!!!!77777777??JJYY5PB&&&&&&&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&&&&&&&&&&&#G5YJJJJJJJJJJJJJJJJJ?7777!!!!!!!!!!!!!!!!!!!!!!
777777777!!!!!!!!!!!!!!!!!!!!!!!!777777???JJY5G&&&&&&&&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&&&&&&&&&&&&&#G5YJJJJJJJJJJJJJJJJJ?7777!!!!!!!!!!!!!!!!!!!!!!
7777777!!!!!!!!!!!!!!!!!!!!!!!!!!!!!7777??JJY5G&&&&&&&&&&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&&&&&&&&&&&&&&&&#PYYJJJJJJJJJJJJJJJJJ?7777!!!!!!!!!!!!!!!!!!!!!!
77777!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!7777??JYYG&&&&&&&&&&&@@@@@@@@@@@@@@@@@&&&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&&@@@@@@&&&&&&&&&&&&&&&&#BPYJJJJJJJJJJJJJJJJJJ7!!!!!!!!!!!!!!!!!!!!!!!!!!
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!77777?JJYG#&&&&&&&@@@@@@@@@@@@@@@@@@&&&&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&&&&&&&&&&&&&&&&##BPYJJJJJJJJJJJJJJJJJJ7!!!!!!!!!!!!!!!!!!!!!!!!!!
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!777????JP&&&&&&&@@@@@@@@@@@@@@@@&&&&&&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&&&&&&&&&&&&&&&&###G5YJJJJJJJJJJJJJJJJJ?77!!!!!!!!!!!!!!!!!!!!!!!!!
!!!!!!!!!!!!!!!!!!!~~~~~~~~~~~~!!!!!!!!!!777777Y#&&&&&&&&@@@@@@@@@@@@@&&&&&&&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&&&&&&&&&&&&&&&&&&#GYYJJJJJJJJJJJJJJJJJ?777!!!!!!!!!!!!!!!!!!!!!!!!
!!!!!!!!!!!!!!!!!!~~~~~~~~~~~~~~~!!!!!!!!!!!!!!75#&&&&&&@@@@@@@@@@@@@&&&&&&&@@@@@@@@@@@@@@&&&&&&&&&@@@@@@@&@@@@@@@&&&&&&&&&&&&&&&&#G5YYJJJJJJJJJJJJJJJJJ?7777!!!!!!!!!!!!!!!!!!!!!!!
!!!!!!!!!!!!!!!!~~~~~~~~~~~~~~~~~~~~!!!!~~~~~~~~?G&&&&&&&@@&&&&&@@@&&&&&&&&&&@@@@@@&&&&&&&&&&&&&&&&&&&&&&&&&@@@@&@&&&&&&&&&&&&&&&&#G5YYJJJJJJJJJJJJJJJJJ?7777!!!!!!!!!!!!!!!!!!!!!!!
!!!!!!!!!!!!!~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^~Y#&&&&&&@&&&&&&&&&&########&&&&&&&&&##################&&&&&&&&&&&&&&&&&&&&&&&&&&#G5YYYJJJJJJJJJJJJJJJJJ?7!77!!!!!!!!!!!!!!!!!!!!!!!
!!!!!!!!!!!~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^::7B&&&&&&&&&&#####BBBB######################################&&&&&&&&&&&&&&&&&&&&&#PYYYYJJJJJJJJJJJJJJJYJ?7777!!!!!!!!!!!!!!!!!!!!!!!
!!!!!!!!!!~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^:^::::^5&&&&&&&&&#BBBB####&&&&&&&&&&&&&&&&###################&&&&&&&&&&&&&#BPPB#&&&&&&BPYYYYJJJJJJJJJJJJJJJYJ?!!!!!!!!!!!!!!!!!!!!!!!!!!!
!!!!!!!!!~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^::::::::::.~P&&&&&&&#BBB##&&&&&&@@@@@@@@@@@@&&&&&&&&######&&&&&&&&@@@@&&&&&&&&&BY?JG#&&&&BPYYYYYJJJJYYYYYJJJJJJYJ?7!!!!!!!!!!!!!!!!!!!!!!!~~~
!!!~~~!!!~~~~~~~~~~~~~~~~~~~~~^^^^^^^:::::::::::...7B&&&&&&BBB#&&&&&&&&@@@@@@@@@@@@@@@&&@&&&&&&&&&&&&&@@@@@@@@&&&&&&&&&BY7YB&&&#G5YYYYYYYYYYYYYYYYYYJJYJ77!!!!!!!!!!!!!!!!!!!!!!!~~~
!!!!!!!!!!!!!~~~~~~~~~~~~~~~^^^^^^^::::::::::::...:5#&&&&&&BBBB#&&&&&&&&&&&&&@@&&@@@@@@@@@&&&&&&&&&&&&@@@@@@@&&&&&##BGGG5?JG&&&#GYYYYYYYYYYYYYYYYYYYYYYJ77!!!!!!!!!!!!!!!!!!!!!!~~~~
?????????????777777777777!!!!!!~~~~~~^^^^^^:::...:?##&&&&&&BBBB###&&&&@@@@&&##&&&&&&&&&&&&&&&&&#&&&&&@@@@@&&&&&&&###BP5YJ?JB&&&#PYYYYYYYYYYYYYYYYYYYYYYJ7!!!!!!!!!!!!!!!!!!!!!~!~~~~
^~7J?!~~~~!77?777777777?7???????????????JYJ?!: ..!GBB##&&&#BBBB###&&&&&@@@&#BBB#&&&&&&&&&#####BG#&&&@@@@@@&#BGP5P#&##PYYJ?JB&&&B5YYYYYYYYYYYYYYYYYYYYYYJ7!!!!!!!!!!!!!!!!!!!!!~~~~~~
^~7?!~^^^~^^~~^::::^^~7!~~~~~^~~~^^^~~~!JYY7^.  :JGGGGB&&&#BBBBB###&####&&&#####&&&&&&&&###BBBGGB&&&&&@@@&&BBGPY?5BBGPYJ?7JB###BYYYYYYYYYYYYYYYYYYYYYYY?7!!!!!!!!!!!!!!!!!!!!!!~~~~~
::~7~::::::^~~~:::~~^~7!~~~^^:::::::::::!J7~:.  :YGGGB#&&&#BGGBBBB#########&&&&&&&&&&&&&##BBBBGPB#&&&&&&&&&&###BGP5Y55JJ?7?B#BBGJJYYYYYYYYYYYYYYYYYYYYY?77!!!!!!!!!!!!!!!!!!!!!!~~~~
  ^7~. ....^~!!:.:!!^^!~^~~^:::^::::::::~~~::.  :5GGBB#####BGGGGGBB#####&&&&&&&&&&&&&####BBBBBP5PB##&&&&&&&&&&#BBP55YYJ??7?GBP5PJJYYYYYYYYYYYYYYJYYYYYJ?77!!!!!!!!!!!!!!!!!!!!!~~~~~
  :!~.   ..:^^::.:~!^^!~^~~:::^^^:.::..:^^^:..  :5GGBBBBB#BGGGGGGGBBBB#################BBGGGGG5Y5PGGGB#&&&&&&&##BGGP5YJ?77?G#BPPYJYYYYYYYYYYYYYYJYYYYYJ?7!!!!!!!!!!!!!!!!!!!!!!~~~~~
  :!~.   ........:~!~^!~^~~:::^^^:.::...^^^:..  :5GGBBBBBBBGGGGGGGGGGBBBBBB###BBBBBBBBBBBGGGGPYY55PPPGGBB######BBBGP5YJ?77?5B#GPYYYYYYYYYYJYYYJJJYYYYYJ?7!!!!!!!!!!!!!!!!!!!!!!!~~~~
  :!~.   .........~!~^~~^~~:::^^^.......^~^:..  ^5GGBBBBBBBBGGGGGGGGGGGGBBBBBBB#####BBBBBGGGGPYY55555PGGGGGGGGGGGGPPYJ??77J5G#BG5YYYYYYYYJJYYYJJJYYYYYJ77!!!!!!!!!!!!!!!!!!!!!!~~~~~
..:!~.   .........^~~:~^^~~:::^^^.......^~^:..  :JGGGGBBBBBGGGGGGGGGGGGGBBBB########BBBBGGGGGP55555PPGBBBGGGGGGGPP55YJ????YPGBBGYJJYJJJYJJJYYYJJJYYYYYJ7!!!!!!!!!!!!!!!!!!!!!!!~~~~~
..:!!.  ..........^~~^~^^~^:.::::.......:~^::.  .:?5PGGBBBGGGGGGGGGGGBBBB####&&&##BBBBGGGGGGGP55555PPG####BBBBGGPPYYJ????J5PPGBGYJJJJJJJJJJYYJJJJJJJYYJ7!!!!!!!!!!!!!!!!!!!!!!!~~~~~
~~!7!~~~~^^^^~~^^^~~~~~^^^^::::^::::::::^~^^:. ..  :75PGGGGGGGGGGGGBBBB###&&&&&&#BGGGGGGGGGGGGP5YYYYYPB#&&###BBBGP5Y?????YPPPGGYJJJJJJJJJJJJJJJJJJJJYYJ7!!!!!!!!!!!!!!!!!!!!!!!~~~~~
:^~!7^:..::::::::^^~~^~^.:^^^^^^:.::^^^^~~^^:. ..    .^!7J5GGGGBBBBB#####&&&&&##BBBBBBBBBBBBBBGP5YYJJ5GB#&&####BGGP5JJJJJPGGG5YJJJYYJJJJJJJJJJJJJJYYYYJ7!!!!!!!!!!!!!!!!!!!!!!!!~~~~
 .:!7:   .........^~^:~^ .^:...:.   ....:~^^:: ..         :J5PBB######&&&&&&#BBBBBB##########BGGGGP5YY5PGB#&&###BBGP5YJJYPP5YJ?JYYYYYYYJJJJJJJJJYYYYYY?7!!!!!!!!!!!!!!!!!!!!!!!~~~~~
:::!7^:^:.........^!~:~~:^^:...:.   . ..:^^^::...          ^YPGB######&&&###BGGGGGGB##&&&&&&###BGP5YYYYYY5PB#####BBGP5?~....!?JJYYYYYYYJJJJJJJJJYYYYYY?!!!!!!!!!!!!!!!!!!!!!!~~~~~~~
:::!7^:^:.........^!~:~~^~~^:::~.   ....:~^^::...  .   ... .?PGB##########BBGGGGGGGBBB#&&&&&&&&#GP555YJJJYY5GBBBBBBGPY~     !JJJYYYYYYYJJJJJJJJJJJYYYY?!!!!!!!!!!!!!!!!!!!!!!~~~~~~~
::.^7^:^:.........^!~:~~^~~^:^^~^...::::^~~^::... ... ...:. ~5GGBB#######BBBGGGGGBBBBBB####&&&#BGP5P5YJJJJJY5PPPGGGP57.     !JJJYYYYYYJJJJJJJJJJJJYYYY?!!!!!!!!!!!!!!!!!!!!!~~~~~~~~
:. ^7~:::.........^!~:~!^~~^:^~~~:.:~^:^~~~^::... .....:::: .?GGBBBB#####BBBBBBBBBBBB##########BGGPP5JJJY55Y5PP5PPP5?^      !JJJJJYYJJJJJJJJJJJJJJYYYJ7!!!!!!!!!!!!!!!!!!!!~~~~~~~~~
:::~7!^~~:::^^^:::^!!^~!~~~~~^~!~^^^~^::^~~^::........::^^...:YGBBBB#################&&&&&&&&&&##BBGGPP5PPGGP55555YJ~      .7JJJJJYYJJJJJJJJJJJJJJYYYJ7!!!!!!!!!!!!!!!!!!!!!~~~~~~~~
..:~7!::::::^^^^^^!7!^~!~~~~~~~!~^^~^:::^~~^::.......:^^^^:...7GBBB######&&&&&&&&&&&&&&&&&&&&&&&&###BBBBBB#BGP5555Y!.      .7JJJJJYJJJJJJ?7???JJJJJJYJ7!!!!!!!!!!!!!!!!!!!!!~~~~~~~~
^^~!7!:..^~~~~~~~~!!!~!!!~~~^~~~~^^~~^^^~~~~^:......:^^^~~:...!GBB######&&&#######&&&&&&&&&&&&&&&##BGPP5PBBBGGPPPY!.       .!??JJJJJJ???7~^~!7??JJYYYJ7!!!!!!!!!!!!!!!!!~~!~~~~~~~~~
^^^~!!~^^^!!77777777777!!!!!!!!!!7!!!!!!!!!~^^......:^~~~~:..:!PBB######&&&########&&##&&&&&&&&&##BGP555PGGGGGGPY?^.........:!?JJJJ???777!!!JYYJ77JYJ?7!!!!!!~~!!!!!!!!!~~~~~~~~~~~~
   .~!:  .::^~!!!~!7??777777???77J?777777!!~^^......:^~~~^...:!PBB#####&&&&#########&&&&&&&&&&&&&#BGPPGGGPPGGGP5J7!~~~^^::::~7?????7!!!!!!77JPP5J7??JJ??7!!!!~~!!!!!!!!!~~~~~~~~~~~~
~~: ~!~~^:^~~7???7777777777???J?JJ7777777!!~^^:.....:^~~^^...:7GBB####&&&&&##&&&###&&&&&&&&&&&&&##BBBBB#BPPPGP5YJ7777!!77!^^~!777777!!!!!!!!7YPGGPP555YJ?7!!!!!!!!!!!!!!~~~~~~~~~~~~
!!~^!!!~.:~7??JJJJ5PP5Y?77???JJJJJ?????77!!~^^:.....:^~~^~!~^~JBBB#####&&&&&&&&&###&&&&&&&&&&&&&&##BBBBBBGGGP5YJ?77777!7JJ?????????7!!!!!!^^!?YGGGGPPPPYJ7!!!!!!!!!!!!!~~~~~~~~~~~~~
^^^^!77!^~7?7!7?5G#&&&#BY??JJJJJJJJJJ???777!~~!!???77?JJ5####BBBBB#####&&&&&&&#########&&&&&&&####BBBGBGGGPPP5YJ?777?777JJJJJJ?????7!!7????J5GGGGP5YJJJYJ?7!!!!!!!!~~~~~~~~~~~~~~~~~
^~!^!77??JJ?!!!7P#&&&&&&BJJYJ!^!JYYYJJYYY55P55PGGGGGGP55PB&&&##########&&&&&&&&&##################BBGGGGPJ^^75YJJ?7??????JYJJJJJ???7!!?55Y??YPGGGPY?????JJ?7!!!!!!!!!!~~~~~~~~~~~~~~
~!7~!77?JJJJ?77!75B####BG5?7!!~~?Y5555PGGGBBGGPGGGGGBGGPPPB&&&#########&&&&&&&&&&&&##&&&&&&&&&&####BBGPPJ^...~YYYJ?7?JJJJJJYJJJJ?77!!!J555YY5PGGGGP5YJJJJ?J?7!!!!!!!!!!~~~~~~~~~~~~~
~7?!!7??J?7??55Y?!?GBBBP55YYY555PPPPGGGGGGBBBGGGGBGBBBGGPPG#&&&########&&&&&&&&&&&&&&&&&&&&&&&&&&#BGP55Y?^^^:^?55YJ???JJJ??JJJJJ?77!!!?5GPPPP5PGGGGBBBBGPYJ??77!!!!!!!!!!!~~~~~~~~~~
~^~!!JYJJ?77?PGGPY775P55555PPPPPPPGGGGGGGGBBBBBGGBBBBBBGGPPG#&&########&&&&&&&&&&&&&&&&&&&&&&&&#G5YYYYYJ???JY55P5YYJJ??????JJJYJ?JYYYJ?J55?77~!YPGGGBB##BGP5J???!!!!!!!!!!!!!~~~~~~~
!~~!777!!!!7JYYYY555555PPPPPPPPGGGGGGGGGGGGBBBBBBBBBBBBBGGGGG#&&&######&&&&&&&&&&&&&&&&&&&&&##BG5YYYYYYPJ?J5PGGP?!~^~~!!!77?JJJ7::!5PJ!~!7!~~^!JPGGGGB###BGG5Y??7!!!!!!!!!!!!!!!!!!!
~^~~^:^!!!?JYYY555PPPPPPPPPPPPPGGGGGGGGGGGGGBBBBBBBGGBBBBGGGGGB&&&#####&&&&&&&&&&&&&&&&&&&&##BGP555555P#5?JYGGGGJ??!^~~~!!!7?JJ?:..~5PP555J7~~7Y5GBBGBBBGPP555JJ?!!!!!!!!!!!!!!!!!!!
7777!~!JYY55555555PPPPPPPPPPPPGPPPPGPGGGGGGGGGBBBBBBBBGBBBBBGGGB#&&&&&&&&&&&&&&&&&&&&&&&&&###BGP555555B&5???5GBBYJPBPJ7!!!7?JJJ?~:.:!5GBGGPY7?5P5GBBGPP55YYY555YJ?!!!!!!!!!!!!!!!!!!
JJJJJYYY555555555PPPPPPPPPPPPPGPPPPGPPPGGGGGGGGBBBBBBBBGGBBBBBBBB##&&&&&&&&&&&&&&&&&&&&&&&&##BGPPPPPY5#&Y???J5GBP?YBBBGPY??JJJJ?!:.:~YGGGGP55PGGGGGGP5YYYJJJJYYJJ??7!!!!!!!!!!!!!!!!
JYY5555555555555PPPPPPPPPPPPPPPPPPPPGPPPPPGGGGGGGGGBBBBBBBBBBBBBBBB##&&&&&&&&&&&&&&&&&&&&&&#BGGGPPP5YY#B????J55GGY5PGB###BGPP5J7777JPBBGGPP5555PGGGGP5YYYJJJYYYYJJ??7!!!!!!!!!!!!!!!
55555555555555PPPPPPPPPPPPPPPPPPGGPPPGGPPPPPGGGGGPPGGGBBBBBBBBBBBBBBB##&&&&&&&&&&&&&&&&&&&##BGPPPP55YYB57???Y5PPP55GGGB#####BBBGGGBBBGGPPPP5555PGGBBBGGGGGGGBBGP5YJ?7!!!!!!!!!!!!!!!
55555555555555PPPPPPPPPPPP55PPPPPGGPPPPPPPPPPGGGBGPPPPGGGBBBBBBBBBBBBBBB##&&&&&&&&&&&&&&&##BGPPP555YY55????JY55PPY5GGGGB#####BBBBGGPPPPPGGGP55PPGGBB###BBBBB####BPY?7!!!!!!!!!!!!!!!
555PPPP555PPPPPPPPPPPGGPP55555555GGGP5PPPPP5PPGGBBGGPPPPGGGBBBBBGGBBBBBBBBBB##&&&&&&&&&&&##BGPPP55555YJ?J??J5PPP5YJPGG5YPBBBBBGP555PPPPPGBBG5Y55PGB#####BBBGBBBBBBPJ7!!!!!!!!!!!!!!!
555PGGP55PPGGGGPPPPPPGGGGP55555555PGG555PPPPPPPGGBBBGGPP55PPGGBBGGGGBBBBBBBBBBBB###&&&&&&##BGGGPP55YYJ?JJ??J5GGP5JJ5PP555PBBBBBBBGGGGGGBB#BB5JY5PGBB###BBBBGGPPPPPP5?!!!!!!!!!!!!!!!
55PGGPP5PPPGGBBGGPPPPPGGGGP55555555GGP555PPPPPPGGBBBBBGGP5555PPGGGGGGGGGGBBBBBBBGGGBBB###BBBGGP555YYJJJJJ??J5PPP5JJ5PGGB######BBBGGGGGGBBBBBBBGGGGGBBBBBBGP555YJJYYY?7!!!!!!!!!!!!7P
55GGGGPPPPGBBBBBBGP5PPGGGGGP5555555PGGP555PPPPPGGGGBBBBBGPP555555PPPGGGGGGGGGGGBGGGGPPPPPPPPP555YYYYJJJJYYJJYPGP5JJ5GBBBBBBBGPPPPP55PBBBBBB#####BGGGGGBBBGP55YYJJJYY?!!!!!!!!!!!75B&
5PGGGGPPPGBBBBBBBBBP5PPGGBBGP555555PPGGP55PPPPPPGGGBBBBBBGGPP55555555PPPPGGPPPPPPPPPPPPPPPPP5555YYYYYYYY5PYJJ5GPYJJ5GGPYY55PGGGGBBBBB###B########BBBB#BBBBGGGGGGPP5J7!!!!!!!!!7YB&&&
PPGGGGPPPGB#BBBBBBBGGPPPGBBBGP55555PGGBGP55PPPPPPGGGBBBBBBBGPPP55555555PPP5PPPPPP55555PPPPP5555YYYYYYYYY5P5JJ5P5YJYPBGPYY55GB###########&&&####################BGP?7!!!!!!!!!?G&&&&@
PGGGGGGPPGB###BBBBBBBGPPGBBBBGP555PPGBBBG555PPPPPGGGGGBBBBBBGGPPPPP55555PP55PPPPPPP5555PPPP55555YYYYYPPJYPPYY55YYYYPBG5Y555GB######&&&&&&&#####BBBBBBB#########G5?7!!!!!!!!!Y#&&&@@@
PGGGGGGPGGB###BBBB##BGPPPGBBBBGP555PGBBBBP555PPPPGGGGGBBBBBBBGPPPPPPPP55555Y555PPPP5555555555YYYYYJJYPPYJPP555YY555GBG55PPPGB#BGPB#&&&&&&&####BBBBBBBBBB######G5?7!!!!!!!!JG&&&&@@@@
GGGGGGGGGGB####BBB###BGPPGB##BBGPP5PGBBBBGP55PPPPPGGGGGBBBBBBBGPPPPPGGGP55555YY55555555PPPPP555YYYJJY5P5JYP5YY55PP5GBG5PPPPGBBBG5YP#&&######BBBBBBBBBBBBB####G5?777!!!!!?P&&&@@@@@@@
GGGGGGGGGGB####BBBB###BGPGB###BBGP5PGBBBBBG555PPPPPGGGGGBBBBBBBGPPPPPGGGPPPP555555555Y5PPGPPPP55YYYJJ5P5YY55YY5GG55GBP5GPPPBBBBP5YJP#&&##BBGGGGGGGGGBBBB###BG5?77777!!75#&&&@@@@@@@@
GGGGGGGGGGB#####BBB####BGPG#####BG5PGBBBBBBG555PPPPGGGGGBBBBBBBBGPP55PGGPPP5555555555YYPPPPPPPP555YJJYPP5YYYY5GGGY5BBPPPPPGBBBGP5PY5G#&##BBGGGGGGGGGGBBBBBBGY?777!!!!?G&&&@@@@@@@@@@
GGGGGGGGGGB######BB#####BGGB####BG55GBBBBBBBP55PPPPPGGPGGBBBB#BBBGG555PGGPPPPP555555555PPPPP555555YYJYPP5JJY5GGGPY5GG5PPPGBBBGGP5P555B###BBGGGGGGBBBBBBBBBBP?77!!!!75#&&&@@@@@@@@@@@