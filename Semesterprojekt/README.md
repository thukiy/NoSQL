#  F1 Analysis API 

An asynchronous REST API for managing Formula 1 data, built with FastAPI and MongoDB.  
Developed as part of the coursework for **NoSQL Databases (cds-115), FS25**, this project demonstrates how RESTful APIs can be combined with document-based data models to deliver fast, flexible, and scalable solutions.

---

##  Project Description

The F1 Analysis API is an asynchronous web API that allows clients to perform **CRUD operations** on Formula 1 entities such as teams, drivers, races, and circuits.

The data is stored in **MongoDB**, enabling flexible schema design ideal for hierarchical, nested, and evolving datasets.  
The application is written in **Python with FastAPI**, providing automatic docs, high performance, and type safety.

Although designed as a backend-only service, this API could easily be integrated into a larger ecosystem with a frontend dashboard or data analytics layer in the future.

---

## Technologies Used

- **FastAPI** – asynchronous Python web framework
- **MongoDB** – NoSQL document-based database
- **Pydantic** – schema validation and data modeling
- **Docker & docker-compose** – containerized development & deployment


---

## Getting Started

## Docker Instructions

To build the Docker image and run the application together with MongoDB:

###  Build the Docker image

```bash
docker build -t f1_analysis.
```

### ▶️ Run the app with MongoDB

```bash
docker-compose up -d
```

This will:
- Start the FastAPI backend on `http://localhost:8000`
- Launch MongoDB on port `27017`

### Requirements

- Docker & Docker Compose installed and running
- (Optional) Python 3.11+ for local development/testing

### ▶️ Start the Application

In the root directory of the project (e.g., `Semesterprojekt/`), run:

```bash
docker-compose up --build
```

Once running, access the API via:

Swagger UI: [http://localhost:8000/docs](http://localhost:8000/docs)  
OpenAPI JSON: [http://localhost:8000/openapi.json](http://localhost:8000/openapi.json)

---

##  Entities Overview

| Entity     | Description |
|------------|-------------|
| **Team**   | Contains F1 team info such as name, chassis, engine supplier, and team principal |
| **Driver** | Holds driver names and optional metadata (expandable in future versions) |
| **Circuit**| Stores information about race tracks, location, and layout |
| **Race**   | Defines race events, including circuit reference, laps, and lap times |

Each entity has its own endpoint (e.g., `/teams/`, `/drivers/`) and supports full CRUD operations.

---

## Database Operations

### Export (Backup)

```bash
docker exec -it MongoDB mongodump --db f1_analysis --out /data/dump
docker cp MongoDB:/data/dump ./mongo-backup
```

### Import (Restore)

```bash
docker cp ./mongo-backup MongoDB:/data/
docker exec -it MongoDB mongorestore --db f1_analysis /data/mongo-backup/dump/f1_analysis
```

---


## Additional Notes

- All endpoints are asynchronous and validated via Pydantic models
- PUT endpoints allow for both updating and creating entries:
  - If an ID exists → update
  - If no ID or invalid ID → create new
- This flexibility supports both frontend dev and controller testing during development

---



**Thuvaraka Yograjah**  
Module: *NoSQL Datenbanken (cds-115)*  
Semester: FS25  
Institution: FHGR
---


---

##  Example Requests (using `curl`)

###  Create a new team

```bash
curl -X POST http://localhost:8000/teams/ \
  -H "Content-Type: application/json" \
  -d '{
    "name": "MoneyGram Haas F1 Team",
    "chassis": "VF-25",
    "power_unit": "Ferrari",
    "team_principal": "Ayao Komatsu"
}'
```

###  Get all teams

```bash
curl http://localhost:8000/teams/
```

###  Update an existing team

```bash
curl -X PUT http://localhost:8000/teams/<team_id> \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Haas F1 Updated",
    "chassis": "VF-25",
    "power_unit": "Ferrari",
    "team_principal": "Ayao Komatsu"
}'
```

###  Delete a team

```bash
curl -X DELETE http://localhost:8000/teams/<team_id>
```


