# Description #####
#this python script generates text based on a series of prompts using Hugging Face's LLMs



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
n = 2 #number of essays to generate in single API call
loops = 2 #number of times to loop through generating text

#count = 0 #provide count number as text id to save
count = len(os.listdir('../rawData/aiEssays/')) +2 #so don't overwrite previously generated text


# Generating Essays #######

#load the tokenizer and model
model_name = "distilgpt2"
#model_name2 = "bigscience/T0pp"

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

#tokenize the prompt using model-specific tokenizer. see https://huggingface.co/docs/transformers/preprocessing
  #using padding as its is best practice
encoded_prompt5 = tokenizer(prompt5) #padding = True)

#loop through x texts generated

for i in range (loops):
  generator = pipeline('text-generation', model = model_name)
  text = generator(prompt5, max_length = 200, num_return_sequences=n)

  for x in range(n): 
    count = count + 1

    #configure the model to sample responses. see https://huggingface.co/docs/transformers/generation_strategies
    outputs = model.generate(encoded_prompt5, do_sample=True, max_new_tokens = max_tokens) #penatly_alpha = 0.6, top_k = 4  #save the encoded generated text as output
    text = tokenizer.batch_decode(outputs, skip_special_tokens=True) #decode the generated text so it is now text.
    #save the text with a name including the essay id, model, and count
    with open(f'../rawData/aiEssays/eid{essay_id}_{model}_{count}.txt', 'w') as f: 
        f.write(text)



# # SAVE RESULTS
# text_list = [] #create a list to add text files to.
# ai_llm = [] #a list of the large language model used
# eid = [] #essay prompt id
# row_id = [] #final number
# files = os.listdir('../rawData/aiEssays/') #get a list of all file names within the directory

# #extract relevant information from ai-generated text files
# for f in files:
#     filename = f'../rawData/aiEssays/{f}' #save the filename

#     with open(filename, 'r') as f: #open filename and save the text in it
#         text_list.append(f.read())
    
#     #append metadata saved in the filename (llm used, essay prompt, and row id)
#     ai_llm.append(filename.split("_")[1])
#     eid.append(filename.split("_")[0].split("d")[1])
#     row_id.append(filename.split("_")[2].split(".")[0])
    
# #save all extracted text to a pandas dataframe, then excel file.
# df = pd.DataFrame({"row_id" : row_id, "essay_id" : eid, "ai_llm": ai_llm, 'ai_essay': text_list})
# df.to_excel("../cleanData/aiGenerated.xlsx")
        