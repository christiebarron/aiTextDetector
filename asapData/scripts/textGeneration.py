#transformers problem might be OneDrive problem

from transformers import AutoTokenizer, AutoModelForCausalLM

tokenizer = AutoTokenizer.from_pretrained("EleutherAI/gpt-j-6B")
model = AutoModelForCausalLM.from_pretrained("EleutherAI/gpt-j-6B")

text = "write an essay on computers"
encoded_input = tokenizer(text, return_tensors = 'tf')
output = model(encoded_input)

print(output)