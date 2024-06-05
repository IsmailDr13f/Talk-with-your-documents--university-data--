# Talk with your documents --university data-- 
# HERCULES 
![poseidon_1297826](https://github.com/IsmailDr13f/Talk-with-your-documents--university-data--/assets/128002689/07e6078a-2c47-4ac1-93a2-6b8c0ef38041)


## Project Objective

	The objective of this project is to develop an intelligent chatbot based on Retrieval-Augmented Generation (RAG), LangChain, and vector databases, fine-tuned 
	for a custom context using French language models (LLMs). The case study focuses on the Faculty of Sciences and Techniques of Tangier (FSTT). 
	This project aims to provide an interactive solution allowing users to ask questions about FSTT and receive accurate answers using various natural language 
	processing technologies.

## RAG vs Fine-Tuning

### RAG (Retrieval-Augmented Generation)
![Capture d'écran 2024-05-22 145804](https://github.com/IsmailDr13f/Talk-with-your-documents--university-data--/assets/128002689/c6570f94-08cb-47dc-bdde-32ed39db05e9)

		RAG combines text generation with information retrieval. This means that the model can first search for relevant documents in a database before 
		generating a response. This approach allows the chatbot to access a vast knowledge base and provide more informed and contextual answers.

### Fine-Tuning
![1_J058x7lmBME4fDT7V-rrZg](https://github.com/IsmailDr13f/Talk-with-your-documents--university-data--/assets/128002689/a566f475-b2ee-4432-b62d-d71c584b3f07)

		Fine-tuning involves training a pre-existing model on a specific dataset to adapt it to a particular context. In this project, we fine-tuned 
		language models on a small French corpus containing specific information about FSTT, enabling the chatbot to provide more precise and relevant 
		answers regarding this institution.

## Data Collection

	We collected data from the Faculty of Sciences and Techniques of Tangier website ([FSTT](https://fstt.ac.ma/Portail2023/)). The data includes:
		- Faculty description
		- Academic programs
		- Departments
		- Commissions
		- Faculty members
		- Clubs, etc.

	For this task, we used the BeautifulSoup library to extract the relevant information.

## Data Processing

### Split to Chunks

		We split the collected data into smaller chunks using the `langchain-text-splitters` library. This step is crucial for efficiently managing the data 
		and optimizing the retrieval and text generation process.

### Text-Embeddings

		To transform text chunks into vector representations, we used embedding models such as `sentence-transformers/all-MiniLM-L6-v2` from Hugging Face 
		and `nomic-embed-text` from Mistral. Embeddings allow us to represent texts in a way that language models can understand and process effectively.

### Vector Storage

		The generated vectors were stored in a vector database, such as ChromaDB or FAISS. These databases are optimized for fast and efficient 
		vector searches, which is essential for the RAG functionality.

## Language Models Used

	We worked with several large language models (LLMs), including:
		- Mistral
		- Llama2
		- Llama3
		- Gemma

	These models were selected for their ability to understand and generate French text with high accuracy.

## Prompt Techniques for Best LLM Responses

	We employed various prompt techniques to optimize LLM responses. This includes precise question formulation, providing additional context, and using 
	specific prompt templates to guide the models towards more relevant and informative answers.

## Web Application Development
![dark_mode user interface](https://github.com/IsmailDr13f/Talk-with-your-documents--university-data--/assets/128002689/9dc8241f-35cd-4a3b-9267-571e5f354271)
![light_mode user interface](https://github.com/IsmailDr13f/Talk-with-your-documents--university-data--/assets/128002689/6206f612-bcdd-4e1f-ac86-3696bc446ede)

	We developed a web application using Streamlit, Flask, and MongoDB. The application allows users to:
		- Enter their queries (questions about FSTT)
		- Choose the type of LLM to use
		- Save conversations
		- Review saved conversations at any time

	The application offers an intuitive and user-friendly interface, facilitating interaction with the chatbot and access to relevant information about FSTT.

## Limitations and Challenges

### Running Time

		The use of a GPU significantly reduced execution time from 17 minutes on a CPU to 2-4 minutes on a GPU.

### Hallucination

		We encountered issues with hallucination due to the quality of data, length of queries, and complexity of queries. This led to the generation 
		of incorrect or nonsensical responses at times.

### Hardware Resources

		Resource constraints, particularly RAM, posed challenges during the development process. Managing large datasets and running complex models 
		required substantial memory.

### Data Quantity

		The limited quantity of high-quality, specific data about FSTT affected the chatbot's ability to provide comprehensive answers. 
		More extensive data collection could improve performance and accuracy.

## Conclusion

	This project showcases the integration of advanced natural language processing and information retrieval techniques to develop an intelligent 
	chatbot tailored for the Faculty of Sciences and Techniques of Tangier (FSTT). By leveraging RAG, fine-tuning, and a robust infrastructure based on vector 
	databases, we created a chatbot capable of providing accurate and contextually relevant answers. 

	The development journey included significant achievements such as the reduction of processing times through GPU utilization and the effective use of various 
	language models. However, it also highlighted challenges like hallucination due to data quality and hardware constraints, emphasizing the need for continuous 
	improvement and optimization.

	Future enhancements could focus on expanding the data collection to cover more comprehensive information about FSTT, improving data quality to minimize 
	hallucinations, and further optimizing the hardware resources to handle larger datasets more efficiently. 
	Additionally, refining the prompt techniques and exploring more advanced LLMs could further enhance the chatbot's performance and user experience.
