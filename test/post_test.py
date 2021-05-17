
import requests

end = "https://josiasaurel.tech"
req = requests.post(f"http://localhost:8000/shorten?url={end}")

result = req.content

print(result)
