#installing dependencies
#if first time, run pip install openai

from config import OPENAI_API_KEY
import pandas as pd

import openai
#openai.organization = "org-YhptOOA3hPuAmtacppubVTs1"
openai.api_key =  OPENAI_API_KEY #os.getenv("OPENAI_API_KEY")
#openai.Model.list()

# see   https://platform.openai.com/docs/api-reference/completions/create

ai_response = []

#model setup
model = "text-davinci-003" #the id of the model to include
prompt = "Write a letter to your local newspaper stating your opinion on the effects computers have on people. Persuade the readers to agree with you." #the prompt to provide 
essay_id = 1
essay_type = "persuasive/narrative"
max_tokens = 300 #maximum number of tokens to include
n = 30 #number of essays to generate in single API call

ai_response.append(openai.Completion.create(model =  model, prompt = prompt, max_tokens = max_tokens, n = n))
#set up lists to store variables in
ai_response_text = []
ai_response_model = []
ai_response_prompt = []
ai_response_essay_id = []
ai_response_essay_type = []
counter = 0

#extract information from the saved data
for i in range(len(ai_response)): #loop through all API calls
    for x in range(len(ai_response[i]["choices"])): #loop through all text generated within single API call
        ai_response_text.append(ai_response[i]["choices"][x]["text"]) #save text response
        ai_response_model.append(ai_response[i]["model"]) #save the large language model used to generate the text
        ai_response_prompt.append(prompt) #save the written prompt given.
        ai_response_essay_id.append(essay_id) #save the essay id
        ai_response_essay_type.append(essay_type)

pd.DataFrame({"ai_prompt" : ai_response_prompt, "ai_llm" : ai_response_model, "ai_text" : ai_response_text}).to_excel("../rawData/aiGenerated.xlsx", sheet_name= "test2")