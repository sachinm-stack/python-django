import requests

url = "https://api.github.com/users/sachinm-stack"
data = requests.get(url).json()

name = data.get("name")
login = data.get("login")
followers = data.get("followers", 0)
public_repos = data.get("public_repos", 0)
location = data.get("location")

print("Name:", name)
print("Username:", login)
print("Followers:", followers)
print("Public Repos:", public_repos)

print("Conditions Are There :")
print("Popular User !") if followers > 10 else print("Keep going..!")
print("Active Contributor !") if public_repos > 5  else print("Just Geting Started..!")
print("location !",location) if location is not None else print("Location not set")

