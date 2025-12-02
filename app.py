import streamlit as st

# Streamlit UI
st.title("Power Calculator")
st.write("Enter a number to calculate its square, cube, and fifth power.")

# Get user input
n = st.number_input("Enter an integer", value=1, step=1)

# Calculate results
square = n ** 2
cube = n ** 3
fifth_power = n ** 5
tenth_power = n ** 10

# Display results
st.write(f"The square of {n} is: {square} \n")
st.write(f"The cube of {n} is: {cube} \n")
st.write(f"The fifth power of {n} is: {fifth_power} \n")
st.write(f"The tenth power of {n} is: {tenth_power} \n")