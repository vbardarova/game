import streamlit as st
import random
import SessionState

ss = SessionState.get(question='',x=1)


data = [
'What is the strangest Christmas/New Year present you ever received?',
'What is your favorite holiday food?',
'Does your family practice any interesting Christmas/New Year traditions?',
'What is your favourite winter sport?,
'What is your favourite holiday dish?,
'What is your favourite holiday song?,
'What is your favourite holiday movie?,
'What is your favourite holiday movie?
]



def sample():
    elem = random.choice(data) 
    data.remove(elem)

    return elem


if st.button('pick a question'):    
    if ss.x==1:
        question = sample()
        st.write(question)
        ss.x = ss.x + 1
        ss.q= question
    else:
        st.write('You have already picked a question.')
        st.write(ss.q)
