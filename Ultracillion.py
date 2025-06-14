import requests
import time
url= 'https://webbrowser11.github.io/Ultracillion/Ultracillion.txt'
response = requests.get(url)
text_content = response.text
print(text_content)
while True:
    time.sleep(1)