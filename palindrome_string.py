#to check whether the string is palindrome string or not
s=input("Enter the string")
s.upper()
b=s[-1::-1]
if s==b:
    print("Palindrome String ")
else:
    print("Not Palindrome String")