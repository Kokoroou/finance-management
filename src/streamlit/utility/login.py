import streamlit as st
import zlib


class Login(object):
    def __init__(self):
        input_username = st.sidebar.text_input("Username")
        input_password = st.sidebar.text_input("Password", type="password")
        submit = st.sidebar.checkbox("Login")

        if submit:
            self.check_account(input_username, input_password)

    def access_approved(self):
        st.write("Access approved!")

    def access_denied(self):
        st.write("Access denied!")
        st.write("Check your username or password")

    def check_account(self, username, password):
        acc_dict = {"ttanh": 2815170622, "tmchien": 3112513328}

        password_hash = zlib.crc32(password.encode('utf-8'))

        if username not in acc_dict or acc_dict[username] != password_hash:
            self.access_denied()
        else:
            self.access_approved()


