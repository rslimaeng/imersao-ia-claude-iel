# CLAUDE.md · template de treinamento

> **Os cursos de origem aparecem como código** (`IC-A`…`IC-D`). O mapa está em
> `0-padrao-de-treinamentos/PROVENIENCIA-INTERNA.md`, que fica fora de `template/`
> e não é copiado para curso nenhum. O G50 confere.
> Copie esta pasta para começar um curso novo.

🔴 **Leia o `COMO-EXECUTAR.md` primeiro.** Ele é o roteiro: diz o que fazer, em que
ordem, e qual componente e qual figura entram em cada seção da aula. **Este arquivo
aqui é a referência**, e o roteiro manda você nele quando precisar do detalhe.

Ler só a referência é o erro que custa a primeira leva: você fica sabendo todas as
regras e não sabe por onde começar.

**Fontes.** A anatomia de aula e a escrita vêm do **IC-A**.
A página de caso em cinco passos, a prévia do resultado e as estruturas de decisão
vêm do **IC-B**. O gerador, os gates e a cura da quebra de linha
vêm do **IC-C**. Rafael aprovou os três como
referência em 20/08/2026.

**Um aviso sobre as fontes:** o IC-B é o mais forte em estrutura de
exercício e o mais antigo em escrita. Ele usa travessão e emoji em card, que
depois viraram proibidos. **Copie a estrutura de lá, a escrita do IC-A.**

---

## 1. Como um curso nasce

Rafael entrega **a ementa e o drill de conteúdo**. O Claude produz o material no
padrão, com liberdade criativa dentro dele.

| Passo | O que acontece | Quem decide |
|---|---|---|
| 0 | `python3 _build/entrada.py <pasta do cliente>` inventaria o que existe e lista o que falta | mecânico |
| 1 | A paleta do cliente entra no `_build/marca.css` | Rafael |
| 2 | O nome, a sigla e a lista de páginas entram no `gerar.py` | Rafael |
| 3 | Cada aula vira um fragmento em `_build/conteudo/` | Claude propõe |
| 4 | `python3 _build/gerar.py` monta as páginas | mecânico |
| 5 | `python3 _build/gates.py` reprova o que quebrou | mecânico |
| 6 | Rafael valida no navegador antes da próxima leva | Rafael |

🔴 **Editar o `index.html` gerado é trabalho perdido.** A próxima execução do
gerador apaga. O conteúdo mora em `_build/conteudo/`.

---

## 2. Trocar de cliente é trocar dois arquivos

| Arquivo | O que tem | Muda por cliente? |
|---|---|---|
| `_build/gerar.py` § `TRILHA` | **a ordem das aulas do curso.** É a única lista escrita à mão, porque ordem pedagógica não se deduz de nome de arquivo. Alimenta a barra lateral: aula feita ✓, aula atual, aula por vir |
| `_build/marca.css` | a paleta, a tipografia, os tokens. ⚠️ **cópia declarada** de `~/developer/17-padrao-visual/aula/tokens-aula.css` — a decisão de cor é de lá; aqui você mexe só nas 5 linhas de `--accent*` do cliente | **sim, é só isso** |
| `_build/gerar.py` · `CURSO` | nome, sigla, subtítulo | **sim** |
| `_build/base.css` | estrutura e componentes | não |
| `_build/gates.py` | as travas do padrão | não |

O `base.css` **não tem nenhuma cor escrita**, só `var()`. Um gate confere isso.
Quando um hex vaza para o `base.css`, ele deixa de ser template e vira o CSS
daquele cliente.

**A cor semântica não é decoração.** Verde é o certo, âmbar é o parecido que
engana, vermelho é o problema. Trocar o significado entre uma página e outra é o
jeito mais rápido de tornar toda figura do site ilegível.

---

## 3. Por que a aula tem essa forma

Esta seção é o **porquê** das regras que vêm depois. Ela existe porque regra sem
motivo só funciona nos casos que quem escreveu a regra imaginou.

**De onde vem.** O bloco de andragogia foi extraído do curso **Didática Lendária, de
Adriano de Marqui** (Academia Lendária), lido nas transcrições originais em 20/08/2026.
O que era do padrão continua marcado como tal. Onde eu inferi, está dito.

### A frase que governa tudo

> As pessoas não entendem o que você fala, mas o que elas veem ou o que elas sentem
> quando você fala.

O caminho é: palavra entra, o cérebro procura uma imagem que já conhece, e **só então**
compreende. Se não virou imagem, não virou entendimento.

O teste dele é bom: **"não pense numa melancia."** Você pensou. A imagem chega antes
da ordem, porque ela vem primeiro no processamento.

É daqui que sai a regra de desenhar sempre que der. Não é preferência estética: é o
mecanismo. E é daqui que sai o piso de três figuras por aula.

**As ferramentas para produzir a imagem**, na ordem em que costumam funcionar:
exemplo · analogia · desenho · narrativa · **a visão do todo** (onde a peça que você
está ensinando se encaixa no conjunto).

### O GPS: destino, origem, rota

A ordem é a de um aplicativo de mapa, e ela não é arbitrária.

| | O que é | O que quebra sem isso |
|---|---|---|
| **Destino** | a motivação, no começo. Para onde o aluno vai, e por que ele precisa disso | a aula abre pela definição, e a pessoa não sabe por que deveria continuar |
| **Origem** | **empatia.** De onde essa pessoa parte, o que ela já sabe, o que ela não sabe | você dá aula sobre a **sua** jornada, do jeito que **você** aprendeu |
| **Rota** | o roteiro. A sequência que leva de um ponto ao outro | quatro defeitos, na tabela abaixo |

🔴 **Origem é a que mais se perde.** No padrão ela já existia aplicada ao exercício
("só pede o que o aluno já tem naquele ponto"). Vale para a aula inteira.

### As cinco perguntas, para achar a essência

O padrão já dizia "a situação vem antes do conceito". Faltava **como encontrar a
situação**. É uma cadeia de cinco "por quê", cada uma em cima da resposta anterior,
até sair do técnico:

```
Por que aprender a montar o relatório com IA?   → para não gastar a segunda de manhã
Por que não gastar a segunda de manhã?          → tenho coisa mais importante
Por que essa coisa é mais importante?           → é ela que muda o resultado da loja
Por que o resultado da loja importa para você?  → é o que me mantém no cargo
Por que o cargo importa?                        → é o que sustenta o que eu construí
```

A aula abre pela **última resposta**, não pela primeira. "Você já pensou em ter a
segunda de manhã de volta?" funciona; "hoje vamos aprender a consolidar planilhas" não.

🔶 **Inferência minha:** em material escrito a essência entra como a **primeira frase
da seção 01**, e não como promessa de venda. Exagerar aqui produz o oposto: material
corporativo que abre com emoção grande soa a folheto, e a sala fecha.

### Um conceito por ciclo, e o ciclo não se mistura

Cada conceito faz o caminho **inteiro** antes de o próximo começar:

```
conceito → imagem (a figura) → prática → link declarado → próximo conceito
```

🔴 **Não emende dois conceitos e depois um exercício só.** A pessoa não consegue
separar as peças depois, e não sabe qual das duas coisas ela não entendeu.

**Teto de dois conceitos por aula**, três no limite. Ele conta ter encontrado aulas
com dezoito. O rótulo da seção 02 declara o teto, e é por isso que ele existe.

E o **nome da aula tem que dizer o assunto da aula**, porque a pessoa vai voltar
procurando. Com nome vago ela varre o curso inteiro e desiste.

### Os quatro defeitos que o roteiro evita

| O defeito | Como aparece | Como aparece **no texto escrito** |
|---|---|---|
| inibição | não conseguir passar o que sabe | a frase que se protege: "de certa forma", "talvez seja o caso de" |
| desconexão | não saber o que fala, pular de assunto | seção que não engata na anterior, e o leitor vai embora sem perceber |
| prolixidade | palavra sobre palavra, técnica sobre técnica | o parágrafo que explica de novo o que o anterior já explicou |
| vício de linguagem | "né", "então", muleta repetida | a expressão-muleta que aparece em toda seção e some quando você a corta |

**A cura dos dois do meio é estrutural**, e o padrão já a tem: a anatomia fixa de oito
seções e o gancho no fim de cada aula.

### Logos, etos, patos

Comunicação que é **só logos** não engaja, mesmo estando certa.

