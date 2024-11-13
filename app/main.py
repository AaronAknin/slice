import os
import psycopg2
from fastapi import FastAPI, HTTPException
from minio import Minio
import spacy

# Initialize spaCy
nlp = spacy.load("en_core_web_sm")

# Initialize FastAPI
app = FastAPI()

# Set up MinIO client
minio_client = Minio(
    os.getenv("MINIO_ENDPOINT"),
    access_key=os.getenv("MINIO_ACCESS_KEY"),
    secret_key=os.getenv("MINIO_SECRET_KEY"),
    secure=False,
)

# Set up PostgreSQL connection
conn = psycopg2.connect(
    host=os.getenv("POSTGRES_HOST"),
    database=os.getenv("POSTGRES_DB"),
    user=os.getenv("POSTGRES_USER"),
    password=os.getenv("POSTGRES_PASSWORD"),
)


def extract_keywords(text):
    doc = nlp(text)
    keywords = [
        token.text
        for token in doc
        if token.pos_ in ["NOUN", "PROPN"] and not token.is_stop
    ]
    return list(set(keywords))


@app.post("/process")
async def process_document(file_name: str):
    try:
        # Fetch document from MinIO
        response = minio_client.get_object("your-bucket-name", file_name)
        file_content = response.read().decode("utf-8")

        # Extract keywords
        keywords = extract_keywords(file_content)

        # Save results to PostgreSQL
        with conn.cursor() as cursor:
            cursor.execute(
                "INSERT INTO processed_files (file_name, file_content, keywords) VALUES (%s, %s, %s)",
                (file_name, file_content, keywords),
            )
            conn.commit()

        return {
            "file_name": file_name,
            "file_content": file_content,
            "keywords": keywords,
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
