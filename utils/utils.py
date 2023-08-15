import openai
from pypdf import PdfReader
from openai.error import InvalidRequestError
from langchain.vectorstores.faiss import FAISS
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import SentenceTransformerEmbeddings
import streamlit as st 

def update_chat(messages, role, content):
    pass

def add_context(messages, content):
    pass

def get_gpt_response(messages, model="gpt-3.5-turbo"):
    pass

@st.cache_data
def get_embeddings():
    pass

@st.cache_data
def parse_pdf(file):
    pass

@st.cache_data
def split_document_into_chunks(document):
    pass

@st.cache_data
def embed_chunks(chunks, _embeddings):
    pass

def get_relevant_docs(index, query):
    pass