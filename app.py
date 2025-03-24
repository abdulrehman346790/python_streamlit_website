import streamlit as st
st.set_page_config(page_title="My Streamlit website ", page_icon="🌍")
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "About", "Contact"])

if page == "Home":
    st.title("🌟 Welcome to my streamlit website!")
    st.write("This is a simple website built with streamlit.")

    name = st.text_input("What's your name?")
    if st.button("Say Hello"):
        st.write(f"Hello {name}! 👋")
        
elif page == "About":
    st.title("📖 About Us")
    st.write("This website is created using Streamlit, a Python framework for building web apps.")

elif page == "Contact":
    st.title("📬 Contact Us")
    st.write("You can reach us at: **ar5254843@gmail.com**")
