def main():
    pass

if __name__ == '__main__':
    main()
import string
alpha_letters=[]
alpha_letters=string.ascii_letters
user_in=input()
print(user_in)
if(user_in in alpha_letters):
    print("Alphabet")
else:
    print("No")