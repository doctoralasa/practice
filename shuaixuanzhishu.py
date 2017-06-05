n=1000
filter(lambda x: all(map(lambda p: x % p != 0, range(2, x))), range(2, n))
print 
