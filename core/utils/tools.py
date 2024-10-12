def Format_Behavior(behavior, links):
    link_str = ''
    for link in links:
        link_str = link_str + links[link] + '\n'
    
    return behavior + '\n' + link_str

def Format_Prompt(behavior, history, request):
    prompt = 'CONV HISTORY:\n'
    for log in history:
        prompt = prompt + log['role'] + ':' + log['content'] + '\n'
    prompt = '\n\nBEHAVIOR' + behavior + '\n\nREQUEST: ' + request
    return [{'role': 'user', 'content': prompt}]

#def Clear_History():