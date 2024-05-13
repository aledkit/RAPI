import requests

def get_puuid():
    # Read puuid from file
    with open('puuid.txt', 'r') as file:
        puuid = file.read().strip()

def set_puuid(puuid):
    # Write puuid to file
    with open('puuid.txt', 'w') as file:
        file.write(puuid)

#3clips3#8715



def puuid_from_username(username, tag):
    # Get puuid from username and tag
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 Edg/124.0.0.0",
        "Accept-Language": "en-US,en;q=0.9",
        "Accept-Charset": "application/x-www-form-urlencoded; charset=UTF-8",
        "Origin": "https://developer.riotgames.com",
        "X-Riot-Token":
    }
    response = requests.get(f'https://americas.api.riotgames.com/riot/account/v1/accounts/by-riot-id/{username}/{tag}', headers = headers)
    if response.status_code != 200:
        return response
    return response.json()['puuid']
print(puuid_from_username('3clips3', '8715'))