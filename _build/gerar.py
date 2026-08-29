# -*- coding: utf-8 -*-
"""Gerador do site de treinamento.

O conteúdo mora em _build/conteudo/<slug>.html, em fragmentos. Este script
monta a casca em volta, inlineia o CSS e grava a página.

🔴 Editar o index.html gerado é trabalho perdido: a próxima execução apaga.

Rodar:  python3 _build/gerar.py
"""
import io
import os
import re

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.dirname(AQUI)


# ---------------------------------------------------------------------------
# O CURSO
#
# Trocar de cliente é mexer aqui e no marca.css. Mais nada.
# ---------------------------------------------------------------------------
CURSO = {
    "nome":  "Imersão em IA com Claude",
    "sigla": "IC",
    "sub":   "Treinamento in-company · Rafael Lima",
    # A valvula do G2: o curso DECLARA o que ensina, e o gate para de acusar
    # so esses termos. Aqui o Claude Code e o Modulo 3 da ementa vendida.
    "ensina": ["claude code"],
}

# 🔴 Existe porque toda pagina precisa terminar com um lugar para ir. Ate
# 26/08 nenhuma das seis terminava: a classe .rodape-nav estava no base.css
# desde o inicio e ZERO paginas usavam. O curso do IEL herdou isso, e a
# pagina de modulo dele acabava no meio de uma secao, sem nada embaixo. Foi
# a primeira coisa que o Rafael apontou: "nao tem um toco, um botao tipo
# voltar pra capa".
#
# Isto e maior que a TRILHA de proposito: a trilha e a barra lateral e so
# lista aula; o rodape existe em pagina que a barra nem mostra (a capa, o
# modulo). Sao duas perguntas diferentes -- "onde eu estou no curso" e
# "para onde eu vou agora".
# 🔴 ACHADO 27/08: esta lista estava agrupada por TIPO (as aulas, depois os
# casos), e o rodape responde "para onde eu vou agora". O resultado e que a
# ultima aula do nivelamento levava para a demonstracao da PRIMEIRA aula, em
# vez de levar para o Modulo 1.
# A sequencia e a JORNADA, e a jornada nao passa pelas paginas de caso: elas
# sao um desvio de dentro da aula, e voltam pela migalha. Fora daqui, o
# rodape delas fica vazio de proposito, que e o que a propria funcao ja faz
# com quem nao esta na lista.
SEQUENCIA = ["index", "nivelamento",
             "n1-dois-modos", "n2-generica", "n3-conferir", "n4-limite",
             "n5-configurar",
             "m1", "m1a1-superficies", "m1a2-mesa", "m1a3-instrucao",
             "m1a4-regra", "m1a5-mapa", "m1a6-tranca", "m1a7-base",
             "m1a8-conta"]

# ---------------------------------------------------------------------------
# A TRILHA · o indice do curso, e a unica lista escrita a mao neste arquivo
# ---------------------------------------------------------------------------
# Por que a mao: a ordem das aulas e decisao de produto do Rafael, nao coisa
# que se deduza da pasta.
#
# Encontro NAO e modulo. A trilha segue o MODULO, que e o contrato da ementa;
# o calendario dos 4 encontros mora na capa.
# 🔴 VAZIA POR DECISAO, 27/08. A barra lateral ocupa 288px fixos da direita,
# e com ela a coluna de leitura para em 780. A figura de dirigir/produzir/
# conferir tem viewBox de 1160: a 780 ela renderiza a 0,67 e o rotulo de
# 12,5px vira 8,4px, ilegivel. Os tres cursos de referencia nao tem barra
# lateral em aula nenhuma, e e por isso que a figura grande respira la.
# A navegacao nao se perde: a migalha volta em um clique e o rodape leva
# para a proxima. Para trazer a barra de volta, basta repovoar esta lista.
TRILHA = [
    # 🔴 ISTO NAO DESENHA MAIS BARRA NENHUMA, desde 28/08. A trilha lateral saiu
    # do padrao (a regra .com-trilha .solta zerava o breakout, e este curso usa
    # 183 breakouts em 193 figuras). O que sobrou da TRILHA e o unico papel que
    # ela sempre teve de verdade: DIZER A ORDEM DAS AULAS.
    # Os gates G42 e G44 leem daqui, e so daqui: sequencia nao se deduz de nome
    # de arquivo. Deixar esta lista vazia deixa os dois cegos, com zero achado.
    ("Nivelamento", [
        ("n1-dois-modos",    "Delegar a execução ou pensar junto"),
        ("n2-generica",      "Por que a resposta vem genérica"),
        ("n3-conferir",      "Conferir o que volta"),
        ("n4-limite",        "O que não entra no chat"),
        ("n5-configurar",    "A primeira configuração"),
    ]),
    ("Módulo 1", [
        ("m1a1-superficies", "Quatro superfícies, e a que a sua tarefa pede"),
        ("m1a2-mesa",        "A mesa tem tamanho fixo"),
        ("m1a3-instrucao",   "A instrução que fica, e as três gavetas"),
        ("m1a4-regra",       "A regra do 2×"),
        ("m1a5-mapa",        "O mapa: onde cada regra mora"),
        ("m1a6-tranca",      "A regra que não mora em texto nenhum"),
        ("m1a7-base",        "Por que a base multiplica"),
        ("m1a8-conta",       "A conta da repetição"),
    ]),
]

