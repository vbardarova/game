import streamlit as st



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
     

