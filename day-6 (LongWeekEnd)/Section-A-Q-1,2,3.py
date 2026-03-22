# Save as: section_a.py

# #1:Answer the following questions in your own words (write as Python comments in your file): (a) What is a domain name and why do
# we need it instead of just using IP addresses? (b) Explain the DNS resolution process step by step — what happens from the
# moment you type google.com to the moment the page loads. (c) What is the IP address 8.8.8.8? What is 1.1.1.1? What type of
# servers are these? (d) If your internet stops working, how can you check and fix the DNS? Which command shows your network
# info? (e) What is the difference between HTTP and HTTPS?





# (a) Domain name explanation:
# A domain name is a human-readable address of a website (like google.com).
# We use domain names instead of IP addresses because IPs are hard to remember,
# while domain names are easy for humans to understand and use.

# (b) DNS resolution steps:
# Step 1:
# You type "google.com" in the browser and press enter.

# Step 2:
# The browser checks cache (browser cache, OS cache, router cache)
# to see if the IP address is already known.

# Step 3:
# If not found, the request goes to a DNS resolver (ISP or public DNS like 8.8.8.8).

# Step 4:
# The resolver contacts root server → TLD server (.com) → authoritative server,
# gets the IP address, returns it to the browser, and the browser loads the website.

# (c) 8.8.8.8 is: Google Public DNS server
#     1.1.1.1 is: Cloudflare Public DNS server

# (d) Command to check DNS: ipconfig (Windows) / ifconfig or ip a (Linux)
# Fix: Change DNS settings to a public DNS (like 8.8.8.8 or 1.1.1.1) and flush DNS cache

# (e) HTTP vs HTTPS:
# HTTP (HyperText Transfer Protocol) is not secure and data is sent in plain text.
# HTTPS (HyperText Transfer Protocol Secure) encrypts data using SSL/TLS,
# making communication secure between browser and server.







# #2:Complete the table by filling in the missing descriptions. Then write a Python comment explaining a real-world example for each
# HTTP method (e.g. GET = loading your Twitter feed).


# HTTP Method | Purpose | Your real-world example
# -------------|-----------------------------|--------------------------
# GET | Retrieve data from server | Loading your Instagram feed
# POST | Send new data to server | Creating a new account / posting a tweet
# PUT | Update existing data completely | Editing your profile details
# DELETE | Remove data from server | Deleting a post or account


# Status Code | Meaning
# -------------|--------------------------------
# 200 | Request successful (everything worked)
# 404 | Resource not found (wrong URL or missing page)
# 500 | Internal server error (problem on server side)
# 401 | Unauthorized (authentication required or failed)


# What is a Request Body? Give an example in JSON format:
# A request body is the data sent from the client to the server.
# Example:
# {
#   "username": "sachin",
#   "password": "123456"
# }


# What is a Response Body? Give an example:
# A response body is the data sent back from the server to the client.
# Example:
# {
#   "status": "success",
#   "message": "Login successful",
#   "token": "abc123xyz"
# }






# Q3. API Call — GitHub Profile

# Using the requests library, call the GitHub API for YOUR username. Extract and print the following 6 fields in a clean formatted
# output. Use .get() with default values so your code never crashes even if a field is missing.



import requests

url = "https://api.github.com/users/sachinm-stack"
data = requests.get(url).json()

name = data.get("name")
login = data.get("login")
followers = data.get("followers", 0)
public_repos = data.get("public_repos", 0)
location = data.get("location")
bio=data.get("Bio")

print("Name:", name)
print("Username:", login)
print("Followers:", followers)
print("Public Repos:", public_repos)
print("bio",bio)

print("Conditions Are There :")
print("Popular User !") if followers > 10 else print("Keep going..!")
print("Active Contributor !") if public_repos > 5  else print("Just Geting Started..!")

