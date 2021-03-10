import requests
import hashlib
import sys

# py main.py [some password]

password = sys.argv[1]


def main(password):
    # Getting list of leaked passwords
    list_of_split_hash_count = []
    sha1password = hashlib.sha1(password.encode()).hexdigest().upper()
    long_string_of_leaked_passwords = get_leaked_passwords(
        sha1password[:5]).text
    list_of_leaked_passwords = long_string_of_leaked_passwords.splitlines()
    for item in list_of_leaked_passwords:
        list_of_split_hash_count.append(item.split(':'))

    # Checking if our password match anything on the list
    for hash_tail, count in list_of_split_hash_count:
        if(hash_tail == sha1password[5:]):
            print(
                f'Your password was leaked {count} times, you probably should change it :\ ')
            sys.exit()

    print('Your password wasn\'t breached :) ')


# Requesting all leaked passwords from API
def get_leaked_passwords(beginning_of_password):
    url = f'https://api.pwnedpasswords.com/range/{beginning_of_password}'
    response = requests.get(url)  # get response with all leaked passwords
    return response


main(password)
