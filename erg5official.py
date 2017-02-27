#5
print "Arithmoi Harshad: "
for i in range(1001):
    xil=i/1000              #xiliades
    yp=i%1000
    ek=yp/100               #ekatontades
    yp=yp%100
    dek=yp/10               #dekades
    mon=yp%10               #monades
    #print xil,ek,dek,mon
    athr=xil+ek+dek+mon         #athroisma pshfiwn
    #print athr
    if athr!=0 and (i%athr)==0 :
        print i

print "Arithmoi poy diairountai apo to ginomeno twn pshfiwn tous:"
for i in range(1001):
    xil=i/1000              #xiliades
    yp=i%1000
    ek=yp/100               #ekatontades
    yp=yp%100
    dek=yp/10               #dekades
    mon=yp%10               #monades
    if i<10 :
        gin=mon
    elif i<100:
        gin=dek*mon
    elif i<1000:
        gin=ek*dek*mon
    else:
        gin=xil*ek*dek*mon



    if gin!=0 and i%gin==0:
            print i

raw_input("press 'enter' to exit: ")
