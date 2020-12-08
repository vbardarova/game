import streamlit as st
import pickle as pkle
import os.path
from sections import pages, results, home


# title
st.sidebar.title('Navigation')
# specify order of pages
PAGES = ["Home",
  "Common",]


# Radio buttto with all sections in the above order.
selection = st.sidebar.radio("Sections",PAGES)
if selection == "Home":
    st.write('succes')
elif selection == "Common":
    st.write('succes')
     

