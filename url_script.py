import json
import requests
import hashlib

from requests.auth import HTTPBasicAuth
from requests.adapters import HTTPAdapter, Retry
from totp_generator import generate_totp

import pyotp

api_url = 'https://api.challenge.hennge.com/challenges/003'


t0 = 0
time_step = 30
user_id = 'sumuduf228@gmail.com'
token_shared_secret = user_id + 'HENNGECHALLENGE003'

req_body = {
    'github_url': 'https://gist.github.com/sumuduFdo/006ef91bf936201f0f8d198e02a12b19',
    'contact_email': user_id,
    'solution_language': 'python'
}

# build requests session
# retry for status codes [500 Internal Server Error] [503 Service Unavailable] [504 Gateway Timeout]
session = requests.Session()
max_retries = Retry(total=3, status_forcelist=[500, 503, 504], backoff_factor=0.1)
session.mount('https://', HTTPAdapter(max_retries=max_retries))

headers = {'Content-Type': 'application/json'}
token = generate_totp(token_shared_secret, digest=hashlib.sha512)

try:
    res = session.post(api_url, timeout=10, headers=headers, allow_redirects=False, auth=HTTPBasicAuth(username=user_id, password=token), data=json.dumps(req_body))
    print('[SUCCESS] | ', res.json())
except requests.exceptions.HTTPError as err:
    raise err('[ERROR] HTTPError, ErrInfo: {}'.format(err))
except requests.exceptions.ConnectionError as err:
    raise err('[ERROR] ConnectionError, ErrInfo: {}'.format(err))
except requests.exceptions.Timeout as err:
    raise err('[ERROR] RequestTimeout, ErrInfo: {}'.format(err))
except requests.exceptions.RequestException as err:
    raise err('[ERROR] RequestException, ErrInfo: {}'.format(err))