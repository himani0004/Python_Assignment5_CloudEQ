#json parse converts json into python using json.loads()------->>>>
import json
x ='{"name":"himani","place":"himachal"}'
z = json.loads(x)
print(z["name"])
print(z["place"])
print(z)



# covert python to json using   json.dumps() -------------->>>>>>>>>>>
#different datatypes------------------------->>>>>>>>>
import json
x ={"name":"himani","place":"himachal"}  #dict
print(x)
y= json.dumps(("apple"))
print(y)


d=json.dumps(True) #boolean value
print(d)

e=json.dumps(False)#boolean value
print(e)


f=json.dumps(12) #int
print(e)


c=json.dumps(12.1)#float
print(c)

c=json.dumps(None)#null
print(c)

f=json.dumps(("hello","hi","bie"))#tuple
print(f)

h=json.dumps(["hello","hie","yes"])#list
print(h)


#using indent-------->>>>>> 
abc = {

    "name":"himani",
    "cource":"mca",
    "uni":"PU",   
    "place":"himachal",
    "gender":"f"   
}
print(abc)
ab =json.dumps(abc,indent=9)
print(ab)
