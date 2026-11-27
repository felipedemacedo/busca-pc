import asyncio
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.text import Text
from rich import box
from pathlib import Path

from busca_pc.models import MissionSpec
from busca_pc.architect.operation_architect import OperationArchitect
from busca_pc.memory.knowledge_base import KnowledgeBase

console = Console()

async def main():
    console.print(Panel.fit(
        "[bold cyan]🖥️ BUSCA-PC[/bold cyan]: [bold white]Sistema Agêntico Multiagente de Auditoria & Classificação de Computadores[/bold white]\n"
        "[dim]Execução paralela orientada pelo Arquiteto da Operação[/dim]",
        border_style="cyan"
    ))

    # Definir a Primeira Missão
    spec = MissionSpec(
        mission_id="MISSAO-01-RECIFE-APPLE",
        title="Busca de Computador Portátil Apple (MacBook) com Melhor Custo-Benefício em Recife/PE",
        target_category="MacBook",
        target_brand="Apple",
        target_city="Recife",
        target_state="PE",
        min_ram_gb=8,
        instructions="Localizar opções de MacBooks novos e seminovos/usados em Recife e região metropolitana, auditar hardware e sentimento em paralelo, e ranquear a melhor relação custo-benefício."
    )

    console.print(f"\n[bold yellow]📋 DIRETRIZ DO ARQUITETO DA OPERAÇÃO:[/bold yellow]")
    console.print(f" • [cyan]Missão:[/cyan] {spec.title}")
    console.print(f" • [cyan]Alvo:[/cyan] {spec.target_brand} {spec.target_category} em {spec.target_city}/{spec.target_state}")
    console.print(f" • [cyan]Critério Prioritário:[/cyan] Máximo Custo-Benefício (Hardware + Confiabilidade / Preço)\n")

    architect = OperationArchitect()

    console.print("[bold green]⚡ [1/4] Arquiteto acionando Scouts em paralelo...[/bold green]")
    console.print("   ├─ [dim]UsedScoutAgent: Consultando OLX PE (DDD 81) e lojas de seminovos em Recife...[/dim]")
    console.print("   └─ [dim]NewScoutAgent: Consultando estoque oficial de novos (Amazon, ML Oficial, Fast Shop)...[/dim]")

    result = await architect.execute_mission(spec)

    console.print(f"[bold green]✓ Busca concluída em {result['elapsed_seconds']}s![/bold green] Total de anúncios analisados: [bold white]{result['total_listings_found']}[/bold white] ({result['used_count']} usados/seminovos e {result['new_count']} novos).\n")

    console.print("[bold green]🧠 [2/4] Analistas trabalhando em paralelo para cada máquina...[/bold green]")
    console.print("   ├─ [dim]HardwareAnalystAgent: Auditando CPU/SoC, RAM unificada, barramentos e eficiência térmica...[/dim]")
    console.print("   └─ [dim]SentimentAnalystAgent: Rastreado fóruns, YouTube, Reddit e falhas crônicas conhecidas...[/dim]\n")

    console.print("[bold green]🎯 [3/4] Especialista em Classificação calculando notas e Custo-Benefício...[/bold green]\n")

    # Tabela com o ranking de classificação
    table = Table(title="📊 RANKING FINAL DE CLASSIFICAÇÃO & CUSTO-BENEFÍCIO (RECIFE/PE)", box=box.ROUNDED)
    table.add_column("Tier", justify="center", style="bold")
    table.add_column("Modelo / Anúncio", style="white", min_width=30)
    table.add_column("Condição", justify="center")
    table.add_column("Preço (R$)", justify="right", style="green")
    table.add_column("Nota HW", justify="center", style="cyan")
    table.add_column("Nota Sent.", justify="center", style="magenta")
    table.add_column("ICB", justify="center", style="bold yellow")
    table.add_column("Veredito", justify="left")

    tier_colors = {
        "S": "[bold green]S[/bold green]",
        "A": "[bold blue]A[/bold blue]",
        "B": "[bold cyan]B[/bold cyan]",
        "C": "[bold yellow]C[/bold yellow]",
        "F": "[bold red]F[/bold red]",
    }

    verdict_styles = {
        "Altamente Recomendado": "[bold green]Altamente Recomendado[/bold green]",
        "Bom Negócio": "[bold blue]Bom Negócio[/bold blue]",
        "Neutro": "[yellow]Neutro[/yellow]",
        "Desaconselhado": "[dim yellow]Desaconselhado[/dim yellow]",
        "Evitar Absolutamente": "[bold red]Evitar Absolutamente[/bold red]",
    }

    for c in result["classifications"]:
        l = c.listing
        tier_fmt = tier_colors.get(c.tier, c.tier)
        verdict_fmt = verdict_styles.get(c.verdict, c.verdict)
        table.add_row(
            tier_fmt,
            f"{l.title}\n[dim]Local: {l.location}[/dim]",
            l.condition.upper(),
            f"{l.price:,.2f}",
            f"{c.hardware_audit.hardware_score:.0f}",
            f"{c.sentiment_audit.sentiment_score:.0f}",
            f"{c.cost_benefit_index:.1f}",
            verdict_fmt
        )

    console.print(table)

    # Detalhar a opção Campeã
    champion = result["champion"]
    if champion:
        champ_l = champion.listing
        champ_panel = (
            f"[bold green]🏆 MODELO CAMPEÃO EM CUSTO-BENEFÍCIO: {champ_l.title}[/bold green]\n\n"
            f"💰 [bold]Preço Anunciado:[/bold] R$ {champ_l.price:,.2f}  |  "
            f"[bold]Preço Justo de Mercado em Recife:[/bold] R$ {champion.fair_market_price_recife:,.2f} "
            f"([bold cyan]{abs(champion.price_delta_pct):.1f}% mais econômico[/bold cyan])\n"
            f"⚙️ [bold]Nota de Hardware:[/bold] {champion.hardware_audit.hardware_score}/100 "
            f"({champion.hardware_audit.processor_eval})\n"
            f"🌐 [bold]Nota de Sentimento/Comunidade:[/bold] {champion.sentiment_audit.sentiment_score}/100 "
            f"({champion.sentiment_audit.community_consensus[:140]}...)\n"
            f"📈 [bold]Índice de Custo-Benefício (ICB):[/bold] [bold yellow]{champion.cost_benefit_index}/100 (Tier {champion.tier})[/bold yellow]\n\n"
            f"📌 [bold]Laudo do Arquiteto & Especialista:[/bold]\n{champion.justification}\n\n"
            f"🛡️ [bold]Precauções e Recomendações de Compra em Recife:[/bold]\n" +
            "\n".join([f"  • {p}" for p in champion.key_precautions])
        )
        console.print(Panel(champ_panel, title="🏅 CAMPEÃO DA MISSÃO", border_style="green"))

    # Mostrar persistência de aprendizados
    console.print(f"\n[bold green]📚 [4/4] Arquiteto registrando {len(result['learnings_recorded'])} novos aprendizados na base persistente...[/bold green]")
    for lr in result["learnings_recorded"]:
        console.print(f" • [cyan]{lr.title}[/cyan] ([dim]{lr.category}[/dim])")

    # Gerar relatório da missão em Markdown para registro permanente
    relatorio_path = Path("knowledge_base/relatorio_missao_recife.md")
    _save_markdown_report(relatorio_path, result)
    console.print(f"\n[bold white]📄 Relatório completo da missão persistido em:[/bold white] [bold cyan]{relatorio_path}[/bold cyan]")
    console.print("[bold green]✨ Missão executada com sucesso absoluto![/bold green]\n")