PAGINAS = {
    "index": dict(
        titulo="Imersão em IA com Claude",
        kicker="Treinamento in-company · IEL",
        h1="Do zero à produtividade total",
        sub="Dezesseis horas-aula, quatro quintas à noite. Você entra com uma rotina "
            "que consome a sua semana e sai com ela funcionando.",
        selos=["16 horas-aula", "4 encontros", "Claude Pro incluso"],
        migalha=None,
    ),
    "nivelamento": dict(
        titulo="Nivelamento",
        kicker="Encontro 1 de 4 · 27 de agosto",
        h1="Onde a IA entra no seu trabalho",
        sub="Cinco aulas para a turma inteira partir do mesmo lugar, sem repetir "
            "para quem já sabe e sem pular etapa para quem está começando.",
        selos=["5 aulas", "Sem instalação"],
        migalha=[("../", "Imersão em IA com Claude"), (None, "Nivelamento")],
    ),
    "n1-dois-modos": dict(
        tipo="pratica",
        titulo="Delegar a execução ou pensar junto",
        kicker="Nivelamento · Aula 1",
        h1="Delegar a execução ou pensar junto",
        sub="Os dois jeitos de usar o Claude no seu trabalho, e o que muda no pedido "
            "em cada um.",
        selos=["Nivelamento", "Traga uma tarefa sua"],
        migalha=[("../", "Imersão em IA com Claude"),
                 ("../nivelamento/", "Nivelamento"),
                 (None, "Delegar a execução ou pensar junto")],
    ),
    "n2-generica": dict(
        tipo="pratica",
        titulo="Por que a resposta vem genérica",
        kicker="Nivelamento · Aula 2",
        h1="Por que a resposta vem genérica",
        sub="Os seis campos que separam um pedido que volta útil de um que volta "
            "bonito e inútil.",
        selos=["Nivelamento", "Traga um pedido que deu errado"],
        migalha=[("../", "Imersão em IA com Claude"),
                 ("../nivelamento/", "Nivelamento"),
                 (None, "Por que a resposta vem genérica")],
    ),
    "caso-dois-modos": dict(
        titulo="O mesmo convênio, pedido de dois jeitos",
        kicker="Demonstração da aula 1 · em cinco passos",
        h1="Uma planilha, dois pedidos, duas respostas",
        sub="O fechamento do convênio do Instituto Farol pedido nos dois modos: "
            "primeiro o que amplia a decisão, depois o que executa ela.",
        selos=["Prestação de contas", "2.829 linhas", "Dois pedidos"],
        migalha=[("../", "Imersão em IA com Claude"),
                 ("../nivelamento/", "Nivelamento"),
                 (None, "O mesmo convênio, pedido de dois jeitos")],
    ),
    "caso": dict(
        titulo="A execução do convênio, conferida",
        kicker="Demonstração da aula 2 · em cinco passos",
        h1="Uma tarde de conferência, em cinco passos",
        sub="A planilha de execução do Instituto Farol, com a sujeira que uma "
            "exportação real tem, e o pedido que dá conta dela.",
        selos=["Prestação de contas", "2.829 linhas", "Planilha suja"],
        migalha=[("../", "Imersão em IA com Claude"),
                 ("../nivelamento/", "Nivelamento"),
                 (None, "A execução do convênio, conferida")],
    ),
    "n3-conferir": dict(
        tipo="pratica",
        titulo="Como saber se a resposta está certa",
        kicker="Nivelamento · aula 3 de 4",
        h1="Como saber se a resposta está certa",
        sub="A resposta errada tem a mesma cara da certa. Quatro camadas de "
            "conferência, e a instrução que transforma erro invisível em pendência.",
        selos=["Quatro camadas", "Promptlet de conferência"],
        migalha=[("../", "Imersão em IA com Claude"),
                 ("../nivelamento/", "Nivelamento"),
                 (None, "Como saber se a resposta está certa")],
    ),
    "n4-limite": dict(
        tipo="fundamento",
        titulo="O que não entra no chat",
        kicker="Nivelamento · aula 4 de 4",
        h1="O que não entra no chat",
        sub="Três caixas para classificar qualquer material, e o caminho que o "
            "arquivo faz quando você anexa.",
        selos=["Três caixas", "O caminho do dado"],
        migalha=[("../", "Imersão em IA com Claude"),
                 ("../nivelamento/", "Nivelamento"),
                 (None, "O que não entra no chat")],
    ),
    "caso-conferir": dict(
        titulo="A prestação conferida antes de assinar",
        kicker="Demonstração da aula 3 · em cinco passos",
        h1="Achar as sete pendências antes que o financiador ache",
        sub="A mesma planilha do convênio, agora como gabarito: sete problemas "
            "plantados, e a conferência que precisa pegar cinco sozinha.",
        selos=["Sete armadilhas", "Origem obrigatória"],
        migalha=[("../", "Imersão em IA com Claude"),
                 ("../nivelamento/", "Nivelamento"),
                 (None, "A prestação conferida antes de assinar")],
    ),
    "caso-limite": dict(
        titulo="O arquivo preparado antes de anexar",
        kicker="Demonstração da aula 4 · em cinco passos",
        h1="Dois minutos que movem o arquivo de caixa",
        sub="A triagem coluna a coluna da planilha do convênio, e o pedido que "
            "impede a resposta de reconstruir o que foi anonimizado.",
        selos=["Triagem por coluna", "Dados fictícios"],
        migalha=[("../", "Imersão em IA com Claude"),
                 ("../nivelamento/", "Nivelamento"),
                 (None, "O arquivo preparado antes de anexar")],
    ),
    "n5-configurar": dict(
        tipo="pratica",
        titulo="A primeira configuração",
        kicker="Nivelamento · aula 5 de 5",
        h1="A primeira configuração",
        sub="O que se repete em todo pedido seu sai do teclado e vira perfil da "
            "conta. Seis blocos, escritos uma vez.",
        selos=["Seis blocos", "Sai funcionando"],
        migalha=[("../", "Imersão em IA com Claude"),
                 ("../nivelamento/", "Nivelamento"),
                 (None, "A primeira configuração")],
    ),
    "caso-configurar": dict(
        titulo="O perfil escrito e testado",
        kicker="Demonstração da aula 5 · em cinco passos",
        h1="Quinze minutos que encurtam todo pedido seu",
        sub="Onde fica o campo, o que escrever em cada um dos seis blocos, e o "
            "teste de doze palavras que prova se ele está sendo lido.",
        selos=["Seis blocos", "Teste de 12 palavras"],
        migalha=[("../", "Imersão em IA com Claude"),
                 ("../nivelamento/", "Nivelamento"),
                 (None, "O perfil escrito e testado")],
    ),
    "m1": dict(
        titulo="Módulo 1",
        kicker="Encontro 2 de 4 · 3 de setembro",
        h1="A regra sai do teclado",
        sub="O método do nivelamento vira base escrita: o que você repetia em todo "
            "pedido passa a morar onde a ferramenta lê sozinha.",
        selos=["4 aulas", "Claude Desktop"],
        migalha=[("../", "Imersão em IA com Claude"),
                 (None, "Módulo 1")],
    ),
    "m1a1-superficies": dict(
        tipo="fundamento",
        titulo="Quatro superfícies, e a que a sua tarefa pede",
        kicker="Módulo 1 · aula 1.1",
        h1="Quatro superfícies, e a que a sua tarefa pede",
        sub="Onde cada tarefa sua mora, decidido em quatro perguntas, sem subir de "
            "superfície por status.",
        selos=["Quatro perguntas", "Pare no primeiro sim"],
        migalha=[("../", "Imersão em IA com Claude"),
                 ("../m1/", "Módulo 1"),
                 (None, "Quatro superfícies, e a que a sua tarefa pede")],
    ),
    "m1a2-mesa": dict(
        tipo="fundamento",
        titulo="A mesa tem tamanho fixo",
        kicker="Módulo 1 · aula 1.2",
        h1="A mesa tem tamanho fixo",
        sub="Por que a conversa longa piora sem ninguém mexer em nada, como medir "
            "isso em trinta segundos, e o que levar quando for recomeçar.",
        selos=["O teste da mesa", "Três linhas que sobrevivem"],
        migalha=[("../", "Imersão em IA com Claude"),
                 ("../m1/", "Módulo 1"),
                 (None, "A mesa tem tamanho fixo")],
    ),
    "m1a3-instrucao": dict(
        tipo="pratica",
        titulo="A instrução que fica, e as três gavetas",
        kicker="Módulo 1 · aula 1.3",
        h1="A instrução que fica, e as três gavetas",
        sub="O texto que ele lê no começo de toda conversa daquele trabalho, e os três "
            "lugares de um projeto que ninguém deve trocar entre si.",
        selos=["Instrução persistente", "Três gavetas"],
        migalha=[("../", "Imersão em IA com Claude"),
                 ("../m1/", "Módulo 1"),
                 (None, "A instrução que fica, e as três gavetas")],
    ),
    "m1a4-regra": dict(
        tipo="fundamento",
        titulo="A regra do 2×",
        kicker="Módulo 1 · aula 1.4",
        h1="A regra do 2×",
        sub="O critério que decide o que vira texto fixo, e o teste contra um trabalho "
            "que você já entregou.",
        selos=["Corrigiu duas vezes", "Teste com trabalho fechado"],
        migalha=[("../", "Imersão em IA com Claude"),
                 ("../m1/", "Módulo 1"),
                 (None, "A regra do 2×")],
    ),
    "caso-superficies": dict(
        titulo="O projeto do relatório de execução",
        kicker="Demonstração da aula 1.1 · em cinco passos",
        h1="Montar o projeto, e rodar o fechamento dentro dele",
        sub="O papel do agente pronto para colar, a planilha que sai suja do sistema, "
            "e o pedido de uma frase que substitui o contexto de toda semana.",
        selos=["Papel pronto", "15 minutos"],
        migalha=[("../", "Imersão em IA com Claude"),
                 ("../m1/", "Módulo 1"),
                 (None, "O projeto do relatório de execução")],
    ),
    "caso-regra": dict(
        titulo="O projeto montado, gaveta por gaveta",
        kicker="Demonstração da aula 1.3 · em cinco passos",
        h1="Vinte minutos que a tarefa devolve toda semana",
        sub="O que vai em cada uma das três gavetas, o texto das instruções em "
            "quatro trechos, e o sinal de cada trecho na resposta.",
        selos=["Três gavetas", "Quatro trechos"],
        migalha=[("../", "Imersão em IA com Claude"),
                 ("../m1/", "Módulo 1"),
                 (None, "O projeto montado, gaveta por gaveta")],
    ),
    "m1a5-mapa": dict(
        tipo="pratica",
        titulo="O mapa: onde cada regra mora",
        kicker="Módulo 1 · aula 1.5",
        h1="O mapa: onde cada regra mora",
        sub="Uma pergunta escolhe o lugar de qualquer regra sua, e os cinco nomes que "
            "aparecem na tela: instruções, skill, comando, conector e plugin.",
        selos=["Sempre, às vezes, nunca", "Cinco lugares"],
        migalha=[("../", "Imersão em IA com Claude"),
                 ("../m1/", "Módulo 1"),
                 (None, "O mapa: onde cada regra mora")],
    ),
    "m1a6-tranca": dict(
        tipo="fundamento",
        titulo="A regra que não mora em texto nenhum",
        kicker="Módulo 1 · aula 1.6",
        h1="A regra que não mora em texto nenhum",
        sub="A pergunta que separa regra comum de regra crítica, e por que escrever em "
            "caixa alta não muda o mecanismo.",
        selos=["Uma vez em cem", "A tranca"],
        migalha=[("../", "Imersão em IA com Claude"),
                 ("../m1/", "Módulo 1"),
                 (None, "A regra que não mora em texto nenhum")],
    ),
    "m1a7-base": dict(
        tipo="pratica",
        titulo="Por que a base multiplica",
        kicker="Módulo 1 · aula 1.7",
        h1="Por que a base multiplica",
        sub="O teto do pedido bem escrito, e a medida do que a base já tirou do seu "
            "teclado.",
        selos=["O teto do pedido", "Dois pedidos lado a lado"],
        migalha=[("../", "Imersão em IA com Claude"),
                 ("../m1/", "Módulo 1"),
                 (None, "Por que a base multiplica")],
    ),
    "m1a8-conta": dict(
        tipo="fundamento",
        titulo="A conta da repetição",
        kicker="Módulo 1 · aula 1.8",
        h1="A conta da repetição",
        sub="A partir de quantas voltas montar a base se paga, e por que a tarefa mais "
            "importante quase nunca é a escolhida.",
        selos=["Repetição, não importância", "Duas de fora"],
        migalha=[("../", "Imersão em IA com Claude"),
                 ("../m1/", "Módulo 1"),
                 (None, "A conta da repetição")],
    ),
    "caso-mapa": dict(
        titulo="A norma da casa vira procedimento",
        kicker="Demonstração da aula 1.5 · em cinco passos",
        h1="Transformar o que já está escrito em algo que ele lê sozinho",
        sub="A pergunta única aplicada antes de tudo, e o pedido que transforma a "
            "norma da sua área sem misturar boa prática de fora.",
        selos=["Etiqueta e conteúdo", "Sem inventar norma"],
        migalha=[("../", "Imersão em IA com Claude"),
                 ("../m1/", "Módulo 1"),
                 (None, "A norma da casa vira procedimento")],
    ),
    "caso-base": dict(
        titulo="A medição que fecha o módulo",
        kicker="Demonstração das aulas 1.7 e 1.8 · em cinco passos",
        h1="Para onde foi cada informação do pedido antigo",
        sub="A conferência que mostra o que a base já cobre, o que se perdeu pelo "
            "caminho e o que está escrito duas vezes.",
        selos=["Quatro textos", "Três listas"],
        migalha=[("../", "Imersão em IA com Claude"),
                 ("../m1/", "Módulo 1"),
                 (None, "A medição que fecha o módulo")],
    ),
    "exemplo": dict(
        titulo="O exemplo pronto",
        kicker="O resultado do caso",
        h1="A prestação de contas, em uma página",
        sub="O documento inteiro, do jeito que ele sai. Imprime em A4 sem levar o "
            "site junto.",
        selos=["Resultado do caso", "Imprime em A4"],
        migalha=[("../", "Imersão em IA com Claude"),
                 ("../caso/", "A execução do convênio, conferida"),
                 (None, "O exemplo pronto")],
    ),
    "componentes": dict(
        titulo="As peças do padrão",
        kicker="Referência do padrão",
        h1="As peças, uma a uma",
        sub="Cada bloco desta página é um componente do padrão, com o nome que "
            "ele tem no HTML e a regra que faz ele funcionar.",
        selos=["Uso interno", "Não vai para a turma"],
        migalha=[("../", "Imersão em IA com Claude"), (None, "As peças do padrão")],
    ),
}


