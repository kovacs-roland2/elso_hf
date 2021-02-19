a, b, c, d = [i*i for i in range(1000,1,-1) if i % 11 == 0 and i % 3 != 0 and i % 2 != 0][:4]
print(a,b,c,d)