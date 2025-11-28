import requests

def fetch_and_display_users(num_users):
    url = "https://jsonplaceholder.typicode.com/users"
    try:
        response = requests.get(url, timeout=5)
        if response.status_code != 200:
            print("Error: Got HTTP", response.status_code)
            return None
        users = response.json()
    except Exception as e:
        print("Error fetching or parsing users:", e)
        return None

    if not isinstance(users, list):
        print("Error: Unexpected data format")
        return None

    for user in users[:num_users]:
        name = user.get("name")
        email = user.get("email")
        city = None
        if isinstance(user.get("address"), dict):
            city = user["address"].get("city")

        print("Name:", name)
        print("Email:", email)
        print("City:", city)
        print("---")



