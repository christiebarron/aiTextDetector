# Description #####
#this python script generates text based on a series of prompts using OpenAI's text-davinci-003 model
#It requires an OpenAI API key, which is not included on github.



#loading depencies #####
#if first time, run pip install openai

from config import OPENAI_API_KEY #loading API key. you will need your own.
import pandas as pd #for data wrangling

import openai #for utilization of large language model
openai.api_key =  OPENAI_API_KEY #save API key

# see   https://platform.openai.com/docs/api-reference/completions/create


# Model Setup ######
model = "text-davinci-003" #the id of the model to include
prompt1 = "Write a letter to your local newspaper stating your opinion on the effects computers have on people. Persuade the readers to agree with you." #the prompt to provide 
prompt7 = "Being patient means that you are understanding and tolerant. A patient person experience difficulties without complaining. Write a true story about a time someone was patient using first person." #using first person. #the prompt to provide 
prompt8 = "Laughter is the shortest distance between two people. Laughter is important in any relationship. Write a true story involving laughter in first person." #using first person. #the prompt to provide 
essay_id = 1 #an id of the essay to save to the text file
essay_type = "persuasive/narrative" #type of essay to potentially the save
max_tokens = 300 #maximum number of tokens to include
n = 30 #number of essays to generate in single API call

count = 0 #provide count number as text id to save

#other prompts used:
#

#prompt 8: 

# Generating Essays #######
#loop through i API calls
for i in range (7): 

    result = openai.Completion.create(model =  model, prompt = prompt, max_tokens = max_tokens, n = n) #API call, keeping result
    
    #loop through x texts generated
    for x in range(len(result["choices"])): 
        count = count + 1
        text = result["choices"][x]["text"] #extract the ai-generated text
        model = result["model"] #extract the model name

        #save the text with a name including the essay id, model, and count
        with open(f'../rawData/aiEssays/eid{essay_id}_{model}_{count}.txt', 'w') as f: 
            f.write(text)
