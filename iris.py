import streamlit as st
st.write("Hello ,let's register first")
sepel_length=st.number_input("Enter your sepel lengh(in kgs)")
sepel_width=st.number_input("Enter your sepel width(in cm)")
petel_length=st.number_input("Enter your petel length (in cm)")
petel_width=st.number_input("Enter your  petel width (in cm)")
if st.button("predict"):
   with open(r"C:\Users\Public\akira internship\iris_model.pkl") as file:
      loaded_model = pickle.load(file)
   result=loaded_model.predict([[sepel_length,petel_length,petel_width]])
   st.write(result)

