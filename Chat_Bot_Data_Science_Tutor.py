import streamlit as st
from langchain_google_genai import GoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

chat_model = GoogleGenerativeAI(model="models/gemini-2.0-pro-exp", api_key="Your_API_Key_Here")

chat_template = ChatPromptTemplate.from_messages([
    ("system", "You are an expert AI tutor specializing in Data Science. Provide accurate explanations and relevant code examples. If a query is unrelated to Data Science, kindly redirect the user to relevant topics."),
    ("human", "{human_input}")
])

output_parser = StrOutputParser()

st.set_page_config(page_title="AI Data Science Tutor", layout="wide")
st.title("🤖 AI Data Science Tutor")
st.write("Ask me anything related to Data Science!")

if "chat_history" not in st.session_state:
    st.session_state["chat_history"] = []

user_input = st.chat_input("Type your message:")

if user_input:
    query = {"human_input": user_input}
    response = chat_model.invoke(chat_template.format(**query))
    
    st.session_state["chat_history"].append((user_input, response))

st.write("### Chat History")
for human, ai in st.session_state["chat_history"]:
    st.write(f"**User:** {human}")
    st.write(f"**AI:** {ai}")
