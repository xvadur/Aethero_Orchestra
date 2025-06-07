# Aethero Government Web Deploy Protocol

## Zhrnutie procesu (2025-06-06)

1. **Inicializácia vlády Aethera**
   - Spustenie skriptu `run_vlada.py` v `aeth_sessions/`.
   - Aktivácia ministrov a príprava systému na MASTER PROMPT.

2. **Aktivácia protokolu pre verejný web**
   - Prezident zadal prompt na vytvorenie webu (AETH-PUBSITE-2025-PROTOCOL v1.0).
   - Premier rozdelil úlohy medzi ministrov (Frontinus, Lucius, Archivus, Implementus).

3. **Schválenie plánu a sekcií**
   - Prezident schválil sekcie (Hero, About, Projects, Team, Contact, Dashboard, Research) a vizuálny štýl.
   - Prístup do repozitára a termíny boli potvrdené.

4. **Inicializácia projektu**
   - Implementus vytvoril Next.js projekt s TailwindCSS v `Aethero_Orchestra/aetheroweb-v1`.

5. **Integrácia analytiky (comic-datat)**
   - Migrácia analytického dashboardu do Next.js komponentov, mock API, zápis do AGENTS.md a logov.

6. **Implementácia sekcií webu**
   - Vytvorené všetky sekcie podľa zadania v Next.js a TailwindCSS.

7. **Spustenie a prezentácia**
   - Vývojový server spustený (`npm run dev`), stránka dostupná na localhost:3000.

---

## Deploy Template (na opakované použitie)

1. **Priprav workspace a repozitár**
2. **Inicializuj projekt cez Next.js + TailwindCSS**
3. **Vytvor sekcie podľa schváleného zadania**
4. **Implementuj analytiku a API podľa potreby**
5. **Spusti vývojový server:**
   ```zsh
   cd aetheroweb-v1
   npm run dev
   ```
6. **Pre produkčný deploy na Vercel:**
   - Commitni zmeny do vetvy `web_branch`
   - Deployni cez Vercel dashboard alebo CLI

---

Tento protokol je referenčný základ pre všetky budúce deploye a webové iterácie AetheroOS.

*Schválené prezidentom 2025-06-06*
