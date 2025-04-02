import streamlit as st

def calculate_bmi(weight, height):
    return weight / (height ** 2)

st.title("BMI Calculator")

st.write("Enter your weight (kg) and height (m) to calculate your Body Mass Index (BMI).")

weight = st.number_input("Weight (kg)", min_value=1.0, format="%.2f")
height = st.number_input("Height (m)", min_value=0.5, format="%.2f")

if st.button("Calculate BMI"):
    if height > 0:
        bmi = calculate_bmi(weight, height)
        st.write(f"Your BMI is: {bmi:.2f}")
        
        if bmi < 18.5:
            st.warning("You are underweight.")
        elif 18.5 <= bmi < 24.9:
            st.success("You have a normal weight.")
        elif 25 <= bmi < 29.9:
            st.warning("You are overweight.")
        else:
            st.error("You are obese.")
    else:
        st.error("Height must be greater than zero.")
