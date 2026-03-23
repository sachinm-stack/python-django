# import requests
# url="https://api.github.com/users/abdulmanaf6361"
# response=requests.get(url)
# print(response.status_code,"\n")
# # print(response.json(),"\n")
# # print(type(response.json()),"\n")
# # data =response.json()
# # print("name"+":"+data["name"])
# # print("resositories")
# respose_dict = response.json()
# id=respose_dict["id"]
# print("id"+":"+str(id))
# type=respose_dict["type"]
# print("type"+":"+type)
# company=respose_dict["company"]
# print("company"+":"+str(company))
# location=respose_dict["location"]
# print("location"+":"+str(location))
# twitter_username=respose_dict["twitter_username"]
# print("twitter_username"+":"+str(twitter_username))



# import requests

# url = "https://api.github.com/users/abdulmanaf6361"
# response = requests.get(url)

# data = response.json()

# for key, value in data.items():
#     print(key + " : " + str(value))


import requests

url = "https://api.github.com/users/abdulmanaf6361"
response = requests.get(url)

data = response.json()

print(data)

