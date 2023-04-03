# list Comprehension------------->>>>>>
list1 = ["hello","hie","hola"]
newlist = []

for x in list1:
  if "e" in x:
    newlist.append(x)
print(newlist)
  



  #another optimize way
list1 = ["hello","hie","hola"]
newlist=[x for x in list1 if "o" in x ]#with condition
print(newlist)



list2 = ["red","green","yellow","black"]
newlist=[x for x in list2 if "black" in x ]#with conditions
print(newlist)



list3 = ["red","green","yellow","black"]
newlist=[x.upper() for x in list3 ]#in upper case
print(newlist)



list4 = ["red","green","yellow","black"]
newlist=[x.lower() for x in list4  ]#in lower case
print(newlist)



list5 = ["red","green","yellow","black"]
newlist=[x for x in list5 if x!="red"  ]#except red color shows all
print(newlist)



list6= ["hello","hie","hola"]
newlist=[x for x in list6 ]#without condition
print(newlist)
