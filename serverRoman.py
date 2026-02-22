import socket
s = socket.socket()
s.bind(("127.0.0.1",4444))
s.listen(2)
while True:
    try:
        cs ,cd = s.accept()
        n = int(cs.recv(1024).decode())
        roman = ""

    except ValueError:
        print("Dont enter alnums and str ")
    else:
        if n<0:
            print("{} do not have any romen number".format(n))
        else:
            print("Clint Data at server --> ".format(n))
            while n>=1000:
                roman = roman +"M"
                n-=1000
            if n>=900:
                roman = roman + "CM"
                n -=900
            if n>=500:
                roman =roman+"D"
                n-=500
            if n>=400:
                roman = roman +"CD"
            while n>=100:
                roman = roman+"C"
                n-=100
            if n>=90:
                roman = roman+"XC"
                n -=90
            if n>=50:
                roman = roman +"L"
                n -=50
            if n>=40:
                roman = roman +"XL"
                n -=40
            while n>=10:
                roman = roman+"X"
                n -= 10
            if n>=9:
                roman = roman +"IX"
                n -=9
            if n>=5:
                roman = roman +"V"
                n -=5
            if n>=4:
                roman = roman +"IV"
                n -=4
            while n>=1:
                roman = roman +"I"
                n-=1
            cs.send(roman.encode())
            print("Roman send to clint success fully...")
