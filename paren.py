#2
s1=0
s2=0
checked=False
user= raw_input("Eisagete ta stoixeia: ")
list(user)
pl=len(user)
cop=user.count('(')
ccl=user.count(')')
if pl%2==0:
    checked=True
    for i in range(0,(pl-1)):
        if user[i]=='(':
            s1+=1
        else:
            s2+=1
        if s1<s2:
            checked=False
            break
    print checked
else:
    print checked

raw_input("press enter to exit: ")
