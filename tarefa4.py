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

for x in range(10):
    L_voos.append(str(r.choice(compa_avioes)) + str(r.randint(1000, 9999)))


arq = open("/home/admin/Documentos/pouso.txt", 'r').readlines()

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

print(L_resp_dec_a)