### In terminal, install python environment
# python -m venv fini_fiction
# .\fini_fiction\Scripts\activate  
### Create requirements.txt in the same folder and include all libraries
# pip install -r requirements.txt

import streamlit as st 

st.title('Welcome to Fini Fiction!')

input, output= st.tabs(['Input', 'Output'])

with input:
    a = st.text_input('Insert book title', value='A lit­tle life: a nov­el')
    b = st.text_input('Insert book settings', value='town, place, country or a year')
    c = st.text_area('The book opens with')
    d = st.text_area('The story is about')
    e = st.text_area('I enjoyed the')
    
    st.subheader('Please rate this book:')
    sentiment_mapping = ["one", "two", "three", "four", "five"]
    f = st.feedback(options='stars')
    if f is not None:
        st.markdown(f"You selected {sentiment_mapping[f]} star(s).")
