#Below are notes on files:

'''
Reading and Writing Files
Suppose you have a file called:
notes.txt
Inside it:
Hello!
This is my first file.
To read it:
with open("notes.txt", "r") as file:
    contents = file.read()

print(contents)
Output:
Hello!
This is my first file.
What does "r" mean?
It tells Python how to open the file.
Mode	Meaning
"r"	Read
"w"	Write (overwrites existing contents)
"a"	Append (adds to the end)
Writing a file
with open("notes.txt", "w") as file:
    file.write("Hello from Python!")
If notes.txt already exists, its previous contents will be replaced.
Appending
with open("notes.txt", "a") as file:
    file.write("\nAnother line")
Now the new text is added instead of replacing everything.

With alwasys closes file for you, make sure to use
'''

#Below are notes on JSON:
'''
JSON stands for JavaScript Object Notation, but don't let the name fool you—it's used by many programming languages, including Python.
It's one of the most common ways to store structured data.
A JSON file might look like this:
{
    "username": "admin",
    "password": "1234",
    "active": true
}
Notice:
Keys are in double quotes.
true/false are lowercase in JSON.
It looks very similar to a Python dictionary.


Loading JSON
First, import the built-in module:
import json
Then:
with open("user.json", "r") as file:
    user = json.load(file)

print(user["username"])
If user.json contains:
{
    "username": "admin",
    "password": "1234"
}
Output:
admin
After json.load(), user is just a normal Python dictionary.


Saving JSON
Suppose you have:
user = {
    "username": "admin",
    "password": "1234"
}
Save it like this:
with open("user.json", "w") as file:
    json.dump(user, file)
Now you have a JSON file on disk.


Making JSON prettier
By default:
{"username":"admin","password":"1234"}
To make it easier to read:
json.dump(user, file, indent=4)
Result:
{
    "username": "admin",
    "password": "1234"
}
You'll use indent=4 all the time.
'''