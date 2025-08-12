# 🤖 Optimus Prime – AI Knowledge Base Automation

This project was developed during my **AI Innovation Intern** role, focusing on automating knowledge ingestion and deploying AI-powered support assistants for domain-specific content.

---

## Features

- **Scrape** ≥ 30 articles from Zendesk Help Center.
- **Clean & Convert** content to Markdown (`<slug>.md`).
- **Upload** docs to OpenAI Vector Store via API.
- **AI Assistant Creation** with a custom domain-specific system prompt.
- **Logging** of ingestion stats: `added`, `updated`, `skipped`, `uploaded`.
- **Dockerized** for consistent deployment across environments.
- **Schedulable** for automated daily runs.

---

## Run locally

### 1. Install dependencies
```bash
pip install -r requirements.txt

```

### 2. Create `.env` file
```
cp .env.sample .env
```

edit OpenAI API key:
```
OPENAI_API_KEY=sk-...
```

### 3. Run the script
```
python main.py
```

### Docker Build & Run
```
docker build -t optimus-prime .
docker run --rm -e OPENAI_API_KEY=sk-... optimus-prime
```

##  AI Assistant Prompt

Using system prompt from file pdf:
```
You are OptiBot, the customer-support bot for OptiSigns.com.
• Tone: helpful, factual, concise.
• Only answer using the uploaded docs.
• Max 5 bullet points; else link to the doc.
• Cite up to 3 'Article URL:' lines per reply.
```

## Chunking Strategy

All 30 scraped Markdown files are uploaded to the OpenAI platform and linked to the Assistant. 
The files are stored in raw Markdown format without any custom preprocessing, as OpenAI automatically handles chunking internally. 
This chunking strategy means the documents are split into optimal segments for embedding and retrieval, ensuring both simplicity and compatibility. 
Once uploaded, each chunk is embedded into vector representations inside a Vector Store, allowing the Assistant to quickly search and retrieve relevant information.
During the ingestion process, logs are generated to record which files were added, updated, skipped, and successfully uploaded.
When queried, the Assistant searches the embedded chunks, selects the most relevant content, and uses it to generate accurate, context-based responses.

## Playground Screenshot
<img width="1510" height="853" alt="image" src="https://github.com/user-attachments/assets/be4aa867-55e7-44b0-a72e-82258945d5e2" />
<img width="1914" height="904" alt="image" src="https://github.com/user-attachments/assets/18b5ad76-667e-439b-bdb0-56b0f59e2ddb" />



## 📁 Project Structure
.
├── main.py             # scraping, upload, assistant creation  
├── scraper.py          # Scrape articles from Zendesk  
├── uploader.py         # Upload Markdown files to OpenAI Vector Store  
├── Dockerfile          # Docker container definition  
├── .env.sample         # Sample env file with API key placeholder  
├── requirements.txt    # Python dependencies  
└── README.md           # Project documentation


