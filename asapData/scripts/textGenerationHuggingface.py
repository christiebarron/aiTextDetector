# Description #####
#this python script generates text based on a series of prompts using OpenAI's text-davinci-003 model
#It requires an OpenAI API key, which is not included on github.



#Loading Depencies #####

#if first time, run:   pip install transformers
from transformers import AutoTokenizer, AutoModelForCausalLM
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
n = 30 #number of essays to generate in single API call

#count = 0 #provide count number as text id to save
count = len(os.listdir('../rawData/aiEssays/')) +2 #so don't overwrite previously generated text


# Generating Essays #######

#load the tokenizer and model
model_name = "distilgpt2"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

#tokenize the prompt using model-specific tokenizer. see https://huggingface.co/docs/transformers/preprocessing
  #using padding as its is best practice
encoded_prompt5 = tokenizer(prompt5) #padding = True)

#loop through x texts generated
for x in range(n): 
    count = count + 1

    #configure the model to sample responses. see https://huggingface.co/docs/transformers/generation_strategies
    outputs = model.generate(encoded_prompt5, do_sample=True, max_new_tokens = max_tokens) #penatly_alpha = 0.6, top_k = 4  #save the encoded generated text as output
    text = tokenizer.batch_decode(outputs, skip_special_tokens=True) #decode the generated text so it is now text.
    #save the text with a name including the essay id, model, and count
    with open(f'../rawData/aiEssays/eid{essay_id}_{model}_{count}.txt', 'w') as f: 
        f.write(text)

        