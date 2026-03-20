inventory={"apples":50,"banana":30,"orange":20}
print(inventory)
inventory["Mangoes"]=44
print(inventory)
inventory.update({"apples":60})
print(inventory)
inventory.pop("banana")
print(inventory)
if "grapes" is inventory :
    print("true")
else:
    print("fAlse")
# print(inventory.__len__)
print(len(inventory))
print(inventory.items())



