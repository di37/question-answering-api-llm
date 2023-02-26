# Building Harry Potter based Question and Answering API

## Motivation

After release of ChatGPT, a lot of people have asked why not we get specific bots for specific area of interest. In this project, we will be building an API that will answer questions about Harry Potter related questions from Harry Potter books.

## Brief Introduction about LangChain and GPT Index

Use of large language models (LLMs) is becoming increasingly prevalent in the development of powerful applications. These models allow developers to build applications that were not previously possible due to their ability to understand and process natural language. However, while LLMs on their own are impressive, their true potential lies in their ability to be combined with other sources of computation or knowledge. This is where this library - **langchain** comes in. It aims to assist developers in the creation of such applications by providing tools to combine large language models with other sources of information. Through this combination, developers can unlock the full potential of LLMs and create truly transformative applications.

**GPT Index (LlamaIndex 🦙)**, is a collection of data structures that simplify the usage of large external knowledge sources with large language models.

These two libraries will enable us to build question and answering model by accessing LLM and fine-tune it for our purpose. 

## Setup before Running the Docker Container
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
- Ensure the items folder have structure like this:
```bash
items
├── data
│   └── harry_potter_corpora_1_to_7.txt
└── index_folder
    └── index.json
```

