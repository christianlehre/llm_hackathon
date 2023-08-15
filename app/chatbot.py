import os
import sys
import streamlit as st 
from streamlit_chat import message
from dotenv import load_dotenv
import openai
from pathlib import Path 
root = Path(__file__).parent.parent
if str(root) not in sys.path:
    sys.path.append(str(root))
from utils.utils import get_gpt_response, update_chat, add_context, split_document_into_chunks, embed_chunks, get_relevant_docs, parse_pdf, get_embeddings

load_dotenv()
openai.api_key=os.environ.get("OPENAI_API_KEY")

def send_prompt():
    st.session_state.send_prompt = True

def prompt_not_sent():
    st.session_state.send_prompt = False

st.title("Welcome to your custom OpenAI chatbot!")
with open("intro.md", "r") as f:
    intro = f.read()

st.markdown(intro)
st.markdown("---")

# initialize session state variables - these are setup to allow configurations ans chat messages to persist when interacting with the dashboard
if "send_prompt" not in st.session_state:
    st.session_state["send_prompt"] = False

if "generated" not in st.session_state:
    st.session_state["generated"] = []

if "history" not in st.session_state:
    st.session_state["history"] = []

if "context" not in st.session_state:
    st.session_state["context"] = ""

if "messages" not in st.session_state:
    st.session_state["messages"] = []

if "context_added" not in st.session_state:
    st.session_state["context_added"] = False

if "total_cost" not in st.session_state:
    st.session_state["total_cost"] = 0.0

with st.sidebar:
    st.title("Reset chatbot")
    st.write("Click below button to reset the chatbot and clear the chat history")
    remove_history = st.button("Clear chat history", key="remove_history", on_click=prompt_not_sent)
    st.markdown("---")
if remove_history:
    st.session_state["history"] = []
    st.session_state["generated"] = []
    st.session_state["messages"] = []
    st.session_state["context"] = ""
    st.session_state["user_prompt"] = ""
    st.session_state["context_input"] = ""
    st.session_state["total_cost"] = 0.0
    

with st.sidebar:
    st.title("Set Context")
    st.write('In the below text field you can specify the wanted behaviour of your chatbot')
    context = st.text_area("Enter the context for your chatbot", key="context_input",placeholder='E.g. "I want you to act as an expert Python programmer"', on_change=prompt_not_sent)
    if context != "":
        st.session_state["context"] = context.strip()
    clear_context = st.button("Clear Context", on_click=prompt_not_sent)

    st.markdown("---")
    st.title("Upload Data")
    st.write("Be careful to not upload sensitive and proprietary data, as requests are sent the OpenAI servers")
    uploaded_file = st.file_uploader(label="Upload file",type= ["pdf"], on_change=prompt_not_sent)

    st.markdown("---")

if clear_context:
    if st.session_state.context_added:
        st.info("Chatbot context removed")
        st.session_state.messages = [message_ for message_ in st.session_state.messages if message_["role"] != "system"]
    st.session_state["context"] = []

st.session_state.context_added = sum([True if message_["role"] == "system" else False for message_ in st.session_state.messages]) != 0
if len(st.session_state.context) != 0 and not st.session_state.context_added:
    st.session_state["messages"] = add_context(st.session_state.messages, content=st.session_state.context)
    st.session_state.context_added = True

vector_db = None
if uploaded_file is not None: 
    with st.spinner("Reading document and embedding to a vector store"):
        embeddings = get_embeddings()
        document = parse_pdf(uploaded_file)
        chunks = split_document_into_chunks(document)
        vector_db = embed_chunks(chunks, embeddings)

cost = None
prompt = st.text_input("Enter your prompt here", key="user_prompt", on_change=send_prompt)
if prompt and st.session_state.send_prompt is True:
    with st.spinner("Generating response..."):
        if vector_db is not None:
            relevant_docs = get_relevant_docs(vector_db, prompt)
            context_window_list = [doc.page_content for doc in relevant_docs]
            context_window = ''.join(context_window_list)
            if st.session_state.context_added:
                context_window = st.session_state.context + "\n" + context_window
            
            add_context(messages=st.session_state.messages, content=context_window)
        messages = st.session_state["messages"]
        messages = update_chat(messages=messages, role="user", content=prompt)

        # The tokens are only needed for estimating conversation cost
        response, total_tokens, prompt_tokens, completion_tokens = get_gpt_response(messages=messages)

        # The below cost is estimated based on the gpt-3.5-turbo model. Other rates apply to e.g. gpt-4.
        cost = (prompt_tokens * 0.0015 + completion_tokens * 0.002) / 1000
        st.session_state.total_cost += cost
        messages = update_chat(messages=messages, role="assistant", content=response)
        st.session_state.history.append(prompt)
        st.session_state.generated.append(response)

if len(st.session_state.generated) != 0:
    # Print chat conversation
    for i in range(len(st.session_state.generated)-1, -1 ,-1):
        message(st.session_state.history[i], is_user=True, key=str(i) + "_user")
        message(st.session_state.generated[i], key=str(i))

with st.expander("Cost of conversation"):
    if cost is None:
        st.write(
            f"Total cost of conversation: \${st.session_state.total_cost:.5f}"
        )
    else: 
        st.write("Cost of previous query: \${:.5f}".format(cost))
        st.write("Total cost of conversation: \${:.5f} ".format(st.session_state.total_cost)) 

with st.expander("Message history"):
    st.write(st.session_state.messages)