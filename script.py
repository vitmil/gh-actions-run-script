import os
import sys
import requests


response = requests.get('http://ident.me')
print(f"response test: {response.text}")
print()
print('Hello DevOps')
print()
