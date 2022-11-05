from time import sleep
from statistics import pvariance, pstdev
T, N = input().split()
T, N = [int(T), int(N)]
lista1_atributos = []
lista1 = []
Tarefa1_referencia = ['bison', 'elephant', 'horse', 'ibis', 'sky', 'mountain', 'building', 'flower',
          'sand', 'tree', 'field', 'road', 'tower', 'ocean', 'cliff', 'waterfall']
lista2_atributos = []
lista2 = []
x_variancia = []
y_variancia = []
larg_variancia = []
alt_variancia = []
lista3 = []
lista3_atributos = []
lista3_final = []
lista4= []
lista4_atributos = []
lista_juncao = []


def T1(n):
    cont = -1
    for i in range(0, N):
        u = input()
        n1 = str(input())
        n2 = str(input())
        if n1 not in lista1_atributos:
            if cont >= 0:
                if n1 != lista1_atributos[0]:
                    lista1.append(lista1_atributos[:])
                    lista1_atributos.clear()
                    lista1_atributos.append(n1)
            else:
                lista1_atributos.append(n1)
                cont += 1
        for e in Tarefa1_referencia:
            if e in n2:
                lista1_atributos.append(e)
        a1, a2, a3, a4 = input().split()
        a1, a2, a3, a4 = [int(a1), int(a2), int(a3), int(a4)]
    lista1.append(lista1_atributos)

def T2(n):
    cont_diferente = -1
    tot_caixas = x_total = x_medio = y_total = y_medio = larg_total = larg_media = alt_total = alt_media = 0
    area_total = area_media = dv_x = dv_y = dv_larg = dv_alt = 0
    x_des = y_des = larg_des = alt_des = 0
    for i in range(0, N):
        u = input()
        n1 = str(input())
        n2 = str(input())
        a1, a2, a3, a4 = input().split()
        a1, a2, a3, a4 = [int(a1), int(a2), int(a3), int(a4)]
        if n1 not in lista2_atributos:
            if cont_diferente >= 0:
                if n1 != lista2_atributos[0]:
                    lista2_atributos.append(tot_caixas/2)
                    x_medio = (x_total / (2 * tot_caixas))
                    lista2_atributos.append(x_medio/128)
                    y_medio = (y_total / (2 * tot_caixas))
                    lista2_atributos.append(y_medio/128)
                    larg_media = (larg_total / tot_caixas)
                    lista2_atributos.append(larg_media/128)
                    alt_media = (alt_total / tot_caixas)
                    lista2_atributos.append(alt_media/128)
                    area_media = area_total / (tot_caixas)
                    lista2_atributos.append(area_media/ (128**2))
                    dv_x = pstdev(x_variancia)
                    lista2_atributos.append(dv_x/32)
                    dv_y = pstdev(y_variancia)
                    lista2_atributos.append(dv_y / 32)
                    dv_larg = pstdev(larg_variancia)
                    lista2_atributos.append(dv_larg / 32)
                    dv_alt = pstdev(alt_variancia)
                    lista2_atributos.append(dv_alt / 32)

                    lista2.append(lista2_atributos[:])
                    lista2_atributos.clear()
                    tot_caixas = 0
                    x_total = y_total = larg_total = alt_total = area_total = 0
                    x_medio = y_medio = larg_media = alt_media = area_media = 0
                    x_variancia.clear()
                    y_variancia.clear()
                    larg_variancia.clear()
                    alt_variancia.clear()

                    lista2_atributos.append(n1)
            else:
                lista2_atributos.append(n1)
                cont_diferente += 1
        tot_caixas += 1

        x_total += (a1 + a3)
        x_des = a1 + a3
        x_variancia.append(x_des/2)
        y_total += (a2 + a4)
        y_des = a2 + a4
        y_variancia.append(y_des/2)

        larg_total += (a3 - a1)
        larg_des = a3 - a1
        larg_variancia.append(larg_des)
        alt_total += (a4 - a2)
        alt_des = a4 - a2
        alt_variancia.append(alt_des)
        largura_atual = (a3 - a1)
        altura_atual = (a4 - a2)
        area_atual = largura_atual * altura_atual
        area_total += area_atual

        if i == N - 1 and n1 == lista2_atributos[0]:
            lista2_atributos.append(tot_caixas / 2)
            x_medio = (x_total / (2 * tot_caixas))
            lista2_atributos.append(x_medio / 128)
            y_medio = (y_total / (2 * tot_caixas))
            lista2_atributos.append(y_medio / 128)
            larg_media = (larg_total / tot_caixas)
            lista2_atributos.append(larg_media / 128)
            alt_media = (alt_total / tot_caixas)
            lista2_atributos.append(alt_media / 128)
            area_media = area_total / (tot_caixas)
            lista2_atributos.append(area_media / 128 ** 2)
            dv_x = pstdev(x_variancia)
            lista2_atributos.append(dv_x / 32)
            dv_y = pstdev(y_variancia)
            lista2_atributos.append(dv_y / 32)
            dv_larg = pstdev(larg_variancia)
            lista2_atributos.append(dv_larg / 32)
            dv_alt = pstdev(alt_variancia)
            lista2_atributos.append(dv_alt / 32)

            lista2.append(lista2_atributos[:])

