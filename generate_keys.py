import pickle
from pathlib import Path

import streamlit_authenticator as stauth

names = ["Jaskirat", "Aparna"]
usernames = ["jaskirat", "aparna"]
passwords = ["abc123", "def123"]

hashed_passwords = stauth.Hasher(passwords).generate()

file_path = Path(__file__).parent / "hashed_pw.pkl"
with file_path.open("wb") as file:
    pickle.dump(hashed_passwords, file)

# hashed_passwords = stauth.Hasher(['abc', 'def']).generate()
# print(hashed_passwords)