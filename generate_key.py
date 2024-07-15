import pickle
from pathlib import Path  
import streamlit_authenticator as stauth

name = "Richmond Kantam Nana Addo Yendam"
username = "Richie"
password = "XXXXXX"

hashed_password = stauth.Hasher(password).generate

file_path = Path(__file__).parent / 'hashed_pw.pkl'
with file_path.open('wb') as file:
    pickle.dump(hashed_password, file)

