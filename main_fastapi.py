from fastapi import FastAPI
from fastapi.responses import JSONResponse

from src import *
from utils import *

app = FastAPI()


@app.post(
    "/generate_index_file",
    description="This endpoint is used to call function that will fine-tune LLM embeddings.",
)
async def generate_index_file():
    try:
        response = ConstructIndex()
        return response
    except ValueError as e:
        return JSONResponse(content={"Error": str(e)}, status_code=400)
    except Exception as e:
        return JSONResponse(content={"Error": "Internal Server Error"}, status_code=500)


@app.post(
    "/ask_bot",
    description="This endpoint is used to call function that will allow the user to ask question and it will retrieve answer.",
)
async def ask_bot(inputBody: InputBody):
    try:
        response = AskBot(inputBody.query)
        return response
    except ValueError as e:
        return JSONResponse(content={"Error": str(e)}, status_code=400)
    except Exception as e:
        return JSONResponse(content={"Error": "Internal Server Error"}, status_code=500)
