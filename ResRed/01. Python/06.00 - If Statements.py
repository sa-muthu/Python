# if = Do some code only IF some conditions is true
#      Else do something else

age = int(input("Enter your age: "))

#if age >= 18:
#   print("you are now signed up!")
#elif age >= 60:
#    print("You are too old...")
#else:
#    print("You must be 18+ and 60- to sign in") 
# output: you are now signed up! for 88, order matters 


if age >= 60:
    print("You are too old...")
elif age >= 18:
   print("you are now signed up!")
else:
    print("You must be 18+ and 60- to sign in") 