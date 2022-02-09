import streamlit as st


st.title("André's First Hackathon App!")
st.write("This app is to help me build and understand each feature that Streamlit offers!")


## Understanding Buttons
button1 = st.button("Click Me To Begin")
if button1: 
    st.write("I'm new to this, so bare with me as I try to figure this out 🧐😅👨🏻‍💻")


st.header("Understanding Checkboxes & Buttons")
like = st.checkbox("Do you like this app so far?")
button2 = st.button("Submit")
if button2: 
    if like: 
        st.write("Thanks. I like it too.")
    else: st.write("Oh well, I'm still learning")


st.header("Understanding of the Radio Button")
streamlit_experience = st.radio("How long have you been using Streamlit?", ("<6 Months", "6-12 Months", "1+ Years"))
button3 = st.button("Submit Answer")
if button3: 
        st.write(streamlit_experience)
        if streamlit_experience == "<6 Months":
            st.write("Same, me too!")


st.header("Understanding of the Select Box")
streamlit_experience2 = st.selectbox("What do you enjoy most about Streamlit?", ("Ease of Use", "Speed of Delivery", "Derisking App Building Process"))
button4 = st.button("Choose from the above dropdown")
if button4: 
        st.write(streamlit_experience2)
        if streamlit_experience2 == "Ease of Use":
            st.write("Great Answer!")

st.header("Understanding of the Multiselect")
options = st.multiselect("What animals do you like?", ["Lion", "Tiger", "Bear"])
button5 = st.button("Print Animals")
if button5: 
    st.write(options)


st.header("Understanding How Sliders Work")
animals_num = st.slider("How many animals are at the zoo?", 1,100,  10)
if st.button("Slider Button"):
    st.write(animals_num)



    