import requests
import browsercookie

# Load cookies from Chrome
cj = browsercookie.chrome()

# Use the loaded cookies with a requests session
session = requests.Session()
session.cookies = cj

# Make a request with the loaded cookies
url = 'https://google.com'
response = session.get(url)

print(f"Status Code: {response.status_code}")
print("Cookies used in the request:")
for cookie in response.request._cookies:
    print(f"  {cookie.name}: {cookie.value}")

print("\nCookies received in the response:")
for cookie in response.cookies:
    print(f"  {cookie.name}: {cookie.value}")