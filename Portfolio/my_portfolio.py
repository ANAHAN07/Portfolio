import streamlit as st

# Task 1

# Set the page title and icon
st.set_page_config(page_title="My Portfolio", page_icon="🤑")

# Task 2

# Navigation Bar
st.sidebar.title("Navigation")
pages = ["Home", "About Me", "Projects", "Skills", "Contact"]
page = st.sidebar.radio("Go to", pages)

# Task 3

# Home Page
if page == "Home":
    st.title("Welcome to My Portfolio")
    st.subheader("""
AN Productions\n
---Turning Ideas into Reality
""")
    
    st.markdown("""
Hi! I'm **Ahnaf Mahmud**, a passionate freelancer and developer specializing in __Python, HTML, data scraping, and digital marketing__. With experience in __B2B lead generation, SEO, automation, and content creation__, 
I help businesses grow by providing efficient and high-quality solutions.
Currently, I'm a student at **Wills Little Flower School and College**, continuously learning and expanding my expertise. 
I have completed various training programs, including Python with __Songjog Foundation__ and freelancing courses from __ETDP__.
Explore my portfolio to see my work, projects, and skills! 🚀
""")


# About Me Page
elif page == "About Me":
    st.header("About Me")
    st.write("""
I am **Ahnaf Mahmud Towseem Ahan**. A **Student** & Part time freelancer, with expertise in **Python, HTML, Java, and digital marketing**. Currently,
I'm studying in Class 10 English Version on Science department at __Wills Little Flower School and College__. 
I have completed various freelance training courses from __ETDP__ and am also learning **Python** through __Songjog Foundation__.
My goal is to help businesses with high-quality design, development, and marketing solutions.
""")

    # Task 4

    # Load images
    # image_1 = "myself.png"  # Replace with your actual image path
    # image_2 = "an_production.png"  # Replace with your actual image path

    # # Create two columns
    # col_1, col_2 = st.columns([2, 1])  # Adjust width ratio if needed

    # # Display images
    # with col_1:
    #     st.image(image_1, caption="My Self", width=350)

    # with col_2:
    #     st.image(image_2, caption="My Logo", width=350)


# Projects Page
elif page == "Projects":
    st.header("Projects")
    st.write("Showcaseing my best work with descriptions and links!!")

    # Project 1
    st.subheader("Project 1: Grocery List Manager")
    st.write("""
Description:\n
Grocery List Manager is a simple yet efficient tool to help users keep track of their grocery items. 
It allows users to add, remove, and manage their shopping lists with ease.
""")
    st.write("""
Features:\n  
    1. Items available in the grocery shop            
    2. Add item to the grocery list
    3. Remove item from the grocery list
    4. View current grocery list 
    5. Check if an item is in the list
    6. Display total number of items
    7. Exit
    8. Admin Panel
         * View shop inventory
         * Add item to shop inventory
         * Back to main menu
""")
    # st.image("project_1_img_1.png", caption="Project 1 | Main Menu", width=350)
    # st.image("project_1_img_2.png", caption="Project 1 | Shop Inventory", width=350)
    # st.image("project_1_img_3.png", caption="Project 1 | Admin Panel", width=350)
    st.markdown("[GitHub Project Link](https://github.com/ANAHAN07/Project-from-songjog-course/tree/main/Grocery%20list%20manager)")            # Task 4

    st.write("---")

    # Project 2
    st.subheader("Project 2: Task Manager and Utility Tools")
    st.write("""
Description:\n
A comprehensive Python-based project that integrates task management, utility calculations, and other productivity tools, all in a user-friendly interface. 
This program is designed to assist users in managing their tasks, performing advanced calculations, measuring utility usage, and more, with seamless functionality and data persistence.
""")
    st.write("""
Features:\n
    1. Login
    2. Register
    3. Exit
       1. Add Task
       2. View Tasks
       3. Update Task
       4. Delete Task
       5. Advanced Calculator
       6. Measurement Calculator
       7. Word Counter
       8. Email Saver
       9. Utiliti Bills Calculator
       10. Exit                                                                           
""")
    # st.image("project_2_img_1.png", caption="Project 2 | Login/Register", width=350)
    # st.image("project_2_img_2.png", caption="Project 2 | Main Menu", width=350)
    st.markdown("[GitHub Project Link](https://github.com/ANAHAN07/Project-from-songjog-course/tree/main/Personal%20Task%20Manager%20with%20Insights)")

    st.write("---")

    # Game 1
    st.subheader("Game 1: Catch the Ball")
    st.write("""
Description:\n
"Catch the Ball" is a simple yet fun arcade-style game built using Python and Pygame. 
The goal of the game is to move the basket left and right to catch the falling ball.
As the score increases, the ball's speed increases, making the game more challenging.
""")
    st.write("""
Features:\n
    1.🎮 Smooth gameplay experience
    2.⏳ Increasing difficulty as you score higher
    3.🏆 Score tracking system
    4.🎨 Simple and clean UI         
""")
    # st.image("game_1_img_1.png", caption="Game 1 | Playing", width=350)
    # st.image("game_1_img_2.png", caption="Game 1 | Game Over", width=350)
    st.markdown("[GitHub Game Link](https://github.com/ANAHAN07/My-Games/tree/main/Catch_the_ball)")

# Skills Page
elif page == "Skills":
    st.header("Skills")
    st.write("Here are some of the skills I possess!!")
    st.write("""
I have expertise in Python and HTML for web development, 
along with strong skills in SEO and digital marketing.
I also offer services in data scraping, lead generation,
and automation to help businesses streamline their operations.
""")

    # List of Skills
    skills = ["Python (Road to Advance)", "HTML (Road to Advance)", "JAVA (Basic)", "Data Analysis", "SEO Research", "Lead Generation", "Canva Design"]
    st.write(skills)

    st.write("---")

# Contact Page
elif page == "Contact":
    st.header("Contact Me")
    st.write("Feel free to reach out to me")
    st.write("""
Contact:\n        
Email: 📧 ahnaftowseem2021@gmail.com\n
[GITHUB](https://github.com/ANAHAN07)\n
[Linkdin](https://www.linkedin.com/in/ahnaf-mahmud-1aa780327)\n
[AyKori](https://aykori.com/freelancer/an_studio)\n
[Fiverr](https://www.fiverr.com/users/an_digital_hub)\n
[Instagram](https://www.instagram.com/its.me.memebd)
""")

    # Bonus

    with st.form(key='contact_form'):
        name = st.text_input("Name")
        email = st.text_input("Email")
        message = st.text_area("Message")
        submit_button = st.form_submit_button(label='Submit')

        if submit_button:
            st.write("Thank you for reaching out! I will get back to you soon.")

# Ownership
st.write("Copyright © 2025 [Ahnaf Mahmud Towseem Ahan](https://www.facebook.com/ahnafNahan). [All rights reserved](https://github.com/ANAHAN07/Portfolio/blob/main/LICENCE).")      # LICENSE AND OWENERSHIP