# ---------------------------------------------------------------------------
# QUEBRA DE LINHA · a cola de espaço rígido
#
# Resolve a linha que termina em "na sua" e joga "área." para baixo. Cola a
# palavra-função na palavra seguinte com espaço rígido, do jeito que uma
# gráfica faz: a quebra procura outro lugar e costuma achar a fronteira da
# frase.
#
# 🔴 Esta é a ÚNICA cura de quebra de linha do padrão. text-wrap:balance e
# text-wrap:pretty NÃO entram na prosa: eles reservam espaço no fim da linha e
# criam o defeito oposto, a frase que quebra do nada com meia linha vazia.
# Medido no Longevidade: 62 quebras assim com balance, 0 sem ele.
# ---------------------------------------------------------------------------
COLAM = {
    "a", "o", "as", "os", "um", "uma", "uns", "umas",
    "seu", "sua", "seus", "suas", "meu", "minha", "nosso", "nossa",
    "de", "da", "do", "das", "dos", "em", "na", "no", "nas", "nos",
    "por", "pelo", "pela", "com", "sem", "ao", "aos", "à", "às",
    "para", "pra", "num", "numa", "dum", "duma",
    "sobre", "entre", "durante", "até", "desde", "após", "contra",
    "sob", "perante", "conforme", "mediante",
    "e", "ou", "mas", "se", "que", "quando", "onde", "enquanto", "porque",
    "não", "já", "só",
}

