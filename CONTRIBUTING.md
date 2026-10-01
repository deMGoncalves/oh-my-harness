# Contribuindo

Obrigado por querer ajudar. Este repositório tem duas partes, e cada uma tem o seu jeito:

| Parte | O que é | Como contribuir |
| ----- | ------- | --------------- |
| [`docs/`](docs/) | O site (HTML puro, sem build) | Edite o `.html` e rode a checagem de links |
| [`.claude/`](.claude/) | O harness: rules, skills, agents, commands, hook | Siga a forma de cada camada (veja abaixo) |

## Antes de começar

- Dúvida ou ideia grande? Abra uma [issue](../../issues/new/choose) antes de escrever código — evita retrabalho.
- Correção pequena (typo, link quebrado, número com fonte errada)? Pode ir direto para o pull request.
- Ao participar, você concorda com o [Código de Conduta](CODE_OF_CONDUCT.md).

## Fluxo

1. Faça um fork e crie uma branch a partir de `main`: `git checkout -b tipo/descricao-curta`.
2. Faça a mudança, pequena e com um propósito só.
3. Rode as checagens da seção correspondente.
4. Commit seguindo [Conventional Commits](https://www.conventionalcommits.org/pt-br/) (`docs:`, `feat:`, `fix:`, `chore:`).
5. Abra o pull request contra `main` preenchendo o template.

## Contribuindo com o site (`docs/`)

Cada página é um arquivo `.html`; o estilo vive todo em `docs/assets/style.css`. Não há build.

```bash
npx serve docs                        # ou: python3 -m http.server 8080 --directory docs
python3 scripts/check-site.py         # todo link e asset interno aponta para algo que existe
```

Regras do site:

- **Todo número tem fonte.** Dado novo entra com link para a origem e, se for de destaque,
  também na página [Evidências](docs/evidencias.html). Sem fonte, não entra.
- **Links internos são relativos** (`faq.html`, `assets/style.css`) — o site é servido de um
  subcaminho no GitHub Pages, então `/faq.html` quebra.
- Uma mudança de menu ou rodapé vale para **as oito páginas**; o cabeçalho e o rodapé são
  repetidos em cada arquivo.
- Mantenha o português do Brasil, com a acentuação correta.
- Sem dependências novas e sem JavaScript sem necessidade.

O CI (`Check site`) roda a mesma checagem de links em todo pull request que toca `docs/`.

## Contribuindo com o harness (`.claude/`)

O harness separa quatro camadas — **a rule exige, a skill executa, o agent decide, o command
sequencia**. Antes de acrescentar algo, decida a camada; a skill
[`standard`](.claude/skills/standard/SKILL.md) tem a tabela e a forma de cada artefato:

| Se é… | Vai para |
| ----- | -------- |
| Um limite verificável, que vale sempre | `.claude/rules/` |
| Um procedimento, um catálogo, algo que precisa de exemplo | `.claude/skills/` |
| Um ofício com julgamento próprio | `.claude/agents/` |
| Uma sequência fixa que o operador dispara | `.claude/commands/` |
| Algo que deve rodar sozinho | `.claude/hooks/` |

Para criar um artefato novo, o caminho é o comando `/extend` no Claude Code. Para validar a
forma do que você mexeu:

```bash
python3 .claude/skills/standard/scripts/validate.py rules     # ou skills, agents, commands
```

Duas ressalvas honestas: o validador ainda reporta problemas pré-existentes (links quebrados
entre skills), por isso ele **não** é um gate do CI — o critério é não adicionar problemas
novos na camada que você tocou. E a informação mora em um lugar só: não repita em
`CLAUDE.md` o que já está numa rule, skill ou agent.

## O que não entra

- Número, estudo ou citação sem fonte verificável.
- Conteúdo copiado de terceiros sem licença compatível.
- Dados de empresa, cliente ou pessoa real em exemplos — use placeholders (`example.com`, `acme`).

## Licença

Ao contribuir, você concorda que sua contribuição será distribuída sob a [licença MIT](LICENSE).
