import streamlit as st
import emoji
from langchain_ollama import ChatOllama

st.title("🤖 LLMS Chatboot ")

st.write("Desenvolvido para fins educacionais")

with st.form("llm-form"):
    text = st.text_area("Entre com seu texto")
    submit = st.form_submit_button("Enviar")

def generate_response(input):
    model = ChatOllama(model='llama3.2', base_url="http://localhost:11434/")
    response = model.invoke(input)

    return response.content

if "chat_history" not in st.session_state:
    st.session_state['chat_history'] = []

if submit and text:
    with st.spinner("Gerando a Resposta ... "):
        response = generate_response(text)
        st.session_state['chat_history'].append({"user":text,
                                                 "ollama":response})
        st.write(response)

st.write("## Chat History ## ")   
for chat in st.session_state['chat_history']:
    st.write(f"**🙂 user**: {chat['user']}")
    st.write(f"**🤖 Assitante**: {chat['ollama']}")
    st.write("------")