import streamlit as st

st.title("Simple Calculator")
st.header("Calculate simple intrest")
st.subheader("Enter the values below to calculate simple intrest")
st.write("Simple intrest is")

col_1, col_2, col_3, col_4=st.columns(4)
user_name=col_1.text_input("Enter your name")
principle=col_2.principle=st.number_input("Enter the principle amount,step=100")
st.write(principle )
rate=col_3.number_input("Enter the rate of intrest")
st.write(rate)
time=col_4.number_input("Enter the time period[In years]",step=1)
st.write(time)
agreed=st.checkbox("i agree to terms and condition")
if agreed:
    clicked=st.button("calculate button")
    if clicked:
        simple_interest = (principle * rate * time) / 100
        st.write(f"{user_name},you have to pay{simple_interest}")
user_dob = st.date_input("Select your date of birth",min_value="1990-01-01")
st.write("Your DOB:", user_dob)
feed_back=st.feedback("stars")
print(feed_back)
