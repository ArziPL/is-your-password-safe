# is-your-password-safe
***
### DESCRIPTION
Python script that send API request to haveibeenpwned, then locally check if your password is publicly available. Script hash your password, then send only first five hashed characters to haveibeenpwned. Site responds with all passwords that start with those five hash characters. Then script check locally list of hashed passwords with your and print result. Project heavily inspired by one of projects from "Complete Python Developer in 2021: Zero to Mastery" by Andrei Neagoie.

### HOW TO
Run `py main.py xxxxxxx` with xxxxxxx as password.

### LINKS
https://haveibeenpwned.com/  
https://www.udemy.com/course/complete-python-developer-zero-to-mastery/
***
