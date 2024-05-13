import requests
import const
import os
from datetime import datetime

debug = False

def fetch_account():
    log("Fetching account data")
    get_puuid()
    

def main():
    log(f"Logged in at {datetime.now()} with puuid {get_puuid()}")

def log(message):
    with open('log.txt', 'a') as file:
        file.write(f"{datetime.now()} | {message} \n")

def get_puuid():
    if os.path.getsize('puuid.txt') == 0:
        return None
    # Read puuid from file
    with open('puuid.txt', 'r') as file:
        puuid = file.read().strip()
   
    return puuid

def set_puuid(puuid):
    # Write puuid to file
    with open('puuid.txt', 'w') as file:
        file.write(puuid)

def puuid_from_username(username, tag):
# Get puuid from username and tag
    # get headers from const.py        
    headers = const.headers
    
    # get puuid from username and tag
    response = requests.get(f'https://americas.api.riotgames.com/riot/account/v1/accounts/by-riot-id/{username}/{tag}', headers = headers)
    
    # handle error codes
    if response.status_code != 200:
        return response
    
    # return puuid
    return response.json()['puuid']

#Test Case
def test_case():
    print(puuid_from_username(const.testUser, const.testTag))

if __name__ == "__main__":
    #make sure puuid.txt exists
    if not os.path.exists('puuid.txt'):
        with open('puuid.txt', 'w') as file:
            pass

    #run test case if debug is true
    if debug:
       test_case()
    
    #normal boot
    else:
        #Check for puuid
        if get_puuid() is None:
            username = input("Enter your username: ")
            tag = input("Enter your tag: ")
            set_puuid(puuid_from_username(username, tag))
            log(f"Set puuid to {get_puuid()}")
        else:
            log(f"PUUID already set to {get_puuid()}")
        main()