# DeltaRAG

### Documentation Change Impact Analysis with RAG & Agentic AI

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:0f172a,100:2563eb&height=210&section=header&text=DeltaRAG&fontSize=64&fontColor=ffffff&animation=fadeIn&fontAlignY=38&desc=Documentation%20Change%20Impact%20Analysis&descAlignY=62&descSize=19" width="100%"/>
</p>

<p align="center">
  <strong>🔍 Detect changes • 🧠 Retrieve context • ⚡ Analyze impact • 📚 Explain evidence</strong>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Status-Active%20Research-22c55e?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/RAG-8B5CF6?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/Agentic%20AI-Research-f97316?style=for-the-badge"/>
</p>

---

## 🧠 What is DeltaRAG?

**DeltaRAG** is a research project focused on **documentation change impact analysis**.

Technical documentation is highly interconnected. A change in one document can make information in other documents outdated or inconsistent.

DeltaRAG explores how **Git history, semantic retrieval, Retrieval-Augmented Generation (RAG), and eventually agentic AI** can be combined to identify documentation that may require review after a change.

```text
Documentation Change
        │
        ▼
   Detect the Delta
        │
        ▼
 Understand the Change
        │
        ▼
 Retrieve Related Docs
        │
        ▼
 Analyze Potential Impact
        │
        ▼
 Explain with Evidence
```

---

## 🎯 The Problem

Consider an API specification that changes:

```text
Before:
Authentication tokens are valid for 24 hours.

After:
Authentication tokens are valid for 12 hours.
```

The changed API document is only the beginning.

Other documentation may also contain information based on the old specification:

```text
                 ┌─────────────────┐
                 │    API Guide    │
                 │   24h → 12h     │
                 └────────┬────────┘
                          │
              ┌───────────┴───────────┐
              ▼                       ▼
     ┌─────────────────┐     ┌─────────────────┐
     │ Authentication  │     │ Troubleshooting │
     │     Guide       │     │      Guide     │
     └─────────────────┘     └─────────────────┘
```

The goal is not simply to find documents containing the same keywords.

The goal is to determine **which documents are semantically related to the change and why they may be affected**.

---

# 🏗️ Architecture

DeltaRAG is being developed incrementally, beginning with a conventional RAG pipeline and then investigating whether an **agentic approach provides additional value**.

```text
                  DOCUMENTATION REPOSITORY
                           │
                           ▼
                  ┌─────────────────┐
                  │ Change Detection│
                  │   Git / Diff    │
                  └────────┬────────┘
                           │
                           ▼
                  ┌─────────────────┐
                  │ Change          │
                  │ Understanding   │
                  └────────┬────────┘
                           │
                           ▼
                  ┌─────────────────┐
                  │ Document        │
                  │ Ingestion       │
                  └────────┬────────┘
                           │
                           ▼
                  ┌─────────────────┐
                  │ Embeddings +    │
                  │ Vector Search   │
                  └────────┬────────┘
                           │
                           ▼
                  ┌─────────────────┐
                  │      RAG        │
                  │ Impact Analysis │
                  └────────┬────────┘
                           │
                           ▼
                  ┌─────────────────┐
                  │ Agentic AI      │
                  │ Investigation   │
                  │    (Research)   │
                  └────────┬────────┘
                           │
                           ▼
                  ┌─────────────────┐
                  │ Explainable     │
                  │ Impact Report   │
                  └─────────────────┘
```

> **Research principle:** Agentic AI is being evaluated as a hypothesis, not assumed to be automatically better than conventional RAG.

---

# 📂 Current Project Structure

```text
DeltaRAG/
│
├── backend/
│   ├── data/
│   │   └── dummy_docs/
│   │       ├── api_guide.md
│   │       ├── authentication.md
│   │       └── troubleshooting.md
│   │
│   ├── git/
│   │   └── history.py
│   │
│   └── ingestion/
│       └── ingest.py
│
├── test_repo/
│   └── docs/
│       ├── api_guide.md
│       ├── authentication.md
│       └── troubleshooting.md
│
└── .gitignore
```

---

# ⚙️ Current Implementation

The repository currently establishes the foundation for the research system.

