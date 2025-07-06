import os


tarefas = [
    {'nome': 'Estudar', 'status': 'pendente'},
    {'nome':'programar','status':'pendente'},
    {'nome':'prova de matematica','status':'pendente'}
]


def mostrarLista():
    maior = 0

    for i in range(len(tarefas)):
        if len(tarefas[i]['nome']) > maior: 
            maior = len(tarefas[i]['nome'])

    print('\n========= LISTA DE TAREFAS =========')
    print('|Nº|Tarefa',' '*(maior - 6),'|Status',' '*(len(tarefas[i]["status"]) - 5),'|')
    for i in range(len(tarefas)):
        print(f'|{(i +1):2.0f}|{tarefas[i]["nome"]}',' '*(maior - len(tarefas[i]['nome'])),f'|{tarefas[i]["status"]}',' '*(9 - len(tarefas[i]['status'])),'|')


def tomadaDecisao(esc):
    if esc == 1:
        adicionar(tarefas)
    elif esc == 2:
        verTafefas(tarefas)
    elif esc == 3:
        marcarCluido(tarefas)
    elif esc == 4:
        remover(tarefas)
    elif esc == 5:
        os.system('cls' if os.name == 'nt' else 'clear')
        print('Finalizado!')
        exit()


def menu(): # MENU
    
    os.system('cls' if os.name == 'nt' else 'clear')
    print('===== LISTA DE TAREFAS =====\n1. Adicionar nova tarefa\n2. Ver tarefas\n3. Marcar tarefa como concluída\n4. Remover tarefa\n5. Sair')


    while True:
        try:
            esc = int(input('Escolha uma opção:'))
            if esc < 6:
                tomadaDecisao(esc)
                break
            print('Digite apenas as opções listada acima!')
        except ValueError:
            os.system('cls' if os.name == 'nt' else 'clear')
            print('Digite apenas as opções listada acima!')



def verTafefas(tarefas): # OPÇÃO 2

    os.system('cls' if os.name == 'nt' else 'clear')
    mostrarLista()
    
    while True:
        esc = input('Voltar ao menu? (S/N)')
        if esc == 's' or esc == 'S':
            menu()
            break
        else:
            verTafefas(tarefas)

def adicionar(tarefas):
    os.system('cls' if os.name == 'nt' else 'clear')
    while True:
        nome = input('Digite o nome da tarefa: ')
        while True:
            try:
                status = int(input('Digite os status da tarefa\n    1 - PENDENTE\n    2 - CONLUIDO\n--> '))
                if status == 1 or status == 2:
                    if status == 1:
                        status = 'pendente'
                        break
                    elif status == 2:
                        status = 'concluido'
                        break
                else:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print('Digite apenas as opções acima!')
                    continue
            except ValueError:
                print('Digite apenas as opções acima!')
        tarefas.append({'nome': nome, 'status': status})

        esc = input(f'Tarefa: {nome}\nStatus: {status}\nDeseja continua? (S/N) ')
        if esc == 's' or esc == 'S':
            os.system('cls' if os.name == 'nt' else 'clear')
            continue
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            menu()
            break
            
    return tarefas


def marcarCluido(tarefas):
    os.system('cls' if os.name == 'nt' else 'clear')
    while True:
        mostrarLista()
        indice = int(input('Qual tarefa concluiu:\n(OBS: digite o numero da tarefa)\n-->'))
        indice -= 1
        if indice <= len(tarefas):
            os.system('cls' if os.name == 'nt' else 'clear')
            try:
                tarefas[indice]['status'] = 'concluido'
                mostrarLista()
            except IndexError:
                os.system('cls' if os.name == 'nt' else 'clear')
                print('Tarefa não esta na lista!\nDIGITE APENAS NO QUE TEM NA LISTA')
                continue
     
        esc = input('Deseja continua? (S/N) ')
        if esc == 's' or esc == 'S':
            os.system('cls' if os.name == 'nt' else 'clear')
            continue
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            menu()
            break
            

def remover(tarefas):
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        mostrarLista()
        indice = int(input('Qual tarefa concluiu:\n(OBS: digite o numero da tarefa)\n-->'))
        indice -= 1
        if indice <= len(tarefas):
            nome = tarefas[indice]['nome']
            del tarefas[indice]
        os.system('cls' if os.name == 'nt' else 'clear')
        mostrarLista()
        print(f'Tarefa {nome} removido')
        
        esc = input('Deseja continua? (S/N) ')
        if esc == 's' or esc == 'S':
            os.system('cls' if os.name == 'nt' else 'clear')
            continue
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            menu()
            break
    

menu()

