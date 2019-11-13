print("What file do you want to decrypt?")
result = ""
name = input()
print("What's the password?")
password = input()
plen = len(password)
f = open(name + ".txt", 'rb')
message = f.read()
for index, byte in enumerate(message):
    result += chr(byte ^ ord(password[index % plen]))
j = open(name + "(decrypted)"".txt", 'w')
j.write(result)
print("Decrypted file created successfully!")
