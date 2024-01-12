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





st.markdown("""
    <style>
        /* Styling for the pathway */
        .pathway {
            display: flex;
            justify-content: space-around;
            align-items: center;
            padding: 20px;
            background-color: #F3F3F3; /* Light grey background */
            border-radius: 10px;
            margin-bottom: 30px;
        }

        /* Styling for individual steps */
        .step {
            text-align: center;
            padding: 20px;
            border-radius: 10px;
            font-size: 18px;
            width: 200px;
            color: black; /* Font color */
        }

        /* Different colors for backend and frontend */
        .backend {
            background-color: #ADD8E6; /* Light blue */
        }

        .frontend {
            background-color: #FFD700; /* Gold */
        }

        /* Description style */
        .description {
            font-size: 14px;
            text-align: center;
            margin-top: 10px;
            color: black; /* Font color */
        }

        /* Title style */
        .step p {
            font-size: 20px;
            font-weight: bold;
            margin-bottom: 5px;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h2 style='text-align: center; color: #1768AC; font-size: 50px;'>How NeuroLumen Works</h2>", unsafe_allow_html=True)

# NeuroLumen Workflow Pathway: Backend Model
st.markdown("<h2 style='color: #1768AC;'>Backend Model</h3>", unsafe_allow_html=True)
st.markdown("""
    <div class="pathway">
        <div class="step backend">
            <p>Image Processing</p>
            <div class="description">Adjusts and standardizes MRI images for analysis.</div>
        </div>
        <div class="step backend">
            <p>Enhancement</p>
            <div class="description">Improves image quality for precise examination.</div>
        </div>
        <div class="step backend">
            <p>Data Analysis</p>
            <div class="description">Analyzes cognitive and brain data using AI models.</div>
        </div>
        <div class="step backend">
            <p>Issue Identification</p>
            <div class="description">Detects potential problems based on analysis outcomes.</div>
        </div>
    </div>
""", unsafe_allow_html=True)

# NeuroLumen Workflow Pathway: Frontend Model
st.markdown("<h2 style='color: #B8860B;'>Frontend Model</h3>", unsafe_allow_html=True)
st.markdown("""
    <div class="pathway">
        <div class="step frontend">
            <p>User Interaction</p>
            <div class="description">Uploads images and performs tests for diagnosis.</div>
        </div>
        <div class="step frontend">
            <p>Diagnosis</p>
            <div class="description">Receives a diagnosis based on uploaded data.</div>
        </div>
        <div class="step frontend">
            <p>Information</p>
            <div class="description">Provides detailed information and recommended actions.</div>
        </div>
    </div>
""", unsafe_allow_html=True)











# White Section
st.markdown("<h2 style='text-align: center; color: #1768AC; font-size: 42px;'>Why Neurolumen?</h2>", unsafe_allow_html=True)

































st.markdown("""
    <style>
        /* Define a specific light blue color */
        .custom-light-blue {
            background-color: #BFE6FF; /* Lighter shade of blue */
            padding: 20px;
            margin-bottom: 20px;
            border-radius: 10px; /* Rounded corners */
            border: 2px solid #ADD8E6; /* Border color */
        }

        /* Flex container to arrange sections horizontally */
        .flex-container {
            display: flex;
            justify-content: space-between;
        }

        /* Style for each individual section */
        .section {
            flex: 1;
            padding: 20px;
            margin: 0 10px; /* Add some spacing between sections */
        }

        /* Apply larger font size to headers */
        .section h2 {
            font-size: 36px;
            color: #1768AC; /* Adjust text color */
        }

        /* Apply larger font size to paragraph */
        .section p {
            font-size: 24px;
            color: black;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown(
    """
    <div class="flex-container">
        <div class="custom-light-blue section">
            <h2>Diagnose</h2>
            <p>Our solution uses Low Field MRI and advanced ensemble learning techniques to provide Alzheimer's diagnoses.</p>
        </div>
        <div class="custom-light-blue section">
            <h2>Access</h2>
            <p>Experience the ease of diagnosis from the comfort of your home.</p>
        </div>
        <div class="custom-light-blue section">
            <h2>Impact</h2>
            <p>By enabling early intervention, we empower individuals and healthcare providers to manage Alzheimer's more effectively.</p>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)









st.markdown("""
    <style>
        /* Define a specific light blue color */
        .custom-light-blue {
            background-color: #BFE6FF; /* Lighter shade of blue */
            padding: 20px;
            margin-bottom: 20px;
            border-radius: 10px; /* Rounded corners */
            border: 2px solid #ADD8E6; /* Border color */
        }

        /* Flex container to arrange sections horizontally */
        .flex-container {
            display: flex;
            justify-content: space-between;
            flex-wrap: wrap;
        }

        /* Style for each individual section */
        .section {
            flex: 1;
            padding: 20px;
            margin: 0 10px; /* Add some spacing between sections */
            max-width: 400px; /* Set maximum width for consistency */
        }

        /* Apply larger font size to headers */
        .section h2 {
            font-size: 36px;
            color: #1768AC; /* Adjust text color */
        }

        /* Apply larger font size to paragraph */
        .section p {
            font-size: 24px;
            color: black;
        }

        /* Team member name style */
        .team-name {
            font-size: 28px;
            font-weight: bold;
            margin-bottom: 10px;
        }
        
        /* Image style */
        .team-img {
            max-width: 100%;
            border-radius: 10px; /* Rounded corners for images */
            margin-bottom: 10px;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h2 style='text-align: center; color: #1768AC; font-size: 42px;'>Meet the Team</h2>", unsafe_allow_html=True)

# Creating a grid for images and descriptions
st.markdown(
    """
    <div class="flex-container">
        <div class="custom-light-blue section">
            <img class="team-img" src="https://i.postimg.cc/756wT6Y2/abigail-chiang.jpg" alt="Abigail Chiang">
            <h2 class="team-name">Abigail Chiang</h2>
            <p>Abby is a sophomore from Palos Verdes Peninsula High School, from the South Bay with a deep passion for the intersection of AI and technology. Alongside her work with Neurolumen, she aims to bridge the gap in STEM education and foster creativity and innovation for a brighter future.</p>
        </div>
        <div class="custom-light-blue section">
            <img class="team-img" src="https://i.postimg.cc/xJC9L1P7/kaashvi.jpg" alt="Kaashvi">
            <h2 class="team-name">Kaashvi Mittal</h2>
            <p>Kaashvi is a sophomore at Saint Francis High School, who is interested in artificial intelligence and computer science. As a leader of her school’s Girls Who Code Club, she teaches a variety of programming languages to other students through hands-on labs and coding activities...</p>
        </div>
        <!-- Add other team members here -->
    </div>
    """,
    unsafe_allow_html=True
)