| Component | Purpose | Status |
|---|---|:---:|
| Documentation dataset | Controlled technical documentation | ✅ |
| Test repository | Simulated documentation repository | ✅ |
| Git history component | Work with documentation history | ✅ |
| Ingestion pipeline | Initial document ingestion | ✅ |
| Semantic embeddings | Document representation | 🔄 |
| ChromaDB retrieval | Vector search | 🔄 |
| RAG pipeline | Impact analysis | 🔜 |
| LLM integration | Reasoning and explanation | 🔜 |
| Agentic workflow | Multi-step investigation | 🔬 |
| FastAPI backend | Application API | 🔜 |
| React interface | Visualization | 🔜 |
| Docker | Deployment | 🔜 |

---

# 🛠️ Technology Stack

### AI & Retrieval

<p>
<img src="https://img.shields.io/badge/RAG-8B5CF6?style=for-the-badge"/>
<img src="https://img.shields.io/badge/LangChain-1C3C3C?style=for-the-badge"/>
<img src="https://img.shields.io/badge/ChromaDB-FF6B35?style=for-the-badge"/>
<img src="https://img.shields.io/badge/Sentence%20Transformers-06B6D4?style=for-the-badge"/>
<img src="https://img.shields.io/badge/Ollama-black?style=for-the-badge"/>
</p>

### Backend & Application

<p>
<img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
<img src="https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white"/>
<img src="https://img.shields.io/badge/React-61DAFB?style=for-the-badge&logo=react&logoColor=black"/>
<img src="https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white"/>
</p>

> Technologies marked as future/planned represent the intended architecture and are not claimed as fully implemented in the current repository.

---

# 🔬 RAG → Agentic AI

## Conventional RAG

The first major implementation stage focuses on establishing a reliable retrieval pipeline:

```text
Changed Document
       │
       ▼
Document Processing
       │
       ▼
Embeddings
       │
       ▼
ChromaDB
       │
       ▼
Semantic Retrieval
       │
       ▼
Relevant Context
       │
       ▼
LLM Analysis
```

## Agentic Investigation

The next research stage explores whether an agent can perform a more dynamic investigation:

```text
                 ┌──────────────────┐
                 │ Changed Document │
                 └────────┬─────────┘
                          ▼
                 ┌──────────────────┐
                 │ Research Agent   │
                 └────────┬─────────┘
                          │
             ┌────────────┼────────────┐
             ▼            ▼            ▼
        Search Docs   Git History   Compare Docs
             │            │            │
             └────────────┼────────────┘
                          ▼
                 ┌──────────────────┐
                 │ Gather Evidence  │
                 └────────┬─────────┘
                          ▼
                 ┌──────────────────┐
                 │ Impact Reasoning │
                 └────────┬─────────┘
                          ▼
                 ┌──────────────────┐
                 │ Explainable      │
                 │ Result           │
                 └──────────────────┘
```

The research will compare both approaches rather than assuming that adding an agent automatically improves the system.

---

# 📊 Planned Evaluation

A major focus of DeltaRAG is **evaluation**, not just implementation.

The system will eventually be tested using controlled documentation changes and known impact relationships.

### Retrieval

- Precision
- Recall
- Top-K relevance
- Relevant document identification

### Impact Analysis

- Correctly identified impacted documents
- False positives
- Missed impacts
- Evidence quality
- Explanation quality

### RAG vs Agentic AI

The two approaches can be evaluated across:

```text
                 RAG        Agentic AI
                  │             │
                  ▼             ▼
            ┌─────────────────────────┐
            │     Evaluation Set      │
            └────────────┬────────────┘
                         ▼
               ┌──────────────────┐
               │ Compare Results  │
               └──────────────────┘
```

Potential evaluation dimensions include:

- Impact detection quality
- Retrieval quality
- Reasoning quality
- Evidence coverage
- Latency
- Computational cost
- Number of investigation steps
- Robustness to complex documentation changes

---

# 🗺️ Development Roadmap

### Phase 1 — Foundation
- [x] Initialize repository
- [x] Create documentation dataset
- [x] Create test documentation repository
- [x] Add Git-history foundation
- [x] Build initial ingestion pipeline

### Phase 2 — Retrieval
- [ ] Document chunking
- [ ] Metadata extraction
- [ ] Sentence Transformer embeddings
- [ ] ChromaDB integration
- [ ] Semantic search
- [ ] Retrieval evaluation

### Phase 3 — RAG Impact Analysis
- [ ] LLM integration
- [ ] RAG pipeline
- [ ] Change-aware retrieval
- [ ] Impact classification
- [ ] Evidence extraction
- [ ] Explainable reports

