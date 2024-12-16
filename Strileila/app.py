# streamlit_app/app.py
import streamlit as st
import requests

def fetch_users():
    response = requests.get("http://127.0.0.1:5000/user/1")
    return response.json()


st.title("Lista de Usuários")
users = fetch_users()
print("AQUII", users)
for user in users:
    st.write(f"**ID:** {user[0]}, **Nome:** {user[1]}, **Email:** {user[2]}")