# Nenhum trecho colado passa disso. Acima, a unidade indivisível fica maior que
# a linha do celular e vira rolagem lateral, que é o defeito que a cola deveria
# evitar. 24 foi calibrado medindo em 5 larguras.
LIMITE_GRUDADO = 24

# Parágrafo longo não leva cola: ninguém repara numa quebra ruim no meio de
# seis linhas, e colar lá tira do navegador a liberdade de achar a melhor linha.
LIMITE_PARAGRAFO = 400

BLOCO_QUE_COLA = re.compile(
    r'(<h[1-4]\b[^>]*>)(.*?)(</h[1-4]>)'
    r'|(<p\b[^>]*>)(.*?)(</p>)'
    r'|(<li\b[^>]*>)(.*?)(</li>)',
    re.S,
)
SEM_TAG = re.compile(r"<[^>]+>")
PECA = re.compile(r'(<[^>]+>|\s+|[^<\s]+)')

# Onde a cola não entra: o prompt é copiado literalmente pelo aluno, e um
# espaço rígido no meio dele quebra o que for colar em planilha ou terminal.
SEM_COLA = ("prompt-txt", "prompt", "tabela")


def _cola(interno):
    pecas = PECA.findall(interno)
    saida, grudado = [], 0
    for i, p in enumerate(pecas):
        if p and not p.strip():
            anterior = next((x for x in reversed(saida)
                             if x.strip() and not x.startswith("<")), "")
            palavra = re.sub(r"[^\wÀ-ÿ]", "", anterior, flags=re.U).lower()
            seguinte = next((pecas[j] for j in range(i + 1, len(pecas))
                             if pecas[j].strip() and not pecas[j].startswith("<")), "")
            if (palavra in COLAM and seguinte
                    and grudado + len(anterior) + len(seguinte) + 1 <= LIMITE_GRUDADO):
                grudado += len(anterior) + 1
                saida.append("&nbsp;")
                continue
            grudado = 0
        saida.append(p)
    return "".join(saida)


def cola_quebra_de_linha(html):
    """Idempotente: rodar de novo no resultado devolve o mesmo arquivo."""
    def troca(m):
        grupos = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
        for a, b, c in grupos:
            if m.group(a):
                abre, interno, fecha = m.group(a), m.group(b), m.group(c)
                break
        else:
            return m.group(0)
        visivel = SEM_TAG.sub("", interno).replace("&nbsp;", " ").strip()
        if len(visivel) > LIMITE_PARAGRAFO:
            return m.group(0)
        return abre + _cola(interno) + fecha

    # o miolo dos blocos protegidos sai da varredura e volta depois
    guardado = []

    def guarda(m):
        guardado.append(m.group(0))
        return "\x00%d\x00" % (len(guardado) - 1)

    protegido = re.compile(
        r'<(pre|code|script|style)\b.*?</\1>'
        r'|<div class="(?:%s)"[^>]*>.*?</div>' % "|".join(SEM_COLA),
        re.S,
    )
    html = protegido.sub(guarda, html)
    html = BLOCO_QUE_COLA.sub(troca, html)
    return re.sub(r"\x00(\d+)\x00", lambda m: guardado[int(m.group(1))], html)


