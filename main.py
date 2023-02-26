import os

# Spinning FastAPI server
os.system("uvicorn main_fastapi:app --reload --host 0.0.0.0 --port 3000")