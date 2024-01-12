# NeuroLumen-Website

import streamlit as st

px;'>Why Neurolumen?</h2>", unsafe_allow_html=True)

































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
































