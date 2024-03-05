import streamlit as st

def main():
    st.title("Resume Builder")

    # Get user input
    name = st.text_input("Enter Your Name")
    email = st.text_input("Enter Your Email")
    experience = st.text_area("Work Experience")
    education = st.text_area("Education")
    skills = st.text_area("Skills")

    # Generate the resume
    resume = f"""
    Name: {name}
    Email: {email}

    Work Experience:
    {experience}

    Education:
    {education}

    Skills:
    {skills}
    """

    # Display the resume
    st.text_area("Your Resume", resume, height=400)

if __name__ == "__main__":
    main()
