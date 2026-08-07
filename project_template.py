import os
from pathlib import Path

# src ="RazorPay_Project_Rag"

structure_list=[

    f"src/__init__.py",
        f"src/logger.py",
        f"src/exception.py",
        f"src/config.py",

        f"src/components/__init__.py",
            f"src/components/data_ingestion.py",
            f"src/components/data_transformation.py",
            f"src/components/vector_store.py",
            f"src/components/llm.py",

        f"src/pipeline/__init__.py",
            f"src/pipeline/rag_pipeline.py",

    "app.py",
    "requirements.txt"
    ".env"
    "README.md"
]


for structure_items in structure_list:

    filepath= Path(structure_items)

    dir_name , file_name = os.path.split(filepath)

    if dir_name!="":
        os.makedirs(dir_name, exist_ok=True)

    if not os.path.exists(file_name) :
        with open(filepath,"w"):
            pass