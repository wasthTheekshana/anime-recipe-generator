# Research Paper Summarizer – Project Planning

## 🎯 Project Overview
A web application that uses NLP and citation graph analysis to automatically summarize academic papers, extract key citations, and support research comprehension.

---

## 🧭 High-Level Goals
- Upload or link a research paper (PDF, arXiv, PubMed)
- Generate a TL;DR summary (1-liner, bullet, paragraph)
- Extract and visualize citation relationships
- Allow Q&A interaction with paper content
- Enable semantic similarity and paper recommendations
- Support export (Markdown, Zotero)

---

## 🧱 MVP Scope

### Must-Have (MVP)
- Upload a PDF and extract full text
- Summarize the paper using a pre-trained model
- Extract references and render a citation graph
- Basic frontend UI for upload + summary + graph
- Export summary as text

### Nice-to-Have (Post-MVP)
- Q&A chatbot for paper content
- Semantic paper search (via embeddings)
- Multilingual summary support (mT5)
- User accounts and saved history
- Notion/Zotero export integration

---

## 🛠 Tech Stack

| Layer           | Tool/Tech                            |
|------------------|---------------------------------------|
| Frontend        | React, Tailwind CSS                   |
| Backend         | FastAPI (Python)                      |
| PDF Parsing     | PyMuPDF / GROBID                      |
| Summarization   | HuggingFace (SciBERT, T5, BART)       |
| Citation Graph  | Neo4j (prod), NetworkX (MVP)          |
| Database        | PostgreSQL (paper metadata)           |
| Semantic Search | FAISS / Qdrant                        |
| Storage         | Local (MVP), AWS S3 (prod)            |
| Deployment      | Docker + Railway / Render             |

---

## 🚧 Architectural Notes
- Use RESTful endpoints: `/summarize`, `/upload`, `/citations`, `/qa`
- Models abstracted into `services/` folder in backend
- Consider caching results for repeated papers

---

## 📈 Milestones

| Phase        | Description                                |
|--------------|--------------------------------------------|
| Week 1       | Setup repo, upload, summarization working  |
| Week 2       | Citation graph + basic frontend UI         |
| Week 3       | Q&A module + export support                |
| Post-MVP     | User auth, multilingual, vector search     |