def T3(n):
    cont_sequencia = 0
    cont = -1
    cont_diferente = -1
    tot_caixas = x_total = x_medio = y_total = y_medio = larg_total = larg_media = alt_total = alt_media = 0
    area_total = area_media = dv_x = dv_y = dv_larg = dv_alt = 0
    x_des = y_des = larg_des = alt_des = 0
    for i in range(0, N):
        u = input()
        n1 = str(input())
        n2 = str(input())
        if n1 not in lista1_atributos:
            if cont >= 0:
                if n1 != lista1_atributos[0]:
                    lista1.append(lista1_atributos[:])
                    lista1_atributos.clear()
                    lista1_atributos.append(n1)
            else:
                lista1_atributos.append(n1)
                cont += 1
        for e in Tarefa1_referencia:
            if e in n2:
                lista1_atributos.append(e)
        a1, a2, a3, a4 = input().split()
        a1, a2, a3, a4 = [int(a1), int(a2), int(a3), int(a4)]
        if n1 not in lista2_atributos:
            if cont_diferente >= 0:
                if n1 != lista2_atributos[0]:
                    lista2_atributos.append(tot_caixas/2)
                    x_medio = (x_total / (2 * tot_caixas))
                    lista2_atributos.append(x_medio/128)
                    y_medio = (y_total / (2 * tot_caixas))
                    lista2_atributos.append(y_medio/128)
                    larg_media = (larg_total / tot_caixas)
                    lista2_atributos.append(larg_media/128)
                    alt_media = (alt_total / tot_caixas)
                    lista2_atributos.append(alt_media/128)
                    area_media = area_total / (tot_caixas)
                    lista2_atributos.append(area_media/ (128**2))
                    dv_x = pstdev(x_variancia)
                    lista2_atributos.append(dv_x/32)
                    dv_y = pstdev(y_variancia)
                    lista2_atributos.append(dv_y / 32)
                    dv_larg = pstdev(larg_variancia)
                    lista2_atributos.append(dv_larg / 32)
                    dv_alt = pstdev(alt_variancia)
                    lista2_atributos.append(dv_alt / 32)

                    lista2.append(lista2_atributos[:])
                    lista2_atributos.clear()
                    tot_caixas = 0
                    x_total = y_total = larg_total = alt_total = area_total = 0
                    x_medio = y_medio = larg_media = alt_media = area_media = 0
                    x_variancia.clear()
                    y_variancia.clear()
                    larg_variancia.clear()
                    alt_variancia.clear()

                    lista2_atributos.append(n1)
            else:
                lista2_atributos.append(n1)
                cont_diferente += 1
        tot_caixas += 1

        x_total += (a1 + a3)
        x_des = a1 + a3
        x_variancia.append(x_des / 2)
        y_total += (a2 + a4)
        y_des = a2 + a4
        y_variancia.append(y_des / 2)

        larg_total += (a3 - a1)
        larg_des = a3 - a1
        larg_variancia.append(larg_des)
        alt_total += (a4 - a2)
        alt_des = a4 - a2
        alt_variancia.append(alt_des)
        largura_atual = (a3 - a1)
        altura_atual = (a4 - a2)
        area_atual = largura_atual * altura_atual
        area_total += area_atual

        if i == N - 1 and n1 == lista1_atributos[0]:
            lista1.append(lista1_atributos[:])
        if i == N - 1 and n1 == lista2_atributos[0]:
            lista2_atributos.append(tot_caixas / 2)
            x_medio = (x_total / (2 * tot_caixas))
            lista2_atributos.append(x_medio / 128)
            y_medio = (y_total / (2 * tot_caixas))
            lista2_atributos.append(y_medio / 128)
            larg_media = (larg_total / tot_caixas)
            lista2_atributos.append(larg_media / 128)
            alt_media = (alt_total / tot_caixas)
            lista2_atributos.append(alt_media / 128)
            area_media = (larg_media * alt_media)
            lista2_atributos.append(area_media / 128 ** 2)
            dv_x = pstdev(x_variancia)
            lista2_atributos.append(dv_x / 32)
            dv_y = pstdev(y_variancia)
            lista2_atributos.append(dv_y / 32)
            dv_larg = pstdev(larg_variancia)
            lista2_atributos.append(dv_larg / 32)
            dv_alt = pstdev(alt_variancia)
            lista2_atributos.append(dv_alt / 32)

            lista2.append(lista2_atributos[:])
    for l in lista1:
        for e in Tarefa1_referencia:
            if any(e in s for s in l[1:len(l)]):
                lista3_atributos.append(1)
            else:
                lista3_atributos.append(0)
        lista3.append(lista3_atributos[:])
        lista_juncao.append(lista3_atributos[:])
        lista3_atributos.clear()
    for l in lista2:
        for c in l:
            if cont_sequencia == 0:
                lista4_atributos.append(c)
            else:
                lista4_atributos.append(c)
            cont_sequencia += 1
        lista4.append(lista4_atributos[:])
        lista_juncao.append(lista4_atributos[:])
        lista4_atributos.clear()
        cont_sequencia = 0


