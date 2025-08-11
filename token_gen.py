#                               Token Generator
# In the token variable, edit the integer value to the desired token length
#--------------------------------------------------------------------------
#                               !!DISCLAIMER!!
# As of 2015, it is believed that 32 bytes (256 bits) of randomness 
# is sufficient for the typical use-case expected for the secrets module.

import secrets

def token_gen():
    token = secrets.token_hex(32)
    return token

print(token_gen())