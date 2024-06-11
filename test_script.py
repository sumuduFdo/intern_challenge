import pyotp
import base64
import hashlib

from gen_script import generate_totp

shared_secret = "fernando.sumu98@gmail.comHENNGECHALLENGE003"
encoded = base64.b32encode(str.encode(shared_secret))

pyotp_build = pyotp.TOTP(encoded, digits=10, digest=hashlib.sha512, interval=30)
pyotp_totp = pyotp_build.now()

gen_otp = generate_totp(shared_secret)

print('pyotp generated: ', pyotp_totp)
print('custom generated otp: ', gen_otp)

print("equality: ", pyotp_totp.__eq__(gen_otp))
