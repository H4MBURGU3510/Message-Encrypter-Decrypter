print ("What file do you want to decrypt?")
result = ""
name = input()
print("What's the password?")
password = input()
f = open (name+".txt",'rb')
message = f.read()
for byte in message:
    result += chr( byte ^ ord(password))
j = open (name+"(decrypted)"".txt",'w')
j.write(result)
print("Decrypted file created successfully!")