| | O que é | No material escrito |
|---|---|---|
| **logos** | a lógica, o número, a conta | a tabela, a figura medida, o número com a variação ao lado |
| **etos** | a credibilidade de quem fala | a fonte citada, o caso que aconteceu de verdade, a cerca que diz o que não fazer |
| **patos** | o que a pessoa sente e deseja | a situação da seção 01, escrita na voz de quem faz o trabalho |

🔶 **Inferência minha:** num treinamento in-company o **etos** carrega mais peso que
o patos. A sala já está lá por obrigação; o que ela precisa é de motivo para confiar.

### Os quatro níveis, e o que a aula pode cobrar

```
não sabe que não sabe  →  sabe que não sabe  →  sabe fazendo força  →  faz sem pensar
```

**A aula não leva ninguém do primeiro ao último.** Ela leva do primeiro ao segundo (é
o que a seção 01 faz) e do segundo ao terceiro (é o que o exercício faz). O quarto é
repetição no trabalho, e prometer isso na sala é prometer o que não se entrega.

### O que do curso dele NÃO se aplica aqui

Metade é voz, dicção, modulação e expressão facial. É oratória para vídeo, e o
material aqui é **escrito**.

Só uma coisa atravessa: **o equivalente escrito da monotonia**. Se todo parágrafo tem
o mesmo tamanho e a página não muda de ritmo, o leitor desliga do mesmo jeito que
desliga de uma voz em um tom só. O padrão já cura isso sem ter dado o nome: nenhuma
seção passa de dois parágrafos seguidos sem uma figura, uma tabela ou um bloco.

---

## 4. A anatomia de aula, e por que ela é fixa

Toda aula tem as mesmas oito seções, na mesma ordem. O rótulo em cinza diz a
**função** da seção; o H2 diz o assunto dela. Quem abre a quinta aula já sabe
onde as coisas estão.

🔴 **O rótulo é CATEGORIA FIXA, e não frase.** `A situação`, `O conceito`,
`Como funciona`, `Demonstração`, `Sua vez`, `Confira`, `Pegadinhas`, `A cerca`.
São sempre essas oito palavras, em todo curso. O que muda de aula para aula é o
H2, que é o assunto daquela aula.

Até 26/08 a aula modelo fazia o contrário: o H2 carregava a categoria
(`<h2>A situação</h2>`) e o rótulo carregava uma frase (`O reconhecimento`).
A regra acima já estava escrita aqui e o modelo a contradizia, então quem
copiava o modelo copiava o erro. **Corrigido no modelo em 26/08**, e as três
entregas de referência fazem assim, todas: `01 · A SITUAÇÃO` em cima,
`A conversa que começou boa e foi piorando` embaixo.

**Antes da 01 vem um bloco que não é seção:** o `nesta-aula`. Ele não define
nada e não conta história, então não fere a regra de não começar pela definição.
Ele é o **contrato**: o que a pessoa vai saber fazer ao sair.

```html
<div class="nesta-aula">
  <div class="nesta-aula-rot">Nesta aula</div>
  <div class="nesta-aula-sub">Ao final, você será capaz de:</div>
  <ul>
    <li>Montar um prompt com os cinco campos, sem consultar o modelo</li>
    <li>Identificar, num pedido que deu errado, qual campo faltou</li>
  </ul>
</div>
```

**A regra de escrita que faz ele valer alguma coisa:** verbo de ação, e o que a
pessoa **faz**. *"Entender o conceito de contexto"* não é verificável, e por
isso não é objetivo: é enfeite. *"Montar um prompt com os cinco campos"* é.
Três linhas bastam; seis viram índice, e índice ninguém lê.

**Não confunda com "Principais aprendizados".** São duas coisas, e a aula leva
as duas: o contrato antes, o **fecho** depois. Em 25/08 esta seção dizia
*"escolha um, e o contrato rende mais"*. **O Rafael decidiu em 26/08 que leva os
dois**, como na referência que originou o bloco. O que sobrou da regra antiga é
o alerta, que continua valendo inteiro:

**Depois da 08 vêm TRÊS blocos que não são seção**, e cada um faz uma coisa
diferente. A anatomia continua com oito.

| bloco | o que ele faz | quem confere |
|---|---|---|
| `.checagem` | itens contáveis ou sim/não, que a pessoa verifica sozinha | ela |
| `.fecho` | o que ela sabe fazer agora, e o artefato que ela tem | ela, relendo |
| `.gancho` | a trava que ESTA aula não resolve, e que abre a próxima | ninguém: é a costura |

Até 26/08 o modelo tinha só o `.fecho`, com o gancho enfiado numa nota dentro
dele. O `.checagem` e o `.gancho` existiam no CSS e em nenhuma página. **É por
isso que o fecho parecia raso**: três momentos comprimidos em um.

```html
<div class="fecho">
  <div class="fecho-rot">Você sabe fazer isto agora</div>
  <div class="fecho-sub">Confira sozinho: se algum item não estiver de pé, volte na seção que o cobre.</div>
  <ul>
    <li><strong>Você montou</strong> um prompt com os cinco campos, sem consultar o modelo</li>
    <li><strong>O artefato:</strong> o arquivo que você tem agora e não tinha ao abrir a aula</li>
  </ul>
  <div class="fecho-nota">O gancho da próxima aula. Última do módulo não tem gancho, tem o que a pessoa faz na segunda de manhã.</div>
</div>
```

🔴 **O fecho escreve-se DEPOIS de escrever a aula.** Escrito antes, ele vira
cópia do contrato e repete o que a pessoa leu quarenta minutos atrás. O par só
funciona porque um é promessa e o outro é registro: *você vai saber fazer* de um
lado, *você sabe fazer agora* do outro. Mesmo verbo, tempo diferente.

| # | A função | O que entra | O erro que ela evita |
|---|---|---|---|
| 01 | A situação | o problema na voz de quem faz o trabalho, sem conceito nenhum | começar pela definição |
| 02 | O conceito | **um, e só um**, e ele nasce com a analogia junto | a aula que ensina seis coisas e fixa nenhuma · conceito sem imagem |
| 03 | Como funciona | o mecanismo, com figura. É a seção mais visual | explicar com três parágrafos o que um desenho resolve |
| 04 | Demonstração | ver acontecer. Leva ao passo a passo, em página própria | mostrar o resultado pronto |
| 05 | Sua vez | o exercício, com o arquivo de partida | exercício que pede o que o aluno ainda não tem |
| 06 | Confira | gabarito, atrás de um toggle fechado | gabarito aberto: ninguém tenta |
| 🏁 | **O divisor** | `.ate-aqui`: a aula acaba aqui, o resto é aprofundamento | a aula de 3.400 palavras que chega toda como obrigatória |
| 07 | Pegadinhas | os erros que quase todo mundo comete ali | a pessoa descobrir sozinha, três semanas depois |
| 08 | A cerca | o que nunca pode acontecer neste nível | ensinar a fazer sem ensinar quando não fazer |

🔴 **A página modelo é `aula/index.html`.** Abra antes de escrever a primeira
aula e copie de `_build/conteudo/aula.html`. Desenhar do zero o que já está
montado é o desperdício que este padrão existe para evitar.

**O que é OBRIGATÓRIO em cada seção, e o que é escolha.** O modelo monta a
coluna do meio. A da direita é o menu da vitrine: escolha UMA, não todas.

| # | obrigatório, toda aula | o modelo mostra | escolha uma na vitrine |
|---|---|---|---|
| 01 | a dor na voz de quem faz | prosa curta | `.glosa` |
| 02 | **um** conceito, nunca dois, **com `.analogia`** | `.conceito` + `.analogia` + `.contraste` | `.venn` · `.cem` · `.antes` |
| 03 | um artefato visual, sempre | `.converge` + `.mesa` | `.ciclo` · `.escada` · `.matriz` · `.cascata` · `.linha-tempo` · mais catorze |
| 04 | o link para a página de caso | `.demo` + link | `.tela` · `.fonte` |
| 05 | **as três, sempre:** `.arquivo`, `.passo`, `.prompt` — mais `.destrave` em todo passo que pede texto do aluno | as três | `.canvas` no lugar do `.arquivo`, quando o insumo é a rotina da própria pessoa |
| 06 | o gabarito fechado | `<details class="gabarito">` | — |
| 🏁 | o divisor, sempre | `.ate-aqui` + `.ate-aqui-nota` | — |
| 07 | os erros de quem parte daqui | `.dg` | `.destrave` |
| 08 | a cerca | `.cartao` com lista | `.aviso erro` |

