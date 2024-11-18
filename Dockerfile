# Use the official Python image
FROM python:3.11

# Set working directory
WORKDIR /app

# Copy the app files
COPY ./app /app

# Install dependencies
RUN pip install --no-cache-dir fastapi uvicorn minio psycopg2-binary spacy \
    && python -m spacy download en_core_web_sm

# Expose the FastAPI port
EXPOSE 8000

# Start the FastAPI server
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
