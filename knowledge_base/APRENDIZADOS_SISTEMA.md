# 🧠 Base de Conhecimento & Aprendizados do Projeto Busca-PC

Este documento consolida os aprendizados técnicos, de engenharia de dados, de arquitetura agêntica e de mercado adquiridos ao longo da evolução do projeto **Busca-PC**.

---

## 1. Arquitetura Agêntica & Concorrência Paralela

- **Divisão de Responsabilidades Estritas**:
  - **Arquiteto da Operação**: Define diretrizes e parâmetros de missão (limites de orçamento, alvos geográficos, regras de mercado).
  - **Scouts Paralelos (`UsedScoutAgent` & `NewScoutAgent`)**: Focados exclusivamente em captura, higienização de metadados e garantia de integridade de links ativos nos marketplaces.
  - **Analista de Hardware (`HardwareAnalystAgent`)**: Avalia especificações brutas com notas precisas (0 a 100), penalizando defeitos crônicos e obsolescência, enquanto premia litografias eficientes (Apple Silicon 3nm, Intel Core Ultra) e aceleração gráfica (NVIDIA GeForce RTX).
  - **Analista de Sentimento de Comunidade (`SentimentAnalystAgent`)**: Mapeia opiniões consolidadas da internet (Reddit, fóruns especializados, canais de tecnologia) para antecipar falhas de lote, desgaste térmico e qualidade de pós-venda.
  - **Classificador de PC (`PCClassifierAgent`)**: Calcula o Índice de Custo-Benefício (ICB/CBI 0-100), atribui Tiers (**S, A, B, C, F**) e emite laudos técnicos justificando a recomendação de compra ou alerta de risco.

- **Concorrência Assíncrona Nativa**:
  O uso de `asyncio.gather` permite que os scouts e analistas processem dezenas de máquinas simultaneamente sem gargalos de I/O de rede.

---

## 2. Resolução e Integridade de URLs de Anúncios

### A. Mercado Livre
- **Problema de IDs de Produtos (`/p/MLB...`)**:
  Identificadores de produto específicos (`/p/MLBxxxxxxx`) expiram com facilidade assim que o estoque do vendedor acaba ou a publicação é pausada, gerando a página de erro *"Parece que esta página não existe"*.
- **Solução Canônica**:
  A utilização de rotas estáveis e vivas (`https://lista.mercadolivre.com.br/<termo-de-busca>`) direciona o usuário diretamente para as opções disponíveis do produto em tempo real, eliminando links quebrados.

### B. OLX (Mercado Secundário / Pernambuco)
- **Diferença entre Busca e Anúncio Individual**:
  - URLs de busca com query string (`?q=...`) abrem uma listagem genérica com 40+ resultados, prejudicando a experiência de quem deseja inspecionar o anúncio específico visto no card.
  - O formato canônico para anúncios individuais de notebooks em Pernambuco é:
    `https://pe.olx.com.br/grande-recife/informatica/notebooks/<slug-do-anuncio>-<id>`
- **Tratamento de Anti-Bot (Cloudflare)**:
  A OLX protege suas rotas com Cloudflare Bot Management (HTTP 403 para requisições de datacenter/crawlers automatizados), enquanto no navegador nativo do usuário a navegação flui normalmente. As URLs validadas devem preservar o padrão esperado pelo navegador desktop.

### C. Dell Brasil, Grandes Varejistas & Comércio Especializado no Recife
- **Dell Brasil Oficial**: Páginas de campanha oficial (`/shop/deals/dc/black-friday-deals`) e catálogo de linhas (`/shop/laptop-computers/scr/laptop`) fornecem rotas permanentes de alta confiabilidade com garantia oficial em domicílio (on-site).
- **Nagem Informática (`nagem.com.br`)**: Gigante regional pernambucana. A URL `/navegacao/Informatica/Notebooks` permite rastrear estoques com a vantagem da retirada expressa em até 2 horas nos shopping centers de Recife (Shopping Recife, RioMar, Tacaruna, Plaza).
- **Techno Space (`technospace.com.br`)**: Loja física especializada em Boa Viagem (Av. Conselheiro Aguiar). Excelente canal para negociação com desconto à vista no Pix e retirada presencial de modelos Dell Inspiron e Gamer.
- **Infohouse Express (`infohouse.com.br`)**: Loja e bancada técnica tradicional em Boa Viagem (Av. Eng. Domingos Ferreira). O rastreamento revelou que a Infohouse não atua como revendedora massiva de notebooks novos lacrados de fábrica, mas sim como um **polo indispensável de suporte técnico, manutenção preventiva, diagnósticos e upgrades de SSD NVMe e memória RAM** para o mercado recifense.

