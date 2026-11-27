# 🖥️ Busca-PC: Plataforma Agêntica Multiagente para Avaliação & Busca de Computadores

Sistema agêntico colaborativo e paralelo projetado para localizar, auditar, classificar e ranquear computadores novos, seminovos e usados com máxima precisão técnica e de mercado.

---

## 🏛️ Arquitetura dos Agentes

O ecossistema opera sob a liderança do **Arquiteto da Operação**, com execução concorrente/paralela:

```mermaid
flowchart TD
    Architect["🏛️ Arquiteto da Operação (Orquestrador)"] -->|"Define estratégia & dispara buscas em paralelo"| Scouts
    
    subgraph Scouts["🔍 Busca Especializada (Paralelo)"]
        UsedScout["🕵️ Agente Scout Usados & Seminovos<br/>(OLX Recife, ML Usados, etc.)"]
        NewScout["🏬 Agente Scout Novos<br/>(Amazon, FastShop, ML Novos, etc.)"]
    end

    Scouts -->|"Candidatos encontrados"| Analysts

    subgraph Analysts["🧠 Análise & Auditoria (Paralelo)"]
        HwAnalyst["⚙️ Analista de Hardware<br/>(Specs, Arquitetura, Longevidade)"]
        SentAnalyst["🌐 Analista de Sentimento & Web<br/>(Reviews, Reddit, Falhas crônicas, Opiniões)"]
    end

    Analysts -->|"Notas e Laudos Técnicos"| Classifier["🎯 Especialista em Classificação de PC<br/>(Cálculo de Custo-Benefício & Veredito Final)"]

    Classifier -->|"Rankings & Pareceres"| Architect
    Architect -->|"Registra Insights & Preços"| KnowledgeBase["📚 Memória & Base de Aprendizados<br/>(Persistência Contínua)"]
```

### 👥 Papéis e Responsabilidades

1. **🏛️ Arquiteto da Operação (`OperationArchitect`)**:
   - Direciona a estratégia e define o escopo da missão.
   - Ponto focal ao qual os demais agentes recorrem para instruções e próximos passos.
   - Orquestra o ciclo de vida: busca paralela ➔ análise paralela ➔ classificação ➔ síntese.

2. **🕵️ Scout de Usados e Seminovos (`UsedScoutAgent`)**:
   - Especializado em garimpar ofertas no mercado secundário (OLX, marketplaces locais, plataformas P2P).
   - Filtra anúncios por localidade (ex: Recife/PE), estado físico declarado, ciclos de bateria e confiabilidade do vendedor.

3. **🏬 Scout de Novos (`NewScoutAgent`)**:
   - Especializado no varejo tradicional e lojas oficiais (Amazon, Magazine Luiza, Mercado Livre Oficial, Fast Shop).
   - Monitora preços à vista, parcelamento, garantia oficial e frete.

4. **⚙️ Analista de Hardware (`HardwareAnalystAgent`)**:
   - Avalia CPU/GPU/SoC, RAM unificada, barramentos, armazenamento NVMe, tela, portas e eficiência térmica.
   - Concede uma **Nota de Hardware (0 a 100)** fundamentada em métricas objetivas (ex: Apple Silicon vs Intel, limitações de 8GB RAM).

5. **🌐 Analista de Sentimento e Comunidade (`SentimentAnalystAgent`)**:
   - Varre fóruns técnicos, Reddit, YouTube e portais de reparo em busca de problemas crônicos (ex: *Flexgate*, teclado borboleta, throttling térmico, descolamento de tela).
   - Concede uma **Nota de Sentimento/Confiabilidade (0 a 100)** baseada na experiência real de proprietários.

6. **🎯 Especialista em Classificação de PC (`PCClassifierAgent`)**:
   - Cruza a Nota de Hardware, a Nota de Sentimento e o Preço de Mercado.
   - Calcula o **Índice de Custo-Benefício (ICB 0-100)** e atribui a classificação em faixas (**Tier S, A, B, C, F**) com recomendação clara (Recomendado, Bom Negócio, Neutro, Não Recomendado).

7. **📚 Base de Aprendizados e Memória (`KnowledgeBase`)**:
   - Registra todos os aprendizados, faixas de preço de mercado em Recife/PE, modelos reprovados e dicas de negociação para alimentar iterações futuras.

---

## 🚀 Instalação e Execução

### Pré-requisitos
- Python 3.12+ (ou [uv](https://docs.astral.sh/uv/))

### Instalação
```bash
git clone https://github.com/felipedemacedo/busca-pc.git
cd busca-pc
uv sync
```

### Executar a Missão 1: MacBook com bom custo-benefício em Recife/PE
```bash
uv run python -m busca_pc.main
```

---

## 🎯 Missões

- [x] **Missão 01**: Encontrar um computador portátil da Apple (MacBook) com bom custo-benefício em **Recife/PE**.
  - Aprendizados registrados em `knowledge_base/aprendizados.json` e `knowledge_base/relatorio_missao_recife.md`.
