# Building Harry Potter based Question and Answering API

## Motivation

After release of ChatGPT, a lot of people have asked why not we get specific question answer systems/bots for specific area of interest. In this project, we will be building an API that will answer questions about Harry Potter related questions from Harry Potter books.

## Brief Introduction about LangChain and GPT Index

Use of large language models (LLMs) is becoming increasingly prevalent in the development of powerful applications. These models allow developers to build applications that were not previously possible due to their ability to understand and process natural language. However, while LLMs on their own are impressive, their true potential lies in their ability to be combined with other sources of computation or knowledge. This is where this library - **langchain** comes in. It aims to assist developers in the creation of such applications by providing tools to combine large language models with other sources of information. Through this combination, developers can unlock the full potential of LLMs and create truly transformative applications.

**GPT Index (LlamaIndex 🦙)**, is a collection of data structures that simplify the usage of large external knowledge sources with large language models.

These two libraries will enable us to build question and answering model by accessing LLM and fine-tune it for our purpose.

## Running the API on Docker Container

- Sign up in OpenAI website and get your API key.
- `.env` must contain the OPENAPI KEY and paths. Sample included. For production purpose, .env file should be included in .gitignore file.
- Run the docker container:

```bash
docker compose up
```

- If any changes made to the code, then run following command for the code changes to be reflected in the docker container.Then, we can run the above command.

```bash
docker compose build
```

- On your web browser, go to `http://localhost:9001/docs` and you will see the documentation.
  ![alt text](https://github.com/di37/question-answering-api-llm/blob/main/items/screenshots/FastAPI_Docs.png?raw=true)
- Make POST request for generating index file.
  ![alt text](https://github.com/di37/question-answering-api-llm/blob/main/items/screenshots/Generating_Index_File.png?raw=true)
- If index file is generated, then we will get following response.
  ![alt text](https://github.com/di37/question-answering-api-llm/blob/main/items/screenshots/Success_Message_For_Generation.png?raw=true)
- Ensure the items directory is having following tree structure:

```bash
items
├── data
│   └── harry_potter_corpora_1_to_7.txt
└── index_folder
    └── index.json
```

- Now we are ready to ask questions to the system for which also, we need to make POST request. Sample as follows.
  ![alt text](https://github.com/di37/question-answering-api-llm/blob/main/items/screenshots/answer_sample_1.png?raw=true)

## Resources

- LangChain Library: https://github.com/hwchase17/langchain
- GPT-Index Library: https://github.com/jerryjliu/gpt_index
- Video Tutorial: https://www.youtube.com/watch?v=Dhc_fq5iCnU&t=106s&ab_channel=1littlecoder
- Harry Potter - Books 1 - 7. By J.K Rowling.

## Important Note

This project is created exclusively for educational purpose. Data is strictly not to be used for commercial purposes.
