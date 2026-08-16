import requests


def fetch_random_user():
    url = 'https://randomuser.me/api/?nat=us&randomapi'
    response =  requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return data
    else:
        raise Exception("Failed to fetch user data!")



def main():
    try:
        data = fetch_random_user()
        gender = data["results"][0]["gender"]
        name = data["results"][0]["name"]["title"] + " " + data["results"][0]["name"]["first"] + " " + data["results"][0]["name"]["last"]
        print(gender, name, end="\n")
    except Exception as e:
        print(str(e))



if __name__ == "__main__":
    main()
