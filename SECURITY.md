# Segurança

Este repositório é um site estático e um conjunto de arquivos de configuração para o Claude
Code. Mesmo assim, há superfícies que importam: o **hook** em `.claude/hooks/`, as
**permissões** em `.claude/settings.json` e qualquer link ou recurso externo do site.

## Reportando uma vulnerabilidade

**Não abra uma issue pública.** Use o relato privado do GitHub:

1. Vá na aba **Security** do repositório.
2. Clique em **Report a vulnerability**.
3. Descreva o problema e como reproduzi-lo.

Você deve receber uma resposta em alguns dias. Se a correção for necessária, ela sai
antes da divulgação pública, com crédito a quem reportou — se a pessoa quiser.

## O que conta

- Hook ou comando que execute algo além do que documenta.
- Permissão em `settings.json` mais ampla do que o fluxo precisa.
- Link do site que leve a destino malicioso ou comprometido.

## Versões suportadas

Só a branch `main` recebe correções.