# ---------------------------------------------------------------------------
# O CEM · a parede de cem quadradinhos
#
# Escrever os cem à mão é onde o desenho para de bater com o número da legenda,
# e ninguém confere contando. O fragmento declara só quantos acendem:
#
#     <div class="cem-grade" data-acesos="13"></div>
#
# e este passo produz os cem. Rodar de novo não muda nada: a grade já expandida
# não tem mais a marca vazia que o padrão procura.
# ---------------------------------------------------------------------------
GRADE_DO_CEM = re.compile(r'<div class="cem-grade" data-acesos="(\d+)"\s*></div>')


def expande_o_cem(html):
    def troca(m):
        n = int(m.group(1))
        pontos = "".join('<i class="cem-p%s"></i>' % (" aceso" if i < n else "")
                         for i in range(100))
        return ('<div class="cem-grade" data-acesos="%d" aria-hidden="true">%s</div>'
                % (n, pontos))
    return GRADE_DO_CEM.sub(troca, html)


# ---------------------------------------------------------------------------
# O RADAR · o polígono sai dos números, não do olho
#
# Calcular seno e cosseno à mão dentro do HTML é como o desenho deixa de
# corresponder aos números, e ninguém confere um polígono com transferidor.
# O fragmento declara só os eixos e os valores:
#
#     <div class="radar" data-eixos="Clareza|Tempo|Risco"
#                        data-valores="80,60,40"
#                        data-valores-b="90,80,30"></div>
#
# A segunda série é opcional, e é ela que faz a figura valer a pena: um radar
# de uma série só quase sempre é uma tabela de quatro linhas.
# ---------------------------------------------------------------------------
import math

RADAR = re.compile(r'<div class="radar"([^>]*)></div>')
RAIO, CENTRO = 108, 150


def _ponto(i, n, v):
    ang = math.radians(-90 + i * 360.0 / n)
    r = RAIO * v / 100.0
    return (CENTRO + r * math.cos(ang), CENTRO + r * math.sin(ang))


# O rótulo é escrito FORA do último anel, e a moldura precisa caber nele. Com
# moldura fixa, "Padrão do formato" sai pela borda e o SVG corta: o texto some e
# nada acusa, porque o recorte é o comportamento normal de um <svg>.
LARGURA_DA_LETRA = 6.2   # medido em Inter 12px, na média do português
ALTURA_DA_LINHA = 14


def largura_estimada(texto):
    return len(texto) * LARGURA_DA_LETRA


def _poligono(valores):
    n = len(valores)
    return " ".join("%.1f,%.1f" % _ponto(i, n, v) for i, v in enumerate(valores))


def desenha_radar(html):
    def troca(m):
        attrs = m.group(1)
        eixos = re.search(r'data-eixos="([^"]*)"', attrs)
        vals = re.search(r'data-valores="([^"]*)"', attrs)
        if not eixos or not vals:
            return m.group(0)
        eixos = [e.strip() for e in eixos.group(1).split("|") if e.strip()]
        a = [float(x) for x in vals.group(1).split(",")]
        b = re.search(r'data-valores-b="([^"]*)"', attrs)
        b = [float(x) for x in b.group(1).split(",")] if b else None
        n = len(eixos)

        p = []
        # anéis de referência, para o olho ter escala
        for anel in (25, 50, 75, 100):
            pts = " ".join("%.1f,%.1f" % _ponto(i, n, anel) for i in range(n))
            p.append('<polygon points="%s" fill="none" stroke="var(--border)" '
                     'stroke-width="1"/>' % pts)
        # raios
        for i in range(n):
            x, y = _ponto(i, n, 100)
            p.append('<line x1="%d" y1="%d" x2="%.1f" y2="%.1f" '
                     'stroke="var(--border)" stroke-width="1"/>'
                     % (CENTRO, CENTRO, x, y))
        if b:
            p.append('<polygon points="%s" fill="none" stroke="var(--text-dim)" '
                     'stroke-width="1.5" stroke-dasharray="5,4"/>' % _poligono(b))
        p.append('<polygon points="%s" fill="var(--accent-soft)" '
                 'stroke="var(--accent)" stroke-width="1.5" fill-opacity="0.75"/>'
                 % _poligono(a))
        # rótulos, empurrados para fora do último anel
        for i, nome in enumerate(eixos):
            x, y = _ponto(i, n, 128)
            ancora = "middle"
            if x > CENTRO + 12:
                ancora = "start"
            elif x < CENTRO - 12:
                ancora = "end"
            p.append('<text x="%.1f" y="%.1f" text-anchor="%s" '
                     'dominant-baseline="middle" font-size="12" '
                     'font-family="var(--font-body)" fill="var(--text-muted)">%s</text>'
                     % (x, y, ancora, nome))
        # a moldura sai das pontas do desenho E das pontas do texto
        x0 = y0 = 1e9
        x1 = y1 = -1e9
        for i, nome in enumerate(eixos):
            x, y = _ponto(i, n, 128)
            larg = largura_estimada(nome)
            if x > CENTRO + 12:
                e, d = x, x + larg
            elif x < CENTRO - 12:
                e, d = x - larg, x
            else:
                e, d = x - larg / 2, x + larg / 2
            x0, x1 = min(x0, e), max(x1, d)
            y0, y1 = min(y0, y - ALTURA_DA_LINHA), max(y1, y + ALTURA_DA_LINHA)
        x0, y0 = min(x0, 0) - 6, min(y0, 0) - 6
        x1, y1 = max(x1, 300) + 6, max(y1, 300) + 6
        return ('<div class="radar"%s><svg viewBox="%.1f %.1f %.1f %.1f" '
                'role="img" aria-label="%s">%s</svg></div>'
                % (attrs, x0, y0, x1 - x0, y1 - y0,
                   " · ".join(eixos), "".join(p)))
    return RADAR.sub(troca, html)


