# Hackathon 
This repo contains some boilerplate code for setting up a custom chatbot that you can use to chat with your own sources of data. We will use the OpenAI API to send requests to their models, either `gpt-3.5-turbo` or `gpt-4`, which we will connect with our own data sources using Retrieval Augmentation Generation. 

Be aware that this setup sends requests over the OpenAI API, and as such the prompts are stored on OpenAIs servers in USA for max 30 days to monitor for abuse and misuse. Consequently, we should not use this setup to upload sensitive nor proprietary data.

## Introduction 
In this hackathon we will set up our own custom chatbot leveraging the OpenAI API. Moreover, we will use the Retrieval Augmentation Generation (RAG) technique to allow us to query our own data sources without having to fine-tune the LLM. 

We will setup our chatbot in a [streamlit](https://docs.streamlit.io/library/get-started) dashboard, using a chat interface from [stremlit-chat](https://pypi.org/project/streamlit-chat/). Moreover, we use the open AI [api](https://platform.openai.com/docs/api-reference/introduction?lang=python) for sending requests to the LLM, as well as components from the [langchain](https://docs.langchain.com/docs/) library. Important components are an in-memory vector database and similarity search using [FAISS](https://github.com/facebookresearch/faiss), text splitters and embeddings. 

The chatbot interface and flow is defined in `app/chatbot.py`, and all utilities are defined in `utils/utils.py`. The boilerplate code will import some core functions from the utilities module, and its up to you to fill in the remaining code.

The flow presented in `app/chatbot.py` is just a suggestion, feel free to modify it as you wish. However, keep in mind that the RAG technique follow the these steps:
1) Parse uploaded document
2) Split document into smaller chunks: Need to consider chunksize and amount of overlap 
3) Embed the chunks and setup a vector database
4) Perform a similarity search between your prompt and the vector database to extract the $k$ most relevant chunks to your prompt
5) Add the results of the similarity search to the hidden context, or system role, to the LLM.


### Useful resources

[Streamlit API reference](https://docs.streamlit.io/library/api-reference)

[OpenAI API reference](https://platform.openai.com/docs/api-reference/introduction?lang=python)
- [Chat completion object](https://platform.openai.com/docs/api-reference/chat/create)

- [Embeddings](https://platform.openai.com/docs/guides/embeddings/what-are-embeddings)

[Langchain Python docs](https://python.langchain.com/docs/get_started/introduction.html)

- [FAISS Vector Database](https://python.langchain.com/docs/integrations/vectorstores/faiss)

- [Sentence Transformers Embeddings](https://python.langchain.com/docs/integrations/text_embedding/sentence_transformers)

- [Recursive Character Text Splitter](https://python.langchain.com/docs/modules/data_connection/document_transformers/text_splitters/recursive_text_splitter)


## Getting Started


### Setup environment
The boilerplate code was developed using python 3.9.4, so I would recommend to use the same version to avoid potential errors due to a mismatch in environments.

Make sure you have poetry installed on your system. If not, visit [their documentation](https://python-poetry.org/docs/).

To set up your environment run the following from the CLI
```console
poetry intstall
```
The above command will go through the `pyproject.toml` and `poetry.lock` files and install all the specified packages and dependencies in a new environment. 

### Authenticate to OpenAI
We need to authenticate to OpenAI to send requests to their servers. To do so simply create a file called `.env` and populate it with `OPENAI_API_KEY=<your api key goes here>`.


### Running the dashboard
We use streamlit to setup a custom chat-interface. To run the dashboard locally you simply run 
```console
streamlit run app/chatbot.py
```

Voila - your chatbot is now up an running on your localhost!




## Nomenclature
CLI - Command-line interface

LLM - Large Language Model 

RAG - Retrieval Augmentation Generation 
