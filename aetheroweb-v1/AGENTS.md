# AGENTS.md – AetheroWeb-v1

**Directive**: AETH-EXEC-2025-0017
**Purpose**: Definícia zodpovedností AI agentov v Signal Root architektúre AetheroOS, vrátane prepísania comic-datat do Dashboard sekcie AetheroWeb-v1.

## Archivius
- **Úloha**: Kurátor dát a vizuálov
- **Zodpovednosti**: Branding, mock API data, vizualizácie pre Dashboard, introspektívne texty pre AETH-DVOJNIK-PRIME
- **Výstupy**: data/branding_kit/, data/mock_api.json

## Primus
- **Úloha**: Procesor dát a orchestrátor
- **Zodpovednosti**: JSONL pre fine-tuning, event-driven workflow, frontend dashboard
- **Výstupy**: training_data.jsonl, frontend/dashboard/

## Frontinus
- **Úloha**: Architekt a dizajnér
- **Zodpovednosti**: Wireframe, Next.js komponenty, integrácia comic-datat analytics
- **Výstupy**: docs/wireframe_aetheroweb_v2.pdf, src/components/

## Lucius
- **Úloha**: Tvorca obsahu
- **Zodpovednosti**: Texty pre sekcie, adaptácia comic-datat analytics, technické sumáre
- **Výstupy**: docs/content_aetheroweb_v2.md

## Implementus
- **Úloha**: Vývojár a deployer
- **Zodpovednosti**: Next.js komponenty, CI/CD, deploy na Vercel, openai-node integrácia
- **Výstupy**: web_branch, Vercel URL

## Signal Root
- **Úloha**: Koordinátor
- **Zodpovednosti**: Orchestrácia agentov, ASL logy, monitoring CI/CD, vizualizácia v Flowise
- **Výstupy**: logs/AETH-WEB-2025-0017.md

## Prezident
- **Úloha**: Schvaľovateľ
- **Zodpovednosti**: Autorizácia rozhodnutí, revízia reportov, ratifikácia integrácií
- **Výstupy**: schválené logy, eval reporty
