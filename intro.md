In this hackathon we will be creating our own chatbot using a technique called Retrieval Augmentation Generation (RAG). 
This technique allows you to upload you own sources of data and use that in conjunction with LLMs to query your data in a chat-like manner, without the need of fine-tuning the LLM.

Once you have uploaded your data,  its content is split into chunks and each chunk is embedded into a vector database. When a query is sent to the LLMs, a similarity search between the prompt and the vector database is performed, and the $k$ most relevant document chunks is added to the prompt as a hidden context (default is $k = 4$). This provides the model with relevant context from your data based on your prompt, without the need of fine-tuning the model on own data sources, which is typically very expensive and time consuming - in particular in the reign of LLMs.

Be aware that we are using the OpenAI API for calling the LLM (`gpt-3.5-turbo`), and all prompts are sent to their servers in the USA where they will be kept solely for abuse and misuse monitoring purposes for maximum 30 days. Consequently, we should not upload any sensitive nor proprietary documents. 
