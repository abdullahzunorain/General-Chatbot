import streamlit as st

# Function to perform addition
def add(x, y):
    return x + y

# Function to perform subtraction
def subtract(x, y):
    return x - y

# Function to perform multiplication
def multiply(x, y):
    return x * y

# Function to perform division
def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    else:
        return x / y

# Streamlit app
def main():
    st.title("Simple Calculator")
    st.write("This is a basic calculator built using Streamlit.")
    
    # Input fields for numbers
    num1 = st.number_input("Enter the first number", value=0.0, step=1.0)
    num2 = st.number_input("Enter the second number", value=0.0, step=1.0)
    
    # Select operation
    operation = st.selectbox("Choose an operation", ("Add", "Subtract", "Multiply", "Divide"))
    
    # Perform calculation based on the selected operation
    if operation == "Add":
        result = add(num1, num2)
    elif operation == "Subtract":
        result = subtract(num1, num2)
    elif operation == "Multiply":
        result = multiply(num1, num2)
    elif operation == "Divide":
        result = divide(num1, num2)
    
    # Display the result
    st.write(f"The result is: {result}")

if __name__ == '__main__':
    main()
