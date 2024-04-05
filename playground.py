print(ord("e") - ord("a"))
print(ord("a") - ord("a"))
print(ord("t") - ord("a"))

nums = [1, 1, 1, 2, 2, 3]
dicto = {5: 2, 3: 4}
freq = [0] * 5
freq = [[]] * (len(nums) +1) # creates the same list object in listcle
freq2 = [[] for i in range(len(nums)+ 1)] # creates dictinct list objects in list
val = range(len(nums) + 1)
print(freq)
print(freq2)
print(val)

for n, c in dicto.items():
    print(n, c)

 
values = set(range(0, 4))
print(values)
values.remove(0)
print(values)
arr = [1] * 2
print(arr)