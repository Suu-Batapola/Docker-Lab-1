# Docker Lab 1

This project demonstrates a multi-container Docker environment setup using Docker Compose. It features a Flask Web API paired with a PostgreSQL database.

---

## 🔌 Ports Used

| Service | Container Port | Host Port | Description |
| :--- | :--- | :--- | :--- |
| **api** (Flask Web App) | `5000` | `5000` | Exposes Flask REST endpoints (`http://localhost:5000/`) |
| **db** (PostgreSQL) | `5432` | Internal | Accessible within Docker network as `db:5432` |

---

## 🚀 Key Commands

### 📦 Docker Compose (Multi-Container Management)

- **Start Services (with build)**
  ```bash
  docker compose up --build
  ```
  *Builds images if necessary and starts all containers in foreground.*

- **Start Services in Detached Mode**
  ```bash
  docker compose up -d
  ```

- **Stop Services**
  ```bash
  docker compose down
  ```

- **Stop Services and Remove Volumes**
  ```bash
  docker compose down -v
  ```

- **Check Running Containers**
  ```bash
  docker compose ps
  ```

- **View Logs**
  ```bash
  docker compose logs -f
  ```

---

### 🐳 Docker CLI (Single Container Management)

- **Build Docker Image**
  ```bash
  docker build -t hello-se:dev .
  ```

- **Run Standalone Container**
  ```bash
  docker run -p 5000:5000 hello-se:dev
  ```

- **List Active Containers**
  ```bash
  docker ps
  ```

- **Stop Container**
  ```bash
  docker stop <container_id>
  ```

---

## 🌐 API Endpoints

- `GET /` - Returns JSON response with student details and greeting message.
- `GET /health` - Health check endpoint returning `{"status": "ok"}`.
