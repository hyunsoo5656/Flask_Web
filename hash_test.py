

from passlib.hash import pbkdf2_sha256

password = '1234'

hash_pw = pbkdf2_sha256.hash(password)
print(hash_pw)
# print(hash_pw == '$pbkdf2-sha256$29000$tNbaO4cQ4hyDEILwfk8pZQ$rgaE5FAjiCbwUrv9ohipfLJfv4UzbW7OY7mWe6NRZZ8')


print(pbkdf2_sha256.verify("1234", hash_pw))











