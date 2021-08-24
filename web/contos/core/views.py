from django.shortcuts import render
import random

LIST_WELCOME = [
    'Procurando princesas',
    'Convocando os soldados do reino',
    'Verificando fadas disponíveis',
    'Buscando reforços de peso',
    'Resgatando animais perdidos',
    'Construindo a casa da vovó',
    'Devolvendo os doces da cesta',
    'Acordando o lobo',
    'Limpando os quartos das crianças',
    'Pesquisando nomes de personagens',
    'Onde estão os porquinhos?',
    'Devolvendo a roupa do rei',
    'Soldados a postos',
    'Procurando anões',
    'Despertando todos os dragões',
    'Regando as plantas da floresta',
    'Plantando as últimas maçãs',
    'Encontrando as bruxas' 
]


def generate_text():
    text = ''''''
    return text


def home(request):
    conto_gerado = False
    welcomes = []
    if request.method == 'POST':
        conto_gerado = True
        welcomes = random.sample(LIST_WELCOME, 5)
        generated_text= generate_text()
    return render(request, 'index.html',{'conto_gerado':conto_gerado, 'welcomes':welcomes, 'generated_text': generated_text})