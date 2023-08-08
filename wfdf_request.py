import requests

data = {
    'query': 'What is the rule for hand fouls in Ultimate Frisbee?'
}

response = requests.post('https://cca7-34-86-206-243.ngrok-free.app/ask', json=data)

if response.status_code == 200:
    print('Response from the server:')
    print(response.json())
else:
    print(f'Request failed with status code {response.status_code}')