import pyshorteners as pyst
import streamlit as st
import pyperclip
shortener = pyst.Shortener()
def copying():
    pyperclip.copy(shorted_url)


st.markdown("<h1 style='text-align:center;'>URL SHORTENER</h1>", unsafe_allow_html=True)
form = st.form('name')
url = form.text_input("URL HERE")
s_btn=form.form_submit_button("SHORT")
if s_btn:
    shorted_url = shortener.tinyurl.short(url)
    st.markdown("<h4 style='text-align:center;'>SHORTED URL</h4>", unsafe_allow_html=True)
    st.markdown(f"<h6 style='text-align:center;'>{shorted_url}</h6>", unsafe_allow_html=True)
    
