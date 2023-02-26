import os, sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)))

from pydantic import BaseModel


class InputBody(BaseModel):
    """
    Class for representing query path.
    """

    query: str = ""
