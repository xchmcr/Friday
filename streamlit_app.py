import streamlit as st
from pymongo import MongoClient
from pprint import pprint

client = MongoClient(f'mongodb+srv://xchmcr:Waffletea27@clustertest01.dc3gd.mongodb.net/')
# client = MongoClient(f'mongodb+srv://mdebinski:<Passcode here>@mytestcluster.5bfpq.mongodb.net/')
client.admin.command('ping')
print("Connection to MongoDB established successfully.")
db = client['databasetest01']
collection = db['collectiontest01']
st.title("Friday")
st.write(
    "Please fill out the form and submit when complete!"
)

st.title("Personal Information Form")

# Initialize session state for form inputs
if 'form_submitted' not in st.session_state:
    st.session_state['form_submitted'] = False

if 'name' not in st.session_state:
    st.session_state['name'] = ""
if 'height' not in st.session_state:
    st.session_state['height'] = 170
if 'weight' not in st.session_state:
    st.session_state['weight'] = 70
if 'bpi_bicep' not in st.session_state:
    st.session_state['bpi_bicep'] = 10.0
if 'bpi_tricep' not in st.session_state:
    st.session_state['bpi_tricep'] = 10.0
if 'age' not in st.session_state:
    st.session_state['age'] = 0
if 'torso_circumference' not in st.session_state:
    st.session_state['torso_circumference'] = 90
if 'waist_circumference' not in st.session_state:
    st.session_state['waist_circumference'] = 80
if 'body_circumference' not in st.session_state:
    st.session_state['body_circumference'] = 100

# Create a form
with st.form("personal_info_form"):
    # Name field (mandatory)
    st.session_state['name'] = st.text_input("Name", value=st.session_state['name'], help="Enter your name")

    # Height field (slider)
    st.session_state['height'] = st.slider("Height (cm)", min_value=100, max_value=250, value=st.session_state['height'], step=1)

    # Weight field
    st.session_state['weight'] = st.number_input("Weight (kg)", min_value=30, max_value=200, value=st.session_state['weight'], step=1)

    # BPI of the bicep
    st.session_state['bpi_bicep'] = st.number_input("BPI of Bicep", min_value=0.0, max_value=100.0, value=st.session_state['bpi_bicep'], step=0.1)

    # BPI of the tricep
    st.session_state['bpi_tricep'] = st.number_input("BPI of Tricep", min_value=0.0, max_value=100.0, value=st.session_state['bpi_tricep'], step=0.1)

    st.session_state['age'] = st.number_input("Age", min_value=0, max_value=140, value=st.session_state['age'], step=1)

    # Circumferences
    st.session_state['torso_circumference'] = st.number_input("Circumference of Torso (cm)", min_value=50, max_value=200, value=st.session_state['torso_circumference'], step=1)
    st.session_state['waist_circumference'] = st.number_input("Circumference of Waist (cm)", min_value=50, max_value=200, value=st.session_state['waist_circumference'], step=1)
    st.session_state['body_circumference'] = st.number_input("Circumference of Body (cm)", min_value=50, max_value=200, value=st.session_state['body_circumference'], step=1)

    # Submit button
    submitted = st.form_submit_button("Submit")

    if submitted:
        if not st.session_state['name']:
            st.error("Please fill out the mandatory field: Name.")
        else:
            st.success("Form submitted successfully!")
            st.write(f"Name: {st.session_state['name']}")
            st.write(f"Height: {st.session_state['height']} cm")
            st.write(f"Weight: {st.session_state['weight']} kg")
            st.write(f"BPI of Bicep: {st.session_state['bpi_bicep']}")
            st.write(f"BPI of Tricep: {st.session_state['bpi_tricep']}")
            st.write(f"Circumference of Torso: {st.session_state['torso_circumference']} cm")
            st.write(f"Circumference of Waist: {st.session_state['waist_circumference']} cm")
            st.write(f"Circumference of Body: {st.session_state['body_circumference']} cm")

            data_to_insert = {
                'name': st.session_state['name'],
                'height': st.session_state['height'],
                'weight': st.session_state['weight'],
                'bpi_bicep': st.session_state['bpi_bicep'],
                'bpi_tricep': st.session_state['bpi_tricep'],
                'torso_circumference': st.session_state['torso_circumference'],
                'waist_circumference': st.session_state['waist_circumference'],
                'body_circumference': st.session_state['body_circumference'],
                'age': st.session_state['age'],
            }
            result = collectiontest01.insert_one(data_to_insert)
            
            # Reset the form inputs
            st.session_state['name'] = ""
            st.session_state['height'] = 170
            st.session_state['weight'] = 70
            st.session_state['bpi_bicep'] = 10.0
            st.session_state['bpi_tricep'] = 10.0
            st.session_state['age'] = 0
            st.session_state['torso_circumference'] = 90
            st.session_state['waist_circumference'] = 80
            st.session_state['body_circumference'] = 100
            st.session_state['form_submitted'] = True

# Thank you message
if st.session_state['form_submitted']:
    st.write("Thank you for submitting the form!")
    st.session_state['form_submitted'] = False