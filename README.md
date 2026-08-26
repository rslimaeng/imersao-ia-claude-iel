# Imersão em IA com Claude

Material de apoio do treinamento in-company **Imersão em IA com Claude, do zero à
produtividade total**, conduzido por Rafael Lima.

16 horas-aula, quatro encontros, quintas à noite: 27/08, 03/09, 10/09 e 17/09 de 2026.

**O site é este repositório**, publicado em GitHub Pages. Ele é o material que fica
depois do curso: navegável, e não um PDF que ninguém reabre.

## Como o site é gerado

O conteúdo mora em `_build/conteudo/<slug>.html`, em fragmentos sem casca. O gerador
monta a página em volta, inlineia o CSS e grava.

```bash
python3 _build/gerar.py     # monta as páginas
python3 _build/gates.py     # reprova o que quebrou
```

Editar um `index.html` gerado é trabalho perdido: a próxima execução apaga.

## Dados

Todo insumo e todo exemplo pertencem ao **Instituto Farol**, uma casa fictícia criada
para este curso. Nenhum dado real de nenhuma organização entra aqui.
