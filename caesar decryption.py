def decrypt(string, shift):
  plain = ''                                                     #intilizing string to store cipher text
  for char in string:                                             
    if char == ' ':                                                #to add space as it is
      plain = plain + char                                       
    elif  char.isupper():                                          #to apply the encryption on the upper case letters 
      plain = plain + chr((ord(char) - shift - 65) % 26 + 65)    #for upper case letters to shift eith ASCII values 
    else:                                                             
      plain = plain + chr((ord(char) - shift - 97) % 26 + 97)    #for lower case letters to shift eith ASCII values
  
  return plain

text = input("Enter string: ")
key = int(input("Enter shift number: "))
print("Encrypted string: ", text)
print("After decryption: ", decrypt(text, key))