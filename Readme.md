Welcome to DocChat!
Have you ever struggled to extract precise information from long, complex documents? Whether it's a research paper, legal contract, technical report, or environmental study, finding the exact details you need can feel overwhelming.

That's where DocChat comes in—a multi-agent RAG tool designed to help you ask questions about your documents and receive fact-checked, hallucination-free answers.

Sure, you could use ChatGPT or DeepSeek to accomplish this task, but when dealing with long documents containing multiple tables, images, and dense text, these models struggle with retrieval and are prone to hallucinations.

They often misinterpret tables, overlook key data hidden in footnotes, or even fabricate citations, as demonstrated below. The problem? These models lack document-aware reasoning and don't verify their responses against structured sources.

That's why DocChat takes a different approach. Instead of relying on a single LLM, it combines multiple AI agents, each with a specific role:

A Hybrid Retriever that intelligently combines BM25 keyword search and vector embeddings to retrieve the most relevant passages
A Research Agent that analyzes the retrieved content and generates an initial response
A Verification Agent that cross-checks the response against the original document to detect hallucinations and flag unsupported claims
A Self-Correction Mechanism that re-runs the research step if any contradictions or unsupported statements are found
This multi-step, verification-driven approach ensures that DocChat provides precise, document-grounded answers, even for complex and long-form documents that general-purpose chatbots struggle with. Whether you need to extract specific data points, summarize sections, compare multiple reports, or analyze tables, DocChat is built to help you navigate your documents with confidence.

--------------------------------------------------------------
A quick look at DocChat
What does the DocChat app do?
With DocChat, you can:

Upload and analyze long documents (PDFs, Word files, text reports) with ease
Ask questions about the content and get precise, source-backed answers
Extract specific details from structured documents, even those with tables, figures, and dense text
Avoid AI hallucinations—every response goes through a verification step to ensure factual correctness
Receive an alert when your question is irrelevant to the uploaded documents—so you know when the AI cannot confidently answer based on the provided sources
Retrieve accurate answers even when multiple documents are uploaded—DocChat intelligently finds the right document to reference

-------------------------------------------------------------
python3.11 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

python app.py

----------------lINKED in---------------------
By building this application, you have successfully explored the power of multi-agent retrieval-augmented generation (RAG) using LangGraph, Docling, watsonX AI, and ChromaDB. This project integrates multiple components—document processing, hybrid retrieval, structured AI workflows, and verification agents—into a seamless, interactive AI-driven application.

With the Gradio-powered UI, users can intuitively upload documents, ask complex questions, and receive fact-checked, AI-generated responses in real time. This marks the culmination of combining retrieval techniques, structured AI interactions, and LLM-based response generation into a production-ready system.

-------------DO Next-------------------
What you can do next
Now that you've built the core system, here are some next steps to further enhance your project:

Try different embedding models: Experiment with OpenAI, Hugging Face, or custom-trained embeddings to compare retrieval performance

Enhance the RAG pipeline: Improve the retriever's ranking logic, adjust retrieval weights, or add post-processing for better answer formulation

Implement Guardrails & AI trust mechanisms: Use Llama Guard, AI moderation tools, or manual review processes to ensure responsible AI usage

Optimize the multi-agent workflow: Tune verification heuristics, introduce feedback loops, or implement self-improving AI responses

Scale & deploy the app: Deploy DocChat on a cloud service (e.g., Hugging Face Spaces, AWS, or IBM Cloud) to make it widely accessible

Customize the UI: Modify the Gradio interface to improve user experience, add chat history tracking, or enable document annotations.

