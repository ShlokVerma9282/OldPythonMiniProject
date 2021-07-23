alphabet=("a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z,a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z")
alphabet_list=alphabet.split(",")
print(alphabet_list)
def encrypt(word,shift_number):
      chiper_text=""
      for letter in word:
          original_position=alphabet_list.index(letter)
          new_original_position=original_position+shift_number
          new_letter=alphabet_list[new_original_position]
          chiper_text+=new_letter
      print(f"The code is:{chiper_text}")
def decrypt(word,shift_number):
    chiper_text = ""
    for letter in word:
        original_position = alphabet_list.index(letter)
        new_original_position = original_position - shift_number
        new_letter = alphabet_list[new_original_position]
        chiper_text += new_letter
    print(f"The decoded word is:{chiper_text}")
loop=False
while not loop:
 shift_number=int(input("You want to shift alphabet by:\n"))
 word=input('The word is:\n').lower()
 first_input = int(input("Do you want encrypt(1) or decrypt(2):\n"))
 if first_input == 1:
    encrypt(word,shift_number)
    pok=str(input("Do you want to continue y or n\n").lower())
    if pok== "y":
        loop=False
    else:
        loop=True
        print("Thank You")
 elif first_input == 2:
     decrypt(word, shift_number)
     pok = input("Do you want to continue y or n\n")
     if pok == "y":
        loop = False
     else:
        loop = True
        print("Thank You")
