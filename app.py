# Import necessary libraries
import streamlit as st

# Define questions and answers (this can be expanded or loaded from a database)
questions = [
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
    }
]

# Set the title of the app
st.title("Physics Review Questions")

# Function to load questions
def load_question(index):
    q = questions[index]
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
for i, q in enumerate(questions):
    user_answer, correct_answer = load_question(i)
    if st.button(f"Submit Answer for Question {i+1}"):
        check_answer(user_answer, correct_answer)

# Optionally, add a summary or score feature
if st.button("Show Summary"):
    correct_count = sum(1 for i, q in enumerate(questions) if st.session_state.get(f"question_{i}") == q['answer'])
    st.write(f"You answered {correct_count} out of {len(questions)} questions correctly!")
