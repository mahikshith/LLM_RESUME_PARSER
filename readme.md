**This repo is ""Work in Progress""**

## objective : 

To parse a resume and extract relevant information in a valid structured 'JSON' format using LLM 

For this I have used OLLAMA : Llama 3.2 - 3b model via langchain_ollama  

llm_script folder contains the code for the LLM and output parser 

And the script has been run in the ollama_resume_runner.ipynb and tested on a resume 

## Output : 

The output is a JSON file containing the extracted information from the resume. 

## Future work / improvements : 

1. Create a GUI for the user to input the resume 

2. Parse the information in JSON or document format 

3. Scrape Linkedin profile from the resume and extract relevant information

4. Create a knowledge base [embeddings + metadata] using the extracted information for each user

5. Create a internal chatbot using the knowledge base

6. Deploy on AWS 
