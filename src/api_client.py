
import requests

# 1. Store the API endpoint
API_URL = "https://jsonplaceholder.typicode.com/posts"

# 2. Send a GET request with a 10-second timeout
response = requests.get(API_URL, timeout=10)

# 3. Print the HTTP status code
print("Status Code:", response.status_code)

# 4. Convert JSON response into Python data
data = response.json()

# 5. Print the total number of records
print("Total Records:", len(data))

# 6. Print the first record
print("First Record:", data[0])
