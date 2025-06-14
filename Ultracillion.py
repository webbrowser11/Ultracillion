# I hate this shit so chatgpt helped me
import requests
from tqdm import tqdm
import time

url = 'https://webbrowser11.github.io/Ultracillion/Ultracillion.txt'

head = requests.head(url)
total_size = int(head.headers.get('Content-Length', 0))

chunk_size = 1000
start = 0

print(f"Total file size: {total_size} bytes (~{total_size/1e6:.2f} MB)")

# Buffer to hold the entire text while downloading
buffer = []

with tqdm(total=total_size, unit='B', unit_scale=True, desc='Downloading') as pbar:
    while start < total_size:
        end = min(start + chunk_size - 1, total_size - 1)
        headers = {'Range': f'bytes={start}-{end}', 'Accept-Encoding': 'identity'}

        r = requests.get(url, headers=headers)
        if r.status_code not in (200, 206):
            print(f"Stopped: unexpected status code {r.status_code}")
            break

        buffer.append(r.text)  # collect chunk silently
        pbar.update(len(r.content))

        start += chunk_size
        time.sleep(0.05)

print("\n\n✅ Download complete! Printing output now...\n")

# Print the full file after progress bar finished
print(''.join(buffer))