### Phase 4 — Agentic AI Research
- [ ] Agent architecture
- [ ] Retrieval tools
- [ ] Git-history tools
- [ ] Document comparison tools
- [ ] Multi-step investigation
- [ ] Evidence verification
- [ ] RAG vs Agentic evaluation

### Phase 5 — Application
- [ ] FastAPI backend
- [ ] React dashboard
- [ ] Impact visualization
- [ ] Documentation dependency graph
- [ ] Analysis history
- [ ] Docker deployment

---

# 🌐 Future Scope

DeltaRAG is designed to grow beyond a basic RAG prototype.

### 🔗 Documentation Dependency Graph

Represent relationships between documents and propagate potential impacts through the graph.

```text
API Guide
 ├── Authentication
 ├── Configuration
 └── Troubleshooting
```

### 🤖 Multi-Agent Investigation

Explore specialized agents for:

- Document retrieval
- Git-history analysis
- Document comparison
- Impact reasoning
- Evidence verification

### 🔄 Continuous Monitoring

Integrate DeltaRAG with development workflows:

```text
Developer Push
      ↓
Documentation Change
      ↓
Automatic DeltaRAG Analysis
      ↓
Potential Impact Detected
      ↓
Developer Review
```

### 🔌 Developer Tooling

Potential integrations include:

- GitHub Actions
- Pull Request checks
- VS Code extension
- CLI
- Slack / Teams notifications
- Automated issue creation

### 📑 Multi-Format Documentation

Future ingestion support could include:

```text
Markdown • PDF • HTML • DOCX
OpenAPI / Swagger • Architecture Documents
```

### 🧬 Historical Intelligence

Use documentation history to understand:

- Previous versions
- Related commits
- Repeated documentation changes
- Historical inconsistencies
- Change patterns

### 🛡️ Human-in-the-Loop Review

Allow developers to accept, reject, or correct AI-generated impact predictions and use those decisions for evaluation.

### 📈 Documentation Health

A future dashboard could surface:

- Documentation drift
- Dependency hotspots
- Unreviewed changes
- Frequently affected documents
- Consistency trends

### 🌍 Enterprise Knowledge Systems

The architecture could eventually extend to large engineering knowledge bases containing:

- API documentation
- Product specifications
- Internal wikis
- Architecture documents
- Operational runbooks
- Developer guides

---

# 🚀 Long-Term Vision

DeltaRAG aims to evolve from a document retrieval system into an **intelligent documentation maintenance platform** capable of answering:

> **What changed?**

> **What else could be affected?**

> **Why is it potentially affected?**

> **What evidence supports the relationship?**

> **What should a developer review?**

The long-term objective is to make documentation maintenance more **automated, explainable, evidence-driven, and scalable**.

---

# 📌 Project Status

**🟢 Active Research & Development**

Current focus:

```text
Foundation
    ↓
Semantic Retrieval
    ↓
RAG
    ↓
Change Impact Analysis
    ↓
Agentic Investigation
    ↓
Evaluation
    ↓
Developer Tooling
```

Each layer will be implemented and evaluated incrementally.

---

# 👨‍💻 Author

### Aradhy Bajpai

**B.Tech Computer Science & Engineering — PSIT Kanpur**

`Full-Stack Development` · `AI/ML` · `Generative AI` · `RAG` · `Agentic AI`

<p align="center">
  <a href="https://github.com/Aradhy2005">
    <img src="https://img.shields.io/badge/GitHub-Aradhy2005-181717?style=for-the-badge&logo=github"/>
  </a>
  <a href="https://www.linkedin.com/in/aradhy-bajpai-897241283/">
    <img src="https://img.shields.io/badge/LinkedIn-Aradhy%20Bajpai-0A66C2?style=for-the-badge&logo=linkedin"/>
  </a>
  <a href="https://leetcode.com/u/aradhy2005/">
    <img src="https://img.shields.io/badge/LeetCode-Aradhy2005-FFA116?style=for-the-badge&logo=leetcode"/>
  </a>
</p>

---

<p align="center">
  <strong>🔄 DeltaRAG</strong><br/>
  <sub>From documentation changes to explainable impact analysis.</sub>
</p>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:2563eb,100:0f172a&height=110&section=footer" width="100%"/>
</p>