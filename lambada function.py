a =[1,3,100,50,20,7,9,5]
filtered = filter(lambda x:x%2,a)
print(list(filtered))

maped = map(lambda x:x%2,a)
print(list(maped))
