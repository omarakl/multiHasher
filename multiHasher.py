#!/usr/bin/python

import hashlib
print("			")
mainPass = raw_input("Enter a text to be hashed ! : ")
print("		")
print("*****************************************************  MultiHasher  ********************************************************************** ")
print("		")
md5_p = hashlib.md5()
md5_p.update(mainPass.encode())
print("1-  MD5 HASH     :  " + md5_p.hexdigest())
print("		")

sha1_p = hashlib.sha1()
sha1_p.update(mainPass.encode())
print("2-  SHA-1 HASH   :  " + sha1_p.hexdigest())
print("         ")


sha224_p = hashlib.sha224()
sha224_p.update(mainPass.encode())
print("3-  SHA-224 HASH : " + sha224_p.hexdigest())
print("         ")


sha256_p = hashlib.sha256()
sha256_p.update(mainPass.encode())
print("4-  SHA-256 HASH : " + sha256_p.hexdigest())
print("         ")


sha512_p = hashlib.sha512()
sha512_p.update(mainPass.encode())
print("5-  SHA-512 HASH : " + sha512_p.hexdigest())
print("         ")

print("Done hashing !")
print("			")
print("*****************************************************  MultiHasher  ********************************************************************** ")
