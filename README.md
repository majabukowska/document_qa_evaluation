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
