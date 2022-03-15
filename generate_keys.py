from random import randint
from soe import gen_primes


###########################
#
#     PART I
#
#     KEY PAIR GENERATION
#
#     
###########################


#  low: the 'load size';
#  This algorithm can only encrypt numbers that are smaller then low.
low  =  10000000
high = 10 * low

#
# 1. Generate primes
# 

# nop: the number of primes we need
nop = 5
gen = gen_primes()

def generate_prime(start):
    for i in gen:
        if i > start:
            break
    return i

p = generate_prime(1000)
print(p)

l = []

for i in range(nop):
    l.append(randint(low,high))

l.sort()

print(l)

p = []
for i in l:
   p.append(generate_prime(i))

print("The primes:")
for i in p:
    print("  {}".format(i))

#
# 2. Generate the private key
#
primary = p[0]

#
# 3. Generate the public key
#

# Actually, it consists of a pair, generated using:
# - two prime products ab and ac
# - and 4 random ints i1, j1, i2 and j2
# - and 2 more prime numbers d1 and d2

n = []
for i in range(4):
    n.append(randint(low, high))

a = p[0]
b = p[1]
c = p[2]
d1 = p[3]
d2 = p[4]

i1 = n[0]
j1 = n[1]
i2 = n[2]
j2 = n[3]

ab = a*b
ac = a*c
pub1 = (i1*ab + j1*ac)*d1
pub2 = (i2*ab + j2*ac)*d2

print("The key pair:")
print("  {}".format(primary))
print("  {}".format(pub1))
print("  {}".format(pub2))


###########################
#
#     PART II
#
#     EXAMPLE USE
#
#     
###########################

number = 1234

print("Two random numbers and one prime:")
a = randint(low,high)
b = randint(low,high)
c = generate_prime(randint(low,high))

print("  {}".format(a))
print("  {}".format(b))
print("  {}".format(c))

print("The number to be encrypted:")
print(number)

hash = (a*pub1 + b*pub2)*c
print("Hash:")
print("  {}".format(hash))

encrypted = hash+number
print("The encrypted number:")
print(encrypted)

(a, decrypted) = divmod(encrypted, primary)

print("The decrypted number:")
print(decrypted)
