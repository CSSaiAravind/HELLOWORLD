nrows = int(input('Enter the No. of Rows to Print : '))

sp = 2 * nrows - 2

i = 1

while(i <= nrows):  # print spaces for pyramid

    	j = 1
    	while(j <= sp):  
              print(end=' ')
              j = j + 1

    	ln=1
    	while(ln <= i):  
              print(ln,'', end='')
              ln = ln + 1
              rn = i-1
        
while(rn >= 1):  
              print(rn, '', end='')
              rn = rn - 1
              sp = sp - 2
              i = i + 1
print("\r")


