from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# Página inicial
@app.route('/')
def menu():
    return render_template('menu.html')

@app.route('/pergunta1', methods=['GET', 'POST'])
def pergunta1():
    if request.method == 'POST':
        resposta1 = request.form.get('resposta1', 0)
        return redirect(f'/pergunta2?resposta1={resposta1}')
    return render_template('pergunta1.html')

# Função para a pergunta 2
@app.route('/pergunta2', methods=['GET', 'POST'])
def pergunta2():
    resposta1 = request.args.get('resposta1', 0)
    if request.method == 'POST':
        resposta2 = request.form.get('resposta2', 0)
        return redirect(f'/pergunta3?resposta1={resposta1}&resposta2={resposta2}')
    return render_template('pergunta2.html')

# Função para a pergunta 3
@app.route('/pergunta3', methods=['GET', 'POST'])
def pergunta3():
    resposta1 = request.args.get('resposta1', 0)
    resposta2 = request.args.get('resposta2', 0)
    if request.method == 'POST':
        resposta3 = request.form.get('resposta3', 0)
        return redirect(f'/pergunta4?resposta1={resposta1}&resposta2={resposta2}&resposta3={resposta3}')
    return render_template('pergunta3.html')

# Função para a pergunta 4
@app.route('/pergunta4', methods=['GET', 'POST'])
def pergunta4():
    resposta1 = request.args.get('resposta1', 0)
    resposta2 = request.args.get('resposta2', 0)
    resposta3 = request.args.get('resposta3', 0)
    if request.method == 'POST':
        resposta4 = request.form.get('resposta4', 0)
        return redirect(f'/pergunta5?resposta1={resposta1}&resposta2={resposta2}&resposta3={resposta3}&resposta4={resposta4}')
    return render_template('pergunta4.html')

# Função para a pergunta 5
@app.route('/pergunta5', methods=['GET', 'POST'])
def pergunta5():
    resposta1 = request.args.get('resposta1', 0)
    resposta2 = request.args.get('resposta2', 0)
    resposta3 = request.args.get('resposta3', 0)
    resposta4 = request.args.get('resposta4', 0)
    if request.method == 'POST':
        resposta5 = request.form.get('resposta5', 0)
        return redirect(f'/pergunta6?resposta1={resposta1}&resposta2={resposta2}&resposta3={resposta3}&resposta4={resposta4}&resposta5={resposta5}')
    return render_template('pergunta5.html')

# Função para a pergunta 6
@app.route('/pergunta6', methods=['GET', 'POST'])
def pergunta6():
    resposta1 = request.args.get('resposta1', 0)
    resposta2 = request.args.get('resposta2', 0)
    resposta3 = request.args.get('resposta3', 0)
    resposta4 = request.args.get('resposta4', 0)
    resposta5 = request.args.get('resposta5', 0)
    if request.method == 'POST':
        resposta6 = request.form.get('resposta6', 0)
        return redirect(f'/pergunta7?resposta1={resposta1}&resposta2={resposta2}&resposta3={resposta3}&resposta4={resposta4}&resposta5={resposta5}&resposta6={resposta6}')
    return render_template('pergunta6.html')

# Função para a pergunta 7
@app.route('/pergunta7', methods=['GET', 'POST'])
def pergunta7():
    resposta1 = request.args.get('resposta1', 0)
    resposta2 = request.args.get('resposta2', 0)
    resposta3 = request.args.get('resposta3', 0)
    resposta4 = request.args.get('resposta4', 0)
    resposta5 = request.args.get('resposta5', 0)
    resposta6 = request.args.get('resposta6', 0)
    if request.method == 'POST':
        resposta7 = request.form.get('resposta7', 0)
        return redirect(f'/pergunta8?resposta1={resposta1}&resposta2={resposta2}&resposta3={resposta3}&resposta4={resposta4}&resposta5={resposta5}&resposta6={resposta6}&resposta7={resposta7}')
    return render_template('pergunta7.html')

