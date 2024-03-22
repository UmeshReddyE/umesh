import re
def solve(s):
    pat="^[A-Z]+[0-9]+[a-zA-Z0-9$#@!%^&*~,.?/]+@[gmail,Hotmail,yahoo.rediff]+.com"
    if(re.match(pat,s)):
        print("valid")
    else:
        print("invalid")
s=input()
print(solve(s))
