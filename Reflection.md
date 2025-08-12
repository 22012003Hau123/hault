## Short Project Reflection

### 1. Concept Understanding
This project focuses on building an automated ingestion pipeline for **OptiBot**.  
It scrapes support articles from OptiSigns’ Zendesk Help Center, converts them to clean Markdown, uploads them to the OpenAI Vector Store, and creates an Assistant that can answer support questions based on this knowledge base.  

The key concept is integrating:
- Web scraping
- Content processing
- Vector storage
- Retrieval Information
---

### 2. Approach & Solution
I approached the problem by breaking it into modular steps:

1. **Scraping** — Used the Zendesk API to fetch ≥30 relevant articles (with keyword filtering when needed).
2. **Cleaning & Conversion** — Removed unwanted HTML elements and converted the articles into clean Markdown.
3. **Storage & Deduplication** — Compared new content with existing local files to avoid redundant uploads.
4. **Embedding & Assistant Creation** — Uploaded files to the OpenAI Vector Store for embedding and linked them to an Assistant with a custom system prompt.
5. **Logging** — Added detailed logs for `added`, `updated`, and `skipped` files 

This modular approach ensures the pipeline is easy to maintain, extend, and debug.

---

### 3. Learning Process
When I encounter something unfamiliar, I:
- Read official documentation and API references first to understand the data structure and capabilities.
- Break the task into small, testable steps (e.g., then clean HTML, then convert to Markdown).
- Iterate quickly, testing at each stage before moving to the next.
- Read document about DigitalOcean Platform 
For this project, I had not worked with the Zendesk Help Center API before, so I started by experimenting with small queries, then integrated them into the full scraping pipeline.

---

### 4. Thoughts & Suggestions for Improvement
To improve clear filtering and tagging of articles from the start, implement a standardized category and tag system, 
use NLP to auto-extract keywords and suggest tags, require tagging during content submission, regularly review and update tags based on user feedback,
and enable advanced filters for users to easily find relevant content. This ensures accurate, consistent tagging and better user experience.

---

### 5. Potential Challenges
- **Search Precision** — Ensuring the Assistant retrieves the most relevant chunks, especially when articles are long or similar.
- **Scaling** — Handling larger volumes of content while keeping ingestion fast and cost-effective, cost a lot of money
