[Database.py](./Database.py)

The Function UDF() adds [User Defined SQL Functions](https://docs.python.org/3/library/sqlite3.html#sqlite3.Connection.create_function)
to the Connection object

To add UD SQL Functions:
    define them before the 'UDF()' function call but only after the UDF() function definition
    Under the UDF() function add the function using the ConnectionObject.create_function method
    The link to documentation for said method is given above

