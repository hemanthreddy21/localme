s=input("Enter string:")
count=0

for x in range(len(s)-2):
    if(s[x]=='b'):
        if(s[x+1]=='o'):
            if(s[x+2]=='b'):
                count=count+1
print(count)
                
