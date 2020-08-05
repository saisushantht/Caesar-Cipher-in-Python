# Caesar-Cipher-in-Python
Caesar cipher is the encryption technique, in which we have to replace each letter in the text by a some other letter at a fixed difference. 

## Example :-
  # Plaintext:  Sushanth
  # Ciphertext: Vxvkdqwk
  Key = 3
  Hence here the letters in the plaintext are moved forward to 3 letters in order as Key==3.
  Therefore, S is replacced with V and u with x so oo=n .....
  
# Concept of Caesar cipher encryption :-
   c = (x + n) mod 26
   where, c is place value of encrypted letter,x is place value of actual letter,n is the number that shows us how many positions of letters we have to replace.
   
   Therefore for S the equation would be like chr((ord('S') + 3) mod 26) which would result in 'V'.
   
   # input = Sushanth
   # output = Vxvkdqwk
   
   
# Concept for decryption of Caser cipher :-
   Similarly to decrypt each letter we’ll use :
    c = (x – n) mod 26 
    
   Where the input would for the equation will be 'V' as the first letter and the output must be 'S'
   therefore  the euation would be chr(ord('V') -3)mod 26) which would result in 'S'.
   
   # input = Vxvkdqwk
   # output = Sushanth
