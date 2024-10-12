from colorama import Fore, Style

def PrintLog(log):
    print(f'{Fore.GREEN}{log}{Style.RESET_ALL}')

def PrintError(error):
    print(f'{Fore.RED}{error}{Style.RESET_ALL}')

def PrintInfo(info):
    print(f'{Fore.BLUE}{info}{Style.RESET_ALL}')