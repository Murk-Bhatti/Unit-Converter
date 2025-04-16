import streamlit as st

st.title("🧮 Simple Unit Converter")

category = st.selectbox("Choose a category:", ["Length", "Weight", "Temperature"])

def length_converter(value, from_unit, to_unit):
    conversions = {
        "Meter": 1,
        "Kilometer": 1000,
        "Centimeter": 0.01,
        "Millimeter": 0.001,
        "Mile": 1609.34,
        "Yard": 0.9144,
        "Foot": 0.3048,
        "Inch": 0.0254,
    }
    return value * conversions[from_unit] / conversions[to_unit]

def weight_converter(value, from_unit, to_unit):
    conversions = {
        "Kilogram": 1,
        "Gram": 0.001,
        "Pound": 0.453592,
        "Ounce": 0.0283495,
        "Ton": 1000,
    }
    return value * conversions[from_unit] / conversions[to_unit]

def temperature_converter(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value
    if from_unit == "Celsius":
        return (value * 9/5) + 32 if to_unit == "Fahrenheit" else value + 273.15
    if from_unit == "Fahrenheit":
        return (value - 32) * 5/9 if to_unit == "Celsius" else ((value - 32) * 5/9) + 273.15
    if from_unit == "Kelvin":
        return value - 273.15 if to_unit == "Celsius" else ((value - 273.15) * 9/5) + 32

if category == "Length":
    units = ["Meter", "Kilometer", "Centimeter", "Millimeter", "Mile", "Yard", "Foot", "Inch"]
    from_unit = st.selectbox("From:", units)
    to_unit = st.selectbox("To:", units)
    value = st.number_input("Enter value:", min_value=0.0)
    result = length_converter(value, from_unit, to_unit)
    st.success(f"{value} {from_unit} = {result:.4f} {to_unit}")

elif category == "Weight":
    units = ["Kilogram", "Gram", "Pound", "Ounce", "Ton"]
    from_unit = st.selectbox("From:", units)
    to_unit = st.selectbox("To:", units)
    value = st.number_input("Enter value:", min_value=0.0)
    result = weight_converter(value, from_unit, to_unit)
    st.success(f"{value} {from_unit} = {result:.4f} {to_unit}")

elif category == "Temperature":
    units = ["Celsius", "Fahrenheit", "Kelvin"]
    from_unit = st.selectbox("From:", units)
    to_unit = st.selectbox("To:", units)
    value = st.number_input("Enter value:")
    result = temperature_converter(value, from_unit, to_unit)
    st.success(f"{value} {from_unit} = {result:.2f} {to_unit}")
