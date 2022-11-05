**Templates:**

Template tasks and projects are a way to quickly replicate projects or tasks.

Given a set of tasks or projects, the template task/project creates a copy 
that can quickly be put into a different place

For example, say a user wishes to create a project to revise for exams
Assuming they have a section for each subject, it would be a pain to go 
and create individual tasks for stuff that would be shared between sections

In the case of exam revision, every subject is going to have 
a 'practice problems' task and a 'make a summary sheet' task and
a bunch of other similar stuff

So, to make things easier you do it ONCE and then save it as a template
And then the user should be able to add that same template somewhere else 
and avoid doing the same thing twice

Similar thing with tasks is a task template

One thing to note here is that completing a task in a template copy does not modify the template itself
They're copies, and not interlinked at all

Ideally, templates will have their own tables

**LinkerTasks: (More on this stuff at the end of [THIS](./PendingFeatures.MD)**

A subclass of tasks that hyperlinks to another set of projects/tasks

Linker tasks can link to other projects, sections or tasks. It can link to MULTIPLE of these

They have a flag used for checking if on completion of its ParentTask (i.e the task that holds the linker task), 

the stuff its linking must also be completed. The user can specify which 
particular tasks/projects/sections that it links to should be completed and which ones shouldn't be completed
on completion of the parent task

Ideally a LinkerTask will user an interfacelinkertask, which is just a linker task that links to one other thing
And that interfacelinker task holds a flag to decide if the things its linking to gets completed on completion of its parent linker task.

Note: Completing a section just refers to finishing all the tasks contained within it and deleting
Completing a project just finishes all the tasks within that project

**In order to know what recursion is you must first know what recursion is to know what recursion is to know what recursion is to know what recursion is to know what recursion is to know what recursion is to know what recursion is to know what recursion is to know what recursion is to know what recursion is to know what recursion is to know what recursion is to know what recursion is to know what recursion is to know what recursion is to know what recursion is to maximum recursion depth exceeded**

Linking and projects within projects cannot be brought up without talking about
the question of recursion. 

Recursion placed its somewhere that its not designed for, is painful to think about

To avoid the user messing stuff up, we define a few rules and conventions

**For Projects:**

All projects referencing other projects will be connected using
a hyperlink object class. They're just references and one is not a subproject of another

When a user wishes to actually nest projects, we connect the 2 projs
using a LinkerObject Class with a parent project and a child project attribute
Same as before, but this DOES NOT HAVE the flag to see if on completion of the parent task/project,
the child proj should be completed. When linked with linker objects they are automatically completed. 

This doesn't really seem to solve the problem of projects potentially linking to themselves, with hyperlinks
especially when completing stuff is involved. 

Using Linker objects, an easy fix for this is to first remove/complete all the 
references to said project first, this will ensure that nothing else links to it and breaks
any possiblity of having an infinite loop

**For Tasks:**

Differentiate between subtasks and tasks that are linked using hyperlinktasks when coding

linkertasks have the flag set as I mentioned before

just ensure that when completing a task you specifically handle the hyperlink class stuff first

**Completion or Deletion**

COMPLETE != DELETE

Completion of a task/project just changes a "iscompleted" attribute on it.
(I was considering moving them to a whole other table but that seemed kind of wasteful and complicated to handle
I'll leave it upto you guys to discuss how you'd like to implement it)

This is because being able to do a quick undo for accidentally completing tasks is useful

**Other Task Related Things:**


**Task Constructor:**
Having a task constructor would be useful. User specifies just names for multiple tasks
and you get a list of them where ever the original "task constructor" task was.

Could Probably use this a lot when making templates because I can see that being useful 

**YOUR TEXT HERE**

A text task, its just that. Its a bunch of text which doesn't count for overall completion. 
It only exists to add notes to stuff.

**Again?**

Tasks should probably be able to repeat perodically
Ideally we give the user options as to how they'd like to
have the tasks repeated

Again, implementation is your discretion. 

Keep an eye on the '\#pending-features' channel, I'll ping you guys if theres anything important

You will be left with a lot of questions and probably won't understand all of it perfectly
because I suck at explaining things properly so just ask if you need help understanding something


&BB###&#GB##&&&&&B5YYYYYYYYJJ?!!!!!!!!!~~~~~!!!!!PGPGP7^^7GG?77?PGGGG7^^!G5!!!!!777??JJYYJ7!?YYYYYY?~!JYYYYY55555J!!?YYYYYYYYYYYYYY55555555YYJ??JJ??????JJYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY
&BGB#&&#BGG###&&&BYJJJJ???!!~~^^^^^~^^^^^~~~~~~~~5GPP5!..^PG7!7JPPPPP~..^5?^^~~~~~~!77??JJ7~~7JJJJ?!^^7JJJJJJJJJ?~^!?JJJJJJJJJJJJJJYYYYYYYYJJ??7777777777??JJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJ
&BB#&GPPP#BGB##&&#5?7777!~~~~~~~~~~~~~~~~!!!!!!!!JPPPPJ:.:YGJ7?JPPPPP~..^P?^^~~!!~!7777?JJJ7~~!JJJ?!^~?JJJJJJJJJ!^~7?JJJJJJJJJJJJYYYYYYYYYJJJ????7777?????JJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJ
&GB#&G??5#BPPG###&BJ~~~~~!777777!!!!!!!!!77!!!!!!JPPPP5^.:JGY??JPPPP5~..~GJ~~~~~~~~!77??JJJJ7~^!7??7~~!?????7777~~~7?JJJJJJJJJJJJYYY555YYYYJJJJJ?7!7???JJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJ
&GBB##&#GG55PPGB###B?~!77?777????????????77777777?5PPPP!..?G5??JPPPPP~..JGJ7!~~~~~!77?JJJJJJ?!~~~!!!!!~~!!!!!!!!!!!777777??J??JJJJYYYYYYYYYJJ????777???JJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJ
&BBBBB#B55YYY5PGB###BY??????????????????777????77!JPPPP7..?G5??JPPPPP~.^PY?7!~!!!!7?JJJJJ???77!!!!!!!!!!!!!!!!!!7!!!7!!~~~!7????JJJJJJJJJJJJJ????????????JJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJ???JJJJ
&B##BBBG55YYY5PPGB####PJ??JJJJJJJJ??????777????7!!75GPPY:.JG5J??5PPP5^.YGJ??7!!77?JJJJ?77!!!!!!!!!!777!!!!!!!!!!!!!7!!!~^~!!!77!77???777???JJ??777!77777777????7?JJJJJJJJJJJJJJJJJJYJJJYYJJJJJJJJJJJJJJJ
&G###BBB5YYYYY5PPGGB###B5YJJJJJJJJJJJJJJJ??????????YPPPP~.JGPJ??5PPP5^~G5JJJ?7777???777!!7777!!7777777!!!!!!!!777?77!!!!!777777777??7777777??????????7!!!!!!777???77JJ??JYYYYYYYYYYYYYJJJJJJJJJJJ???JJJJ
&PGB##BB5YYYYYYY55PPGGB##BPYJJJJJJJJJJJJJJJJJJJ?JJJJY5GPY!5GPJ?JYPGP57PGJJJJJ??7777777777???????????77!!7???????JJ?77777777?????????7777??????JJJJJJJJJJJJJJJJJJJJJYYJJYYYYYYYJJJJJJJJJJJJJJJJJJJ??JJJJJ
&PPGB##BP5YYYYYYYY5555PG###BP5YYYJYYYJJJJJJJJJJJJ????JPPPPPGPJYGGGBGPPG5JJJJJ??????????JJJJJJJJJJ?????77?JJJJJJJJJ??????????JJJJ?????????JJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJ???777777???777
#5PPGB##B5JY555YYYY5555PGGBBBGGPP55YYJJJ??????????????YPPPPGGPGGBBBBBGGJ???????????????????JJJJ?JJJJ??????JJJJJJ????????????????????7????????????????????777777777??????????????????????7777777777777777
#5PPGBBBBGYY5PPYJJJJJJ5555PPPPPP55YJ????7????????????7?GPPPPB#&#PPPGGGGBGJ??????????????????????????????????????7777777777777777777777777777777777777777777777????????????????777777777777777777777?7777
#Y5PPPPPPP5YYY55YJ?77?JY555YYYJ??????777777?777?777777JGPPPPG&#GPPPPPPPBBG5J7???????????????????????777777777777777777777777777777777777777777!!!!!!!!!77777777777777777777777777!!!77777777777777777777
#Y555YYYYYYY5555J??????????77777777777777777777777777?PPPPPPGBPPPPPPPPPP5PGPJ77????????777777777777777777777777777!!!!!!!!!!!!!777777777777!!!!!!!!!!!!!!!!!777777777!777!!!!!!!!!!!!777777!!!!!!777!!!!
#?JJJJJJJJJJJJJJ???777777777777777777777777777777777?YGPPPPPPPPPPPPPPPPPPPPBG?7777777777777777777777!!!!!!!!!!!!!!!!!!!!!!!!!!!!7!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!~~~~~~~~~~~!!!!!!!!!!!!!!!!!!!!!!!
B77??77777777777777777777777777777777777777777777777?5PPPPPPPPPGGGGPPPPPPPGGG577777777777777!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^~~~!!!!!!!!!!~~~!!!!!!!!~~
B77777777777777777777777777777777777777777777777777775PPPPPPPPPGGG5YPPPPPPGG557!7!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^~~~~!~~~~~~~~~~~~~~~~~~~~~^
B7777777777777777777777777777777777777777777777777777YPPPPPPPPGG5GB:!PPPP5G&5?7!!!!!!!!!!!!~!!!!!~~~~~~~~~~~~~~~^^^^^^^^^:::::::^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^~~~~^^~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^
B7777777777777777777777777777777777!!!!!!!77!!!!!!!!!YP5Y?!!~!7???7.~PPPPPYJ!::^7?!~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^:^^::::::::::::::::^^^^^^^^^^^^^^^^^^^^^~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
B!777777777777777777!77777777777!!!!!!!!!!!!!!!!!!!!!JP?:.......:^^^?5J5PPY!:^~~^7?~^~^^~~~~~^^~~~~^^^^^^^^^::::::::::::::::::::::::::::::::::^^^^^~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
B~!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!~~~~!Y7:.......::::^~!^^7J~^7!^^:~?~^^^^^^^^^^^^^^^^^::::::::::::::::::::::::::::::::::::::::^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^:::::::::^^^^^^
G^~~^^~~~~~~~~~~~~~~~~~!!!!!!!!!!!!!!!~~~~~~~~~~~~^^!J:........:~7J5P7^.:~^~^....!!^^^^^^^^^^^^^^^^::::::::::::::::.:...::::::::::::::^^^^::^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^::::::::::::^^^^^^
G^^^^~~~~~~~~~~~~~~~~~~~!!!!!!~~~~~~~~~~^^^^^^^^^^^^75!..........^G###5..:.:....:!!^^^^^^:::::::^:::::::::::::::.........::::::::::::^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^:^^:^::::^^^^^^^^
G^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^::::^Y5J!:.........~55P57!^:......:7^^^^^:::::::::::::::::::::::........:::::::::::::^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^:::^^^^^^^^^^^^^^^^
B~~~~!!!!!~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^:::::::::^JP5J:..........:^^~!~:.........!~:^^^^^^^^^^^^:::::::::::::::::::::::::::::::::^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^::::::::^^^^^^^^^^^^^^
B~~~~~~~~~~~~^~^^^^^^^:::::::::::::::^^^:::::::^~?5555?............:::::..........!~:^^^^^^^^^^^^:::::::::::::::::::::::::::^^^^:^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^:::::::::::^^^^^^^^^^^^
B~~~~~~^^^^^^^^^^^^:::::::::::::::::::^::::::~7Y555555!......................... .7~:^^^^^^^^^^^^^:^^:::::::::::::::::::::::^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^:::::::::::^^^^^^^^^^^^
G^^^^^^^^^^^^^^^^::::::::::::::::^^^^^^^::^!?Y5555555J:...........::.....::......^5J~::^^^^^^^^^^^^^^^^^^^:^:::::::::::::::^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^::::::::::::^^^^^^^^^^^^
G^^^^^^^^^^^^:::::::::::::::::^^^^^^^^^^~?Y5555555555!...............:::.........:?P57^::::^^^^^^^^^^^^^^^::::^:::::::::::^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^::::::::::::::^^^^^^::
G:^^^^^^^^:::::^:::::::::::^^^^^^^^^^~!JPP5555555555?:............................:J55Y!^:::^^^^^^^^^^^^^^:::^::::::::::::^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^:::::::::::^::::::::::
G::^^^^^^^^^^^^^^^^^:::^^:^^^^^:::^~?55555555555555?:..............................~Y555Y!^::::^^^^^^^^^^^::::::::::::::::^^^^^^^^^^^^^:::^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^::::^^^^^::::::::::^^::::::::::
G::^^^^^^^^^^^^^^^^^^^^^^^^^^^:::~?5P55555555555P5?:................................~Y5555J!::^^^^^^^^^^^:::::::::::::::::::::::^^^:::::::^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^::::^^^^^:::::::::::::^::::::::
G:^^^^^^^^^^^^^^^^^^^^^^^^:::::^?55555555PPPPPPGP7. ............................... .~555555?~:::^^:^::::::::::::::::::::::::::::::::^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^:::::::^^^^^^^::::::^
G^^^^^^^^^^^^^^^^^^^::::::::::!5PP5555555PPPPPPJ~. ................................  .~555555Y!::::::::::::::::::::::::::::::::::::::^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^:::^^^^^^^^^^^^^^^^^
G^^~~^^^^^^^^^^^^::::::::::.^JPPP55555555PPPPY~...............................        .^Y555555?^::::::::::::::::::::::::::::::...::^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^::::::::::^^^^^^^^^^^
G^^^^^^^^^^^::::::::::::::.^JP5555555555PPP5J^................   ..  ... ..             ^5555555Y~::::::::::::::::::.:..::::::::::::^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^:::::::::::^^^^^^^^^^^^
G::::::::::::::::::::::::::JP5PPPP5555PPPP5!..................                          .~555555557:::::::::::::::::::::::::::::::::^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^::::::^^^::::::::::::::^^^^^^^^^^^
G:::::::::::::::::::::::::!55J?7!7?Y5PPPPJ^.....................                         .75555YYY57::::::::::::::::::::::::::::::^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^:::^~^::::::::::::::::^^^^^^^^^^^^
G.::::::::::::::::::::::::?J~::.:...!PP5J:. .....................                         ^5J~::::~7!^::::::::::::::::::::::::::::::^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^:::::!P!::::::::::::::::::^^:::::::^
G.::::::::::::::::::::::.^~^::..:   :YPY^. ......................                     ....^~.  .:.^^~!:...........:..::::::::::::::::::::::::^^^^^^^^^^^^^^^^^^^:::::::::7G!::::::::::::::::::::::::::::
P.:::::::::...:::::::::.:^.......    :?~..................  .....              ....  .:. .      . ...:!~~~~^~~~~~~~~~~~~~~~~~~~~~~!!~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^::::?P7::::::::::::::::::::::::::::
P...........::::::::::::^.      .        .:.............    .....              .......:.. .          .JPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP5555PY?~^7PJ^:::::::::::!7:::::::::^^^^^
P.........::::::::::::::^.           ..................     .....              ...........^.         .PBBB#BBBBBBBBBBBBBGGGGPPPPPPPPPPPPPPPPPPPPPPGGGGGGGGGGGGGGGPPPPPPP55P?:::::::::::~PY:::::::^^^^^^^
G.:::::::::::::::::::::.::           ::               .     .....         ..  ............:.        .7PGGPGPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPGBG57^:::::::::7P7:::::::^^^^^^^
G.::::...................::           :.              .      ...          ............. .:.   .    .JP5PPPGPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPGGGGGGBBBBGPY!^::::^JP~::::::::^^^^^^
G.:::.....................::      ..  .:.             .      ...         .............. .:....  .:~5GGGGGGBGGGGGGGGGGGGGGGGGGPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPGGGGGGGGGGGGGGGPJ!^:75J^::::::::::^^^^
P.:::......................^?: ..   .. :.  .          ....................................^?^~?5PGBBBBBBGG##BBBBBBBGGGGGGGGGGPPPPPPPPPPPPPPPPGGGBBBGGGGGGGGGGGGGGGPPPPPPPPPPPPPGGGGP55G5!:.::::::::::^^^
G.:::..:...................^55J?J?!~^:...             ....................................^~:~JGBGGGPPPGGGPPPPPPPPPPPPPPPPPPPPPPPPPPPGGGPPPPPPPPGPPPPPPPPPPGGGGPPGPPPPGGGGGGGGGGGGGPPBBGP5?~^::::::::::^
P..........................:YP5555557.    ..         ....................................:~:..:^JPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPGGPPGGPGGGGGPGPPPPGGGGGGGGGPGGGGGGGGGPPGGGGPPPPPPPPPPPPP5J!^::::::::
P...........................!5555555J:                  .   ..     ...  ............... .~^::....^?PPPPGGBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBG5J^:::::
G...........................:?P5555557.                      .     ................... .~^.........^?PPPBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB#B~:::::
P............................^Y555555Y7.      ...            .      ...............   .^^.......:::::^75BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBP~:::::
P.:::...:.....................^YP5555557.   ........         .............          .:~:.......:::::::.^7YPGGGGBBBBBBBBBBGGGGGGP555P5555YY5PPP5PGGGG555Y55PPPP5YJJJ??JJJJ55J?JYJJYPG5J?YY5PGBBGJ?!^^::::
G.:::::::::....................:JP555555J^.   ......      ..............          .^^^::^^:..:::::::::::::!5GBBBBGGGGBBBBGPGBPPPYY5PP5P555PPPPYYGGGG555555PPPPJ77JY?7?JJJ55Y?7??YPGBG5JY55GBBBJ^^~!!!~^:
G.::::::::::....................:75555555Y!:.  . .........................    ..:^~::....^~^:::::::::::::::^?PBBBBBBBBBBBGPGBGGG5Y5GG55PPPGGPGYYGGGG55PP55PPPY?7?Y5J?JJJJ5PP5J7?5GBBGPY5GGGBBG?^^^^^~~!!
G.:::::::::::::...................^75555555Y!:.   ................  ..   ...::^:.....:::. .^!::::::::::::::::~?5BBBBBBBBBGPGBBBBP5PGG55GGGGGPPYYPGGGP5GG55PP5YJ?J5PYJJYJJJ5PP5?7YGGBG55GGGGPGG?~~~~~~~~~
G.::::::::::::::::.....::::::::^^:::^J5555555Y7~:.      ................:^^::..  ......::..^!::::::::::::::::::~Y5GGGGGGGPPGBBBGGPGBG5PGGGBBG5YPGPPGPPGGPY5PP5YJ?Y5JJYYYJ7YPGPJ7YPGG5YPGGGP5G57~!!~~~!!~
P...................:::........^?JYYYY5555555555J?!^:::::::::::...........          ...^^:^:..........:..........:^:::::...^?PGGGGBBGGGGBBBBGPGGGGPPPPGGGPY55Y5Y?JYYYJJJJ7YPPPJ7YPGPJJPGGG5YPY!~~~~^~~~~
#??JJJJJJJJJJ?JJJJ??YYJ??????777?YGBBBBBBBBBBBBBBBBG555J?????JJJJJJJJJJJJJJ??JJJJJJJJYYJ??????????JJJJJJJ?????????JJ??7777?7?YB####################BB#####BBBBBBGGBBBGGGGGBBBBGGB##BGG####BBBG55555Y555Y
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@