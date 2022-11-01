Kiosk.py contains an execution function that will ensure no two functions can use the connection at the same time.

Firstly, we start by defining the following functions:

IdGenerator-Generates a random ID 
IdValidator-Validates that random ID to check that nothing else is using the DB
MainExecutor-Executes the Queries
SendQuery-This is the function thats actually accessed
CurrentlyServing-Returns token no that is currently being served


SendQuery issues a 'Token' using IdGenerator and IdValidator
Keeping Track of the Token is the responsibility of the Caller
You find out where you are in the line and accordingly check again after sometime if the result exists
If it is, then get the result and leave.

Other not that important functions:
FetchData-returns None if data is not ready
CancelRequest

Notes for implementing this:
Use a whileloop to keep checking if your result is accessible in the FetchData function



ID of projects,sections,labels etc are all stored as integers

Each of them have a parentid attribute which links to the ID of the parent of the said object.
This way we can quickly arrange it into a tree datastructure with nodes, and operate using that.

Alternatively all objects also can have a relative ID thats stored as TEXT.
The structure of the relative ID is as follows

Relative IDs starting with 0's are reserved for template objects

├───Project1    [100001 ] (relative ID)
│   ├───Task1   [100001 151341] (this inherits the relative ID of its parent)
│   │   └───Task2(subtask) [100001 151341 846594]
│   ├───Task7
│   │   ├───Task10
│   │   ├───Task8 (subtask)
│   │   │   └───Task4     (sub-subtask) 
│   │   └───Task9
│   ├───Section1
│   │   └───Task3
│   └───Task6
└───Project2

Basically, i'm asking for a huffman tree.
RelativeIDs are not currently going to be implemented because they don't serve a purpose that you can't accomplish using the regular IDs

The List of all Tables and their Attributes are in "Initialize.py"
