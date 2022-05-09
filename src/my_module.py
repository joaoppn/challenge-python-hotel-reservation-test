from calendar import weekday
import re



class Lakewood:
    name = "Lakewood"
    classificacao = 3
    class Regular:
        weekday = 110
        weekend = 90
    class Reward:
        weekday = 80
        weekend = 80 


class Bridgewood:
    name = "Bridgewood"
    classificacao = 4
    class Regular:
        weekday = 160
        weekend = 60
    class Reward:
        weekday = 110
        weekend = 50  

class Ridgewood:
    name = "Ridgewood"
    classificacao = 5
    class Regular:
        weekday = 220
        weekend = 150
    class Reward:
        weekday = 100
        weekend = 40   
    

def separar(texto):
     return [ s for s in re.split(r'[ :,().!]', texto) if s != ''and s != ' ' ]


def booking(information, hotel):
    #definir o hotel
    if (hotel == "Lakewood"): 
        hotel = Lakewood()
    elif (hotel == "Bridgewood"):
        hotel = Bridgewood()
    elif (hotel == "Ridgewood"):
        hotel = Ridgewood()

    final_semana = ("sat", "sun")
    cost = 0
    information = separar(information)    

    if (information[0] == "Regular"):  # se for um cliente regular 
        del(information[0])
        for x in range(3):
            if (information[(2*x)+1] in final_semana): #se for um final de semana
                cost = cost + hotel.Regular.weekend
            else:
                cost = cost + hotel.Regular.weekday

    elif (information[0] == "Rewards"):  # se for um cliente reward
        del(information[0])
        for x in range(3):
            if (information[(2*x)+1] in final_semana): #se for um final de semana
                cost = cost + hotel.Reward.weekend
            else:                        #se for dia de semana
                cost = cost + hotel.Reward.weekday           
    return cost


def get_cheapest_hotel(information):   #DO NOT change the function's name
    orcamento1 = booking(information, "Lakewood")
    orcamento2 = booking(information, "Bridgewood")
    orcamento3 = booking(information, "Ridgewood")
    lista = (orcamento1, orcamento2, orcamento3)
    lista= list(lista) #lista com os orçamentos dos hoteis
    menor = min(lista)
    index = lista.index(menor)
    cheapest_hotel = lista.pop(index) #menor valor
    if (menor in lista): #caso tenha valores iguais
        index = lista.index(menor)
        auxiliar = lista[index]
        #definir o hoteis
        #opção1
        if (cheapest_hotel ==  orcamento1): 
            cheapest_hotel_class = Lakewood()
            if (auxiliar == orcamento2):
                auxiliar_class = Bridgewood()
            elif ( auxiliar == orcamento3):
                 auxiliar_class = Ridgewood()
        #opção2
        elif (cheapest_hotel == orcamento2):
            cheapest_hotel_class = Bridgewood()
            if (auxiliar ==  orcamento1):
                auxiliar_class = Lakewood()
            elif ( auxiliar == orcamento3):
                 auxiliar_class = Ridgewood()
        #opção3
        elif (cheapest_hotel == orcamento3):
            cheapest_hotel_class = Ridgewood()
            if (auxiliar ==  orcamento1):
                auxiliar_class = Lakewood()
            elif ( auxiliar == orcamento2):
                auxiliar_class = Bridgewood()
           
        classficacoes = (cheapest_hotel_class.classificacao, auxiliar_class.classificacao)
        melhor = max(classficacoes)
        index = classficacoes.index(melhor)
        hoteis = (cheapest_hotel_class, auxiliar_class)
        cheapest_hotel = hoteis[index].name

        return cheapest_hotel

    else: #se não tiver valores iguais
        if (cheapest_hotel ==  orcamento1):
            cheapest_hotel_class = Lakewood()
        elif (cheapest_hotel == orcamento2):
            cheapest_hotel_class = Bridgewood()
        elif (cheapest_hotel == orcamento3):
            cheapest_hotel_class = Ridgewood()
        cheapest_hotel = cheapest_hotel_class.name
        return cheapest_hotel




while (True):
    pergunta = input("Digite seu programa de fidelidade e as datas de hospedagem: ")
    if (pergunta != "exit"):
        print(get_cheapest_hotel(pergunta))
        pergunta
        print("Digite 'exit' para sair")
    else:
        break