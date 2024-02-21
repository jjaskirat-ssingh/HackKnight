import streamlit as st
import pymongo
import bcrypt
import secrets  # For generating secure tokens

# Connect to MongoDB
client = pymongo.MongoClient("mongodb+srv://sidakchuchra:99140sidak@<cluster-address>/<database_name>")
db = client["cluster0"]
users_collection = db["users"]

# Secret key for secure token generation
SECRET_KEY = "2a5e8b4f5c505312d870d3075cfe4067"

# Function to generate a secure token for sessions
def generate_session_token():
    return secrets.token_hex(16)  # 16 bytes = 32 characters

# Sidebar for navigation
st.sidebar.header("Navigation")
menu = st.sidebar.radio("", ["Home", "Login", "Signup"])

# Session state
if "session_token" not in st.session_state:
    st.session_state.session_token = None

if menu == "Home":
    if st.session:
        import streamlit as st
        import pymongo
        import bcrypt
        import secrets  # For generating secure tokens

# Connect to MongoDB
client = pymongo.MongoClient("mongodb+srv://sidakchuchra:99140sidak@<cluster-address>/<database_name>")
db = client["cluster0"]
users_collection = db["users"]

# Secret key for secure token generation
SECRET_KEY = "2a5e8b4f5c505312d870d3075cfe4067"

# Function to generate a secure token for sessions
def generate_session_token():
    return secrets.token_hex(16)  # 16 bytes = 32 characters

# Sidebar for navigation
st.sidebar.header("Navigation")
menu = st.sidebar.radio("", ["Home", "Login", "Signup"])

# Session state
if "session_token" not in st.session_state:
    st.session_state.session_token = None

if menu == "Home":
    if st.session_state.session_token:
        st.write(f"Welcome, {st.session_state.username}!")
    else:
        st.warning("Please log in.")
elif menu == "Login":
    st.header("Login")
    login_username = st.text_input("Username")
    login_password = st.text_input("Password", type="password")
    login_button = st.button("Login")

    if login_button:
        user = users_collection.find_one({'username': login_username})
        if user and bcrypt.checkpw(login_password.encode('utf-8'), user['password']):
            session_token = generate_session_token()
            st.session_state.session_token = session_token
            st.session_state.username = login_username
            st.experimental_rerun()
        else:
            st.error("Invalid username or password")
elif menu == "Signup":
    st.header("Signup")
    signup_username = st.text_input("New Username")
    signup_password = st.text_input("New Password", type="password")
    signup_button = st.button("Sign Up")

    if signup_button:
        existing_user = users_collection.find_one({'username': signup_username})
        if existing_user:
            st.error("Username already exists.")
        else:
            hashed_password = bcrypt.hashpw(signup_password.encode('utf-8'), bcrypt.gensalt())
            users_collection.insert_one({'username': signup_username, 'password': hashed_password})
            st.success("Signup successful! Please log in.")