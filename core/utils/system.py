import subprocess

def SystemRequest(request, prev_agent):
    #GERER PLUSIEUR TYPE DE REQUETE PLUS TARD
    # GENRE 'if request_type == 'exec'' , etc...

    result = subprocess.run(request, shell=True, capture_output=True, text=True)
    output = result.stdout
    err_output = result.stderr
    exit_code = result.returncode
    res_prompt = f'{prev_agent} output: "{output}"\n err_output: "{err_output}"\n exit_code: {exit_code}'
    return res_prompt
