from AO_GPT import AO_GPT
from utils.logs import PrintLog, PrintInfo, PrintError
from agents_config import Get_Config

global agents
agents = AO_GPT(Get_Config(), workflow=['Supervisor', 'Executer'], OAI_API='XXXXXXXXXXXXXXX')

if __name__ == '__main__':
    try:
        while True:
            User_request = input('\n==========  System  ==========\n ==> ')
            request = 'Assistant ' + User_request
            prev_agent = 'no one'

            while True:
                nxt_agent, *request = request.split(' ')
                request = ' '.join(request)
                
                if nxt_agent == 'User':
                    break
                elif nxt_agent == 'Assistant':
                    request = agents.Request(nxt_agent, request)
                elif nxt_agent == 'Workflow':
                    request = agents.Start_Workflow('Assistant', request)
                prev_agent = nxt_agent

            PrintError(f'\n==========  Assistant  ==========')
            PrintError(f' ===> {request}')

    except Exception as error:
        PrintError(error)