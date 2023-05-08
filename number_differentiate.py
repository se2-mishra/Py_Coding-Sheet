import math
num=int(input('Enter a number:'))
for i in range(int(math.ceil(math.log10(num)+1))):
    num,remainder=divmod(num,10)
    print(remainder)