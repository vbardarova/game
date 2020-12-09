import streamlit as st
import random

data = [
    "Who is your favourite Avenger and why?",
"What’s the funniest word in the English language?",
"What gets you fired up?",
"What’s your funniest story involving a car?",
"What movie or song, is your favourite quote from?",
"What would we most likely find you doing on the weekend?",
"What is your favourite lockdown activity?",
"If you could choose a name for yourself, what would it be and why?",
"If you could choose a superpower, what would it be?",
"What’s one song you have completely memorized?",
"What’s the top destination on your must-visit list?",
"What’s your favourite TV show—the one you’re always watching on repeat?",
"What’s your go-to karaoke song?",
"What’s your most hated household chore and why?",
"What’s your favourite video/board games and why?",
"Do you put jam or cream on your scone first?",
"What’s something you’re proud of?",
"Who is your favourite family member and why?",
"What show are you currently binge-watching?",
"You have your own late night talk show, who do you invite as your first guest?",
"What is the course that you regret taking at uni?",
"At which store would you like to max-out your credit card?",
"There are now 25 hours in a day! How do you spend your extra hour?",
"Professional, casual or sweatpants? If there were no dress code, how would you dress for work?",
"If you could have dinner with any famous person, who would you choose?",
"If all the superheroes went to battle against each other, who do you think would win?",
"If you could only pick three foods to eat for a month, which foods would you choose?",
"If you could compete in any Olympic sport, which would it be?",
"If you could have any job in the world, what would you do?",
"If you could take a month to travel anywhere, where would you go?",
]

def sample():
    elem = random.choice(data) 
    data.remove(elem) 
    return elem


# # title
# st.sidebar.title('Navigation')
# # specify order of pages
# PAGES = ["Home",
#   "Common",]


# # Radio buttto with all sections in the above order.
# selection = st.sidebar.radio("Sections",PAGES)
# if selection == "Home":
#     st.write('succes')
# elif selection == "Common":
#     st.write('succes')

x=1
question = []

if st.button('pick a question'):
    if question is  None: 
        question = sample()
        x=x+1
        st.write(question)

    else:
        st.write(question)
     

