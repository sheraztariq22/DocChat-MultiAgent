import google.generativeai as genai
from typing import Dict, List
from langchain.schema import Document
from config.settings import settings
import json

# Configure Gemini API
genai.configure(api_key=settings.GOOGLE_API_KEY)


class ResearchAgent:
    def __init__(self):
        """
        Initialize the research agent with Google Gemini.
        """
        print("Initializing ResearchAgent with Google Gemini...")
        
        # Initialize the Gemini model
        self.model = genai.GenerativeModel('gemini-pro')
        
        # Configure generation settings
        self.generation_config = {
            'temperature': 0.3,
            'max_output_tokens': 300,
        }
        
        print("Gemini model initialized successfully.")

    def sanitize_response(self, response_text: str) -> str:
        """
        Sanitize the LLM's response by stripping unnecessary whitespace.
        """
        return response_text.strip()

    def generate_prompt(self, question: str, context: str) -> str:
        """
        Generate a structured prompt for the LLM to generate a precise and factual answer.
        """
        prompt = f"""
        You are an AI assistant designed to provide precise and factual answers based on the given context.

        **Instructions:**
        - Answer the following question using only the provided context.
        - Be clear, concise, and factual.
        - Return as much information as you can get from the context.
        
        **Question:** {question}
        **Context:**
        {context}

        **Provide your answer below:**
        """
        return prompt

    def generate(self, question: str, documents: List[Document]) -> Dict:
        """
        Generate an initial answer using the provided documents.
        """
        print(f"ResearchAgent.generate called with question='{question}' and {len(documents)} documents.")

        # Combine the top document contents into one string
        context = "\n\n".join([doc.page_content for doc in documents])
        print(f"Combined context length: {len(context)} characters.")

        # Create a prompt for the LLM
        prompt = self.generate_prompt(question, context)
        print("Prompt created for the LLM.")

        # Call the Gemini model to generate the answer
        try:
            print("Sending prompt to the model...")
            response = self.model.generate_content(
                prompt,
                generation_config=self.generation_config
            )
            llm_response = response.text.strip()
            print("LLM response received.")
            print(f"Raw LLM response:\n{llm_response}")
        except Exception as e:
            print(f"Error during model inference: {e}")
            llm_response = "I cannot answer this question based on the provided documents."

        # Sanitize the response
        draft_answer = self.sanitize_response(llm_response) if llm_response else "I cannot answer this question based on the provided documents."

        print(f"Generated answer: {draft_answer}")

        return {
            "draft_answer": draft_answer,
            "context_used": context
        }