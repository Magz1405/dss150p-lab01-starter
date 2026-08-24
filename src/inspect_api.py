import json
from datetime import datetime, timezone
import requests
from pathlib import Path

API_URL = "https://jsonplaceholder.typicode.com/posts"

print(f"Sending GET request to: {API_URL}")

# 1 & 2. Send GET request with a 10-30 second timeout
response = requests.get(API_URL, timeout=20)

# 3. Check status code and fail clearly if unsuccessful
response.raise_for_status()

# 4. Print Content-Type header
print("Status Code:", response.status_code)
print("Content-Type:", response.headers.get("Content-Type"))

# 5. Parse the JSON response
payload = response.json()

# 6. Determine top-level structure (list or dict)
print("Top-level type:", type(payload).__name__)

# 7 & 8. Print number of records and a sample record
if isinstance(payload, list):
    print("Number of records:", len(payload))
    print("\n--- Sample Record ---")
    print(json.dumps(payload[0], indent=2) if len(payload) > 0 else "Empty List")
elif isinstance(payload, dict):
    print("Number of records (keys):", len(payload))
    print("\n--- Sample Record ---")
    # Grabs the first value from the dictionary to show as a sample
    sample = next(iter(payload.values())) if len(payload) > 0 else "Empty Dict"
    print(json.dumps(sample, indent=2))

# 9. Save the raw response exactly as received
# Setting up the path to your data folder
output_path = Path("data") / "api_snapshot.json"

with open(output_path, "w", encoding="utf-8") as f:
    json.dump(payload, f, indent=2, ensure_ascii=False)

print(f"\nData successfully saved to {output_path}")

# 10. Record the retrieval timestamp in UTC
retrieval_time = datetime.now(timezone.utc).isoformat()
print("\nretrieved_at_utc:", retrieval_time)