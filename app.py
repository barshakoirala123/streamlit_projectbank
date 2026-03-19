import streamlit as st
# st.title("Demo Page")
# st.header("H1 Welcome to my Demo page")
# st.subheader("H2 This is a subheader")
# st.text("This is regular text.")
# st.write("This is a simple text element")

st.title("Interest calculator- ADB")
#st.header("H1 Welcome to my Demo page")
#st.subheader("H2 This is a subheader")
st.text("This method is used for calculating the interest for the provided bank yearly, monthly and quarterly.")
st.write("This is a simple text element")

username = st.text_input("Enter your name:") 
principle_amount = st.number_input("Enter Principle amount:", min_value= 10000, max_value = 100000)
time_period = st.number_input("Enter time duration(in years):")
time_duration =st.selectbox ("Enter Time Duration(in years):", [1,2,3,4,5])
user_services = st.multiselect("Service you are using:", ['Credit card', 'Debit card', 'Online Banking'])
user_accounttype= st.radio("Choose your account type:", ['Savings Account', 'Current Account', 'Others'])


rate = st.number_input("Total rate of interest(in %):", min_value = 2.0, max_value = 15.0)
user_dateofbirth = st.date_input("Enter your date of birth:") 
st.slider("Rate your experience")

user_agreed = st.checkbox ("I agree with the terms and conditions")
if user_agreed:
   submit_button= st.button("Calculate Interest")
   if submit_button:
     
    submit_button = st.button("Calculation of interest")
    if submit_button:
       interest_amount = (principle_amount* time_period* rate)/ 100
       st.write(f"Hello {username}, if you deposit {principle_amount} for {time_period} years, with {rate} of yearly rate, your total interest amount will be :{interest_amount}. Thank you so much for banking with us.") 

Feedback = st.text_area("Provider feedback or comments here:")
if Feedback:
    st.write(f"hello {username}, thank you so much for your feedback. We will work with it and wont make you regret banking with us.")
st.write(f"Hello {username}")
st.write(f"principle amount:{principle_amount}")

