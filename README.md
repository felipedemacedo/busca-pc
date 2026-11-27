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

### Opção 1: Rodando Tudo em Containers Docker (Recomendado)
O ecossistema completo (banco de dados PostgreSQL 16 + aplicação Web com FastAPI e orquestrador agêntico) sobe com um único comando:

```bash
docker compose up --build -d
```

- **Website / Dashboard Interativo:** [http://localhost:8000](http://localhost:8000)
- **Documentação Interativa Swagger API:** [http://localhost:8000/docs](http://localhost:8000/docs)
- **Banco PostgreSQL:** Porta mapeada `127.0.0.1:5442` (internamente na rede docker `db:5432`).

### Opção 2: Execução Local via CLI com UV
```bash
git clone https://github.com/felipedemacedo/busca-pc.git
cd busca-pc
uv sync
uv run python -m busca_pc.main
```

---

## 🌐 Funcionalidades do Website & Dashboard

1. **Catálogo Geral sem Teto de Compra**: Mapeia todas as possibilidades de computadores (de modelos de baixo custo a workstations pesadas).
2. **Classificação Precisa em Tempo Real**:
   - **Nota de Hardware (0 a 100)**: CPU, núcleos GPU, RAM unificada, barramento, SSD e eficiência térmica.
   - **Nota de Sentimento Web (0 a 100)**: Análise de reputação no Reddit/YouTube e detecção de falhas crônicas (*Flexgate*, teclado borboleta).
   - **Índice de Custo-Benefício (ICB 0 a 100)**: Relação entre qualidade técnica e preço justo de mercado em Recife.
   - **Tiers Coloridos (S, A, B, C, F)** e vereditos detalhados.
3. **Disparo de Nova Varredura Agêntica**: Botão interativo para acionar o Arquiteto e Scouts em tempo real.
4. **Central de Memória & Aprendizados**: Aba dedicada com os aprendizados persistidos no PostgreSQL para futuras iterações.

---

## 🗄️ Estrutura da Base de Dados PostgreSQL

O banco de dados relacional armazena de forma estruturada:
- `listings`: Dados cadastrais de cada máquina encontrada (novas, seminovas e usadas).
- `hardware_audits`: Laudos técnicos emitidos pelo Analista de Hardware.
- `sentiment_audits`: Laudos de comunidade e histórico de defeitos crônicos pelo Analista de Sentimento.
- `classifications`: Índices de custo-benefício, Tiers, justificativas e checklists de compra em Recife.
- `learnings`: Regras de mercado e aprendizados persistentes gerados pelos agentes.
- `mission_runs`: Histórico de execuções das missões e tempo decorrido.

---

## 🎯 Missões

- [x] **Missão 01**: Encontrar um computador portátil da Apple (MacBook) com bom custo-benefício em **Recife/PE**.
  - Aprendizados registrados em `knowledge_base/aprendizados.json` e `knowledge_base/relatorio_missao_recife.md`.
