
print ("What will be the file's name?")
name = input()
print("What do you want to write?")
text = input()
print("What will be the password?")
password = input()
result = bytearray()
for letter in text:
    result.append(ord(letter) ^ ord(password))
f = open (name+'.txt','w')
f.write(result.decode())
print("Encrypted file created successfully!")
