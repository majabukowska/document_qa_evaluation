# Document QA with Answer Evaluation

This project demonstrates how to build a document-based question answering system
that not only generates answers from retrieved context, but also evaluates whether
the generated answers are supported by the source documents.

## High-level idea

1. Documents are ingested and split into semantic chunks
2. Relevant chunks are retrieved for a user question using embedding similarity
3. A language model generates an answer based on the retrieved context
4. The answer is evaluated to verify whether it is supported by the retrieved documents

## Current status

The project implements a complete retrieval-augmented generation (RAG) pipeline,
including retrieval evaluation and answer support verification.

### Implemented components

### 1. Document loaders
- HTML loader (BeautifulSoup-based)
- PDF loader (pdfplumber)
- DOCX loader (python-docx)
- Unified document loader interface based on file extension

### 2. Text cleaning
- Removal of navigation elements, cookie banners and boilerplate content
- Generic blacklist-based filtering (login, subscribe, privacy, etc.)
- Whitespace normalization and paragraph reconstruction
- Post-processing for sentence and word continuity
- Designed to be domain-agnostic (not source-specific)

### 3. Chunking
- Paragraph-based chunking with configurable maximum length
- Word-based fallback splitting for long paragraphs
- Configurable overlap between chunks
- Chunk-level metadata:
  - chunk index
  - word count
  - source document
  - split type (paragraph / word split)

### 4. Embedding-based retrieval
- Vector embedding computation for document chunks
- Similarity-based retrieval of relevant context for a query
- Retrieval scoring and ranking
- Retrieval quality evaluation (Hit@K, MRR)

### 5. Answer generation and evaluation
- LLM-based answer generation using retrieved context
- Answer support verification using semantic similarity between the answer and context
- Detection of unsupported or potentially hallucinated answers

## Example run

**Example question:**
> What is PyTorch?

**Retrieved context:**
- IBM PyTorch documentation

**Generated answer:**
> PyTorch is an open-source, Python-based deep-learning framework that provides a
> flexible high-level API for building and training neural networks. It supports
> rapid prototyping, automatic differentiation, and execution on CPUs or GPUs.
