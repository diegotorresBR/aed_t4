#[P] - Solicitação de Pouso
#[PE] - Pouso de Emergência
#[RP_AG] - Resposta de Pouso - Aguardar
#[RP_A] Resposta pouso autorizado. 

#[C]Comunicação
#[R_C]Resposta de Comunicação
#[D]Decolagem - Solicitacao
#[RD_AG]Resposta de Decolagem Aguardar
#[RD_A]Resp Decolagem Autorizado

import random as r
import fila as fila
import time as tempo
import threading as thread
espera = 3
tempo_operacao = 4
L_voos = []
fila_pouso = fila.Fila()
fila_pista = fila.Fila()
compa_avioes = ["AZUL", "TAM", "GOL", "COPA"]
l_cidade = ["Manaus", "Belem", "Salvador", "Rio de Janeiro", "Florianópolis"]
l_cidade_destino = ["Natal", "Teresina", "Fortaleza", "Curitiba"]

L_pousos_soli = []
L_pousos_eme = []
L_resp_p_ag = []
L_resp_p_a = []
L_dec_soli = [] 
L_resp_dec_a = []
L_resp_dec_ag = []
L_c = []
L_resp_c = []

for x in range(4):
    L_voos.append(str(r.choice(compa_avioes)) + str(r.randint(1000, 9999)))


arq = open("/home/diego/AEDTarefa/aed_t4/pouso.txt", 'r').readlines()

for x in arq:
    if("[P]" in x):
        L_pousos_soli.append(x.replace("[P]", ""))
    elif("[PE]" in x):
        L_pousos_eme.append(x.replace("[PE]", ""))
    elif("[RP_AG]" in x):
        L_resp_p_ag.append(x.replace("[RP_AG]", ""))
    elif("[RP_A]" in x):
        L_resp_p_a.append(x.replace("[RP_A]", ""))
    elif("[C]" in x):
        L_c.append(x.replace("[C]", ""))
    elif("[R_C]" in x):
        L_resp_c.append(x.replace("[R_C]", ""))
    elif("[D]" in x):
        L_dec_soli.append(x.replace("[D]", ""))
    elif("[RD_AG]" in x):
        L_resp_dec_ag.append(x.replace("[RD_AG]", ""))
    elif("[RD_A]" in x):
        L_resp_dec_a.append(x.replace("[RD_A]", ""))


def decolar():
    while(fila_pista.isEmpty() != True):
        print("--PREPARANDO PARA DECOLAR.")
        tempo.sleep(tempo_operacao)
        print(f"--{fila_pista.desenfileirar()} DECOLOU.")
def pousar():
    while(fila_pouso.isEmpty() != True):
        print("--PREPARANDO PARA POUSAR.")
        tempo.sleep(tempo_operacao)
        print(f"--{fila_pouso.desenfileirar()} POUSOU.")

for x in L_voos:
    #Iniciando a Comunicacao
    cida = r.choice(l_cidade)
    cida_destino = r.choice(l_cidade_destino)
    n_voo = str(x)
    texto_piloto = str(r.choice(L_c))
    print(texto_piloto.format(cidade=cida, voo=n_voo))
    tempo.sleep(espera)
    texto_torre = str(r.choice(L_resp_c))
    print(texto_torre.format(voo=n_voo))
    tempo.sleep(espera)

    t = thread.Thread(target=decolar)
    t2 = thread.Thread(target=pousar)


    #Solicitando
    deco_ou_pousa = r.randint(0,1)
    if(deco_ou_pousa == 0): #Decola
        texto_piloto = str(r.choice(L_dec_soli))
        print(texto_piloto.format(cidade=cida, voo=n_voo, cidade_destino = cida_destino))
    else:#pousa
        texto_piloto = str(r.choice(L_pousos_soli))
        print(texto_piloto.format(cidade=cida, voo=n_voo, cidade_destino = cida_destino))
    
    #respondendo
    if(deco_ou_pousa == 0):#Decola
        
        if(fila_pista.isEmpty()):
            fila_pista.enfileirar(n_voo)
            texto_torre = str(r.choice(L_resp_dec_a))
            print(texto_torre.format(cidade=cida, voo=n_voo, cidade_destino = cida_destino))
        else:
            texto_torre = str(r.choice(L_resp_dec_ag))
            print(texto_torre.format(cidade=cida, voo=n_voo, cidade_destino = cida_destino))
            fila_pista.enfileirar(n_voo)
    else:
        t2 = thread.Thread(target=pousar)
        if(fila_pouso.isEmpty()):
            fila_pouso.enfileirar(n_voo)
            texto_torre = str(r.choice(L_resp_p_a))
            print(texto_torre.format(cidade=cida, voo=n_voo, cidade_destino = cida_destino))
        else:
            texto_torre = str(r.choice(L_resp_p_ag))
            print(texto_torre.format(cidade=cida, voo=n_voo, cidade_destino = cida_destino))
            fila_pouso.enfileirar(n_voo)

    t.start()
    t2.start()
        
