import os
from dotenv import load_env
load_env()

GROQ_API_KEy= os.getenv("GROQ_API_KEY")
GROQ_MODEL_NAME=os.getenv("GROQ_MODEL_NAME")

EMBEDDING_MODEL=os.getenv("EMBEDDING_MODEL")
