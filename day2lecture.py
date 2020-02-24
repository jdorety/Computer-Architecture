
"""
boolean bitwise operations

  OR
a = False
b = True

a || b == True

a = 1
b = 0
a | b == 1

  AND
a = False
b = True

a && b == False

a = 1
b = 0

a & b == 0

  NOT

!True == False
!False == True

~1 == 0
~0 == 1

  NOR

  XOR "there can only be one!"
a = True
b = True

a XOR b == False

c = False
d = False

c XOR d == False

e = True
f = False

e XOR f == True

1 ^ 0 == 1
1 ^ 1 == 0

   0b01110110
 ^ 0b10110101
-------------
   0b11000011

0b01100011
  AABCDDDD

shifting

0b 1100 >> 1
   0110 >> 1
   0011

0b01110110 >> 2
  0b011101

1100 << 1
11000

masking

"""