# Import necessary libraries
import streamlit as st
import random

# Define a pool of questions and answers (expandable or load from a database)
question_pool = [
    {
        "question": "What is the acceleration due to gravity on Earth?",
        "options": ["9.8 m/s^2", "10 m/s^2", "9.81 m/s^2", "8.9 m/s^2"],
        "answer": "9.8 m/s^2"
    },
    {
        "question": "What is the formula for kinetic energy?",
        "options": ["KE = 1/2 mv^2", "KE = mv", "KE = 1/2 mv", "KE = m^2v^2"],
        "answer": "KE = 1/2 mv^2"
    },
    {
        "question": "What is the speed of light?",
        "options": ["3 x 10^8 m/s", "1.5 x 10^8 m/s", "3 x 10^6 m/s", "2 x 10^8 m/s"],
        "answer": "3 x 10^8 m/s"
    },
    {
        "question": "What is Newton's second law of motion?",
        "options": ["F = ma", "F = mv", "F = m/a", "F = v/a"],
        "answer": "F = ma"
    },
    {
        "question": "Which of these is a scalar quantity?",
        "options": ["Velocity", "Force", "Speed", "Acceleration"],
        "answer": "Speed"
    }
]

# Set the title of the app
st.title("Physics Review Questions")

# Randomly select a subset of questions for each session
def get_random_questions(num_questions=3):
    return random.sample(question_pool, num_questions)

# Load the selected questions
selected_questions = get_random_questions()

# Function to load questions
def load_question(index):
    q = selected_questions[index]
    st.write(f"**Q{index+1}:** {q['question']}")
    user_answer = st.radio("Choose your answer:", q['options'], key=f"question_{index}")
    return user_answer, q['answer']

# Function to check answers
def check_answer(user_answer, correct_answer):
    if user_answer == correct_answer:
        st.success("Correct!")
    else:
        st.error(f"Incorrect. The correct answer is: {correct_answer}")

# Iterate through each question
for i, q in enumerate(selected_questions):
    user_answer, correct_answer = load_question(i)
    if st.button(f"Submit Answer for Question {i+1}", key=f"submit_{i}"):
        check_answer(user_answer, correct_answer)

# Optionally, add a summary or score feature
if st.button("Show Summary"):
    correct_count = sum(1 for i, q in enumerate(selected_questions) if st.session_state.get(f"question_{i}") == q['answer'])
    st.write(f"You answered {correct_count} out of {len(selected_questions)} questions correctly!")
