def egcd(a,b):
    if a == 0:
      return (b, 0, 1)
    else:
      g, y, x = egcd(b % a, a)
      return (g, x - (b // a) * y, y)
def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
      raise Exception('modular inverse does not exist')
    else:
      return x % m
p = 3487583947589437589237958723892346254777
q = 8767867843568934765983476584376578389
e = 65537
d = modinv(e, (p-1)*(q-1))
print d