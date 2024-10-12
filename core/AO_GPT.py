from openai import OpenAI

from utils.logs import PrintLog, PrintInfo
from utils.system import SystemRequest
from utils.tools import Format_Behavior, Format_Prompt

class AO_GPT:
    def __init__(self, agents_config, workflow=None, OAI_API=None):
        self.agents = {}
        self.workflow = workflow
        self.first_in_workflow = workflow[0] if workflow is not None else None
        self.OAI_API = OAI_API

        for agent_name in agents_config:
            self.agents[agent_name] = {}
            self.agents[agent_name]['behavior'] = Format_Behavior(agents_config[agent_name]['behavior'], agents_config[agent_name]['links'])
            self.agents[agent_name]['history'] = [{'role': 'system', 'content': self.agents[agent_name]['behavior']}]
            self.agents[agent_name]['model'] = agents_config[agent_name]['model']

    def Request(self, nxt_agent, request): #for 'Assistant' or other independant AI
        agent_model = self.agents[nxt_agent]['model']
        if agent_model == 'OAI_API':
            return self.oai_gen(nxt_agent, request)
        elif agent_model == 'gpt2':
            return self.gpt2_gen(nxt_agent, request)
        
        raise Exception(f'Error:\n===> Model unsupported :{agent_model}')
    
    def Start_Workflow(self, workflow_user, request): #for starting the AI 'Workflow'    
        nxt_agent = self.first_in_workflow
        prev_agent = 'no one'

        while nxt_agent != workflow_user:
            if nxt_agent == 'System':
                request = SystemRequest(request, prev_agent)
            else:    
                request = self.Request(nxt_agent, request)
            
            prev_agent = nxt_agent
            nxt_agent, *request = request.split(' ')
            request = ' '.join(request)
        
        #clear workflow history
        return nxt_agent + ' ' + request


    def oai_gen(self, nxt_agent_name, request):
        client = OpenAI(api_key=self.OAI_API)
        nxt_agent = self.agents[nxt_agent_name]

        conv = Format_Prompt(nxt_agent['behavior'], nxt_agent['history'], request)
        generated = client.chat.completions.create(
                model="gpt-4",
                messages=conv
        )
        answer = generated.choices[0].message.content

        PrintLog(f'\n==========  {nxt_agent_name}  ==========')
        PrintInfo(f' ===> {answer}')
        nxt_agent['history'].append({'role': 'user', 'content': request})
        nxt_agent['history'].append({'role': 'assistant', 'content': answer})
        return answer

    def gpt2_gen(self, nxt_agent_name, request):
        return