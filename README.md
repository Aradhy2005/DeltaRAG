# DeltaRAG
### Documentation Change Impact Analysis Using Hybrid Retrieval and Agentic Verification

DeltaRAG is a research project that investigates how changes in software code can be used to identify potentially affected technical documentation through hybrid information retrieval and evidence-based agentic investigation.

The system aims to help developers discover documentation that may require review when a software repository changes. It combines code-change analysis, lexical and semantic retrieval, evidence verification, and controlled evaluation.

> **Research principle:** The effectiveness of agentic investigation will be evaluated experimentally against a fixed hybrid-RAG baseline. Improvements are not assumed in advance.

## Problem Statement

Software documentation describes system behavior, interfaces, configuration, and implementation details. When the underlying code changes, related documentation may also require review.

Identifying all potentially affected documents can require manually examining code changes, locating relevant documentation, and determining whether the documented behavior remains consistent with the implementation.

DeltaRAG investigates an evidence-grounded approach to this problem by analyzing repository changes and retrieving documentation that may be affected.

## Research Objectives

- Detect changes between specified Git commits.
- Represent code changes in a structured format suitable for downstream analysis.
- Ingest and index technical documentation.
- Retrieve potentially relevant documentation using lexical and semantic search.
- Establish a reproducible hybrid-RAG baseline.
- Investigate whether agentic evidence gathering and verification improve impact identification.
- Compare both approaches using a common labelled evaluation dataset.
- Produce traceable impact reports containing supporting evidence and uncertainty.

## Proposed Workflow

```text
Software Repository
        |
        v
Git Change Detection
        |
        v
Structured Change Analysis
        |
        v
Documentation Ingestion
        |
        v
Hybrid Retrieval
(BM25 + Semantic Search)
        |
        v
Candidate Fusion and Ranking
        |
        v
Fixed Hybrid-RAG Baseline
        |
        +---------------------------+
        |                           |
        v                           v
Baseline Evaluation       Agentic Investigation
                                    |
                                    v
                          Evidence Verification
                                    |
                                    v
                          Agentic System Evaluation
        |                           |
        +-------------+-------------+
                      |
                      v
             Comparative Analysis
                      |
                      v
             Evidence-Grounded Report
```

The workflow separates the fixed baseline from the agentic extension so that their performance can be evaluated independently under comparable conditions.

## Core Components

### 1. Git Change Detection

Identifies files changed between a base commit and a target commit. The change-analysis stage will extract relevant old and new content and construct structured change records.

### 2. Documentation Ingestion

Loads documentation, divides it into searchable chunks, attaches metadata, and prepares the content for indexing.

### 3. Hybrid Retrieval

Combines two complementary retrieval approaches:

- **Lexical retrieval:** BM25-based matching to identify documentation containing relevant terms.
- **Semantic retrieval:** Embedding-based search to identify passages with related meaning, including cases where wording differs.

### 4. Candidate Fusion and Ranking

Combines retrieved candidates and ranks potentially affected documentation using an explicitly defined ranking strategy.

### 5. Fixed Hybrid-RAG Baseline

Provides the reference system against which the agentic extension will be evaluated. Its retrieval process and configuration will be fixed for controlled comparisons.

### 6. Agentic Investigation and Verification

Investigates the initial evidence, identifies information gaps, selects additional retrieval actions, and checks whether the collected evidence supports an impact assessment.

The agentic workflow will use explicit stopping criteria and investigation budgets. When evidence is insufficient, the system should preserve uncertainty rather than invent a conclusion.

### 7. Impact Reporting

Produces a ranked report of potentially affected documents, explanations, supporting evidence, and uncertainty.

The system is intended to assist human review. It will not automatically modify documentation.

### 8. Evaluation

Evaluates both approaches using the same labelled dataset, change scenarios, and evaluation protocol.

## Research Evaluation

The evaluation will investigate whether agentic investigation provides measurable benefits over the fixed hybrid-RAG baseline.

Planned evaluation measures include:

| Metric | Purpose |
|---|---|
| Precision | Measures how many identified documents are relevant. |
| Recall | Measures how many relevant documents are identified. |
| F1-score | Combines precision and recall. |
| False-positive rate | Measures the proportion of negative cases incorrectly flagged. |
| Evidence coverage | Measures whether impact assessments contain the required supporting evidence. |
| Latency | Measures the time required to produce results. |
| Resource usage | Tracks computational resources and, where applicable, model calls and token consumption. |

The dataset, labelling rules, comparison procedure, and system configurations should be documented to support reproducibility.

Results will be reported after experiments are conducted. No performance improvement is claimed in advance.

## Technology Stack

The implementation is planned around the following technologies:

- **Python** — backend logic and orchestration.
- **Git** — repository history and change detection.
- **ChromaDB** — vector storage and semantic retrieval.
- **BM25** — lexical information retrieval.
- **Embedding models** — semantic representation of documentation and changes.
- **LLM integration** — evidence analysis and agentic investigation, where appropriate.
- **Automated tests and evaluation scripts** — correctness and reproducibility.

Specific libraries, models, and configurations will be documented as they are selected and implemented.

## Research Methodology

The project will proceed through the following stages:

1. Implement and validate Git change detection.
2. Define a structured change representation.
3. Build reproducible documentation ingestion and indexing.
4. Implement lexical and semantic retrieval.
5. Establish the fixed hybrid-RAG baseline.
6. Create and label an evaluation dataset.
7. Evaluate the baseline and document its limitations.
8. Implement agentic investigation and evidence verification.
9. Compare both approaches using the same evaluation protocol.
10. Analyze errors, limitations, resource usage, and experimental results.

## Project Status

**Current stage:** Repository reset and project documentation.

The implementation will be developed incrementally. A component will be described as implemented only after it has been developed and validated.

| Component | Status |
|---|---|
| Project scope and workflow | Defined |
| Git change detection | To implement |
| Structured change analysis | To implement |
| Documentation ingestion | To implement |
| Hybrid retrieval | To implement |
| Candidate fusion and ranking | To implement |
| Fixed hybrid-RAG baseline | To implement |
| Agentic investigation and verification | To implement |
| Labelled evaluation dataset | To prepare |
| Comparative evaluation | Pending implementation and experiments |

## Repository Structure

The repository structure will evolve as components are implemented. The intended organization separates ingestion, Git analysis, retrieval, agentic investigation, reporting, testing, and evaluation.

```text
DeltaRAG/
├── README.md
├── .gitignore
├── backend/
│   ├── git/
│   ├── ingestion/
│   ├── retrieval/
│   ├── analysis/
│   ├── agent/
│   ├── reporting/
│   └── evaluation/
├── tests/
├── test_repo/
└── docs/
```

This is the planned structure, not a claim that all directories or components already exist.

## Scope and Limitations

- The initial scope focuses on technical documentation associated with software repository changes.
- Retrieved documents are candidates for review, not automatically confirmed impacts.
- Retrieval relevance does not by itself establish that a document is incorrect or outdated.
- Agentic investigation may introduce additional latency and resource consumption.
- Evaluation quality depends on the correctness and coverage of the labelled dataset.
- Human review remains part of the intended workflow.

## Future Work

Potential extensions include dependency-aware impact analysis, broader repository support, improved change representations, more advanced evidence-verification strategies, and integration with developer workflows.

These extensions will be considered after the baseline and initial comparative evaluation are established.