from datetime import datetime
import requests
import os

def generate_log(data):
    if type(data) != list:
        raise ValueError("It's not a list. Cannot work")

    else:
        filename = f"log_{datetime.now().strftime('%Y%m%d')}.txt"
        with open(filename, "w") as file:
            for entry in data:
                file.write(f"{entry}\n")
                print(f"Data saved to {filename}!")
        return filename
    
def fetch_data():
    response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
    if response.status_code == 200:
        return response.json()
    return{}

if __name__ == "__main__":
    post = fetch_data()
    print("Fetched Post Title:", post.get("title", "No title found"))