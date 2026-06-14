import ollama
import streamlit as st

st.title("AI Interview Prep Coach")

job_role = st.text_input("Enter the Job Role you are preparing for:")
question = st.text_input("Ask your interview question...")

def interview_coach(job_role, question):
    response = ollama.chat(
        model='mistral',
        messages=[
            {
                'role': 'system',
                'content': f"""You are an expert interview coach specializing in {job_role} roles.
                rules:
                    - Be encouraging and constructive
                    - Give clear, structured answers with bullet points
                    - For technical questions, provide code examples when relevant
                    - For behavioral questions, use the STAR method (Situation, Task, Action, Result)
                    - Keep answers concise and interview-ready
                    - End with a quick tip to improve the answer
                """
            },
            {
                'role': 'user',
                'content': question
            }
        ]
    )
    return response['message']['content']

if st.button("Send"):
    st.write(interview_coach(job_role, question))
