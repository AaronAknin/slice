# Containerized Data Processing Simulation

## Overview

This project sets up a containerized environment to process text files stored in MinIO. It extracts keywords from each document and saves the results in PostgreSQL, with a FastAPI server handling the data processing and API requests.

## Prerequisites

- **Docker** and **Docker Compose** installed on your machine.
- Basic understanding of REST APIs, Docker, and Python.

## Setup Instructions

### Step 1: Clone the Repository

```bash
git clone https://github.com/AaronAknin/slice.git
cd containerized-data-processing
```

### Step 2: Configure Environment Variables

The following environment variables are pre-configured in `docker-compose.yml`, but ensure they are correct if you make any adjustments:

```yaml
MINIO_ENDPOINT=minio:9000
MINIO_ACCESS_KEY=minioadmin
MINIO_SECRET_KEY=minioadmin
POSTGRES_HOST=postgres
POSTGRES_DB=analysis_db
POSTGRES_USER=admin
POSTGRES_PASSWORD=admin
```

### Step 3: Build and Run the Containers

Use Docker Compose to build and start all services:

```bash
docker-compose up --build
```

This will start:

- **MinIO** at `http://localhost:9000` (Default credentials: `minioadmin:minioadmin`)
- **FastAPI server** at `http://localhost:8000`
- **PostgreSQL** on port `5432`

### Step 4: Set Up MinIO and Upload Files

1. Access MinIO at `http://localhost:9000` and log in with the default credentials (`minioadmin:minioadmin`).
2. Create a new bucket (e.g., `text-files`).
3. Upload your `.txt` files to this bucket.

### Step 5: Set Up PostgreSQL Database Table

You can connect to the PostgreSQL database using a client like `psql` or pgAdmin. Use the following command to create the required table:

```sql
CREATE TABLE processed_files (
    id SERIAL PRIMARY KEY,
    file_name VARCHAR(255) NOT NULL,
    file_content TEXT NOT NULL,
    keywords TEXT[]
);
```

## Usage Instructions

### Testing the `/process` Endpoint

To process a file, send a POST request to the `/process` endpoint, specifying the filename in the MinIO bucket.

#### Using `curl`

```bash
curl -X POST "http://localhost:8000/process" -H "Content-Type: application/json" -d '{"file_name": "files/sample1.txt"}'
```

#### Using Postman

1. Open Postman and create a new **POST** request.
2. Set the URL to `http://localhost:8000/process`.
3. In the **Body** tab, choose **raw** and set the format to **JSON**.
4. Enter the JSON data:

   ```json
   {
     "file_name": "files/sample1.txt"
   }
   ```

5. Send the request.

### Viewing Saved Results in PostgreSQL

To view the saved results in PostgreSQL, connect to the database with:

```bash
psql -h localhost -U admin -d analysis_db
```

Then run the following query:

```sql
SELECT * FROM processed_files;
```

This will display processed file data including the `file_name`, `file_content`, and `keywords`.

## Troubleshooting

- Ensure Docker and Docker Compose are installed and running.
- Check MinIO credentials if you have issues uploading files.
- # Verify PostgreSQL configurations if database connections fail.

# Containerized Data Processing Simulation

## Overview

This project sets up a containerized environment to process text files stored in MinIO. It extracts keywords from each document and saves the results in PostgreSQL, with a FastAPI server handling the data processing and API requests.

## Prerequisites

- **Docker** and **Docker Compose** installed on your machine.
- Basic understanding of REST APIs, Docker, and Python.

## Setup Instructions

### Step 1: Clone the Repository

```bash
git clone https://github.com/your-repo/containerized-data-processing
cd containerized-data-processing
```

### Step 2: Configure Environment Variables

The following environment variables are pre-configured in `docker-compose.yml`, but ensure they are correct if you make any adjustments:

```yaml
MINIO_ENDPOINT=minio:9000
MINIO_ACCESS_KEY=minioadmin
MINIO_SECRET_KEY=minioadmin
POSTGRES_HOST=postgres
POSTGRES_DB=analysis_db
POSTGRES_USER=admin
POSTGRES_PASSWORD=admin
```

### Step 3: Build and Run the Containers

Use Docker Compose to build and start all services:

```bash
docker-compose up --build
```

This will start:

- **MinIO** at `http://localhost:9000` (Default credentials: `minioadmin:minioadmin`)
- **FastAPI server** at `http://localhost:8000`
- **PostgreSQL** on port `5432`

### Step 4: Set Up MinIO and Upload Files

1. Access MinIO at `http://localhost:9000` and log in with the default credentials (`minioadmin:minioadmin`).
2. Create a new bucket (e.g., `text-files`).
3. Upload your `.txt` files to this bucket.

### Step 5: Set Up PostgreSQL Database Table

You can connect to the PostgreSQL database using a client like `psql` or pgAdmin. Use the following command to create the required table:

```sql
CREATE TABLE processed_files (
    id SERIAL PRIMARY KEY,
    file_name VARCHAR(255) NOT NULL,
    file_content TEXT NOT NULL,
    keywords TEXT[]
);
```

## Usage Instructions

### Testing the `/process` Endpoint

To process a file, send a POST request to the `/process` endpoint, specifying the filename in the MinIO bucket.

#### Using `curl`

```bash
curl -X POST "http://localhost:8000/process" -H "Content-Type: application/json" -d '{"file_name": "sample1.txt"}'
```

#### Using Postman

1. Open Postman and create a new **POST** request.
2. Set the URL to `http://localhost:8000/process`.
3. In the **Body** tab, choose **raw** and set the format to **JSON**.
4. Enter the JSON data:

   ```json
   {
     "file_name": "sample1.txt"
   }
   ```

5. Send the request.

### Viewing Saved Results in PostgreSQL

To view the saved results in PostgreSQL, connect to the database with:

```bash
psql -h localhost -U admin -d analysis_db
```

Then run the following query:

```sql
SELECT * FROM processed_files;
```

This will display processed file data including the `file_name`, `file_content`, and `keywords`.

## Troubleshooting

- Ensure Docker and Docker Compose are installed and running.
- Check MinIO credentials if you have issues uploading files.
- Verify PostgreSQL configurations if database connections fail.
