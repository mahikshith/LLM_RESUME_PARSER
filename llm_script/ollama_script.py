from langchain_ollama import ChatOllama 

from langchain_core.prompts import(

    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
    ChatPromptTemplate,
)

# output parser  

from langchain.output_parsers import StringOutputParser , JsonOutputParser

base_url_ollama = "http://localhost:11434"
model = 'llama3.2:3b'

llm = ChatOllama(base_url=base_url_ollama, model=model)  # not using all the parameters here 

# System Message 
system_message_prompt = SystemMessagePromptTemplate.from_template("""You are helpful AI assistant who answers user's questions based on the provided context""")

# we get resume text [context] from pypdf reader 
# Question is passed later in the function call

prompt = """
            **Task:** Extract key information from the following resume text.

            **Resume Text:**
            {context}

            **Instructions:**
            Please extract the following information and format it in a clear structure:

            1. **Contact Information:**
            - Name:
            - Email:
            - Phone Number:
            - Website/Portfolio/LinkedIn:
            - Github Profile:

            2. **Education:**
            - Institution Name:
            - Degree:
            - Field of Study:
            - Graduation Date:

            3. **Experience:**
            - Job Title:
            - Company Name:
            - Location:
            - Dates of Employment:
            - Responsibilities/Projects:

            4. **Projects:**
            - Project Title:
            - Description/Technologies Used:
            - Outcomes/Results:

            5. **Skills:**
            - Programming Languages:
            - Technologies/Tools/frameworks:

            6. **Additional Information:** (if applicable)
            - Certifications:
            - Awards or Honors:
            - Professional Affiliations:
            - Languages:

            **Question:**
            {question}

            **Extracted Information:**
        """
# Human Message 
human_message_prompt = HumanMessagePromptTemplate.from_template(prompt)

# LLM chain that can be called : 

def LLM_chain(context , question):
    template = ChatPromptTemplate.from_messages([system_message_prompt , human_message_prompt])
    # LLM Chain 
    ollama_chain  = template | llm | StringOutputParser()   
    return ollama_chain.invoke({"context" : context , "question" : question}) 

# if the above strparser doesn't give out answers in the required format then we can use the json parser 

def LLM_chain_json(context):

    json_prompt_validate = """
            **Task:** Validate and correct the following JSON data : 

            **JSON Data:**
            {context}

            **Instructions:**
            Provide JSON  only output with no explantion or preamble.

            **Corrected JSON:**"""
    human_message = HumanMessagePromptTemplate.from_template(json_prompt_validate)

    template = ChatPromptTemplate.from_messages([system_message_prompt , human_message])

    # JSON llm chain  
    json_ollama_chain = template | llm | JsonOutputParser()
    return json_ollama_chain.invoke({"context" : context})