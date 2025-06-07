# Rewrite Plan: comic-datat → AetheroWeb-v1 Dashboard

**Schválené prezidentom 2025-06-06**

- Prepísať layout a sekcie z index.html a style.css do Next.js komponentov s TailwindCSS
- Vytvoriť Dashboard sekciu v /dashboard/page.tsx
- Komponenty: Card, Metrics, Demographics, Trends, GenreMatrix
- Mock API: src/lib/api.ts (nahradí research_api/v3)
- CI/CD: GitHub Actions, deploy na Vercel
- Branding: tmavý režim, neónové akcenty (#1A1B2E, #4B0082, #00B7EB)
- Prístup: web_branch v xvadur/Aethero_github
- Priorita: web development, alphaXiv a audit nespúšťať paralelne

**Úlohy:**
- Frontinus: wireframe, komponenty
- Lucius: obsah Dashboardu
- Archivus: vizuály, mock API
- Implementus: implementácia, CI/CD, deploy
- Signal Root: koordinácia, logy

**Deadline:** 2025-06-08
