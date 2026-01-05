## iteratio tools 
## for , compehension 

## iteratable object 
## list ,file,tuple,range,

## __next__
## jaise hi koi iteratble object pr hum koi iteratble tool use krte hai to hume next me uske current address ke next ka address milta hai 

## iter() -> ye imp hai file ke andar khud ka iter tool hota hai list ya tuple etc me nhi hota 

## ye jo list iterator hota hai vo strting memory address pr hi point krte hai but uske andar next hota hai jo next krta hai (important for interview)

## f=open('chai.py')
## iter(f) is f (iska output true hoga)

## file open krne ke baad ya to f.readline() karoge to apne ap stopIteration error handle hoga jabki agar ap .__next__() karoge to ye error handle nhi hoga 

