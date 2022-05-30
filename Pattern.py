n=int(input("Enter The Limit: "))
for i in range(0,n,1):
    for j in range(0,i+1,1):
        print("*",end='')
    print("\n")
for k in range(0,n,1):
    for l in range(k,n-1,1):
        print("*",end='')
    print("\n")


