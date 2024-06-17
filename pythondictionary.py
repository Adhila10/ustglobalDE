

my_stocks={"TCS":2000,"Infosys":5000,"UST":890}
# print(type(my_stocks))

my_stocks["SBI"]=1700

print("Price of infosys is ", my_stocks["Infosys"])

# if we added another tcs that is same key value the latest one will be there, no duplicates in keys

print(my_stocks)
print(len(my_stocks))

# my_stocks.clear()   it will clear the dictionary

print("values", my_stocks.values())

print(my_stocks.keys())

for stock in my_stocks:
    print(stock,"has price" , my_stocks[stock])

for stock in my_stocks.items():
    print(my_stocks)
    print(stock[0])

print(my_stocks.items())

print(my_stocks.pop("TCS"))
print(my_stocks.popitem())
# popitem removes last item and pop requires a value and the key will be removed.value is printed if we print that..value will be there.

# update in dictionary
print("=========")

#


# swapping the values and keys

swapped={}
for key,value in my_stocks.items():
    swapped[value]=key
print(swapped)