# Função para a pergunta 8
@app.route('/pergunta8', methods=['GET', 'POST'])
def pergunta8():
    resposta1 = request.args.get('resposta1', 0)
    resposta2 = request.args.get('resposta2', 0)
    resposta3 = request.args.get('resposta3', 0)
    resposta4 = request.args.get('resposta4', 0)
    resposta5 = request.args.get('resposta5', 0)
    resposta6 = request.args.get('resposta6', 0)
    resposta7 = request.args.get('resposta7', 0)
    if request.method == 'POST':
        resposta8 = request.form.get('resposta8', 0)
        return redirect(f'/pergunta9?resposta1={resposta1}&resposta2={resposta2}&resposta3={resposta3}&resposta4={resposta4}&resposta5={resposta5}&resposta6={resposta6}&resposta7={resposta7}&resposta8={resposta8}')
    return render_template('pergunta8.html')

# Função para a pergunta 9
@app.route('/pergunta9', methods=['GET', 'POST'])
def pergunta9():
    resposta1 = request.args.get('resposta1', 0)
    resposta2 = request.args.get('resposta2', 0)
    resposta3 = request.args.get('resposta3', 0)
    resposta4 = request.args.get('resposta4', 0)
    resposta5 = request.args.get('resposta5', 0)
    resposta6 = request.args.get('resposta6', 0)
    resposta7 = request.args.get('resposta7', 0)
    resposta8 = request.args.get('resposta8', 0)
    if request.method == 'POST':
        resposta9 = request.form.get('resposta9', 0)
        return redirect(f'/pergunta10?resposta1={resposta1}&resposta2={resposta2}&resposta3={resposta3}&resposta4={resposta4}&resposta5={resposta5}&resposta6={resposta6}&resposta7={resposta7}&resposta8={resposta8}&resposta9={resposta9}')
    return render_template('pergunta9.html')

# Função para a pergunta 10
@app.route('/pergunta10', methods=['GET', 'POST'])
def pergunta10():
    resposta1 = request.args.get('resposta1', 0)
    resposta2 = request.args.get('resposta2', 0)
    resposta3 = request.args.get('resposta3', 0)
    resposta4 = request.args.get('resposta4', 0)
    resposta5 = request.args.get('resposta5', 0)
    resposta6 = request.args.get('resposta6', 0)
    resposta7 = request.args.get('resposta7', 0)
    resposta8 = request.args.get('resposta8', 0)
    resposta9 = request.args.get('resposta9', 0)
    if request.method == 'POST':
        resposta10 = request.form.get('resposta10', 0)
        return redirect(f'/resultado?resposta1={resposta1}&resposta2={resposta2}&resposta3={resposta3}&resposta4={resposta4}&resposta5={resposta5}&resposta6={resposta6}&resposta7={resposta7}&resposta8={resposta8}&resposta9={resposta9}&resposta10={resposta10}')
    return render_template('pergunta10.html')

@app.route('/resultado', methods=['GET'])
def resultado():
    respostas = {
        'resposta1': request.args.get('resposta1', 0),
        'resposta2': request.args.get('resposta2', 0),
        'resposta3': request.args.get('resposta3', 0),
        'resposta4': request.args.get('resposta4', 0),
        'resposta5': request.args.get('resposta5', 0),
        'resposta6': request.args.get('resposta6', 0),
        'resposta7': request.args.get('resposta7', 0),
        'resposta8': request.args.get('resposta8', 0),
        'resposta9': request.args.get('resposta9', 0),
        'resposta10': request.args.get('resposta10', 0)
    }
    respostas = {key: int(value) if value.isdigit() else 0 for key, value in respostas.items()}

    print("Respostas convertidas:", respostas)

