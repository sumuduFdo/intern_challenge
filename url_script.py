import base64
import json
import requests
import hashlib

from requests.auth import HTTPBasicAuth
from totp_generator import generate_totp

import pyotp

api_url = "https://api.challenge.hennge.com/challenges/003"


t0 = 0
time_step = 30
user_id = "fernando.sumu98@gmail.com"
token_shared_secret = user_id + "HENNGECHALLENGE003"

req_body = {
    "github_url": "https://gist.github.com/sumuduFdo/006ef91bf936201f0f8d198e02a12b19",
    "contact_email": "fernando.sumu98@gmail.com",
    "solution_language": "python"
}
