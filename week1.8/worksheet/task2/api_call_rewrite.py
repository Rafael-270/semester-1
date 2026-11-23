import httpx

base_url = "https://dummyjson.com/"
endpoint = "products/search"
url = base_url + endpoint

# Pass the search query cleanly using params
response = httpx.get(url, params={"q": "apple"})

print(response.status_code)
data = response.json()
print(data)
