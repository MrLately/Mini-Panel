import base64

# Set the email and password for your account
with open("credentials.txt", 'r') as f:
    email = f.readline().strip()
    password = f.readline().strip()

# Encode the email and password in base64 and set the value of the authorization header
credentials = f'{email}:{password}'
b64_credentials = base64.b64encode(credentials.encode()).decode()
headers = {
    'Host': 'api-v1.serverpoint.com',
    'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Microsoft Edge";v="108"',
    'accept': 'application/json, text/plain, */*',
    'sec-ch-ua-mobile': '?0',
    'authorization': f'Basic {b64_credentials}',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.46',
    'sec-ch-ua-platform': '"Windows"',
    'origin': 'https://portal.serverpoint.com',
    'sec-fetch-site': 'same-site',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://portal.serverpoint.com/',
    'accept-language': 'en-US,en;q=0.9',
}