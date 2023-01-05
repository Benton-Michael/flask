
Build a flask application that counts the number of times the root route ('/') has been viewed. 

This assignment is to test your understanding of session.

As part of this assignment, please start with the following features first:

localhost:5000 - have the template render the number of times the client has visited this site

localhost:5000/destroy_session - 

Clear the session. Once cleared, redirect to the root.

Some Helpful Tips
We can't increment something that doesn't exist! Here's how to check if a key exists in session yet:

if 'key_name' in session:
    print('key exists!')
else:
    print("key 'key_name' does NOT exist")

If we want to get rid of what is currently stored in session:

session.clear()		# clears all keys
session.pop('key_name')		# clears a specific key



# Session Notes

- python3
- import base64
- base64.urlsafe_b64decode('eyJjb3VudCI6OX0')
- eyJjb3VudCI6OX0 

