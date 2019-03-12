#codebysuji
x=100
while True:
 
  x=x-1
  if x==0:
   break

  elif x%5==0 and x%3==0:
   print ("BuzzFizz")

  elif x%5==0:
   print("Buzz")

  elif x%3==0:
   print("Fizz")

  else:
   print(x)

 
   
