# Healthcare_Data_Modelling_Analysis_with_LLMs
## 🧠 Overview
Natural language interface to a medical knowledge graph (Amazon Neptune) using AWS Bedrock LLM.

## ✨ Features
- NL-to-SPARQL query engine using Claude on AWS Bedrock
- Medical knowledge graph querying via SPARQL
- Future: Clinical note summarization module

## 🏗️ Architecture
```
[User] --(NL Query)--> [Claude LLM (Bedrock)] --(SPARQL)--> [Neptune DB] --> [JSON Results]
```

## 🚀 Run Locally
```bash
git clone https://github.com/yourname/icu-query-app.git
cd icu-query-app
python app/main.py
```

## ⚙️ Requirements
- Python 3.8+
- AWS credentials configured for Bedrock

## 🧪 Testing
```bash
pytest tests/
```

## 📍 Status
Prototype, core functionality implemented. Summarization WIP.
