import streamlit as st
import requests as req 

def generate_random_user():
    api_url = 'https://api.api-ninjas.com/v1/randomuser'
    res = req.get(api_url, headers={
        'X-Api-Key': 'MtlV61EQ51315I0ySN47bg==OQT3EbNKPTP6CtX2'
    })

    if res.status_code == req.codes.ok:
        return res.json()  # Return JSON response
    else:
        st.error(f"Error {res.status_code}: {res.text}")

st.header("Random User Generator")

# Use one button for generating random user
if st.button("Generate"):
    user = generate_random_user()
    st.write("Generated User:")
    st.write(f"Username: {user['username']}")
    st.write(f"Name: {user['name']}")
    st.write(f"Sex: {user['sex']}")
    st.write(f"Address: {user['address']}")
    st.write(f"Email: {user['email']}")
    st.write(f"Birthday: {user['birthday']}")
