# is-your-password-safe
***
### Description
Python script that send API request to haveibeenpwned, then LOCALLY check if your password is publicly available. Script hash your password, then send only first five hashed characters to haveibeenpwned. Site responds with all passwords that start with those five hash characters. Then script check locally list of hashed passwords with your and print result.

### How to
Run py main.py with password as argument. Then you get info how many times your password was leaked.  
py main.py qwerty

### Rest
Project heavily inspired by one of projects from "Complete Python Developer" on Udemy by Andrei Neagoie.

### Technologies
Python

### Links
https://haveibeenpwned.com/  
https://www.udemy.com/course/complete-python-developer-zero-to-mastery/
***
### Informations
> Author : ArziPL  
> License : MIT  
> Last update : 10.03.2021  
> Status : Finished  