# ---------------------------------------------------------------------------
# UMA FRASE POR LINHA · a quarta reclamação da quebra de linha
#
# Dentro de um bloco marcado .fr-host, cada frase vira <span class="fr">. O CSS
# decide por container query se elas ficam em linha ou empilhadas: quem manda é
# a largura DO BLOCO, não a da janela.
#
# 🔴 Idempotente por reconstrução: desmarca tudo antes de marcar de novo. Marcar
# em cima do que já estava marcado aninharia span dentro de span a cada execução,
# e o arquivo cresceria sozinho até alguém notar.
# ---------------------------------------------------------------------------
ABRE_FR_HOST = re.compile(r'<(\w+)([^>]*\bclass="[^"]*\bfr-host\b[^"]*"[^>]*)>')
SPAN_FR = '<span class="fr">'

# Ponto que NÃO termina frase. Sem esta lista, "R$ 1.200,00." e "Dr. Silva"
# viravam duas frases, e o corte caía no meio de um número.
NAO_CORTA_DEPOIS = (
    "sr", "sra", "dr", "dra", "prof", "etc", "ex", "obs", "art", "pág", "pag",
    "fig", "n", "nº", "no", "vs", "cf", "aprox", "máx", "max", "mín", "min",
)


def _desmarca_fr(interno):
    """Tira a marcação anterior. Sem isto, cada execução aninha span dentro de
    span e o arquivo cresce sozinho até alguém notar."""
    anterior = None
    while anterior != interno:
        anterior = interno
        interno = re.sub(r'<span class="fr">(.*?)</span>', r"\1", interno, flags=re.S)
    return interno


# Tag de bloco fecha a frase. Sem isto o corte atravessa o <p> e produz
# <span class="fr"><p>Uma.</span>, que é HTML inválido e o navegador conserta
# do jeito dele.
TAG_DE_BLOCO = re.compile(
    r"</?(p|div|li|ul|ol|h[1-6]|section|table|tr|td|th|pre|blockquote|br)\b",
    re.I)


def _corta_frases(interno):
    """Marca cada frase do miolo. Não entra em tag: o corte olha só o texto.

    🔴 O espaço que separa duas frases fica FORA do span. Dentro, ele some no
    modo empilhado e as frases grudam no modo inline, que é o que o container
    query entrega em bloco estreito.
    """
    pedacos = re.split(r"(<[^>]+>)", interno)
    saida, buffer_, marcou = [], [], False

    def fecha():
        if not buffer_:
            return
        txt = "".join(buffer_)
        del buffer_[:]
        if not txt.strip():
            saida.append(txt)
            return
        # o branco das pontas sai do span e fica no meio, entre as frases
        m = re.match(r"^(\s*)(.*?)(\s*)$", txt, flags=re.S)
        esq, meio, dir_ = m.group(1), m.group(2), m.group(3)
        saida.append(esq + SPAN_FR + meio + "</span>" + dir_)

    for p_ in pedacos:
        if p_.startswith("<"):
            if TAG_DE_BLOCO.match(p_):
                fecha()          # fronteira de bloco fecha a frase corrente
                saida.append(p_)
            else:
                buffer_.append(p_)
            continue
        resto = p_
        while resto:
            m = re.search(r"[.!?](?:&nbsp;|\s)+(?=[A-ZÀ-Ý])", resto)
            if not m:
                buffer_.append(resto)
                break
            antes = resto[:m.start()]
            ultima = re.search(r"([\wÀ-ÿ]+)$", antes)
            # só abreviação. Ponto dentro de número ("1.200") não chega aqui:
            # o padrão exige espaço depois do ponto, e número não tem.
            if ultima and ultima.group(1).lower() in NAO_CORTA_DEPOIS:
                buffer_.append(resto[:m.end()])
                resto = resto[m.end():]
                continue
            buffer_.append(resto[:m.start() + 1])
            fecha()
            saida.append(resto[m.start() + 1:m.end()])   # o espaço, fora do span
            marcou = True
            resto = resto[m.end():]
    fecha()
    return "".join(saida) if marcou else interno


def uma_frase_por_linha(html):
    """Sempre recalcula do zero: rodar de novo devolve o mesmo arquivo."""
    saida, i = [], 0
    for m in ABRE_FR_HOST.finditer(html):
        tag = m.group(1)
        # Acha o fechamento do próprio bloco, contando profundidade.
        # 🔴 O regex casa a TAG INTEIRA, com o ">". Casar só "</p" devolve uma
        # posição um caractere curta, e o miolo perde o último caractere: o
        # ponto final da última frase ficava fora do span, a cada execução.
        prof, j, fim = 1, m.end(), len(html)
        while prof and j < len(html):
            t = re.search(r"<(/?)%s\b[^>]*>" % tag, html[j:])
            if not t:
                break
            if t.group(1):
                prof -= 1
                if prof == 0:
                    fim = j + t.start()
                    j = j + t.end()
                    break
            else:
                prof += 1
            j += t.end()
        interno = html[m.end():fim]
        saida.append(html[i:m.end()])
        saida.append(_corta_frases(_desmarca_fr(interno)))
        i = fim
    saida.append(html[i:])
    return "".join(saida)


# ---------------------------------------------------------------------------
# A CASCA
# ---------------------------------------------------------------------------
def css():
    partes = []
    for nome in ("marca.css", "base.css"):
        partes.append(io.open(os.path.join(AQUI, nome), encoding="utf-8").read())
    return "\n".join(partes)


