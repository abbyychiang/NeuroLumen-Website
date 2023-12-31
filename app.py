import streamlit as st

# Set page config
st.set_page_config(page_title="NeuroLumen", page_icon="https://i.imgur.com/unbYWKD.jpg", layout="wide")

# CSS styles for the navigation bar and blue sections
st.markdown("""
    <style>
        .navbar {
            overflow: hidden;
            background-color: #1768AC;
            position: fixed;
            top: 40px; /* Adjusted top position */
            width: 100%; /* Full width */
            left: 0;
            z-index: 1000;
            display: flex;
            align-items: center;
            justify-content: flex-start; /* Changed alignment to flex-start */
            transition: top 0.3s;
        }

        .navbar a {
            display: block;
            color: white;
            text-align: center;
            padding: 20px 20px; /* Adjusted padding */
            text-decoration: none;
            font-size: 24px;
            margin-top: 10px;
        }

        .navbar a:hover {
            background-color: #ddd;
            color: black;
        }

        /* Style for the light blue section */
        .light-blue-section {
            background-color: #ADD8E6; /* Baby blue color code */
            padding: 20px;
            width: 100vw; /* Full viewport width */
            margin-left: calc(-50vw + 50%);
            margin-right: calc(-50vw + 50%);
        }

        /* Extend the light blue section */
        #extended-section {
            width: 100%;
            padding: 20px;
            background-color: #E8F3FD; /* Background color for the extended section */
            color: black; /* Text color set to black */
            margin-left: 0; /* Remove the left margin */
            margin-right: 0; /* Remove the right margin */
        }

        /* Update font sizes */
        #extended-section p {
            font-size: 35px;
        }

        /* Adjust space */
        h1 {
            margin-top: 50px; /* Increase space above NEUROLUMEN */
        }

        p {
            margin-bottom: 50px; /* Increase space below the subheader */
        }
    </style>
""", unsafe_allow_html=True)

# Navigation bar with anchor links
st.markdown("""
    <div class="navbar" id="navbar">
        <a href="#neurolumen" class="scroll-link">NEUROLUMEN</a>
        <a href="#team" class="scroll-link" style="margin-left: 20px;">Meet the Team</a> <!-- Adjusted margin -->
    </div>
""", unsafe_allow_html=True)

# Header
st.markdown("<h1 style='text-align: center; color: #1768AC; font-size: 65px;'>NEUROLUMEN</h1>", unsafe_allow_html=True)

# Subheader
st.markdown("<p style='text-align: center; font-size: 30px; font-style: italic; margin-bottom: 50px;'>Illuminating the Path to Early Alzheimer's Detection</p>", unsafe_allow_html=True)

# Extended light blue section with black font
st.markdown(
    """
    <div class="light-blue-section" id="extended-section">
        <p style='font-size: 35px; color: black;'>Did you know that Alzheimer's Disease impacts <b>6.7 million</b> people worldwide?</p>
        <p style='font-size: 35px; color: black;'>About <b>1</b> in <b>9</b> people age 65 and older (<b>10.7%</b>) has Alzheimer's.</p>
    </div>
    """,
    unsafe_allow_html=True
)

# Rest of the sections (White Section, How Neurolumen Works, etc.)...


# White Section
st.markdown("<h2 style='text-align: center; color: #1768AC; font-size: 32px;'>Why Neurolumen?</h2>", unsafe_allow_html=True)
st.markdown("<h3 style='color: #1768AC;'>Accessible Technology:</h3>", unsafe_allow_html=True)
st.markdown("We've developed a solution using Low Field MRI technology for prompt, accurate Alzheimer's diagnosis.")

st.markdown("<h3 style='color: #1768AC;'>Empowering Healthcare Access:</h3>", unsafe_allow_html=True)
st.markdown("Our mission is to ensure equitable healthcare access for all, regardless of location or resources.")

st.markdown("<h2 style='text-align: center; color: #1768AC; font-size: 32px;'>How Neurolumen Works</h2>", unsafe_allow_html=True)

st.markdown("<h3 style='color: #1768AC;'>Diagnose</h3>", unsafe_allow_html=True)
st.markdown("Our solution uses Low Field MRI and advanced ensemble learning techniques to provide Alzheimer's diagnoses.")

st.markdown("<h3 style='color: #1768AC;'>Access</h3>", unsafe_allow_html=True)
st.markdown("Experience the ease of diagnosis from the comfort of your home.")

st.markdown("<h3 style='color: #1768AC;'>Impact</h3>", unsafe_allow_html=True)
st.markdown("By enabling early intervention, we empower individuals and healthcare providers to manage Alzheimer's more effectively.")
