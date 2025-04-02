# BMI Calculator using Python and Streamlit

## Overview
This is a simple **BMI (Body Mass Index) Calculator** built using Python and Streamlit. Users can enter their weight and height, and the application calculates their BMI and categorizes it.

## Features
- Accepts user input for weight (kg) and height (m)
- Calculates BMI using the formula: `BMI = weight / (height ** 2)`
- Provides feedback on BMI category:
  - **Underweight** (BMI < 18.5)
  - **Normal weight** (18.5 ≤ BMI < 24.9)
  - **Overweight** (25 ≤ BMI < 29.9)
  - **Obese** (BMI ≥ 30)
- Interactive UI using **Streamlit**

## Prerequisites
- Python 3.x installed
- Streamlit library installed (`pip install streamlit`)

## How to Run
1. Clone this repository or copy the script.
2. Install dependencies:
   ```bash
   pip install streamlit
   ```
3. Run the application:
   ```bash
   streamlit run bmi_calculator.py
   ```
4. Open the provided local URL in your browser to use the BMI calculator.

## Example Output
```
Enter your weight (kg): 70
Enter your height (m): 1.75
Your BMI is: 22.86
Category: Normal weight ✅
```

## License
This project is open-source and available for modification and redistribution.

## Contributions
Feel free to improve the project and submit a pull request!

Happy coding! 🚀

