# Document QA with Answer Evaluation

This project explores how to build a document-based question answering system
that not only generates answers using retrieved context, but also evaluates
whether the answer is supported by the source documents.

## High-level idea
1. Documents are ingested and split into chunks
2. Relevant chunks are retrieved for a user question
3. A language model generates an answer based on the retrieved context
4. A separate evaluation model estimates whether the answer is supported
   by the documents

## Current status

The project currently implements the document ingestion stage of a RAG-style pipeline.

### Implemented components

**1. Document loaders**
- HTML loader (BeautifulSoup-based)
- PDF loader (pdfplumber)
- DOCX loader (python-docx)
- Unified document loader interface based on file extension

**2. Text cleaning**
- Removal of navigation, cookie banners and boilerplate content
- Generic blacklist-based filtering (login, subscribe, privacy, etc.)
- Whitespace normalization and paragraph reconstruction
- Post-processing for sentence and word continuity
- Designed to be domain-agnostic (not source-specific)

**3. Chunking**
- Paragraph-based chunking with configurable max length
- Word-based fallback splitting for long paragraphs
- Configurable overlap between chunks
- Chunk-level metadata:
  - chunk index
  - word count
  - source document
  - split type (paragraph / word split)

The ingestion pipeline outputs clean, structured text chunks ready for embedding and retrieval.
