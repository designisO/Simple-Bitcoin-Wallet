from bitcoin import *

my_private_key = random_key()
print("Private Key: %s\n" % my_private_key)

print("Public Key")
# converting private key to public key
public_key = privtopub(my_private_key)
print(public_key)

print("Wallet Address")
# Creating an address using public key
wallet_address = pubtoaddr(public_key)
print(wallet_address)
