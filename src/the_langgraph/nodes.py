from langchain.prompts import PromptTemplate
from langchain.schema.runnable import RunnableSequence
from typing import Dict
from termcolor import colored

from .utils import get_openai_llm, get_pinecone_vectorstore
from .state import MovieState

class Nodes:
    def __init__(self):
        self.llm = get_openai_llm()
        self.vectorstore = get_pinecone_vectorstore()
        
    def research_movie(self, state: MovieState):
        query = state['question']
        docs = self.vectorstore.similarity_search(query, k=3)
        context = "\n".join([doc.page_content for doc in docs])
        
        template = """
        Based on the following question and context,
        provide detailed information about the movie:
        
        Question: {question}
        
        Context:
        {context}
        
        Provide a comprehensive overview of the movie,
        including its plot, cast, director, release
        date, and any other relevant details:
        """
        
        research_prompt_template = PromptTemplate(
            input_variables=["question", "context"],
            template=template
        )
        
        research_chain = research_prompt_template | self.llm
        ai_msg = research_chain.invoke({"question": state['question'], "context": context})
        response = ai_msg.content
        
        state['research_output'] = response
        print(colored(f"Researcher 👩🏿‍💻: {response}", 'cyan'))
        return state
    
    def analysis_movie(self, state: MovieState):
        query = f"analysis of {state['question']}"
        docs = self.vectorstore.similarity_search(query, k=2)
        analysis_context = "\n".join([doc.page_content for doc in docs])
        
        template = """
        Based on the following movie information and additional
        context,provide an in-depth analysis:
        
        Movie Information:
        {movie_info}
        
        Additional Context:
        {context}
        
        Please provide a comprehensive analysis of the movie, including:
        • Themes and symbolism
        • Cinematography and visual style
        • Character development and performances
        • Critical reception and impact
        • Comparison to other films in the same genre or by the same director
        """
        
        analysis_prompt_template = PromptTemplate(
            input_variables=["movie_info", "context"],
            template=template
        )
        
        analysis_chain = analysis_prompt_template | self.llm
        ai_msg = analysis_chain.invoke({"movie_info": state['research_output'], "context": analysis_context})
        response = ai_msg.content
        
        state['analysis_output'] = response
        print(colored(f"analyst 🧑🏼‍💻: {response}", 'green'))
        return state