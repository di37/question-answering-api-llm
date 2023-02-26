import os, sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)))

from gpt_index import GPTSimpleVectorIndex

from utils import *


def AskBot(query: str):
    """
    Asks the user a question and returns the response.

    Args:
        index_file_path (str): Path of index.json file.
        query (str): Question to be asked.

    Returns:
        dict: Response from the bot.
    """
    # Loading the created index.json file by providing its path.
    index = GPTSimpleVectorIndex.load_from_disk(INDEX_FILE_PATH)
    if query is None or len(query) == 0:
        raise Exception("Please provide a query.")
    else:
        response = index.query(query, response_mode="compact")
        return {"Response": str(response.response)}


# if __name__ == "__main__":
#     print(AskBot("What is Voldemort famous for?"))
