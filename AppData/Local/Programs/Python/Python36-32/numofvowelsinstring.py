s=input("enter string:")
count=0
for letter in s:
  if(letter=='a' or letter=='e' or letter=='i' or letter=='u' or letter=='o'):
      count=count+1
      print(count)
print('Number of vowels:',count)

