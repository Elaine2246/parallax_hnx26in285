# parallax_hnx26in285

# 📚 RAG PDF Assistant

## Project Overview

Large Language Models (LLMs) are powerful tools capable of understanding and generating human-like responses. However, they may not always have access to the latest or domain-specific information contained in private documents. They can also generate incorrect or unsupported information when the required knowledge is not available in their context.

Retrieval-Augmented Generation (RAG) helps address this limitation by connecting an LLM with external knowledge sources. Instead of relying only on the model's existing knowledge, the system first retrieves relevant information from the uploaded documents and then provides that information to the LLM as context for generating an answer.

The aim of this project is to build an interactive **RAG-based PDF question-answering assistant** that allows users to upload PDF documents and ask questions about their content using natural language.

The application extracts text from uploaded PDF documents using **PyMuPDF**, creates a searchable representation using **TF-IDF**, retrieves relevant pages using **cosine similarity**, and uses **Google Gemini** to generate context-aware answers.

The application also provides **document and page-level source references**, allowing users to verify the information used to generate an answer.

A user-friendly interface has been developed using **Streamlit**.

---

## ✨ Features

- 📄 Upload one or multiple PDF documents
- 🔎 Search and retrieve relevant information from documents
- 🧠 Retrieval-Augmented Generation (RAG)
- 📊 TF-IDF-based document retrieval
- 📐 Cosine similarity for relevance matching
- 🤖 Google Gemini-powered answer generation
- 📑 Page-level source references
- 📊 Retrieval relevance scores
- 💬 Natural-language question answering
- 💡 Quick question suggestions
- ⚡ Retrieves only relevant document content before sending it to the LLM
- 🖥️ Interactive Streamlit interface

---

## 🏗️ RAG Pipeline

The application follows the following pipeline:

```text
PDF Document
     ↓
Text Extraction
     ↓
Text Cleaning
     ↓
TF-IDF Vectorization
     ↓
Document Index
     ↓
User Question
     ↓
Query Vectorization
     ↓
Cosine Similarity
     ↓
Relevant PDF Pages
     ↓
Context Construction
     ↓
Google Gemini
     ↓
Generated Answer
     ↓
Page-Level Sources
