#installing dependencies
#if first time, run pip install openai

from config import OPENAI_API_KEY
import pandas as pd

import openai
#openai.organization = "org-YhptOOA3hPuAmtacppubVTs1"
openai.api_key =  OPENAI_API_KEY #os.getenv("OPENAI_API_KEY")
#openai.Model.list()

# see   https://platform.openai.com/docs/api-reference/completions/create

#model setup
model = "text-davinci-003" #the id of the model to include
prompt = "Write a letter to your local newspaper stating your opinion on the effects computers have on people. Persuade the readers to agree with you." #the prompt to provide 
essay_id = 1 #an id of the essay to save to the text file
essay_type = "persuasive/narrative" #type of essay to potentially the save
max_tokens = 300 #maximum number of tokens to include
n = 30 #number of essays to generate in single API call

count = 0 #provide count number as text id to save

for i in range (7): #loop through i API calls

    result = openai.Completion.create(model =  model, prompt = prompt, max_tokens = max_tokens, n = n) #API call, keeping result
    
    
    for x in range(len(result["choices"])):
        count = count + 1
        text = result["choices"][x]["text"]
        model = result["model"]

        with open(f'../rawData/aiEssays/eid{essay_id}_{model}_{count}.txt', 'w') as f:
            f.write(text)


pd.DataFrame({"ai_prompt" : ai_response_prompt, "ai_llm" : ai_response_model, "ai_text" : ai_response_text}).to_excel("../rawData/aiGenerated.xlsx", sheet_name= "test2")