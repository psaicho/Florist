import time
import requests
import zlib
import base64

new_timestamp = int(time.time())
challenge = "971ad26d6b70e736928780288af69fe9f6667d4da47b1ed2a9126bef542fe8fe"
new_url = f"https://task.zostansecurity.ninja/?step=1&challenge={challenge}&timestamp={new_timestamp}"

headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/png,image/svg+xml,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "pl,en-US;q=0.7,en;q=0.3",
    "Alt-Used": "task.zostansecurity.ninja",
    "Connection": "keep-alive",
    "Host": "task.zostansecurity.ninja",
    "Priority": "u=0, i",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "none",
    "Sec-Fetch-User": "?1",
    "TE": "trailers",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0"
}

response = requests.get(new_url, headers=headers)

print(f"Status code: {response.status_code}")
print("Response headers:")
for key, value in response.headers.items():
    print(f"{key}: {value}")



print(response)