🔴 **UMA AULA, UM CONCEITO — mudou em 28/08.** Até aqui a linha 02 dizia "um, no
máximo dois", e o resultado medido no primeiro curso real foi: **9 de 9 aulas com dois
conceitos empilhados na 02 e a primeira prática só na 05.** A regra 1 do roteiro
(*conceito → imagem → prática → próximo conceito*) estava escrita e era inaplicável:
duas voltas do ciclo não cabem em oito seções. Com um conceito por aula o ciclo fecha
sozinho, a aula encolhe, e **o encontro passa a ter mais voltas de prática, não menos**.
Medido pelo **G39**.

🔴 **O DIVISOR 🏁 — peça herdada, declarada como herdada.** Vem de *Claude para
Líderes*, de Adriano Couto: a aula com **dois comprimentos**. Até o divisor é
obrigatório; depois dele é aprofundamento, e o aluno escolhe. Herdamos a forma e nada
do texto. Medido na aula `n1` do piloto: **2.349 palavras até o gabarito e 1.118
depois**, sendo 982 só na seção 08 — mais que a prática inteira, numa aula de
nivelamento. Medido pelo **G40**.

🔴 **TRÊS TIPOS DE AULA. Dois desde 28/08, o terceiro desde 30/08.** Declare em
`PAGINAS`, e a anatomia é a mesma nos três: oito seções, na mesma ordem. O que muda é o
contrato das seções 05 e 06. Medido pelo **G43**.

| `tipo=` | o que ela é | o que a 05 entrega | o que a 06 cobra |
|---|---|---|---|
| `"pratica"` | a pessoa faz | `.arquivo` + `.passo` + `.prompt` + `.passo-ok` | o gabarito |
| `"fundamento"` | como a coisa funciona | um **instrumento**: `.arquivo`, `.canvas` ou `.criador` | a **`.verifique`** |
| `"organizacao"` | a pessoa mapeia a própria rotina | `.canvas` + figura de estrutura + `.destrave` | o gabarito |

Uma anatomia só, aplicada aos três casos, foi o que produziu exercício postiço em aula de
conceito. **A aula de fundamento não é aula sem entrega: é aula que entrega outra coisa.**
E em três aulas seguidas, pelo menos uma é de `pratica` ou `organizacao` — **G44**. A de
organização quebra a fila porque nela a sala não só escuta: ela preenche, decide, ordena.

🔴 **EXPLICAR E CONFIRMAR SÃO DUAS COISAS, e o padrão só tinha a primeira.** Regra do
Rafael, 30/08: *"há aulas de fundamentos que são só de explicação e de confirmar com a
turma se todo mundo entendeu"*. A `.checagem` é lista de conferência no fim, que a pessoa
lê concordando com ela mesma: isso confirma **leitura**. O que confirma **entendimento** é
a `.verifique` — pergunta fechada, resposta escondida, colada no conceito que ela testa. É
a peça que torna a aula de fundamento conduzível numa sala, e não só legível sozinha.

🔴 **O RESULTADO ESPERADO DO PASSO, desde 30/08.** Todo exercício leva pelo menos um
`.passo-ok` dizendo o que deveria ter acontecido. Sem ele o aluno só descobre que errou no
passo 2 quando chega ao 5 e nada bate — e aí ele não sabe qual dos quatro passos foi. A
peça estava na lista de 27/08 como proposta e ficou três dias fora do padrão.

🔴 **MODELO PARA CADA CONTRATO.** `aula/` é o modelo de prática e `fundamento/` é o de
fundamento. **Contrato sem modelo não é regra: é texto no roteiro que ninguém segue.** Até
30/08 o padrão declarava dois tipos e mostrava um só, e quem escrevia aula de conceito
copiava a de prática e inventava exercício para preencher a 05. Foi assim que a trilha IEL
40h ganhou cinco aulas de conceito com exercício postiço, seguidas.

🔴 **A TRILHA LATERAL SAIU, desde 28/08.** A regra `.com-trilha .solta` zerava o breakout,
e toda figura larga encolhia para a largura da coluna. A barra custava o espaço largo da
página em troca de um índice que a página de módulo já dá. Navegação fica no `.rodape-nav`
e na migalha.

🔴 **A ANATOMIA NÃO PARA NA AULA. Regra de módulo, desde 28/08.**

**Em quaisquer três aulas seguidas da `TRILHA`, pelo menos uma entrega artefato** —
`.arquivo`, `.canvas` ou `.criador`, uma peça que produz algo que **sai da tela**.
Exercício não é entrega. Medido pelo **G42**, que é o primeiro gate do padrão a olhar a
**sequência** e não a página.

Nasceu de defeito real na trilha IEL 40h: cinco aulas seguidas de fundamento, 15 passos de
exercício, **zero artefato**, e as cinco passando em todos os 41 gates da época.

🔴 **O CONCEITO NASCE COM A IMAGEM. A fórmula AIDEN, desde 28/08.**

> *"As pessoas não entendem o que você fala, mas o que elas veem ou o que elas sentem
> quando você fala."* E: *"a imagem vem primeiro, para depois processar o entendimento."*

Cinco partes, e o padrão já tinha duas:

| | | onde mora |
|---|---|---|
| **A** | abstrato — o conceito técnico, **em uma frase** | `.conceito` |
| **I** | imagem — o visual do cotidiano | `.analogia` |
| **D** | detalhamento — o de-para entre a analogia e a coisa | `.analogia-mapa` |
| **E** | extensão — onde mais aquilo aparece | `.analogia-mais` |
| **N** | negação — o que **não** é | `.contraste` |

**A imagem não é ilustração que vem depois: é como o conceito se diz.** Medido no piloto
IEL: a seção de conceito tinha **632 palavras** e a primeira figura só chegava na seção
seguinte, com 312. Seiscentas palavras de abstração antes de qualquer imagem foi o que
travou a sala em 27/08 — e a ordem das seções não tem nada a ver com isso.

Forma herdada de Adriano de Marqui (*Didática Lendária*). Pesquisa em
`4-ativo-pedagogico/notas/vault-alan--didatica-e-feynman.md`. Medido pelo **G41**.

🔴 **A seção 05 é a que mais nasce magra**, e ela tem três peças obrigatórias.

E o `.destrave` mora **aqui**, não só na 07: ele é a peça que faz o exercício
ser respondível. A linha da 07 continua valendo — o destrave serve nos dois
lugares — mas quem escreve procura a peça nesta linha, e até 28/08 ela não
estava. O primeiro curso real nasceu sem destrave em nenhum exercício.
Aula sem arquivo para baixar, sem passo numerado e sem pedido pronto para
copiar vira "agora faça você" e ninguém faz. As três entregas de referência têm
as três, nas oito aulas: nenhuma exceção.

**Por que o modelo não mostra as 57.** Um modelo que mostra tudo deixa de ser
modelo e vira segunda vitrine, e o curso copiado dele sai carregado. O modelo
mostra a espinha; a vitrine mostra o acervo. Se você abriu só o modelo, você
viu um terço do padrão.

**A anatomia não é uma invenção deste padrão.** Ela é o GPS da seção 3, aberto em
oito passos:

| Seção | O que ela é, no GPS |
|---|---|
| 01 situação | **destino**, escrito pela essência que as cinco perguntas acharam |
| 02 conceito | o conceito, com o teto declarado no rótulo |
| 03 como funciona | a **imagem**. É a seção que responde "virou filme na cabeça?" |
| 04 demonstração | ver acontecer, antes de fazer |
| 05 sua vez | a **prática** daquele conceito, e ela fecha o ciclo antes do próximo |
| 06 confira | a revisão, para fixar |
| 07 pegadinhas | **origem**: os erros que quem parte daquele ponto comete |
| 08 a cerca | o **etos**: o que nunca pode acontecer neste nível |
| o gancho | o **hook** da próxima aula |

**Situação vem antes de conceito** porque a pessoa precisa se reconhecer no
problema antes de aceitar a explicação. A ordem andragógica é experiência →
pergunta → conceito, nunca conceito → ilustração. Inverter os dois é o erro mais
comum de material técnico.

### ⭐ O padrão de ouro da demonstração: a sala escreve a resposta

