# `<oh-my-harness />`

> A IA já escreve o código. O que falta é o harness que a faz escrever o código certo.

[![Licença: MIT](https://img.shields.io/badge/licen%C3%A7a-MIT-F7DF1E.svg)](LICENSE)
[![Check site](https://github.com/deMGoncalves/oh-my-harness/actions/workflows/check-site.yml/badge.svg)](https://github.com/deMGoncalves/oh-my-harness/actions/workflows/check-site.yml)
[![PRs bem-vindos](https://img.shields.io/badge/PRs-bem--vindos-18181B.svg)](CONTRIBUTING.md)

**[Ver o site →](https://demgoncalves.github.io/oh-my-harness/)**

by **deMGoncalves** — um harness para o [Claude Code](https://claude.com/claude-code): o
`.claude/` que transforma um agente de IA num time com ofícios, regras e ritmo, dentro de
um fluxo de **Spec-Driven Development**.

Este repositório tem duas partes:

| Parte | O que é |
| ----- | ------- |
| [`.claude/`](.claude/) | O harness em si — rules, skills, agents, commands e um hook |
| [`docs/`](docs/) | O site que apresenta e defende a ideia, com as fontes de cada número |
| [`design/`](design/) | O protótipo de design de onde o site saiu (`prototipo.html`, arquivo único) — não é publicado |

## Usar o harness no seu projeto

O `.claude/` é só uma pasta: copie-a para a raiz do seu repositório e abra o Claude Code ali.

```bash
git clone https://github.com/deMGoncalves/oh-my-harness.git
cp -r oh-my-harness/.claude  /caminho/do/seu/projeto/
```

Depois descreva o que quer em linguagem natural, ou digite `/craft`. Ajuste rules, agents e
o `settings.json` ao seu stack — algumas rules citam ferramentas (Biome, pnpm, bun) que o
seu projeto pode não usar. O `.claude/CLAUDE.md` descreve o harness e o repositório de
origem; reescreva-o para o seu.

## O problema

Adoção de IA sem método não vira ganho de entrega. Os números estão em
[Evidências](https://demgoncalves.github.io/oh-my-harness/evidencias.html), cada um com a fonte:

- **84%** dos desenvolvedores usam ou vão usar IA — e 46% desconfiam da precisão (Stack Overflow 2025)
- **−19%**: devs experientes ficaram mais lentos com IA, achando que estavam 20% mais rápidos (METR 2025)
- **−7,2%** na estabilidade de entrega a cada 25% a mais de adoção (DORA 2024)
- **+91%** no tempo de revisão de PR em times de alta adoção (Faros AI)

A IA amplifica o que já existe: as forças de quem tem método e as disfunções de quem não tem.

## O que há no `.claude/`

A rule exige, a skill executa, o agent decide, o command sequencia.

| Camada | Quantidade | Responde |
| ------ | ---------: | -------- |
| **rules** | 47 | O que é proibido — anti-patterns, code smells, regras de componente |
| **skills** | 52 | Como se faz — procedimentos e catálogos que o agent carrega |
| **agents** | 11 | Quem faz, com julgamento próprio — cada ofício na sua janela de contexto |
| **commands** | 5 | Em que ordem — `/craft`, `/ship`, `/audit`, `/sync`, `/extend` |
| **hooks** | 1 | O que roda sozinho, sem gastar turno |

**Os onze ofícios:** `architect`, `developer`, `tester`, `reviewer`, `designer`, `surveyor`,
`investigator`, `writer`, `releaser`, `builder` e `curator`. Quatro só leem (`architect`,
`investigator`, `reviewer`, `surveyor`); os outros sete escrevem, cada um com um artefato
exclusivo — por isso podem rodar em paralelo sem pisar um no outro.

**Quem está no teclado descreve o que quer; a máquina se organiza.** O pedido é classificado
pela forma — pergunta, bug, feature, fechar mudança — e roteado para os ofícios certos, no
ritmo **research → plan → implement → verify**. O operador não precisa decorar nada disso.

Leia [`.claude/CLAUDE.md`](.claude/CLAUDE.md) para o desenho completo.

## O site

HTML puro, sem build e sem dependências: cada página é um arquivo `.html` em `docs/`.

| Página | Assunto |
| ------ | ------- |
| [Início](https://demgoncalves.github.io/oh-my-harness/) | O paradoxo da IA que escreve código |
| [IA generativa](https://demgoncalves.github.io/oh-my-harness/ia.html) | Como a IA funciona |
| [Harness](https://demgoncalves.github.io/oh-my-harness/harness.html) | `.claude/` por dentro |
| [Specs](https://demgoncalves.github.io/oh-my-harness/specs.html) | `specs/` e `changes/` |
| [Código](https://demgoncalves.github.io/oh-my-harness/codigo.html) | `src/` navegável |
| [Fluxo](https://demgoncalves.github.io/oh-my-harness/fluxo.html) | research → plan → implement → verify |
| [Evidências](https://demgoncalves.github.io/oh-my-harness/evidencias.html) | Todos os números, com as fontes |
| [FAQ](https://demgoncalves.github.io/oh-my-harness/faq.html) | Perguntas frequentes |

### Rodar localmente

```bash
npx serve docs            # ou: python3 -m http.server 8080 --directory docs
```

### Publicação

O site é publicado no GitHub Pages a partir da branch `main`, pasta `/docs` — todo merge em
`main` atualiza o ar em poucos minutos, sem workflow de deploy. `docs/.nojekyll` desliga o
Jekyll para os arquivos serem servidos como estão, e `docs/404.html` cobre links antigos.

Para publicar um fork: **Settings → Pages → Deploy from a branch**, `main`, `/docs`.

### Estilo

Tudo em `docs/assets/style.css`: tokens em `:root` (paleta JavaScript `#F7DF1E` + ink
`#18181B`, IBM Plex Sans e JetBrains Mono), cabeçalho e rodapé, classes `.omh-*`, diagramas
em SVG inline e o responsivo no fim do arquivo. O gutter lateral é `--omh-gx`: 120px a
1440px, com a coluna de conteúdo fixa em 1200px.

## Contribuindo

Correções e ideias são bem-vindas — leia o [CONTRIBUTING](CONTRIBUTING.md) e o
[Código de Conduta](CODE_OF_CONDUCT.md). Vulnerabilidades: [SECURITY](SECURITY.md).

```bash
python3 scripts/check-site.py     # links e assets internos do site
```

## Licença

[MIT](LICENSE) © 2026 Cleber de M. Goncalves (deMGoncalves).
