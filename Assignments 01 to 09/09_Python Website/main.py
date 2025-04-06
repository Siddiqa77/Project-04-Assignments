import streamlit as st

# --- Page config ---
st.set_page_config(page_title="My Recipe Book", page_icon="🍔", layout="wide")

# --- Hide default Streamlit style ---
hide_st_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
"""
st.markdown(hide_st_style, unsafe_allow_html=True)

# --- Custom CSS for header ---
st.markdown("""
    <style>
    .header {
        background-color: #FF6F61;
        padding: 2rem;
        border-radius: 10px;
        text-align: center;
        color: white;
    }
    </style>
""", unsafe_allow_html=True)

# --- Sidebar navigation ---
st.sidebar.title("🍴 Menu")
page = st.sidebar.radio("Go to", ["Home", "Recipes", "Contact"])

# --- Header section ---
st.markdown('<div class="header"><h1>Welcome to My Recipe Book</h1><p>Delicious recipes at your fingertips! 🍽️</p></div>', unsafe_allow_html=True)
st.markdown("---")

# --- Pages ---
if page == "Home":
    st.subheader("🏠 Home")
    st.write("""
        Welcome to **My Recipe Book**!  
        Here you'll find a collection of mouth-watering recipes from all around the world. 🌎
        
        Browse the recipes or share your own favorite dish with us!
    """)
    st.image("https://images.unsplash.com/photo-1504674900247-0877df9cc836", caption="Cooking is an art! 🎨", use_container_width=True)

elif page == "Recipes":
    st.subheader("🍝 Recipes")

    # Layout using columns
    col1, col2 = st.columns(2)

    with col1:
        st.image("https://images.unsplash.com/photo-1601050690591-1f79e2b2fd91", use_container_width=True)
        st.markdown("""
            ### 🍕 Margherita Pizza
            - Fresh basil
            - Mozzarella cheese
            - Homemade tomato sauce
        """)

    with col2:
        st.image("https://images.unsplash.com/photo-1546069901-ba9599a7e63c", use_container_width=True)
        st.markdown("""
            ### 🍔 Classic Cheeseburger
            - Juicy beef patty
            - Cheddar cheese
            - Fresh lettuce and tomato
        """)

    st.markdown("---")

    col3, col4 = st.columns(2)

    with col3:
        st.image("https://images.unsplash.com/photo-1551218808-94e220e084d2", use_container_width=True)
        st.markdown("""
            ### 🍜 Ramen Noodles
            - Savory broth
            - Soft-boiled egg
            - Sliced pork and vegetables
        """)

    with col4:
        st.image("https://images.unsplash.com/photo-1506086679526-a687b9a5b42e", use_container_width=True)
        st.markdown("""
            ### 🥗 Greek Salad
            - Feta cheese
            - Fresh cucumbers
            - Olives and vinaigrette
        """)

elif page == "Contact":
    st.subheader("📬 Share Your Recipe")
    st.write("Have a delicious recipe you want to share? Fill out the form below!")

    # --- Initialize session state to store recipes ---
    if "recipes" not in st.session_state:
        st.session_state.recipes = []

    with st.form(key="contact_form"):
        name = st.text_input("Your Name")
        email = st.text_input("Your Email")
        recipe = st.text_area("Your Recipe")

        submit_button = st.form_submit_button(label="Submit")

        if submit_button:
            if recipe.strip() != "":
                # Save submitted recipe
                st.session_state.recipes.append({
                    "name": name,
                    "email": email,
                    "recipe": recipe
                })
                st.success(f"Thank you {name}! Your recipe has been submitted successfully. 🍽️")
            else:
                st.warning("Please enter a recipe before submitting.")

    st.markdown("---")
    st.subheader("🍴 Submitted Recipes")

    # --- Show all submitted recipes ---
    if st.session_state.recipes:
        for idx, entry in enumerate(st.session_state.recipes):
            st.markdown(f"### {idx + 1}. {entry['name']}")
            st.write(f"📩 **Email:** {entry['email']}")
            st.write(f"📝 **Recipe:** {entry['recipe']}")
            st.markdown("---")
    else:
        st.info("No recipes submitted yet. Share yours above!")

# --- Footer ---
st.markdown("---")
st.write("Made with ❤️ by Siddiqa Badar - Powered by Streamlit")