def indicadores_objetos(n):
    cont2 = 0
    contseq = 0
    T1(N)
    for l in lista1:
        print(l[0], end=' ')
        for e in Tarefa1_referencia:
            contseq += 1
            if any(e in s for s in l[1:len(l)]):
                if contseq < 16:
                    print(1, end=' ')
                else:
                    print(1)
            else:
                if contseq < 16:
                    print(0, end=' ')
                else:
                    print(0)
        contseq = 0
        cont2 = 0


def estatistica_caixas(n):
    cont_sequencia = 0
    T2(N)
    for l in lista2:
        for c in l:
            if cont_sequencia == 0:
                print(c, end=' ')
            elif 0 < cont_sequencia < len(l) - 1:
                print(f'{c:.1f}', end=' ')
            else:
                print(f'{c:.1f}')
            cont_sequencia += 1
        cont_sequencia = 0



def vetor_medio(n):
    cont_sequencia = 0

    indice1 = 0
    indice2 = 0
    indice3 = 0
    indice4 = 1
    soma = 0
    soma2 = 0
    T3(N)
    while True:
        if indice1 == len(lista3):
            indice1 = 0
            indice2 += 1
            print(f'{soma / len(lista3):.1f}', end=' ')
            soma = 0
            if indice2 == 16:
                break
        soma += lista3[indice1][indice2]
        indice1 += 1
    while True:
        if indice3 == len(lista2):
            indice3 = 0
            indice4 += 1
            if indice4 < 11:
                print(f'{soma2 / len(lista2):.1f}', end=' ')
            else:
                print(f'{soma2 / len(lista2):.1f}')
            soma2 = 0
            if indice4 == 11:
                break
        soma2 += lista2[indice3][indice4]
        indice3 += 1
        cont_sequencia += 1



def amostra_prototipica(n):
    distancias_pre = []
    distancias_pos = []
    distancias_pre2 = []
    distancias_pos2 = []
    lista_pre = []
    lista_pos = []
    indice = 0
    soma = 0
    mais_perto = 0
    mais_perto_index = 0
    T3(N)
    if len(lista_juncao) % 2 == 0:
        quantidade_imagens = int(len(lista_juncao) / 2)
    else:
        quantidade_imagens = int((len(lista_juncao) + 1) / 2)
    for a in range(0, quantidade_imagens):
        for d in lista_juncao[a + quantidade_imagens]:
            lista_pre.append(d)
        for c in lista_juncao[a]:
            lista_pre.append(c)
        lista_pos.append(lista_pre[:])
        lista_pre.clear()
    for e in range(0, len(lista_pos)):
        for f in range(0, len(lista_pos)):
            for g in range(0, 26):
                a =  (lista_pos[e][1 + g] - lista_pos[f][1 + g])
                if a < 0:
                    a *= -1
                soma += a
            distancias_pre.append(soma)
            soma = 0
        distancias_pos.append(distancias_pre[:])
        distancias_pre.clear()
    for g in range(0, len(distancias_pos)):
        distancias_pre2.append(sum(distancias_pos[g]))
    distancias_pos2.append(distancias_pre2[:])
    amaia = distancias_pos2[0]
    mais_perto = min(amaia)
    mais_perto_index = amaia.index(mais_perto)
    print(lista_pos[mais_perto_index][0])




if T == 1:
    indicadores_objetos(N)

elif T == 2:
    estatistica_caixas(N)

elif T == 3:
    vetor_medio(N)

elif T == 4:
    amostra_prototipica(N)
