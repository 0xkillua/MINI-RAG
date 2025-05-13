# 📚 Mini-RAG: Local LLM Retrieval-Augmented Generation

A simple yet powerful RAG (Retrieval-Augmented Generation) system using local LLMs with FastAPI, Ollama, and PostgreSQL.

---

## 🧰 Requirements

- Python 3.8
- Conda (MiniConda preferred)


---

## 🛠️ Setup Instructions

### 1. **System Dependencies**

```bash
sudo apt update
sudo apt install libpq-dev gcc python3-dev
```
###  Step 2: Create a new environment

```bash
conda create -n mini-rag python=3.8
```
### (Optional) Run Ollama Local LLM Server using Colab + Ngrok

###  Installation
#### Install the required packages
```bash
$ pip install -r requirements.txt
```
#### Setup the environment variables
```bash
$ cp .env.example .env
```
### Run the FastAPI server 
```bash
$ uvicorn main:app --reload --host 0.0.0.0 --port 5000
```