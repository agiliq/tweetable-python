n=int(input('Enter number of terms: '))
x=[0,1]
[x.append(x[-2]+x[-1]) for _ in range(n-2)]
print(x)
