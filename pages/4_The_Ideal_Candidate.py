import utils
import streamlit as st

from langchain.agents import AgentType
from langchain.chat_models import ChatOpenAI
from langchain.agents import initialize_agent, Tool
from langchain.chains import LLMChain, SequentialChain
from langchain.prompts import PromptTemplate

# For python execution
from langchain.tools import PythonREPLTool

# Prompt templates
import templates

st.set_page_config(page_title="The Ideal Candidate", page_icon="🌐")
st.header('Chatbot That Solves Coding Challenge Problems')
st.write('Generates problems and solves them with Python code')


class ChatbotIdealCandidate:

    def __init__(self):
        utils.configure_openai_api_key()
        self.openai_model = "gpt-3.5-turbo"
        print(templates.ideal_candidate_chain_problem)
        utils.divider()
        print(templates.ideal_candidate_chain_solution)
        utils.divider()
        self.template_problem = PromptTemplate(input_variables=["problem_type", "difficulty"], template=templates.ideal_candidate_chain_problem)
        self.template_solution = PromptTemplate(input_variables=["problem"], template=templates.ideal_candidate_chain_solution)

    def render_page_elements(self):
        topic_options = [
            "Array", "String", "Hash Table", "Dynamic Programming", "Math",
            "Sorting", "Greedy", "Depth-First Search", "Binary Search", "Database",
            "Breadth-First Search", "Tree", "Matrix", "Two Pointers", "Bit Manipulation",
            "Binary Tree", "Heap (Priority Queue)", "Stack", "Prefix Sum", "Graph",
            "Simulation", "Design", "Counting", "Backtracking", "Sliding Window",
            "Union Find", "Linked List", "Ordered Set", "Enumeration", "Monotonic Stack",
            "Trie", "Recursion", "Divide and Conquer", "Number Theory", "Bitmask",
            "Queue", "Binary Search Tree", "Memoization", "Segment Tree", "Geometry",
            "Topological Sort", "Binary Indexed Tree", "Game Theory", "Hash Function",
            "Shortest Path", "Combinatorics", "Interactive", "String Matching", "Data Stream",
            "Rolling Hash", "Brainteaser", "Randomized", "Monotonic Queue", "Merge Sort",
            "Iterator", "Concurrency", "Doubly-Linked List", "Probability and Statistics",
            "Quickselect", "Bucket Sort", "Suffix Array", "Minimum Spanning Tree", "Counting Sort",
            "Shell", "Line Sweep", "Reservoir Sampling", "Strongly Connected Component",
            "Eulerian Circuit", "Radix Sort", "Rejection Sampling"
        ]
        difficulty_options = ["Very Easy", "Easy", "Medium", "Hard", "Very Hard", "Insane", "Unsolvable"]
        
        self.problem_type = st.selectbox("Select a topic:", topic_options)
        self.difficulty = st.selectbox("Select a difficulty:", difficulty_options)
        if st.button("Execute Function"):
            self.run()
        

    def run(self):
        if self.problem_type is None or self.difficulty is None:
            st.toast("Required inputs are not selected!")
        else:
            agent = self.setup_agent()
            print(self.problem_type)
            utils.divider()
            print(self.difficulty)
            utils.divider()
            st.write(agent({"problem_type": self.problem_type, "difficulty": self.difficulty}))

    def setup_agent(self):
        # Define tool
        python_repl = PythonREPLTool()

        tools = [
            Tool(
                name="Python REPL",
                func=python_repl.run,
                description="A Python shell. Use this to execute python commands. Input should be a valid python command. If you expect output it should be printed out.",
            ),
        ]
        llm = ChatOpenAI(model_name=self.openai_model, streaming=True)

        problem_chain = LLMChain(llm=llm, prompt=self.template_problem, output_key="problem")
        solution_chain = LLMChain(llm=llm, prompt=self.template_solution, output_key="solution")
        seq_chain = SequentialChain(chains=[problem_chain, solution_chain], input_variables=["problem_type", "difficulty"], output_variables=["problem", "solution"])
        
        return seq_chain

        # Setup LLM and Agent
        
        # agent = initialize_agent(
        #     tools=tools,
        #     llm=llm,
        #     agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        #     handle_parsing_errors=True,
        #     verbose=True
        # )
        # return agent
    
    def main(self):
        self.render_page_elements()



if __name__ == "__main__":
    obj = ChatbotIdealCandidate()
    obj.main()
