# 4
contin="y"
while contin=="y" or contin=="Y" :
    try:
            pl=int(raw_input("Plithos timwn: "))
            lista=[]
            print "Eisagete times: "

            for i in range(pl):
                    lista.insert(i,float(raw_input()))
            #        print lista

            lista.sort()
            #print lista      taksinomimenh
            count=int(0)
            for i in range(1,(pl-1)):
                count=count+ lista[i]
            #print count
            mo=float(count/(pl-2))
            #print mo
            s2=float(0)
            for i in range(1,(pl-1)):
                s2=s2+((lista[i]-mo)**2/(pl-2))
            #print s2      diakymansh
            import math
            s=math.sqrt(s2)
            print  "Typikh apoklish (xwris tis max kai min times): ", s
            contin=raw_input("press 'y' to try again or 'enter' to exit: ")

    except ValueError:
            print "Invalid Input"
            contin="n"
            contin=raw_input("press 'y' to try again or 'enter' to exit: ")