def _save_markdown_report(path: Path, result: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    spec: MissionSpec = result["mission_spec"]
    champion = result["champion"]
    champ_l = champion.listing

    md = f"""# 📋 Relatório de Execução da Missão 01: MacBook em Recife/PE

**Data de Execução:** 27 de Novembro de 2026  
**Arquiteto da Operação:** OperationArchitect  
**Status da Missão:** Concluída com Sucesso  
**Tempo de Execução:** {result['elapsed_seconds']} segundos  

---

## 🎯 Objetivo da Missão
Localizar, auditar tecnicamente e ranquear opções de computadores portáteis Apple (MacBook) disponíveis para compra física ou entrega imediata em **Recife/PE**, identificando a máquina com a melhor relação **Custo-Benefício**.

---

## 🏆 Opção Campeã Recomendada

- **Modelo:** {champ_l.title}
- **Condição:** {champ_l.condition.upper()}
- **Localização:** {champ_l.location}
- **Preço Anunciado:** R$ {champ_l.price:,.2f}
- **Preço Médio de Referência (Recife):** R$ {champion.fair_market_price_recife:,.2f} ({abs(champion.price_delta_pct):.1f}% de economia)
- **Nota de Hardware:** {champion.hardware_audit.hardware_score}/100
- **Nota de Sentimento/Comunidade:** {champion.sentiment_audit.sentiment_score}/100
- **Índice de Custo-Benefício (ICB):** **{champion.cost_benefit_index}/100 (Tier {champion.tier})**
- **Veredito:** **{champion.verdict}**

### Justificativa Técnica
{champion.justification}

### Precauções Recomendadas para Fechamento em Recife
"""
    for p in champion.key_precautions:
        md += f"- {p}\n"

    md += """
---

## 📊 Ranking Completo de Candidatos Analisados

| Tier | Modelo | Condição | Preço (R$) | Nota HW | Nota Sentimento | ICB | Veredito |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: | :--- |
"""
    for c in result["classifications"]:
        l = c.listing
        md += f"| **{c.tier}** | {l.title} | {l.condition.upper()} | R$ {l.price:,.2f} | {c.hardware_audit.hardware_score:.0f} | {c.sentiment_audit.sentiment_score:.0f} | **{c.cost_benefit_index:.1f}** | {c.verdict} |\n"

    md += """
---

## 📚 Aprendizados Registrados para Iterações Futuras
"""
    for lr in result["learnings_recorded"]:
        md += f"### 📌 {lr.title}\n"
        md += f"- **Categoria:** {lr.category}\n"
        md += f"- **Lição:** {lr.lesson_learned}\n"
        md += "- **Regras Operacionais:**\n"
        for rule in lr.market_rules:
            md += f"  - {rule}\n"
        md += "\n"

    path.write_text(md, encoding="utf-8")

if __name__ == "__main__":
    asyncio.run(main())
