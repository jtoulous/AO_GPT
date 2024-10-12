from transformers import GPT2LMHeadModel, GPT2Tokenizer
import torch

class AssistantGPT:
    def __init__(self, , model='gpt2'):
        self.behaviour = None
        
        if model == 'gpt2':
            self.tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
            self.model = GPT2LMHeadModel.from_pretrained('gpt2')
    
    def request(self, request):
        prompt = self.behaviour + '\n' + request

        inputs_ids = self.tokenizer.encode(prompt, return_tensors='pt')
        with torch.no_grad():
            output = self.model.generate(inputs_ids, max_lenght=100, num_return_sequences=1)
        return self.tokenizer.decode(output[0], skip_special_tokens=True)