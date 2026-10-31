# Changelog

## 3.1

Origem: um mês de uso no projeto COMPESA Faturamento, revisado por Estevao Eller entre 30 e 31/10/2026.

- a wiki passa de `.wiki/` para `_wiki/`;
- frontmatter portátil na `_wiki/` e no `history/`, em três modos (`perfil` padrão, `nucleo`, `nenhum`), escolhido por perguntas
  na criação do projeto e gravado no `PROJECT.md`; datas DD/MM/AAAA;
- registro sem pedido ao fim de cada passo com gatilho, e linha final `Registrado em:`;
- tabela de destinos (`references/destinos.md`), com registro de achados, `PERGUNTAS.md` e "Destinos deste projeto" no `AGENTS.md`;
- pedido repetido vira regra; consultar wiki e history antes de propor;
- nada se apaga: nota "Revisto mais à frente", `z.old/`, cópia antes de mexer em arquivo em uso;
- regras fixas no topo do `PROJECT.md`; `NOW.md` com até cerca de 150 linhas;
- `TASKS.md` em lista por frente; rastreabilidade de agente e modelo fica opcional;
- regras para várias sessões e agentes no mesmo projeto, e para salvar planos aprovados em `_wiki/planos/`;
- modelos novos: `_wiki/_modelo-pagina.md` e `history/_modelo-registro.md`;
- as cópias locais da skill nos projetos passam a levar `references/` e são geradas pelo `build_wiki_kit.py`.

## 3.0 — Adaptive

- reduziu o núcleo inicial para seis elementos;
- substituiu perfis fixos por estrutura emergente;
- unificou atividades humanas e fila de agentes em `TASKS.md`, mantendo seções distintas;
- adotou leitura progressiva e proibição de varredura integral automática;
- tornou o histórico sob demanda;
- simplificou o registro de agente, provedor e modelo;
- manteve validação humana separada da conclusão técnica;
- removeu YAML obrigatório por execução, taxonomias antecipadas e pastas vazias especializadas.
