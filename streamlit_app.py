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

st.markdown("<br><br>", unsafe_allow_html=True)


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



st.markdown("<br><br>", unsafe_allow_html=True)








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





st.markdown("<br><br>", unsafe_allow_html=True)


st.markdown(
    """
    <style>
        /* Additional style for team images to set a consistent width and height */
        .team-img {
            width: 200px; /* Adjust the width as needed */
            height: 200px; /* Adjust the height as needed */
            object-fit: cover; /* Maintain aspect ratio and cover the container */
            border-radius: 10px; /* Rounded corners for images */
            margin-bottom: 10px;
        }
    </style>
    <div class="flex-container">
        <div class="custom-light-blue section">
            <img class="team-img" src="https://i.imgur.com/lSN6v0S.jpeg" alt="Abigail Chiang">
            <h2 class="team-name">Abigail Chiang</h2>
            <p>Abby is a sophomore in high school with a deep passion for the intersection of AI and technology. Alongside her work with Neurolumen, she aims to bridge the gap in STEM education and foster creativity and innovation for a brighter future.</p>
        </div>
        <div class="custom-light-blue section">
            <img class="team-img" src="https://i.imgur.com/85TI2YJ.jpeg" alt="Kaashvi Mittal">
            <h2 class="team-name">Kaashvi Mittal</h2>
            <p>Kaashvi is a sophomore in high school, who is interested in artificial intelligence and computer science. As a leader of her school’s Girls Who Code Club, she teaches a variety of programming languages to other students through hands-on labs and coding activities...</p>
        </div>
        <div class="custom-light-blue section">
            <img class="team-img" src="https://i.imgur.com/KrjmJSt.png" alt="Parth Tornekar">
            <h2 class="team-name">Parth Tornekar</h2>
            <p>Parth is a senior in high school, and is interested in aeronautical engineering and international relations. Parth loves existing in the intersection between engineering and humanities. He loves Model UN, and has secretariated on six different continents...</p>
        </div>
        <div class="custom-light-blue section">
            <img class="team-img" src="https://i.imgur.com/bjTyLPA.png" alt="Aarav Minocha">
            <h2 class="team-name">Aarav Minocha</h2>
            <p>Aarav is a junior in high school, who is interested in neuroscience and philosophy. He is deeply interested in the intersection between tangible research and abstract concepts and ideas that can spring from scientific innovation...</p>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown("<br><br>", unsafe_allow_html=True)












st.markdown("""
    <style>
        /* Style for the FAQ section */
        .faq-section {
            display: flex;
            flex-wrap: wrap;
            justify-content: space-between;
        }

        /* Style for individual FAQ questions */
        .faq-question {
            flex-basis: 48%; /* Adjust the width as needed for two rows of four */
            padding: 20px;
            margin: 10px;
            background-color: #DCEEFB; /* Lighter blue background color */
            border-radius: 10px; /* Rounded corners */
            text-align: center;
            color: #1768AC; /* Adjust text color */
        }

        /* Adjust spacing for better aesthetics */
        .faq-section p {
            margin: 0;
        }

        /* Larger font size for question headings */
        .faq-question h3 {
            font-size: 18px; /* Adjust font size */
            margin-bottom: 10px;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h2 style='text-align: center; color: #1768AC;'>Frequently Asked Questions</h2>", unsafe_allow_html=True)

# Individual FAQ questions
st.markdown("""
    <div class="faq-section">
        <div class="faq-question">
            <h3><strong>Why was NeuroLumen created?</strong></h3>
            <p>The inception of NeuroLumen is rooted in personal experiences, as our team was motivated by witnessing the impact of Alzheimer's on our own family members. This heartfelt connection fuels our commitment to creating a solution that addresses the pressing need for accessible and early Alzheimer's diagnosis.</p>
        </div>
        <div class="faq-question">
            <h3><strong>What sets NeuroLumen apart from existing alternatives like SAGE?</strong></h3>
            <p>Unlike current alternatives such as the Self-Administered Gerocognitive Exam (SAGE), which primarily detect AD symptoms in later stages, NeuroLumen focuses on early diagnosis. By integrating Low Field MRI (LFM) technology and precise clinical assessments, our solution offers a unique and holistic approach for accurate, convenient, and home-based Alzheimer's diagnosis.</p>
        </div>
        <div class="faq-question">
            <h3><strong>Who is NeuroLumen for?</strong></h3>
            <p>Our target audience includes individuals in underserved regions with limited hospital access, especially those who face challenges with lengthy MRI scans. NeuroLumen brings the diagnostic experience to their homes, making it accessible and comfortable for early Alzheimer's detection.</p>
        </div>
        <div class="faq-question">
            <h3><strong>How will NeuroLumen reach its initial customers?</strong></h3>
            <p>NeuroLumen will utilize online channels to market itself as an accessible alternative for Alzheimer's diagnosis. The entire diagnostic process, including clinical tests with basic questions, can be conveniently completed at home. This approach aligns with our commitment to providing a user-friendly and home-based solution.</p>
        </div>
       
    </div>
""", unsafe_allow_html=True)

# Add some spacing after the FAQ section
st.markdown("<br><br>", unsafe_allow_html=True)





















import streamlit as st

# Contact Us Section
st.markdown("<h2 style='text-align: center; color: #1768AC; font-size: 42px;'>Contact Us</h2>", unsafe_allow_html=True)

# Centered Display of Google Form
google_form_url = "https://forms.gle/y4rZBxnSJMUoTpHi9"
st.markdown(
    f'<div style="display: flex; justify-content: center; align-items: center; height: 600px;">'
    f'<iframe src="{google_form_url}" width="800" height="600" frameborder="0" marginheight="0" marginwidth="0">Loading...</iframe>'
    f'</div>', 
    unsafe_allow_html=True
)


