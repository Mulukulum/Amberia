Incase we run into errors and issues with SQLite not being able to handle multiple functions using the DB at once
then I should probably look into implementing this


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

Incase we run into errors and issues with SQLite not being able to handle multiple functions using the DB at once
then I should probably look into implementing this

Handler.py contains an execution function that will ensure no two functions can use the connection at the same time.
This is not suitable for use with multiprocessing, however asyncio and threading should handle this just fine
As long as the same object is used to verify that nothing is using the database it should be just fine.

Firstly, we start by defining the following functions:

IdGenerator-Generates an ID
MainExecutor-Executes the Queries
SendQuery-This is the function thats actually accessed
CurrentlyServing-Returns token no that is currently being served

SendQuery issues a 'Token' using IdGenerator and IdValidator
Keeping Track of the Token is the responsibility of the Caller
You find out where you are in the line and accordingly check again after sometime if the result exists
If it is, then get the result and leave.

Other not that important functions:
FetchDataState-Gets the state of the result
GetResult-Gets the result (DOES NOT CHECK Wheter the data exists or not)
CancelRequest-Self Explanatory

Notes for implementing this:
Use a whileloop to keep checking if your result is accessible in the FetchDataState function.
Implement a sleep timer of around 0.2 Seconds between each check.
If it is, then getting the result will automatically clean up your request.