num=7
k=4
for i in range(7):
    for j in range(7):
        if(i==0 or j==0 or j==6 or i==6):
            print(k,end=" ")
        elif(i==1 or j==1 or j==5 or i==5):
            print(k-1,end=" ")
        elif (i==2 or j==2 or j==4 or i==4):
            print(k-2, end=" ")
        elif (i==3 or j==3 or j==3 or i==3):
            print(k-3, end=" ")
    print(" ")
