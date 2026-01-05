import requests

def fetch_random_user():
    url="https://api.freeapi.app/api/v1/public/randomusers/user/random"
    response=requests.get(url)

    data =response.json()

    if data["success"] and "data" in data :
        user_data=data["data"]
        username=user_data["login"]["username"]
        country=user_data["location"]["country"]
        return username,country
    else:
        raise Exception ("Failed to fetch user_data")


def main():
    try:
       username,country= fetch_random_user()
       print(f"username : {username}\ncountry:{country}")
    except Exception as e:
        print(e)


if __name__=="__main__":
    main()


# import requests

# def fetch_random_user():
#     url = "https://api.freeapi.app/api/v1/public/randomusers?page=1&limit=10"
#     response = requests.get(url)
#     data = response.json()

#     if data.get("success") and "data" in data:

#         users = data["data"].get("data", [])

#         if not users:
#             raise Exception("No users returned from API")

#         # loop until we find a valid user
#         for user in users:
#             login = user.get("login")
#             location = user.get("location")

#             if login and location:
#                 username = login.get("username")
#                 country = location.get("country")

#                 if username and country:
#                     return username, country
        
#         raise Exception("No user record contained login + location")

#     else:
#         raise Exception("Failed to fetch user data")


# def main():
#     try:
#         username, country = fetch_random_user()
#         print(f"username : {username}\ncountry : {country}")
#     except Exception as e:
#         print(str(e))


# if __name__ == "__main__":
#     main()

    