O passo a passo da demonstração é do aluno e vive na página (§5). **A condução é do
instrutor e vive no arquivo interno dele.** E existe um movimento que vale montar
sempre que der, porque é o que separa demonstração de exposição:

1. Mostre o resultado ruim e pergunte **"o que falta aqui?"**
2. Anote no quadro **com as palavras deles**
3. Minutos depois, mostre a solução boa: **"é o que vocês me disseram há cinco minutos, só que escrito antes"**

Deixa de ser você ensinando e vira eles descobrindo. Variações que funcionaram: um
formulário em branco que a sala preenche · uma tela de configuração vazia que a sala
dita e você só digita · uma classificação em voz alta com **um item ambíguo de
propósito**, onde a discordância é que leva ao conceito.

🔴 **Mostrar o resultado pronto entrega o conceito já resolvido.** O aluno assiste
mágica, e mágica não se aprende, se assiste.

E a demonstração **roda na mesma superfície que o aluno vai usar**. Ferramenta que ele
não tem vira mágica, e o instrutor não consegue dizer "agora façam igual", que é a
mecânica inteira.

🔴 **Isso não vai para a página.** Vai para o roteiro do instrutor, junto com o plano
B de cada momento. O material publicado leva o passo a passo; a pergunta que a sala
responde antes de você explicar é bastidor.

A aula fecha com **a checagem** (o aluno confere sozinho) e **o gancho** (a trava
que esta aula não resolve, e que abre a próxima). O gancho não é retórica: é o
que faz um curso ser uma corrente, e não uma lista de páginas.

---

## 5. Como se escreve aqui

**O material é para o aluno ler, não anotação do que o professor vai conduzir.**
Esta é a correção que o Rafael mais repetiu, em três projetos.

| Vocabulário proibido em página do aluno | Onde ele vive |
|---|---|
| "pergunte à sala", "espere o silêncio", "plano B", "o que apontar" | roteiro de palco, arquivo interno |
| duração de aula, minutagem por passo | grade de planejamento, arquivo interno |
| "verificado em DD/MM", "reconferido na semana da turma" | arquivo de fatos, interno |

🔴 **A lista acima não basta, e já falhou.** Depois de três reprovações e de um gate
com 19 frases proibidas, as quatro aulas continuavam escritas na primeira pessoa do
instrutor: *"Abro uma conversa"*, *"Mostro onde ficam as Instruções"*, *"Paro e
pergunto"*. O gate tinha `leia em voz alta`; o texto dizia **`leio` em voz alta**.
Passou.

> **A regra que substitui a lista: no bloco que narra a demonstração, verbo em
> primeira pessoa do singular reprova.** Quem opera o teclado não aparece. O que
> aparece é o que acontece na tela, e o passo dá ao aluno algo para fazer enquanto
> assiste (*"conte as mensagens"*, *"pare aqui e responda para você mesmo"*).

⚠️ **A correção inversa, igualmente importante:** *"vocês"* sozinho **não** é defeito.
*"O dia a dia de vocês"* trata a turma como profissionais, e é dos melhores trechos
que o material pode ter. O defeito é a turma como **plateia**: `pergunto para vocês`,
`na frente de vocês`, `vocês veem`. **Gate largo demais reprova o que era bom.**

**Duração** existe para o instrutor caber na grade, não para o aluno se sentir
atrasado: quem leva 40 minutos numa aula marcada como de 25 conclui que é lento.
**A data de verificação** só levanta a pergunta "então isso pode estar errado
agora?" sem dar o que fazer com ela. A fonte fica; o carimbo sai.

### Ganho, nunca conserto

Ao fechar o título e a seção 01, pergunte: **isto promete que ele vai parar de errar,
ou que ele vai passar a conseguir?**

Promessa de conserto pressupõe que a pessoa fez errado, e ela não sente isso. O mesmo
conteúdo técnico cabe nas duas molduras, e só uma delas o público adota.

E teste o título contra **a leitura errada mais provável** antes de escrever a aula em
cima dele. "A skill que aguenta o mês difícil" foi lido como duração, não como
dificuldade.

### Quem opera o teclado não aparece

