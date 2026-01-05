import requests


# ------------------ USER INFO ------------------
def get_user_info():
    print("\n=== User Information Lookup ===\n")

    user_id = input("Enter user ID (1-10): ").strip()

    if not user_id.isdigit():
        print("❌ User ID must be numeric.")
        return

    user_id = int(user_id)

    if user_id < 1 or user_id > 10:
        print("❌ User ID must be between 1 and 10.")
        return

    url = f"https://jsonplaceholder.typicode.com/users/{user_id}"

    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print("❌ Failed to fetch user:", e)
        return

    data = response.json()

    print(f"\n--- User #{user_id} Info ---")
    print(f"Name   : {data['name']}")
    print(f"Email  : {data['email']}")
    print(f"Phone  : {data['phone']}")
    print(f"Website: {data['website']}")


# ------------------ POSTS BY USER ------------------
def search_posts():
    print("\n=== Post Search ===\n")

    user_id = input("Enter user ID (1-10): ").strip()

    if not user_id.isdigit():
        print("❌ User ID must be numeric.")
        return

    user_id = int(user_id)

    if user_id < 1 or user_id > 10:
        print("❌ User ID must be between 1 and 10.")
        return

    url = "https://jsonplaceholder.typicode.com/posts"
    params = {"userId": user_id}

    try:
        response = requests.get(url, params=params, timeout=5)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print("❌ Failed to fetch posts:", e)
        return

    posts = response.json()

    if not posts:
        print("No posts found.")
        return

    print(f"\n--- Posts by User #{user_id} ---")
    for i, post in enumerate(posts, 1):
        print(f"{i}. {post['title']}")


# ------------------ CRYPTO PRICE ------------------
def get_crypto_price():
    print("\n=== Cryptocurrency Price Checker ===\n")
    print("Available coins: btc-bitcoin, eth-ethereum, doge-dogecoin")

    coin_id = input("Enter coin ID: ").strip().lower()

    if not coin_id:
        print("❌ Coin ID cannot be empty.")
        return

    url = f"https://api.coinpaprika.com/v1/tickers/{coin_id}"

    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
    except requests.exceptions.RequestException:
        print("❌ Coin not found or API error.")
        return

    data = response.json()

    price = data["quotes"]["USD"]["price"]
    change = data["quotes"]["USD"]["percent_change_24h"]

    print(f"\n--- {data['name']} ({data['symbol']}) ---")
    print(f"Price       : ${price:,.2f}")
    print(f"24h Change  : {change:+.2f}%")


# ------------------ COMMENTS FROM POST ------------------
def get_comments_from_post():
    print("\n=== Comments from a Post ===\n")

    post_id = input("Enter post ID (1-10): ").strip()

    if not post_id.isdigit():
        print("❌ Post ID must be numeric.")
        return

    post_id = int(post_id)

    if post_id < 1 or post_id > 10:
        print("❌ Post ID must be between 1 and 10.")
        return

    url = "https://jsonplaceholder.typicode.com/comments"
    params = {"postId": post_id}

    try:
        response = requests.get(url, params=params, timeout=5)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print("❌ Failed to fetch comments:", e)
        return

    comments = response.json()

    if not comments:
        print("No comments found.")
        return

    print(f"\n--- Comments for Post #{post_id} ---")
    for i, comment in enumerate(comments, 1):
        print(f"\nComment {i}")
        print(f"Name : {comment['name']}")
        print(f"Email: {comment['email']}")
        print(f"Body : {comment['body']}")


# ------------------ WEATHER BY CITY ------------------
def get_weather_by_city():
    print("\n=== Weather Information ===\n")

    city = input("Enter city name: ").strip()

    if not city:
        print("❌ City name cannot be empty.")
        return

    geo_url = "https://geocoding-api.open-meteo.com/v1/search"
    geo_params = {"name": city, "count": 1}

    try:
        geo_response = requests.get(geo_url, params=geo_params, timeout=5)
        geo_response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print("❌ Failed to fetch city location:", e)
        return

    geo_data = geo_response.json()

    if "results" not in geo_data:
        print("❌ City not found.")
        return

    lat = geo_data["results"][0]["latitude"]
    lon = geo_data["results"][0]["longitude"]

    weather_url = "https://api.open-meteo.com/v1/forecast"
    weather_params = {
        "latitude": lat,
        "longitude": lon,
        "current_weather": "true"
    }

    try:
        weather_response = requests.get(weather_url, params=weather_params, timeout=5)
        weather_response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print("❌ Failed to fetch weather:", e)
        return

    weather = weather_response.json()["current_weather"]

    print(f"\n--- Weather in {city.title()} ---")
    print(f"Temperature : {weather['temperature']}°C")
    print(f"Wind Speed  : {weather['windspeed']} km/h")


# ------------------ TODOS BY STATUS ------------------
def search_todos_by_status():
    print("\n=== TODO Search ===\n")

    status = input("Enter status (true / false): ").strip().lower()

    if status not in ["true", "false"]:
        print("❌ Status must be 'true' or 'false'")
        return

    url = "https://jsonplaceholder.typicode.com/todos"
    params = {"completed": status}

    try:
        response = requests.get(url, params=params, timeout=5)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print("❌ Failed to fetch todos:", e)
        return

    todos = response.json()

    print(f"\n--- Todos (Completed = {status}) ---")
    for i, todo in enumerate(todos[:10], 1):
        print(f"{i}. {todo['title']}")


# ------------------ MAIN MENU ------------------
def main():
    print("=" * 40)
    print("  Dynamic API Query Demo")
    print("=" * 40)

    while True:
        print("\nChoose an option:")
        print("1. Look up user info")
        print("2. Search posts by user")
        print("3. Check crypto price")
        print("4. Get comments from a post")
        print("5. Get weather by city")
        print("6. Search todos by status")
        print("7. Exit")

        choice = input("\nEnter choice (1-7): ").strip()

        if choice == "1":
            get_user_info()
        elif choice == "2":
            search_posts()
        elif choice == "3":
            get_crypto_price()
        elif choice == "4":
            get_comments_from_post()
        elif choice == "5":
            get_weather_by_city()
        elif choice == "6":
            search_todos_by_status()
        elif choice == "7":
            print("\nGoodbye!")
            break
        else:
            print("❌ Invalid choice. Try again.")


if __name__ == "__main__":
    main()