def trilha(slug_atual):
    """A barra do curso: onde esta a aula aberta, dentro da trilha inteira.

    Tres estados, e o estado E o conteudo: `feita` (antes da atual), `agora`
    e o resto. A aula atual nao vira link — clicar nela nao leva a lugar
    nenhum, e um link que nao vai a lugar nenhum e ruido.
    """
    plana = [(g, sl, t) for g, aulas in TRILHA for sl, t in aulas]
    total = len(plana)
    pos = next((i for i, (_, sl, _) in enumerate(plana) if sl == slug_atual), None)
    if pos is None:
        return ""                      # pagina fora da trilha: sem barra

    partes = ['<aside class="trilha">',
              '<div class="trilha-cab">Aula %d de %d</div>' % (pos + 1, total),
              '<div class="trilha-agora">%s</div>' % plana[pos][2]]
    grupo_aberto = None
    for i, (grupo, sl, titulo) in enumerate(plana):
        if grupo != grupo_aberto:
            if grupo_aberto is not None:
                partes.append('</ol>')
            if grupo:
                partes.append('<div class="trilha-grupo">%s</div>' % grupo)
            partes.append('<ol>')
            grupo_aberto = grupo
        if i < pos:
            estado, marca = "feita", "&#10003;"
        elif i == pos:
            estado, marca = "agora", "%02d" % (i + 1)
        else:
            estado, marca = "", "%02d" % (i + 1)
        n = '<span class="tl-n">%s</span>' % marca
        if i == pos:
            corpo = '<span class="tl">%s<span>%s</span></span>' % (n, titulo)
        else:
            href = "../%s/" % sl if sl != "index" else "../"
            corpo = '<a href="%s">%s<span>%s</span></a>' % (href, n, titulo)
        partes.append('<li class="%s">%s</li>' % (estado, corpo))
    partes.append('</ol></aside>')
    return "".join(partes)


def rodape(slug):
    """O par anterior/proxima, tirado da SEQUENCIA. Ponta sem vizinho fica vazia.

    Nunca inventa destino: se a pagina e a primeira, nao existe "anterior", e
    o lado fica em branco em vez de apontar para a propria pagina.
    """
    if slug not in SEQUENCIA:
        return ""
    i = SEQUENCIA.index(slug)
    # 🔴 A capa mora na RAIZ; as outras cinco moram um nivel abaixo. O caminho
    # relativo depende de onde a pagina ATUAL esta, nao de onde o alvo esta.
    # O gate G7 pegou isto na primeira rodada: da capa, "../modulo/" sai do site.
    base = "" if slug == "index" else "../"
    def href(s):
        return base if s == "index" else base + "%s/" % s
    lados = []
    if i > 0:
        alvo = SEQUENCIA[i - 1]
        lados.append('<a href="%s">&larr; %s</a>' % (href(alvo), PAGINAS[alvo]["titulo"]))
    else:
        lados.append("<span></span>")
    if i < len(SEQUENCIA) - 1:
        alvo = SEQUENCIA[i + 1]
        lados.append('<a href="%s">%s &rarr;</a>' % (href(alvo), PAGINAS[alvo]["titulo"]))
    else:
        lados.append("<span></span>")
    return '<nav class="rodape-nav">%s</nav>' % "".join(lados)


def secoes(fragmento):
    """A nav lateral sai das seções do fragmento, nunca de uma lista à mão."""
    padrao = re.compile(
        r'<section class="secao" id="(?P<id>[^"]+)"[^>]*>\s*'
        r'<div class="secao-topo">\s*'
        r'<div class="secao-n">(?P<n>.*?)</div>.*?'
        r'<h2>(?P<h2>.*?)</h2>',
        re.S,
    )
    return [(m.group("id"),
             SEM_TAG.sub("", m.group("n")).strip(),
             SEM_TAG.sub("", m.group("h2")).strip())
            for m in padrao.finditer(fragmento)]


def monta(slug, cfg, fragmento):
    selos = "".join('<span class="selo">%s</span>' % s for s in cfg.get("selos", []))
    if cfg.get("migalha"):
        pedacos = []
        for href, texto in cfg["migalha"]:
            pedacos.append('<a href="%s">%s</a>' % (href, texto) if href else texto)
        migalha = '<nav class="migalha">%s</nav>' % " &rsaquo; ".join(pedacos)
    else:
        migalha = ""
    raiz = "./" if slug == "index" else "../"
    # 🔴 A BARRA LATERAL NAO NASCE MAIS, decisao do padrao em 28/08 e medida
    # neste curso: 0 de 30 paginas a montavam, e 183 das 193 figuras sao
    # breakout, que a regra .com-trilha .solta zerava. A funcao trilha() fica
    # no arquivo: quem quiser a barra de volta troca esta linha por
    # barra = trilha(slug), e nada mais.
    barra = ""
    abre = '<div class="com-trilha">' + barra if barra else ""
    fecha = "</div>" if barra else ""
    return TEMPLATE % dict(
        titulo=cfg["titulo"], css=css(), raiz=raiz,
        sigla=CURSO["sigla"], nome=CURSO["nome"], sub=CURSO["sub"],
        migalha=migalha, kicker=cfg["kicker"], h1=cfg["h1"],
        sub_pagina=cfg["sub"], selos=selos, corpo=fragmento,
        # aula-pratica ou aula-fundamento, lido do tipo= em PAGINAS. Pagina que
        # nao e aula fica sem classe, e os gates de tipo nao a enxergam.
        tipo=("aula-" + cfg["tipo"]) if cfg.get("tipo") else "",
        abre_trilha=abre, fecha_trilha=fecha, rodape=rodape(slug),
    )


TEMPLATE = r"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>%(titulo)s</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
<style>
%(css)s
</style>
</head>
<body>

<header class="topo">
  <div class="topo-in">
    <a href="%(raiz)s" class="marca">
      <div class="marca-sigla">%(sigla)s</div>
      <div>
        <div class="marca-nome">%(nome)s</div>
        <div class="marca-sub">%(sub)s</div>
      </div>
    </a>
  </div>
</header>

%(migalha)s

%(abre_trilha)s
<main class="folha %(tipo)s">
  <div class="heroi">
    <div class="heroi-kicker">%(kicker)s</div>
    <h1>%(h1)s</h1>
    <p class="heroi-sub">%(sub_pagina)s</p>
    <div>%(selos)s</div>
  </div>

%(corpo)s
%(rodape)s
</main>
%(fecha_trilha)s