🔴 **Verbo em primeira pessoa do singular reprova** no bloco que narra a demonstração.
Não aparece quem digita; aparece o que acontece na tela. E o passo dá ao aluno **algo
para fazer enquanto assiste** ("conte as mensagens", "pare aqui e responda para você
mesmo").

**Esta regra substitui a lista de palavras proibidas, que falha.** O gate tinha "leia em
voz alta" e o texto dizia **"leio** em voz alta". Passou. Pessoa gramatical pega; palavra
não. É o **G33**.

**A correção inversa importa igual:** "vocês" sozinho **não** é defeito. "O dia a dia de
vocês" trata a turma como profissionais, e é dos melhores trechos que ele já aprovou. O
defeito é a turma como **plateia**: "pergunto para vocês", "na frente de vocês".

### Dois públicos, dois artefatos

| Artefato | Quem abre | Fala de |
|---|---|---|
| proposta, deck de aprovação | gestão, patrocinador, quem contrata | ganho de negócio, processo, método, medição, condição de execução |
| material da sala | participante | o trabalho dele, o exercício, o que ele leva |

O conteúdo do dia não muda; **o argumento da proposta sim**. E o bloco "o que fica
deliberadamente de fora, e por quê" soa como censura para a sala e como **critério
editorial** para quem aprova: mesma informação, valor oposto conforme o leitor.

Mais regras de escrita, todas dele:

- 🔴 **Travessão proibido** em qualquer lugar, inclusive comentário de CSS. Vírgula,
  dois-pontos, ponto e frase nova, ou ponto médio `·`.
- **Frase que precisa ser explicada duas vezes é frase quebrada**, mesmo estando
  certa.
- **Não devolva premissa que o cliente mesmo deu.** Justificar o recorte dele é ruído.
- **Título é nome, não tese.**
- **Promessa de ganho vende, promessa de conserto não.** Ver acima.
- **Número não é critério, é consequência do critério.** Ver abaixo.
- **Nome de outro cliente nunca entra.** Papel e persona de prompt vão anonimizados.

### Número não é critério, e o primeiro exemplo real vai te contradizer

Uma aula dizia *"tamanho certo: 20 a 40 linhas"*. A página de exemplo, **a um clique
dali**, mostrava um arquivo real de **128 linhas** funcionando bem. Rafael achou em
trinta segundos.

**Número é fácil de escrever e fácil de conferir, e é por isso que ele entra sozinho
no texto.** Mas o que decide quase nunca é a quantidade:

| O número dizia | O critério de verdade |
|---|---|
| "20 a 40 linhas" | "toda linha vale em **toda** conversa" |
| "poucos arquivos" | são os arquivos **parecidos entre si** que atrapalham |
| "cabe em uma página" | "isso vale sempre, ou só quando eu peço uma tarefa específica?" |

**O número não some, muda de estatuto:** vira andaime declarado do primeiro exercício
(*"nesta primeira, fique entre 20 e 40"*), com o porquê de cada extremo. Andaime dito
como andaime ajuda; andaime dito como regra vira mentira no primeiro caso real.

**O teste:** ao escrever qualquer critério com número, pergunte *"existe um caso bom
que viola isto?"*. Se existe, é andaime e vem rotulado.

> ⚠️ **Nem todo número deste template é andaime.** O piso de 100 linhas do insumo e o
> teto de dois conceitos por aula são pedidos diretos dele, e a §11 e a §3 explicam o
> porquê de cada um. A distinção é essa: **número com o mecanismo explicado ao lado é
> critério; número solto é andaime disfarçado.**

> 🔢 E **todo número anunciado precisa de um gate que reconte.** Um validador prometia
> *"quatro conferências"* e a lista tinha cinco, porque uma leva anterior acrescentou
> item e ninguém releu o texto de cima.

### Como a promessa é escrita: quatro padrões

O objetivo é que um coordenador abra a página e reconheça **a própria rotina**, não
uma lista de recursos. Rafael pediu isto depois de analisar como um concorrente
comunica as mesmas funcionalidades:

> *"O ponto aqui é a linguagem para a empresa sentir que está usando o Claude para
> negócios. Eu acho que a pessoa da empresa vai entender a minha rotina, a minha
> atividade, o meu contexto."*

| | O padrão | O que obriga |
|---|---|---|
| **P1** | Todo nome carrega **a rotina e o nome oficial do recurso** | `[o que muda na sua rotina]` com o nome oficial visível ao lado. Só a rotina, e a pessoa não sabe o que aprendeu nem consegue pesquisar depois. Só o nome oficial, e ela não sabe para que serve |
| **P2** | Toda promessa tem **hora marcada** | *"toda segunda o painel reabre atualizado"*, não *"você aprende a criar painéis"*. Capacidade abstrata não gruda; batida de calendário gruda |
| **P3** | 🔴 Nomeia-se **a espera, nunca a pessoa** | *"você deixa de esperar o relatório de terça"*, **nunca** *"você não precisa mais do analista"* |
| **P4** | Diz-se **o que o material não faz**, em bloco visível | Filtra a expectativa errada e diz ao gestor que ele é o protagonista, não o convidado que veio assistir a um curso de TI |

🔴 **O P3 é regra de segurança, não de estilo.** Curso vendido a indivíduo pode ser
cru (*"sem designer na fila"*). Material **in-company não pode: as pessoas dessa fila
estão na sala.** Mesmo mecanismo, sujeito diferente:

| Escreva | ❌ Nunca escreva |
|---|---|
| Você deixa de esperar o relatório de terça | Você não precisa mais do analista |
| A montagem manual sai do seu caminho | Substitui o trabalho do assistente |
| O dado chega pronto para a sua decisão | Corta a etapa do time de apoio |

**A espera é o vilão. A pessoa nunca é.**

**Sobre o P1, e a ressalva que ele fez questão de deixar clara:** isto é troca de
**rótulo**, não de método. *"Não quero deixar de pegar os princípios andragógicos."* O
esqueleto da §3 e da §4 fica intacto. O vocabulário interno do projeto (os nomes que
você inventou para organizar as aulas) vira **comentário HTML**, nunca texto visível.

> ⚠️ **Ao mecanizar, confira a lista aprovada, não cace palavra proibida.** Verbos como
> *alcançar* e *delegar* aparecem em prosa legítima, e um gate que os caça gera falso
> positivo. Gate com exceção deixa de ser gate.

---

## 6. O padrão é piso, não jaula

Rafael foi explícito em 20/08: o Claude **pode e deve adaptar** o padrão de um exemplo
para outro, como o IC-B fez, **até criar diagrama novo quando o assunto
pedir**. Material que sai igual em toda página vira formulário preenchido, e ninguém
lê formulário.

O que separa adaptação de bagunça é saber o que é osso e o que é músculo:

| Não muda, nunca | Muda a cada exemplo |
|---|---|
| a anatomia de 8 seções da aula | a figura de cada seção |
| os 5 passos da página de caso, com os mesmos títulos | o diagrama, o desenho, a metáfora |
| as regras de escrita | o exemplo concreto, o setor, o número |
| as duas larguras e a quebra de linha | o componente novo, quando nenhum dos 20 serve |
| a cor vindo do `marca.css` | como os componentes se compõem na página |

**Componente novo nasce como classe no `base.css`, com `var()` e nada mais.** Nunca
como `style=` com cor no meio do HTML: é assim que um curso deixa de trocar de cliente
trocando um arquivo. Se você precisou de uma cor que não existe, o que falta é um token
no `marca.css`, não um hex no HTML.

### 🔁 "Padrão" na boca dele é o padrão do módulo, não estética

Ele olhou um exercício e disse: *"gostei, mas acho que o tópico 5 não tá no mesmo
padrão"*. Eu li **ritmo visual** e reescrevi o layout. Ele teve que explicar de novo:
*"eu falei muito no sentido de ter o padrão, exemplos, não ser o docx, essas coisas."*

Ele falava do **padrão que as aulas irmãs já tinham**: quadro preenchível na página em
vez de `.docx` para baixar, e página de exemplo com o artefato pronto. Aquela aula era
a única do módulo sem os dois.

> **Feedback curto sobre um artefato dele quase nunca é sobre a aparência daquele
> bloco. É sobre ele destoar dos irmãos.**

**O que fazer antes de agir:** monte a tabela `página × atributo` das páginas da mesma
família e ache quem está fora. Leva dois comandos e evita uma rodada inteira gasta no
defeito errado.

E antes de inventar: **abra a vitrine**. São 57 peças, e a chance de já
existir o que você quer é alta. Inventar o que já existe custa duas vezes: o trabalho
de criar, e a inconsistência de ter dois jeitos de mostrar a mesma coisa.

---

## 7. Sempre que der para desenhar, desenhe

**Nenhuma seção passa de dois parágrafos seguidos sem uma figura, uma tabela ou
um bloco estruturado.** Lista numerada de cinco itens em prosa é texto corrido
disfarçado. **Piso de três figuras por aula**: se tiver menos, a aula está
explicando com palavra o que dava para mostrar.

- **HTML e CSS puro.** Sem biblioteca de gráfico, sem imagem externa. A página
  abre sem servidor, de um pen drive, na sala do cliente.
- **Toda figura leva uma frase de leitura embaixo** (`.fig-leg`) dizendo o que a
  pessoa deveria ter reparado. Figura sem legenda vira enfeite.
- **Reaproveite o componente antes de inventar um novo.** A vitrine em
  `/componentes/` mostra todos, com o nome da classe.
- **Desenhe a ferramenta, não printe** (`.tela`). Print envelhece na primeira
  atualização do produto e sai borrado no projetor.
- `aria-hidden="true"` em seta e enfeite.

Figura que mostra só o lado bom de uma escolha não é figura, é propaganda: os
`.vereditos` sempre trazem a linha do custo.

---

## 8. Como o diagrama nasce

🔴 **Antes de desenhar qualquer figura, carregue a skill `diagram-design`.** Sempre.
Ela traz 28 tipos de visual e os padrões semânticos por trás deles, e **a escolha do
tipo é a decisão que mais muda a figura**: um processo desenhado como cadeia e um
processo desenhado como raia contam histórias diferentes com o mesmo conteúdo.

Rafael pediu isso com todas as letras em 20/08, junto com a mesma liberdade para os
artefatos: **criar sempre que ajudar a pessoa a aprender.**

### Pegue o cérebro, deixe a pele

A `diagram-design` vem com um sistema visual próprio: fontes Instrument Serif e Geist,
laranja de destaque, papel cinza claro, fundo pontilhado. **Nada disso entra aqui.**
A cor sai do `marca.css`, a fonte sai do `marca.css`, e um gate reprova cor escrita
fora dele. O que entra é o raciocínio.

| Vale de lá, sempre | Não vale de lá, nunca |
|---|---|
| a escolha do tipo entre os 28 | a paleta e as fontes |
| o orçamento de complexidade | o fundo pontilhado |
| as regras de conector e rótulo | gerar arquivo HTML separado |
| os anti-padrões de composição | o marcador `.diagram-design` e os perfis |

O diagrama aqui é **bloco dentro da página da aula**, em HTML e CSS puro, com os
tokens do cliente. A página tem de abrir de um pen drive, sem servidor, na sala.

### O que vale literalmente, e que já poupou figura ruim

- **A melhor jogada costuma ser apagar.** Dois nós que sempre andam juntos são um nó
  só. Se a relação já é óbvia pelo layout, tire a linha.
- **Alvo de densidade: 4 de 10.** Acima de nove nós, provavelmente são dois diagramas.
- **Destaque é editorial: um ou dois nós por figura**, no `--accent`. Cinco nós em
  destaque apagam o sinal e a figura volta a ser uma pilha de caixas.
- **Conector em ângulo reto arredondado, nunca diagonal.** Diagonal entre caixas fora
  do mesmo eixo é reprovação automática lá, e fica igual de feio aqui.
- **Rótulo de seta com folga de 6 a 10px da linha**, e com máscara atrás, senão a
  linha atravessa o texto.
- **Conector não passa por trás de caixa que não é ponta dele**, e dois conectores
  nunca se sobrepõem: cada seta tem de ser rastreável sozinha.
- **Se uma tabela de três colunas diz a mesma coisa, escolha a tabela.**
- **Diga o tipo antes de desenhar.** Uma frase: que tipo, por quê, e o que fica de
  fora por causa do orçamento.

### A ponte: o que já é classe aqui

| Tipo na `diagram-design` | A classe do padrão |
|---|---|
| Process · fluxo com atores | `.fluxo` + `.fl-ator` |
| Sequence · cadeia de etapas | `.cadeia` + `.no` |
| Loop · ciclo que se realimenta | `.loops` (aberto × fechado) · `.ciclo` (um ciclo, com a volta) |
| Data flow · o que volta e alimenta | `.retorno` |
| Fan-in · vários caminhos, uma exigência | `.converge` |
| Swimlane · o trabalho atravessa áreas | `.raias` |
| Quadrant · duas perguntas | `.matriz` · `.priorizar` |
| Scatter · duas medidas contínuas | `.dispersao` |
| Radar · o mesmo item em várias frentes | `.radar` |
| Flowchart · decisão | `.decide` |
| Bar chart | `.barra` (segmentada) · `.colunas` (em pé, por etapa) |
| Funnel · o que aperta até a decisão | `.cascata` |
| Part-of-whole · proporção que se conta | `.cem` |
| Treemap · o tamanho é o argumento | `.mapa-area` |
| Layer stack · níveis | `.escada` |
| Timeline · eventos em ordem | `.linha-tempo` |
| Gantt · o que anda junto | `.gantt` |
| Tree · isto se divide em | `.arvore` |
| Org chart · onde a decisão para | `.organograma` |
| Nested · o que está dentro do quê | `.aninhado` |
| Venn · o encontro de dois conjuntos | `.venn` |
| Comparação lado a lado | `.contraste` · `.antes-depois` · `.demo` |
| Diagnóstico · o que quebrou e por quê | `.diagnostico` |

**O que ficou de fora, e por quê.** Os tipos que a `diagram-design` traz e que não
viraram classe são de software e engenharia de dados: architecture, IT current-state,
state machine, ER, high-level, medallion, DP integration e DP security matrix. Se um
curso para gestor precisar de um deles, o problema provavelmente não é a figura, é o
recorte da aula. **A exceção é o gráfico de linha**: ele serve, e nasce no dia em que
um curso tiver série temporal de verdade para mostrar.

### Três desenhos são montados pelo gerador, não escritos à mão

| Classe | O que o fragmento declara | Por quê |
|---|---|---|
| `.cem` | `data-acesos="12"` | os cem quadrados à mão é onde a legenda desencontra do desenho |
| `.radar` | `data-eixos` e `data-valores` | ninguém confere polígono com transferidor |
| a cola de quebra de linha | nada | o espaço rígido some se alguém editar o HTML publicado |

🔴 **O `<svg>` recorta o que passa da moldura, e recortar é o comportamento normal
dele.** O rótulo simplesmente some: sem erro, sem console, sem nada torto na página.
Por isso o gerador calcula a moldura do radar a partir da largura dos próprios
rótulos, e o **G29** confere que nenhum texto sai dela.

🔴 **Grade com número variável de colunas usa `minmax(0,1fr)`, nunca `1fr` puro.**
`1fr` não encolhe abaixo da palavra mais comprida, e um rótulo de gráfico estica a
faixa inteira até a página rolar de lado no celular. Custou 101px de rolagem na
vitrine, com todos os outros gates passando. Virou o **G27**.

🔴 **Quando o desenho não cabe no celular, ele rola dentro do próprio envelope.**
Espremer sete colunas em 375px deixa rótulo de quarenta pixels, ilegível de qualquer
jeito. Fazem isso: `.tabela`, `.colunas`, `.raias` e `.gantt`.

### As travas que não mudam

Toda figura leva `.fig-leg` embaixo dizendo o que a pessoa deveria ter reparado.
Figura sem legenda é enfeite. Piso de três figuras por aula. E figura de escolha mostra
o custo dos dois lados: só o lado bom não é figura, é propaganda.

---

## 9. A largura, e a frase que não pode quebrar no meio

A página tem **duas larguras, e só duas**: `--col` (780px) para prosa, e
`--col-larga` (1140px) para o que estoura. Componente que estoura leva a classe
`.solta`. Prosa **não tem largura própria**: a coluna já é a medida.

🔴 **Três jeitos de partir uma frase sem perceber**, os três já aconteceram:

1. **`display:block` num seletor de tag inline.** `.bloco strong{display:block}`
   pega todo `<strong>`, inclusive o do meio de uma frase. Rótulo ganha a classe
   `.rot`, nunca um seletor de tag.
2. **`display:flex` no pai**, com texto solto e tag inline como irmãos.
3. **`text-wrap:balance` ou `:pretty` na prosa.** Os dois reservam espaço no fim
   da linha para equilibrar o bloco. **No padrão, `text-wrap` existe só em
   `h1..h4`.**

### As três quebras ruins são três defeitos diferentes, com três curas

🔴 **Rafael reclamou disso quatro vezes, e nas duas primeiras eu consertei o
defeito errado.** Elas se parecem na tela e não têm nada a ver uma com a outra:

| O que incomoda | A causa | A cura |
|---|---|---|
| A linha termina em **"na sua"** e joga **"área."** para baixo | artigo ou preposição separado do substantivo | a **cola de espaço rígido** do `gerar.py`, que muda ONDE a linha quebra sem abrir folga |
| A linha quebra **do nada, com folga à direita** | `text-wrap` reservando espaço para equilibrar o bloco | `text-wrap` só em `h1..h4` |
| 🔴 **A frase quebra e ainda sobra coluna** | a frase **começou no meio da linha**, no resto que a anterior deixou | **uma frase por linha** |

**A terceira é a que ele reclamou mais vezes, e é a menos óbvia.** Medido no
IC-C: **283 de 491 frases** quebravam no meio, e a frase mediana ocupava
**497px numa medida de 720px**. Três de cada quatro já cabiam inteiras numa linha
e quebravam mesmo assim, porque começavam no resto da anterior.

> *"Era sobrar o espaço para continuar a frase e vc quebrar ela. Eu gosto dos
> bullet points, mas tem pontos que poderiam ficar em uma única frase e vc quebra
> ela."*

🔴 **Alargar a coluna é a saída errada.** De 720 para 920 resolve 13% e produz 122
caracteres por linha, que ninguém lê. A saída é **uma frase por linha**, decidida
por largura de bloco, e o visual que sai é o que ele chama de "bullet points".

**Isso já está implementado, e é opt-in:** escreva **`.fr-host`** no bloco, do mesmo
jeito que quem estoura a coluna escreve `.solta`. O `gerar.py` envolve cada frase num
`<span class="fr">` e o `base.css` decide por **container query**: quem manda é a
largura **do bloco**, não a da janela. O mesmo parágrafo dentro de um cartão estreito
continua prosa corrida; dentro da coluna larga, cada frase ganha a sua linha.

> ⚠️ **É marcação explícita de propósito.** Detectar sozinho exigiria caminhar a árvore
> inteira do HTML, e aqui marcação explícita ganha de adivinhação. **Se você escreveu
> um bloco de prosa que ele vai ler na sala e não pôs `.fr-host`, o efeito não
> acontece**, e nenhum gate reclama: é escolha, não defeito.

**Medido, não estimado.** Cola de espaço rígido no IC-C, 437 linhas de
prosa: 192 quebras órfãs sem ela, 8 com ela, 0 quebras precoces sem o `text-wrap`.
E a medida só vale se ela souber reprovar: desfaça a correção no DOM vivo e
confirme que o número sobe.

> ⚠️ **Se ele reclamar duas vezes da mesma coisa e a sua correção "resolveu"
> segundo a sua própria métrica, a métrica está errada, não a execução.** Pergunte
> o que exatamente incomoda, ou meça o que o print mostra, em vez do que você supõe.

> 🔴 **A página menos auditada costuma ser a mais usada.** No IC-C o canvas,
> que é o que a turma abre no celular, tinha 13 quebras ruins em 375px contra 3 no
> site. Ele é a exceção do gerador, e por isso ninguém o mede.

---

## 10. O exercício

O arquivo que ele baixa tem seção própria, a 11. Aqui é o exercício em si.

- **Só pede o que o aluno já tem naquele ponto do curso.** Se o conceito precisa de
  ferramenta que ele ainda não instalou, vai para a demonstração na tela do instrutor.
  É a **origem** do GPS aplicada ao exercício: quem não sabe de onde a pessoa parte,
  pede o que ela não tem.
- **Um exercício por conceito**, e ele fecha o ciclo antes do conceito seguinte
  começar. Dois conceitos e um exercício só deixa a pessoa sem saber qual dos dois ela
  não entendeu.
- **O gabarito não é resposta certa única.** Vem sempre com "o seu vai ser diferente
  do meu, e tudo bem. Compare a estrutura, não o conteúdo". Sem isso, gestor
  não-técnico trava achando que errou.
- **O exercício leva a pessoa do segundo ao terceiro nível**, de "sabe que não sabe"
  para "sabe fazendo força". O quarto nível, fazer sem pensar, é repetição no trabalho,
  e prometer isso na sala é prometer o que não se entrega.

### ⚙️ Toda promessa operacional precisa fechar na prática

O material dizia, em três versões seguidas: *"régua de maturidade aplicada
individualmente, com o consolidado da turma lido na hora"*. Ele perguntou: **"na
descrição diz que eles vão fazer isso manual. Como é que ele vai dar esse resultado
lá na hora?"**

Não existia resposta. Papel preenchido por 40 pessoas não vira consolidado em cinco
minutos sem alguém tabulando, e ninguém ia tabular.

> **Toda frase que promete algo acontecendo em sala responde três perguntas antes de
> entrar no material: quem faz · com o quê · em quanto tempo, com o número real de
> pessoas.** Se qualquer uma ficar sem resposta, ou a frase muda ou o mecanismo muda.

**E a saída boa quase nunca é enfraquecer a promessa.** Ali virou um canvas de celular
que gera uma linha de planilha, cada um cola numa planilha projetada, e a análise ao
vivo deixou de ser tabulação e virou **a primeira demonstração do dia**, com dado que
a sala acabou de gerar sobre ela mesma.

É o mesmo erro da regra do exercício, aplicado à condução: eu escrevi olhando para o
**desenho pedagógico** e não para a **execução**.

---

## 11. O insumo: o arquivo que o aluno baixa

Todo caso tem um arquivo de partida. Ele parece detalhe e é onde o exercício quebra na
sala, porque **o prompt da página cita colunas que precisam existir no arquivo**, e as
duas coisas nascem em momentos diferentes.

### A especificação, e ela não é negociável

| Regra | Por quê |
|---|---|
| **`.xlsx` ou `.docx`**, nunca `.csv` nem `.txt` | são os formatos que a sala usa no trabalho. `.csv` abre torto no Excel em português e a aula vira suporte técnico |
| **Piso de 100 linhas**, 120 é melhor | em 15 linhas alguém pensa "isso eu fazia na mão em dez minutos" e a demonstração perde o argumento |
| **Mais de uma armadilha**, declaradas | planilha limpa não ensina nada: o trabalho real é sujo |
| **Aviso de dados fictícios**, dentro do arquivo | sem ele alguém pergunta se é dado de cliente, e a pergunta atrapalha a aula |
| **Nenhum dado real de nenhum cliente** | nem anonimizado. Nome de empresa, valor de contrato e volume saem |
| **Uma aba de leitura**, com o que cada coluna significa | a pessoa volta ao arquivo semanas depois, sem o instrutor do lado |

### As armadilhas, e o que cada uma ensina

A sujeira é **de propósito** e cada uma existe para provocar um erro específico:

| A armadilha | O que ela ensina quando a pessoa cai |
|---|---|
| data em dois formatos (`03/08/2026` e `2026-08-03`) | que a IA vai ordenar errado sem avisar |
| o mesmo nome escrito de dois jeitos ("Loja Centro" e "centro") | que juntar por semelhança é decisão, não detalhe. É a origem do parágrafo "Na dúvida" do prompt |
| cabeçalho mesclado ou linha em branco antes do cabeçalho | que o arquivo precisa ser olhado antes de ser usado |
| coluna com espaço no nome (`" Valor"`) | que o nome que ela vê não é o nome que a ferramenta lê |
| número como texto, com vírgula decimal | que soma que não soma tem causa, e a causa é achável |
| uma linha duplicada, e só uma | que conferir o total contra a soma é barato |
| um valor faltando no meio | que o buraco tem de ser declarado, nunca estimado em silêncio |

🔴 **Toda armadilha do arquivo aparece em algum lugar do material.** No prompt, no
gabarito ou nas pegadinhas. Armadilha que ninguém explica depois não é pedagogia, é
pegadinha de prova.

### O acoplamento que quebra em silêncio

O prompt do passo 4 cita as colunas. Se o arquivo mudar e o prompt não, **o aluno cola
o prompt e a IA responde sobre uma coluna que não existe**. Nada falha: a resposta sai
plausível e errada, na frente da sala.

Escreva o insumo e o prompt **na mesma leva**, e confira o par antes de fechar.

### O gerador

```bash
python3 _build/insumo.py
```

A especificação mora no topo do `_build/insumo.py`: colunas, volume, e **as armadilhas
declaradas por nome**. Ele grava o `.xlsx` em `_arquivos/`, escreve o
`_build/insumos.json`, e imprime **o que cada armadilha ensina**, porque esse texto
precisa reaparecer no material.

**Semente fixa, sempre.** Sem ela cada execução gera uma planilha diferente, a turma
recebe arquivos que não batem entre si, e o gabarito deixa de valer.

O **G32** confere o par página × arquivo, e pega quatro coisas: arquivo oferecido que
sumiu do disco, número de linhas inventado, número de abas errado, e coluna citada no
prompt que não existe em aba nenhuma.

🔶 **O `.docx` ainda não tem gerador.** A especificação acima vale para ele; o código
nasce quando um curso precisar.

---

## 12. O bloco "o mesmo conceito, no seu setor"

Accordion por setor, todos fechados ao abrir. Anatomia fixa de quatro partes:

1. **O pedido pela tarefa** · a fala real, curta, entre aspas
2. **O que falta** · as perguntas que aquela fala deixa em aberto
3. **O pedido pelo resultado** · o prompt pronto, com botão de copiar
4. **O que muda na resposta** · a consequência, com número quando existe

🔴 **Sem a quarta parte o bloco vira banco de prompts**, e banco de prompts
ninguém abre depois do dia do treinamento.

O prompt tem **quatro parágrafos, sempre nesta ordem**, e é isso que o aluno leva
como método: `Anexei ...` · `O que eu preciso:` · `Restrições:` · `Na dúvida:`.
O quarto é o que transforma pedido em procedimento: sem ele o modelo preenche
buraco por estimativa e ninguém percebe.

---

## 13. A página de caso, em cinco passos

Vem do IC-B, e é a peça que o Rafael chamou de maior ganho daquele
material. Toda página de caso tem os **mesmos cinco passos**, na mesma ordem,
com os mesmos títulos. Conferido nas oito páginas de lá: nenhuma variação.

| # | O título, literal | O que entra |
|---|---|---|
| 01 | Descreva a tarefa | o problema real e quem enfrenta na rotina |
| 02 | Dê o contexto que a IA precisa | o que ela precisa para não devolver algo genérico |
| 03 | Baixe o insumo | o `.xlsx` ou `.docx`, com dados fictícios |
| 04 | Cole o prompt no chat | prompt pronto, testado, com os dados embutidos |
| 05 | **O que esperar** | a **prévia do resultado**, antes de rodar |

🔴 **O passo 5 é o que separa este material de uma lista de prompts.** Sem ele a
pessoa roda o prompt sem saber o que deveria sair, e qualquer resposta parece
certa. Com ele, ela compara.

A prévia tem duas colunas: à esquerda uma **miniatura desenhada** do artefato
(título, metadado, três números, a figura de dentro), à direita **o que vem
dentro dele**, em bullets. A miniatura não é o artefato de verdade: ela mostra a
forma da resposta em cinco segundos de olhada.

E o passo 5 fecha com o callout **"depois de gerar · como refinar"**, com as
falas literais que a pessoa usa para melhorar o resultado. É o que evita a
desistência em casa, na primeira resposta ruim.

**Por que oito casos e não um exercício:** numa sala de quarenta pessoas de áreas
diferentes, um exercício só não serve. A grade de casos deixa cada um escolher o
seu, e por isso a descrição segue a fórmula **entrada vira saída**, numa frase:
*"4 semanas de fechamento de 12 lojas viram um relatório de uma página."* Sem a
entrada a pessoa não sabe se tem o material; sem a saída não sabe se quer. O
rodapé do card diz o **tipo** do que ela vai ter na mão.

**O insumo leva sempre o aviso de dados fictícios**, dizendo o que é real e o que
foi inventado. Sem ele, alguém da sala pergunta se aquilo é dado de cliente, e a
pergunta atrapalha a aula.

---

## 14. Como fazer a pessoa decidir sozinha

Todo curso chega numa hora em que a pessoa pergunta *"então eu uso qual?"*.
Responder com uma lista de vantagens não resolve. Duas estruturas resolvem:

| Estrutura | Quando usar | Regra |
|---|---|---|
| **Matriz 2×2** (`.matriz`) | quando a escolha depende de duas perguntas | uma célula leva o selo **comece aqui**. Matriz sem recomendação deixa a pessoa onde ela estava |
| **Tabela de decisão** (`.decide`) | quando são 3 a 5 perguntas independentes | a resposta de cada lado começa com **Sim** ou **Não** em negrito |

E toda figura de escolha mostra **o custo dos dois lados**. Figura que só mostra
o lado bom de uma opção não é figura, é propaganda.

---

## 15. As três peças que o aluno opera

A vitrine tem 57 componentes, e 54 deles são para ler. Três não:

| Peça | Classe | A regra que não pode cair |
|---|---|---|
| **Criador de prompt** | `.criador` | nasce **preenchido** com um caso plausível |
| **Canvas** | `.canvas` | `data-chave` própria, e o aviso de "neste aparelho" |
| **Exemplo pronto** | `.doc` | o que é do site leva `.so-tela` e some na impressão |

**O criador nasce preenchido de propósito.** Ferramenta que abre vazia é formulário,
e formulário vazio numa sala de treinamento faz a pessoa olhar para o lado antes de
digitar. Preenchida, ela troca o texto de um campo e entende o mecanismo pelo que
muda do outro lado. Os seis campos são sempre os mesmos, nesta ordem, e é isso que o
aluno leva como método: **papel · contexto · tarefa · formato · limitações · critério
de sucesso**.

**O canvas guarda no aparelho e diz isso na tela.** Sem o aviso, quem fecha a aba acha
que perdeu, e quem não fecha acha que mandou para alguém. Quatro coisas que já
custaram caro faltar: o número em chip (para achar de novo o campo que o instrutor
citou), o "Ex:" em cinza **acima** da caixa (dentro dela é placeholder, e some
justamente quando ela precisa), o indicador que só acende depois de salvar de verdade,
e o botão que copia a linha inteira para a planilha da turma.

🔴 **O botão da linha exporta TAB entre campos e troca quebra de linha por ponto
médio.** Sem isso, um campo de duas linhas vira duas linhas na planilha e desalinha a
turma inteira.

**O exemplo pronto mora em página própria.** No meio da aula ele compete com o
conceito e vira ilustração; em página própria vira entregável, e a pessoa consegue
mandar o link para o chefe. O link para ele fica no fim da página de caso, depois do
passo 5, nunca antes: quem vê o resultado pronto antes de tentar não tenta.

---

## 16. Armadilhas já pagas neste template

**Hex de 8 dígitos dentro de SVG não renderiza.** `fill="#26262322"` é CSS válido,
o XML abre sem erro, o servidor entrega HTTP 200 com o content-type certo, e o
console fica limpo. A imagem simplesmente não aparece. Use 6 dígitos e resolva a
transparência com `opacity`.

**`loading="lazy"` numa imagem que precisa aparecer sempre.** Ela só carrega
quando entra no campo de visão. Em página que vai ser impressa, exportada em PDF
ou publicada como artefato de uma página só, tire o `lazy`.

**Imagem local não vai junto num artefato.** Artefato é uma página só. Quando
publicar uma página do site como artefato, embuta a imagem como `data:` URI.

🔴 **A casca do gerador tem de ser uma string CRUA (`r"""`).** Ela é uma string de
Python, e o JavaScript dentro dela usa `\n` e `\t`. Sem o `r`, o Python converte os
dois em quebra de linha e tabulação de verdade, e o script publicado morre na primeira
linha com "Invalid or unexpected token". A página abre normal, o layout fica perfeito,
todas as classes têm CSS, todos os links resolvem, e o criador de prompt simplesmente
não faz nada quando alguém digita. **Nenhum outro gate pega isso**, e por isso existe
o G21.

**Peça com JavaScript pede teste FUNCIONAL.** Ler o código não prova. Abra no
navegador, digite, clique, recarregue com uma query diferente na URL (o navegador
restaura formulário sozinho no reload, e isso faz um canvas quebrado parecer que
salvou).

**Viewport de largura zero mente sobre o layout.** Se a medição no navegador
acusar rolagem lateral e altura absurda ao mesmo tempo, confira
`window.innerWidth` antes de sair caçando o CSS: o painel pode estar oculto, e aí
todo número que ele der é lixo.

---

## 17. Gates

Auditoria de leitura não substitui gate mecânico. Toda leva fecha com
`python3 _build/gates.py`, que sai com código 1 se algo falhar.

**Gate com exceção permanente deixa de ser gate.** Se um gate acusa, conserta o
código. E gate que procura uma palavra não pode rodar contra o arquivo que
enuncia a regra sobre ela, senão se auto-reprova.

**Exit code sozinho nunca é prova.** Leia a saída: ela imprime achado por gate e
diz quais gates não se provaram contra o próprio defeito injetado.

São **41 gates**, em cinco famílias: escrita (travessão, vocabulário de bastidor,
direção de cena, duração fora da capa, os quatro parágrafos do prompt), estrutura
(classe sem CSS, link, imagem, gabarito, botão de copiar, numeração, seção completa,
tabela no envelope), quebra de linha (a cola aplicada, `text-wrap` só em título),
marca (cor só no `marca.css`, hex de 8 dígitos em SVG) e as peças que o aluno opera
(criador, canvas, exemplo, script vivo).

**Dois gates só valem porque a vitrine é exceção declarada:** ela é o único arquivo
que ENUNCIA as regras em vez de obedecer a elas, e cita "pergunte à sala" justamente
para dizer que isso é proibido. A exceção é estrutural, não caso a caso, e cai no dia
em que a vitrine for para uma turma.

---

## O que falta

| O que | De onde vem | Estado |
|---|---|---|
| Anatomia de aula, 8 seções | IC-A | ✅ no template |
| Página de caso, 5 passos, com prévia | IC-B | ✅ no template |
| Grade de casos, matriz, tabela de decisão | IC-B | ✅ no template |
| Cura da quebra de linha + cola de espaço rígido | IC-C | ✅ no template |
| Cartão de vídeo, matriz esforço × impacto, tela com campos | os três cursos | ✅ no template |
| Demonstração A/B, anatomia de arquivo, três opções | IC-A | ✅ no template |
| Antes e depois, cadeia de nós | IC-B | ✅ no template |
| Criador de prompt, ferramenta viva de 6 campos | IC-B, M1 §09 | ✅ no template |
| Canvas preenchível com rascunho salvo | IC-B M5 · IC-C | ✅ no template |
| Página de exemplo pronto, com CSS de impressão | IC-A, `m1/a1/exemplo/` | ✅ no template |
| Capa modelo, com as aulas e a grade de casos | os três cursos | ✅ no template |
| `gates.py` · 41 gates, todos calibrados | IC-C + 4 novos + 5 do piloto IEL | ✅ no template |
| Skill `criar-treinamento` que dita o processo | `~/.claude/skills/` | ✅ instalada |
| **23 tipos de diagrama**, com classe e regra própria | os 12 prints + os 28 tipos da `diagram-design` | ✅ no template |
| A regra do diagrama, com a ponte para a `diagram-design` | pedido dele, 20/08 | ✅ seção 7 |
| **Os 4 padrões de linguagem (P1 a P4)** | IC-A, 07/08 | ✅ seção 5 |
| **Pessoa gramatical no lugar da lista de palavras** | IC-A, 07/08 | ✅ seção 5 |
| **Número é andaime, não critério** | IC-A, 07/08 | ✅ seção 5 |
| **Promessa de ganho, não de conserto** | IC-A, 17/08 | ✅ seção 5 |
| **O padrão de ouro da demonstração** | IC-A, 07/08 | ✅ seção 4 |
| **"Padrão" é o padrão do módulo** | IC-A, 08/08 | ✅ seção 6 |
| **Promessa operacional fecha na prática** | IC-C, 17/08 | ✅ seção 10 |
| **As três quebras de linha, com a cura de cada** | IC-C, 4 reclamações | ✅ seção 9 |
| **Proposta de aprovação não é material de sala** | IC-C, 17/08 | ✅ seção 5 |
