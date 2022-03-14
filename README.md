# ASAEA - A Simple Anonymous Encryption Algorithm

Take 5 primes P1...P5 and 4 random integers I1...I2, all different and greater then MAX.

Let the private key be P1:

```
P = P1
```


Let two internediate keys K1 and K2 be:

```
K1 = P.P2
K2 = P.P3
```


Let the public keys PUB1 and PUB2 be:

```
PUB1 = (I1.K1 + I2.K2).P4
PUB2 = (I3.K1 + I4.K2).P5
```


# Encrypt

Let the secret be S, an integer smaller then MAX.

Let it be encrypted as follows:

Take one prime P6 and two random integers I3 and I4, all different and greater then MAX.

Let HASH be:

```
HASH = (I3.PUB1 + I4.PUB2).P6
```


Encrypt S by adding it to the hash:

```
E = HASH + S
```


# Decrypt

Decrypt it by integer divide the E with P and calculate the remainder:

```
S = E modulo P
```


# Proof

```
E modulo P = S + (I3.PUB1 + I4.PUB2).P6 modulo P
            = S + (I3.((I1.K1 + I2.K2).P4) + I4.((I3.K1 + I4.K2).P5)).P6 modulo P
            = S + (I3.((I1.P.P2 + I2.P.P3).P4) + I4.((I3.P.P2 + I4.P.P3).P5)).P6 modulo P
            = S + (I3.((I1.P2 + I2.P3).P4).P + I4.((I3.P2 + I4.P.P3).P5).P).P6 modulo P
            = S + (I3.((I1.P2 + I2.P3).P4) + I4.((I3.P2 + I4.P.P3).P5)).P6.P modulo P
            = S
```
