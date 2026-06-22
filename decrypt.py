from cryptography.fernet import Fernet
import os 

files = []
thisFile = os.path.basename(__file__)
keyFile = "key.key"
safes = [thisFile, keyFile, "encrypt.py", "node_modules", ".next", ".git"]

def addFiles(path):
    for file in os.listdir(path):

        if file in safes:
            continue

        if not (os.path.isfile(f"{path}/{file}")):
            addFiles(f"{path}/{file}")
            continue

        files.append(F"{path}/{file}")

addFiles(".")
print(files)


with open(keyFile, "rb") as k:
    key = (k.read())

fer = Fernet(key)

for f in files:
    with open(f, "rb") as r:
        content = r.read()
        decrypted_content = fer.decrypt(token=content)
    
    with open(f, "wb") as w:
        w.write(decrypted_content)

print("Every file is Recovered")