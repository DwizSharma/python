cars2=["maruti","audi","verna"]
cars2.sort()
print(cars2)
cars2.clear()
print(cars2)

#tupple[]- a collection ,ordered ,unchangable ,allows duplicates
tupl=(10,5,6,'a','d',False)
print(len(tupl))
tup2=tuple((10,20,30,40))
print(tup2)
print(100 in tup2)
list22=list(tup2)
print(list22,type(list22))
list22.insert(2,25)
print(list22,type(list22))
tup2_new=tupl(list22)
print(tup2_new,type(tup2_new))

