# Description #####
#this python script generates text based on a series of prompts using HuggingFace's transformers library.

#Loading Depencies #####

#if first time, run:   pip install transformers
from transformers import pipeline, AutoTokenizer, AutoModelForCausalLM
import os #for working with paths


# Model Setup ######


#create list of prompts
prompt1 = "Write a letter to your local newspaper stating your opinion on the effects computers have on people. Persuade the readers to agree with you." #the prompt to provide 
prompt2 = "Write a persuasive essay to a newspaper about censorship in libraries. Do you believe that certain materials, such as books, music, movies, and magazines should be removed from the shelves if they are found offensive? " #the prompt to provide 
prompt3 = "Write a 200 word response that explains how the features of the setting affect the cyclist in 'Rough Road Ahead' by Joe Kurmaski."
prompt4 = "Why does Winter Hibiscus by Minfong Ho end with 'When they come back in the spring, when the snows melt and the geese return and this hibiscus is budding, then I will take that test again?'" 
prompt5 = "Write a 200 word essay about the mood created in the memoir 'From Home: The Blueprints of Our Lives' by Narciso Rodriguez."
prompt6 = "Write an essay describing the obstacles the builders of the Empire State Building faced in allowing dirigibles to dock. Use information from 'The Mooring Mast' by Marcia Amidon Lüsted."
prompt7 = "Being patient means that you are understanding and tolerant. A patient person experience difficulties without complaining. Write a true story about a time someone was patient using first person." #using first person. #the prompt to provide 
prompt8 = "Laughter is the shortest distance between two people. Laughter is important in any relationship. Write a true story involving laughter in first person." #using first person. #the prompt to provide 
prompts = ['prompt{}'.format(i) for i in range(1, 9)] #doesn't work
prompts = [prompt1, prompt2, prompt3, prompt4, prompt5, prompt6, prompt7, prompt8]

essay_ids = [1, 2, 3, 4, 5, 6, 7, 8]
essay_id = 5 #an id of the essay to save to the text file
essay_type = "persuasive/narrative" #type of essay to potentially save
max_tokens = 50 #maximum number of tokens to include
n = 2 #number of essays to generate in single API call
loops = 2 #number of times to loop through generating text

#count = 0 #provide count number as text id to save
count = len(os.listdir('../rawData/aiEssays/')) +2 #so don't overwrite previously generated text


# Generating Essays #######

#load the tokenizer and model
model_name = "distilgpt2"

#alternative models:
#model_name = "bigscience/T0pp"
#model_name = "EleutherAI/gpt-j-6B"


#loop through i number of loops using model to generate a series of essays

for i in range(loops):
  generator = pipeline('text-generation', model = model_name)
  outputs = generator(prompt5, max_length = max_tokens, num_return_sequences=n)

  #within each call, extract a single text and save it
  for x in range(n): 
    count = count + 1

    #configure the model to sample responses. see https://huggingface.co/docs/transformers/generation_strategies
    text = outputs[x]["generated_text"] #decode the generated text so it is now text.
    #save the text with a name including the essay id, model, and count
    with open(f'../rawData/aiEssays/eid{essay_id}_{model_name}_{count}.txt', 'w') as f: 
        f.write(text)


        