---

## 3. Higienização de Dados e Gestão do Ciclo de Vida (PostgreSQL)

- **Problema de Registros Órfãos (Dead Links)**:
  Em bancos relacionais onde execuções adicionam itens via `upsert`, registros de protótipos antigos ou fontes descontinuadas continuam existindo e sendo servidos via API se não houver política de purga.
- **Protocolo de Limpeza**:
  Toda sincronização completa deve incluir purga em cascata de listings órfãos (`DELETE WHERE id NOT IN active_listings`), mantendo a consistência referencial em `classifications`, `hardware_audits` e `sentiment_audits`.

---

## 4. Calibração de Hardware & Mercado em Recife/PE

### Caso Real de Auditoria (MacBook Pro OLX 1555547340):
- **Discrepância Detectada**: Um anúncio real com preço de R$ 2.716 no Pix estava associado a um card de "M1 Pro de R$ 7.990 (Tier S)".
- **Correção Fiel**: A leitura das fotos reais do anúncio revelou um **MacBook Pro 13'' 2019 com processador Intel Core i5 1.4 GHz, 8GB LPDDR3 e Teclado Borboleta**.
- **Impacto da Reclassificação Agêntica**:
  - Nota de Hardware caiu de 100/100 para **41/100**.
  - Nota de Sentimento caiu de 96/100 para **25/100** (alto risco crônico de teclado borboleta).
  - Veredito rebaixado de *Tier S (Altamente Recomendado)* para **Tier F (Evitar Absolutamente)**.
  - O sistema cumpriu perfeitamente sua função de proteção anti-prejuízo ao comprador em Recife!

| Categoria | Hardware | Veredito | Aprendizado de Mercado |
| :--- | :--- | :--- | :--- |
| **MacBook Air M1 (2020)** | M1 / 8GB / 256GB | **Tier S** | Melhor custo-benefício histórico em Recife (R$ 3.650 a R$ 4.200 seminovo). Liquidez altíssima. |
| **MacBook Neo (2026)** | A18 Pro (3nm) / 8GB | **Tier S** | Novo padrão de entrada Apple: ultraleve, bateria duradoura, fanless e suporte a Apple Intelligence. |
| **Dell Inspiron 15** | i5 13ª Ger / 16GB DDR5 | **Tier S** | Excelente opção Windows de produtividade no Brasil com RAM e SSD expansíveis e suporte em domicílio. |
| **Dell G15 Gamer** | i5/i7 + RTX 3050/4050 | **Tier S** | Potência gráfica robusta para render 3D e games pesados; foco em uso conectado à tomada. |
| **MacBooks Intel (2015-2019)** | Intel Core i5/i7 | **Tier F (Evitar)** | Armadilhas financeiras: falhas de teclado borboleta e rompimento de tela (Flexgate) com reparo inviável em Recife. |

---

## 5. Interface com Usuário (Three.js & Alpine.js)

- **Minimalismo Focado**:
  O carrossel centralizado 3D permite navegação horizontal rápida com suporte a teclado e drag.
- **Filtros Flexíveis em Tooltip**:
  Sliders de preço dinâmicos (mínimo e máximo), ordenação por menor preço e alternância por marca (**Todas, Apple, Dell**) e condição (**Todos, Usados, Novos**).
- **Acesso Direto ao Anúncio**:
  Botão com link direto tanto na face do card do carrossel quanto no modal detalhado de inspeção técnica.