<script>
(function(){
  'use strict';

  /* Confirmação no proprio botao. Toast flutuante exige posicao fixa e some
     atras do teclado no celular, que e onde o aluno mais copia. */
  function avisa(b, texto){
    if(b.dataset.antes === undefined) b.dataset.antes = b.textContent;
    b.textContent = texto;
    clearTimeout(b._t);
    b._t = setTimeout(function(){ b.textContent = b.dataset.antes; }, 1600);
  }

  function copia(b, texto){
    if(!texto) return;
    if(navigator.clipboard && navigator.clipboard.writeText){
      navigator.clipboard.writeText(texto).then(function(){ avisa(b, 'copiado'); },
                                               function(){ avisa(b, 'nao deu'); });
      return;
    }
    /* Sem clipboard (http em rede da sala, navegador antigo) o botao nao pode
       simplesmente nao fazer nada: seleciona o texto para o aluno usar Ctrl+C. */
    var t = document.createElement('textarea');
    t.value = texto; t.setAttribute('readonly','');
    t.style.position='fixed'; t.style.opacity='0';
    document.body.appendChild(t); t.select();
    try{ document.execCommand('copy'); avisa(b, 'copiado'); }
    catch(e){ avisa(b, 'use ctrl+c'); }
    document.body.removeChild(t);
  }

  /* ---- prompt copiavel ---- */
  document.querySelectorAll('.btn-copiar[data-alvo]').forEach(function(b){
    b.addEventListener('click', function(){
      var alvo = document.getElementById(b.dataset.alvo);
      if(alvo) copia(b, alvo.textContent.trim());
    });
  });

  /* ---- imprimir o documento ----
     A pagina de exemplo pronto imprime em A4 sem levar o site junto: o CSS de
     impressao esconde a moldura, e este botao so dispara o dialogo. */
  document.querySelectorAll('[data-acao="imprimir"]').forEach(function(b){
    b.addEventListener('click', function(){ window.print(); });
  });

  /* ---- o criador de prompt ----
     O texto a direita nasce dos proprios campos: nao existe uma segunda copia
     do prompt no HTML para sair de sincronia com a esquerda. */
  function escapa(s){
    return s.replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;');
  }

  document.querySelectorAll('.criador').forEach(function(c){
    var campos = [].slice.call(c.querySelectorAll('textarea[data-titulo]'));
    var saida  = c.querySelector('.cr-txt');
    if(!campos.length || !saida) return;
    var exemplo = campos.map(function(t){ return t.value; });

    function texto(){
      return campos.filter(function(t){ return t.value.trim(); })
                   .map(function(t){ return '# ' + t.dataset.titulo + '\n' + t.value.trim(); })
                   .join('\n\n');
    }
    function pinta(){
      var t = texto();
      if(!t){
        saida.innerHTML = '<span class="cr-vazio">Preencha um campo à esquerda '
                        + 'e o prompt aparece aqui.</span>';
        return;
      }
      saida.innerHTML = escapa(t).replace(/^# (.+)$/gm, '<span class="cr-h"># $1</span>');
    }

    campos.forEach(function(t){ t.addEventListener('input', pinta); });
    c.querySelectorAll('[data-acao]').forEach(function(b){
      b.addEventListener('click', function(){
        var a = b.dataset.acao;
        if(a === 'copiar'){ copia(b, texto()); return; }
        if(a === 'limpar')  campos.forEach(function(t){ t.value = ''; });
        if(a === 'exemplo') campos.forEach(function(t, i){ t.value = exemplo[i]; });
        pinta();
      });
    });
    pinta();
  });

  /* ---- o canvas preenchivel ----
     Guarda no proprio aparelho. Nada sai daqui: nao ha envio, e o aviso na tela
     diz isso, senao metade da sala acha que mandou para alguem. */
  document.querySelectorAll('.canvas[data-chave]').forEach(function(c){
    var campos = [].slice.call(c.querySelectorAll('textarea[id]'));
    var estado = c.querySelector('.canvas-estado');
    var chave  = 'trn_' + c.dataset.chave;
    if(!campos.length) return;

    function diz(txt, ok){
      if(!estado) return;
      estado.textContent = txt;
      estado.classList.toggle('salvo', !!ok);
    }
    function salva(){
      var d = {};
      campos.forEach(function(t){ d[t.id] = t.value; });
      try{
        localStorage.setItem(chave, JSON.stringify(d));
        diz('Rascunho salvo neste aparelho', true);
      }catch(e){
        diz('Este navegador nao deixa salvar rascunho', false);
      }
    }
    function carrega(){
      try{
        var d = JSON.parse(localStorage.getItem(chave) || '{}');
        var achou = false;
        campos.forEach(function(t){
          if(d[t.id]){ t.value = d[t.id]; achou = true; }
        });
        if(achou) diz('Rascunho salvo neste aparelho', true);
      }catch(e){}
    }
    /* TAB entre campos, ponto medio no lugar da quebra: um campo de duas linhas
       viraria duas linhas na planilha e desalinharia a turma inteira. */
    function linha(){
      return campos.map(function(t){
        return t.value.replace(/\t/g,' ').replace(/\r?\n/g,' · ').trim();
      }).join('\t');
    }

    campos.forEach(function(t){ t.addEventListener('input', salva); });
    c.querySelectorAll('[data-acao]').forEach(function(b){
      b.addEventListener('click', function(){
        if(b.dataset.acao === 'linha'){ copia(b, linha()); return; }
        if(b.dataset.acao === 'apagar'){
          campos.forEach(function(t){ t.value = ''; });
          try{ localStorage.removeItem(chave); }catch(e){}
          diz('O rascunho fica salvo neste aparelho', false);
        }
      });
    });
    carrega();
  });
})();
</script>
</body>
</html>
"""


def main():
    for slug, cfg in PAGINAS.items():
        fonte = os.path.join(AQUI, "conteudo", slug + ".html")
        if not os.path.exists(fonte):
            print("  pulou:   %s (sem fragmento)" % slug)
            continue
        fragmento = io.open(fonte, encoding="utf-8").read()
        html = monta(slug, cfg, fragmento)
        html = desenha_radar(expande_o_cem(html))
        html = cola_quebra_de_linha(uma_frase_por_linha(html))
        destino = (os.path.join(RAIZ, "index.html") if slug == "index"
                   else os.path.join(RAIZ, slug, "index.html"))
        os.makedirs(os.path.dirname(destino), exist_ok=True)
        with io.open(destino, "w", encoding="utf-8") as f:
            f.write(html)
        print("  gravado: %-34s %d bytes"
              % (os.path.relpath(destino, RAIZ), len(html.encode("utf-8"))))
    print("\n  %d páginas" % len(PAGINAS))


if __name__ == "__main__":
    main()
