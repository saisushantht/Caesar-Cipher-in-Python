def encrypt(string, shift):
  cipher = ''                                                     #intilizing string to store cipher text
  for char in string:                                             
    if char == ' ':                                                #to add space as it is
      cipher = cipher + char                                       
    elif  char.isupper():                                          #to apply the encryption on the upper case letters 
      cipher = cipher + chr((ord(char) + shift - 65) % 26 + 65)    #for upper case letters to shift eith ASCII values 
    else:                                                             
      cipher = cipher + chr((ord(char) + shift - 97) % 26 + 97)    #for lower case letters to shift eith ASCII values
  
  return cipher

text = input("Enter string: ")
key = int(input("Enter shift number: "))
print("Original string: ", text)
print("After encryption: ", encrypt(text, key))