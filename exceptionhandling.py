#exception handling------------->>>>>
try:
    print(a)
except:
    print("error") 
else:
    print("value")       
finally:
    print("yes")

#here we define the value--------->>>
x=10
try:
    print(x)
except:
    print("some error")

else:
    print("here the value")

finally:
    print("this block will be executed")    

#Raising an Exception--------------->>>>>
x=5
if x<0:
    print("value")
else:
    raise Exception("oops error")    
    
