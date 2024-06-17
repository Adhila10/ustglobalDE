

arr = [2,3,2,3,5,6]

prime=[]
new=[]
for num in range(len(arr)):
    for i in range(2,num):
        if num%i == 0:
            print("hii")
            break
        else:
            prime.append(num)

print(prime)

for i in prime:
    if prime.count(i) > 1:
        new.append(i)

print(new)


print("hiiiiii")
print("welcomeeee")