# Cursos
    cursos = {
    'Administração': {
    'respostas': {
        'resposta1': 1,
        'resposta2': 1,
        'resposta3': 1,
        'resposta4': 2,
        'resposta5': 3,
        'resposta6': 2,
        'resposta7': 3,
        'resposta8': 1,
        'resposta9': 1,
        'resposta10': 1
    },
    'link': 'https://seja.univille.br/curso/presencial/administracao',
    'resumo': 'O curso de Administração capacita profissionais para gerenciar negócios e liderar equipes em diversos setores.'
},
'Análise e Desenvolvimento de Sistemas': {
    'respostas': {
        'resposta1': 2,
        'resposta2': 1,
        'resposta3': 2,
        'resposta4': 3,
        'resposta5': 2,
        'resposta6': 2,
        'resposta7': 2,
        'resposta8': 1,
        'resposta9': 1,
        'resposta10': 1
    },
    'link': 'https://seja.univille.br/curso/presencial/analise-e-desenvolvimento-de-sistemas',
    'resumo': 'Forma profissionais capazes de desenvolver sistemas e soluções tecnológicas.'
},
'Arquitetura e Urbanismo': {
    'respostas': {
        'resposta1': 2,
        'resposta2': 4,
        'resposta3': 4,
        'resposta4': 3,
        'resposta5': 1,
        'resposta6': 1,
        'resposta7': 4,
        'resposta8': 2,
        'resposta9': 3,
        'resposta10': 1
    },
    'link': 'https://seja.univille.br/curso/presencial/arquitetura-e-urbanismo',
    'resumo': 'O curso de Arquitetura capacita profissionais para o planejamento urbano e design.'
},
'Artes Visuais': {
    'respostas': {
        'resposta1': 1,
        'resposta2': 2,
        'resposta3': 4,
        'resposta4': 2,
        'resposta5': 1,
        'resposta6': 1,
        'resposta7': 3,
        'resposta8': 2,
        'resposta9': 2,
        'resposta10': 1
    },
    'link': 'https://seja.univille.br/curso/ead/artes-visuais',
    'resumo': 'Capacita profissionais a desenvolver habilidades criativas em diversas expressões artísticas.'
},
'Biomedicina': {
    'respostas': {
        'resposta1': 3,
        'resposta2': 3,
        'resposta3': 2,
        'resposta4': 1,
        'resposta5': 1,
        'resposta6': 3,
        'resposta7': 2,
        'resposta8': 1,
        'resposta9': 1,
        'resposta10': 1
    },
    'link': 'https://seja.univille.br/curso/presencial/biomedicina',
    'resumo': 'Foca no diagnóstico laboratorial e pesquisa científica na área de saúde.'
},
'Ciências Contábeis': {
    'respostas': {
        'resposta1': 1,
        'resposta2': 1,
        'resposta3': 1,
        'resposta4': 2,
        'resposta5': 2,
        'resposta6': 2,
        'resposta7': 3,
        'resposta8': 1,
        'resposta9': 1,
        'resposta10': 1
    },
    'link': 'https://seja.univille.br/curso/presencial/ciencias-contabeis',
    'resumo': 'Forma profissionais para atuar na gestão financeira de empresas e organizações.'
},
'Ciências Econômicas': {
    'respostas': {
        'resposta1': 1,
        'resposta2': 1,
        'resposta3': 2,
        'resposta4': 3,
        'resposta5': 2,
        'resposta6': 2,
        'resposta7': 2,
        'resposta8': 1,
        'resposta9': 1,
        'resposta10': 1
    },
    'link': 'https://seja.univille.br/curso/presencial/ciencias-economicas',
    'resumo': 'Capacita profissionais para a análise econômica e desenvolvimento de estratégias financeiras.'
},
'Direito': {
    'respostas': {
        'resposta1': 1,
        'resposta2': 1,
        'resposta3': 1,
        'resposta4': 2,
        'resposta5': 2,
        'resposta6': 2,
        'resposta7': 1,
        'resposta8': 3,
        'resposta9': 1,
        'resposta10': 1
    },
    'link': 'https://seja.univille.br/curso/presencial/direito',
    'resumo': 'Forma profissionais para atuar na área jurídica em diversos ramos do direito.'
},
'Engenharia Civil': {
    'respostas': {
        'resposta1': 2,
        'resposta2': 3,
        'resposta3': 2,
        'resposta4': 3,
        'resposta5': 1,
        'resposta6': 1,
        'resposta7': 2,
        'resposta8': 1,
        'resposta9': 1,
        'resposta10': 1
    },
    'link': 'https://seja.univille.br/curso/presencial/engenharia-civil',
    'resumo': 'Forma engenheiros para atuar em projetos de construção civil e infraestrutura.'
},
'Enfermagem': {
    'respostas': {
        'resposta1': 3,
        'resposta2': 3,
        'resposta3': 1,
        'resposta4': 1,
        'resposta5': 1,
        'resposta6': 2,
        'resposta7': 2,
        'resposta8': 1,
        'resposta9': 1,
        'resposta10': 1
    },
    'link': 'https://seja.univille.br/curso/presencial/enfermagem',
    'resumo': 'Prepara profissionais para atuar no cuidado com a saúde em diversas áreas.'
},
'Engenharia de Software': {
    'respostas': {
        'resposta1': 2,
        'resposta2': 1,
        'resposta3': 2,
        'resposta4': 3,
        'resposta5': 2,
        'resposta6': 2,
        'resposta7': 2,
        'resposta8': 1,
        'resposta9': 1,
        'resposta10': 1
    },
    'link': 'https://seja.univille.br/curso/presencial/engenharia-de-software',
    'resumo': 'Forma profissionais para o desenvolvimento de softwares e sistemas.'
},
'Farmácia': {
    'respostas': {
        'resposta1': 3,
        'resposta2': 3,
        'resposta3': 2,
        'resposta4': 1,
        'resposta5': 1,
        'resposta6': 2,
        'resposta7': 2,
        'resposta8': 1,
        'resposta9': 1,
        'resposta10': 1
    },
    'link': 'https://seja.univille.br/curso/presencial/farmacia',
    'resumo': 'Capacita profissionais para atuar em análises clínicas e na manipulação de medicamentos.'
},
'Nutrição': {
    'respostas': {
        'resposta1': 3,
        'resposta2': 3,
        'resposta3': 1,
        'resposta4': 1,
        'resposta5': 1,
        'resposta6': 2,
        'resposta7': 2,
        'resposta8': 1,
        'resposta9': 1,
        'resposta10': 1
    },
    'link': 'https://seja.univille.br/curso/presencial/nutricao',
    'resumo': 'Forma profissionais para atuar na promoção da saúde por meio da alimentação.'
},
'Fotografia': {
    'respostas': {
        'resposta1': 1,
        'resposta2': 2,
        'resposta3': 4,
        'resposta4': 2,
        'resposta5': 1,
        'resposta6': 2,
        'resposta7': 3,
        'resposta8': 2,
        'resposta9': 2,
        'resposta10': 1
    },
    'link': 'https://seja.univille.br/curso/presencial/fotografia',
    'resumo': 'Prepara profissionais para atuar na área da fotografia artística e comercial.'
},
'Gastronomia': {
    'respostas': {
        'resposta1': 3,
        'resposta2': 1,
        'resposta3': 4,
        'resposta4': 2,
        'resposta5': 1,
        'resposta6': 1,
        'resposta7': 3,
        'resposta8': 1,
        'resposta9': 1,
        'resposta10': 1
    },
    'link': 'https://seja.univille.br/curso/ead/gastronomia',
    'resumo': 'Forma profissionais para atuar na cozinha, com foco em técnicas culinárias e gestão gastronômica.'
},
'História': {
    'respostas': {
        'resposta1': 1,
        'resposta2': 1,
        'resposta3': 1,
        'resposta4': 2,
        'resposta5': 2,
        'resposta6': 2,
        'resposta7': 1,
        'resposta8': 1,
        'resposta9': 1,
        'resposta10': 1
    },
    'link': 'https://seja.univille.br/curso/ead/historia',
    'resumo': 'Capacita profissionais para ensinar e pesquisar o desenvolvimento humano e social.'
},
'Letras': {
    'respostas': {
        'resposta1': 1,
        'resposta2': 1,
        'resposta3': 1,
        'resposta4': 2,
        'resposta5': 2,
        'resposta6': 2,
        'resposta7': 1,
        'resposta8': 1,
        'resposta9': 1,
        'resposta10': 1
    },
    'link': 'https://seja.univille.br/curso/presencial/letras',
    'resumo': 'Prepara profissionais para atuar no ensino e pesquisa de línguas e literatura.'
},
'Marketing': {
    'respostas': {
        'resposta1': 1,
        'resposta2': 1,
        'resposta3': 1,
        'resposta4': 3,
        'resposta5': 2,
        'resposta6': 2,
        'resposta7': 1,
        'resposta8': 1,
        'resposta9': 1,
        'resposta10': 1
    },
    'link': 'https://seja.univille.br/curso/presencial/marketing',
    'resumo': 'Capacita profissionais para planejar e executar estratégias de marketing e comunicação.'
},
'Medicina': {
    'respostas': {
        'resposta1': 3,
        'resposta2': 3,
        'resposta3': 1,
        'resposta4': 1,
        'resposta5': 1,
        'resposta6': 2,
        'resposta7': 2,
        'resposta8': 1,
        'resposta9': 1,
        'resposta10': 1
    },
    'link': 'https://seja.univille.br/curso/presencial/medicina',
    'resumo': 'Forma médicos capacitados para atuar no diagnóstico, tratamento e prevenção de doenças.'
},
'Pedagogia': {
    'respostas': {
        'resposta1': 1,
        'resposta2': 1,
        'resposta3': 1,
        'resposta4': 2,
        'resposta5': 2,
        'resposta6': 2,
        'resposta7': 1,
        'resposta8': 1,
        'resposta9': 1,
        'resposta10': 1
    },
    'link': 'https://seja.univille.br/curso/presencial/pedagogia',
    'resumo': 'Forma profissionais para atuar no ensino infantil e na gestão educacional.'
},
'Publicidade e Propaganda': {
    'respostas': {
        'resposta1': 1,
        'resposta2': 1,
        'resposta3': 1,
        'resposta4': 3,
        'resposta5': 2,
        'resposta6': 2,
        'resposta7': 1,
        'resposta8': 1,
        'resposta9': 1,
        'resposta10': 1
    },
    'link': 'https://seja.univille.br/curso/presencial/publicidade-e-propaganda',
    'resumo': 'Capacita profissionais para desenvolver campanhas publicitárias e estratégias de comunicação.'
},
'Ciência de Dados': {
    'respostas': {
        'resposta1': 2,
        'resposta2': 1,
        'resposta3': 2,
        'resposta4': 3,
        'resposta5': 3,
        'resposta6': 2,
        'resposta7': 2,
        'resposta8': 1,
        'resposta9': 1,
        'resposta10': 1
    },
    'link': 'https://seja.univille.br/curso/presencial/ciencia-de-dados',
    'resumo': 'Forma profissionais para analisar grandes volumes de dados e extrair insights para a tomada de decisões.'
},
'Ciências Biológicas': {
    'respostas': {
        'resposta1': 3,
        'resposta2': 3,
        'resposta3': 3,
        'resposta4': 1,
        'resposta5': 1,
        'resposta6': 3,
        'resposta7': 2,
        'resposta8': 2,
        'resposta9': 1,
        'resposta10': 1
    },
    'link': 'https://seja.univille.br/curso/presencial/ciencias-biologicas',
    'resumo': 'Prepara profissionais para atuar na pesquisa e conservação da biodiversidade.'
},
'Comércio Exterior': {
    'respostas': {
        'resposta1': 1,
        'resposta2': 1,
        'resposta3': 1,
        'resposta4': 3,
        'resposta5': 2,
        'resposta6': 2,
        'resposta7': 2,
        'resposta8': 1,
        'resposta9': 1,
        'resposta10': 1
    },
    'link': 'https://seja.univille.br/curso/ead/comercio-exterior',
    'resumo': 'Capacita profissionais para atuar com negociações internacionais e comércio global.'
},
'Engenharia Ambiental e Sanitária': {
    'respostas': {
        'resposta1': 2,
        'resposta2': 3,
        'resposta3': 2,
        'resposta4': 3,
        'resposta5': 1,
        'resposta6': 3,
        'resposta7': 2,
        'resposta8': 2,
        'resposta9': 1,
        'resposta10': 1
    },
    'link': 'https://seja.univille.br/curso/presencial/engenharia-ambiental-e-sanitaria',
    'resumo': 'Prepara engenheiros para trabalhar com soluções sustentáveis e preservação ambiental.'
},
'Sistemas de Informação': {
    'respostas': {
        'resposta1': 2,
        'resposta2': 1,
        'resposta3': 2,
        'resposta4': 3,
        'resposta5': 2,
        'resposta6': 2,
        'resposta7': 2,
        'resposta8': 1,
        'resposta9': 1,
        'resposta10': 1
    },
    'link': 'https://seja.univille.br/curso/ead/sistemas-de-informacao',
    'resumo': 'Forma profissionais para desenvolver e gerenciar sistemas de informação em diferentes setores.'
    }
}
    
    respostas = {key: int(value) if value else 0 for key, value in respostas.items()}
    print("Respostas convertidas:", respostas)

    pontuacao_cursos = {}
    for curso, dados in cursos.items():
        pontuacao = 0
        for chave, opcoes in dados['respostas'].items():
            if respostas.get(chave) == opcoes:
                pontuacao += 1
        pontuacao_cursos[curso] = pontuacao

    top_cursos = sorted(pontuacao_cursos.items(), key=lambda x: x[1], reverse=True)[:3]

    return render_template('resultado.html', respostas=respostas, cursos=top_cursos, detalhes=cursos)

if __name__ == '__main__':
    app.run(debug=True)