from typing import List, Dict, Tuple, Any
import openai
from pypdf import PdfReader
from openai.error import InvalidRequestError
from langchain.docstore.document import Document
from langchain.vectorstores.faiss import FAISS
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import SentenceTransformerEmbeddings
import streamlit as st


def get_gpt_response(
    messages: List[Dict[str, str]],
    model="gpt-3.5-turbo",
) -> Tuple[str, int, int, int]:
    """Function that get the gpt response using the messages and input

    The goal here is to fill in the blanks for the 'chat_completion' and 'response' variables.

    A parameter we can play around with that will impact the response is 'temperature', so
    find a suitable value for your use-case.

    We can also change the model to 'gpt-4', but note that this will
    make the cost estimates implemented in 'app/chatbot.py' invalid.
    See https://openai.com/pricing for more info.

    Extra challenge: Add a streamlit widget on the dashboard (in app/chatbot.py) that
    allows the user to specify the temperature.

    Hint: Look at the python sdk documentation from OpenAI, or just ask your favorite chatbot :)
    https://platform.openai.com/docs/libraries/python-library

    Args:
        messages (List[Dict[str, str]]): List of messages
        model (str, optional): OpenAI model to use. Defaults to "gpt-3.5-turbo".

    Raises:
        Exception: if the request sent to OpenAI is invalid

    Returns:
        Tuple[str, int, int, int]: Tuple with the response and tokens for cost estimation
    """
    try:
        # FIXME: Use the openai library to get the chat_completion
        chat_completion = None

    except InvalidRequestError as e:
        raise Exception(
            f"Invalid request to OpenAI. See the following error message to troubleshoot: {e}"
        )
    total_tokens = chat_completion.usage.total_tokens
    prompt_tokens = chat_completion.usage.prompt_tokens
    completion_tokens = chat_completion.usage.completion_tokens

    # FIXME: Use chat_completion variable to get the content of the response
    response = None

    return response, total_tokens, prompt_tokens, completion_tokens


def update_chat(
    messages: List[Dict[str, str]],
    role: str,
    content: str,
) -> List[Dict[str, str]]:
    """Updates the chat according to a role and content

    The goal here is to update the list of chat messages.

    Hint: A single message is a dictionary with two keys, namely 'role' and 'content'.
    Refer to the OpenAI documentation if youre stuck on the format, or just ask your favorite chatbot :)

    Args:
        messages (List[Dict[str, str]]): list of messages
        role (str): Either 'user', 'assistant' or 'system'
        content (str): Content of chat, either prompt or response

    Returns:
        List[Dict[str, str]]: Updated list of messages
    """
    # FIXME: Update the variable passed as the messages argument to update the chat
    return messages


def add_context(
    messages: List[Dict[str, str]],
    content: str,
) -> List[Dict[str, str]]:
    """Function that adds context to the list of messages

    Hint: Context can be added by assigning the 'system' role to a message

    Args:
        messages (List[Dict[str, str]]): list of messages
        content (str): context

    Returns:
        List[Dict[str, str]]: upated list of messages
    """
    # FIXME: Update messages such that context is added
    return messages


@st.cache_data
def get_embeddings() -> SentenceTransformerEmbeddings:
    """Function that will get and cache embeddings

    # Hint: Look at the langchain documentation about Sentence Transformers Embeddings
    (https://python.langchain.com/docs/integrations/text_embedding/sentence_transformers)
    Returns:
        SentenceTransformerEmbeddings: embeddings
    """
    # FIXME: Update the below variable to get the embeddings
    embeddings = None
    return embeddings


@st.cache_data
def parse_pdf(file: Any) -> str:
    """Function that parses an uploaded file and returns the content as a string

    Hint: There are a lot of ways to do this, one of which leverages
        the PdfReader class from the pypdf library.
        If in doubt, just ask your favorite chatbot :)
    Args:
        file (Any): uploaded file (using streamlit widget)

    Returns:
        str: parsed file
    """
    return "parsed pdf"


@st.cache_data
def split_document_into_chunks(document: str) -> List[str]:
    """Function that takes a parsed file as input and returns
    a list of chunks of the input file.

    There are typically two parameters one can play around with when
    it comes to text spltiter, namely 'chunk_size' and 'overlap'.
    Consequently, this might require some tuning.

    Extra challenge: Add widgets to the dashboard in 'app/chatbot.py'
    allowing the user to specify the value of those parameters
    before uploading a file for RAG.


    Hint: Check out the langchain documentation about text splitters
    (https://python.langchain.com/docs/modules/data_connection/document_transformers/text_splitters/recursive_text_splitter)

    Args:
        document (str): parsed document

    Returns:
        List[str]: list of chunks
    """
    # FIXME: implement this
    chunks = None
    return chunks


@st.cache_data
def embed_chunks(
    chunks: List[str],
    _embeddings: SentenceTransformerEmbeddings,
) -> FAISS:
    """Function that will create an in-memory vector database based on chunks
    of an uploaded document.

    Hint: Check out the langchain documentation for FAISS
    (https://python.langchain.com/docs/integrations/vectorstores/faiss)

    Args:
        chunks (List[str]): chunks of the uploaded document
        _embeddings (SentenceTransformerEmbeddings): embeddings for embedding
            the input chunks

    Raises:
        Exception: If something fails when creating the index

    Returns:
        FAISS: index with embedded vectors
    """

    try:
        # FIXME: implement how to get the FAISS index
        index = None
    except Exception:
        raise Exception(
            "Failed to create vector embedding from the uploaded document. Please try another document"
        )
    return index


def get_relevant_docs(
    index: FAISS,
    prompt: str,
) -> List[Document]:
    """Function that performs a similarity search between an index and a query

    Hint: The FAISS index has built-in similary-search

    Args:
        index (FAISS): vector database containing embedded chunks
            of the uploaded data
        prompt (str): prompt sent to OpenAI

    Returns:
        List[Document]: List of the most relevant documents from the
            vector database based on the prompt
    """
    # FIXME: implement how to perform the similarity search
    relevant_docs = None
    return relevant_docs
