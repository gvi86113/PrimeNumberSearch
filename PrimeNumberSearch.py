Limit = int(input("Please set the upper limit for your list: "))

PrimeList = [2]

for i in range(2,Limit+1):
   for ele in PrimeList:
       if i % ele == 0:
           break
       if ele == PrimeList[-1]:
           PrimeList.append(i)

print(PrimeList)
print("The biggest prime number smaller than {} is {}".format(Limit, PrimeList[-1]))
