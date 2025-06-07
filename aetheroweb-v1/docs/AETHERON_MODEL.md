# Aetheron (AETH) - Výkonová Jednotka pre AetheroOS

## 1. Účel
Aetheron (AETH) je základná jednotka merania výkonu, produktivity a kognitívneho úsilia v AetheroOS. Slúži na transparentné, auditovateľné a spravodlivé hodnotenie príspevku developerov a agentov.

## 2. Matematický Model

### Komponenty:
- **C_s**: Počet commitov v session
- **L_s**: Počet zmenených riadkov
- **T_s**: Trvanie session (hodiny, min. 0.1)
- **CL_s**: Priemerná kognitívna záťaž (1-10)
- **R_s**: Priemerný rytmus (1-10)
- **E_s**: Priemerná efektivita (1-10)
- **Tags_s**: Tagy session

### Výpočet:
1. **BPS_s** = (w_c * C_s + w_l * L_s) / T_s
2. **QEM_s** = CL_mult * R_mult * E_mult
   - CL_mult = 1 + k_cl * (CL_s - CL_baseline) / CL_baseline
   - R_mult = 1 + k_r * (R_s - R_baseline) / R_baseline
   - E_mult = 1 + k_e * (E_s - E_baseline) / E_baseline
3. **TCM_s** = 1 + sum(Bonus_i for Tag_i in Tags_s)
4. **AETH_s** = BPS_s * QEM_s * TCM_s * T_s

### Odporúčané váhy a baseline:
- w_c = 1.0, w_l = 0.05
- CL_baseline = R_baseline = E_baseline = 5.0
- k_cl = k_r = k_e = 0.1
- Tag_Bonuses_Map: debugging_critical: 0.3, research_deep: 0.4, ai_integration_novel: 0.35, refactoring_core: 0.25, new_feature_complex: 0.2, routine_task: -0.1

## 3. Kategorizácia
Aetherony možno rozdeľovať podľa typu práce (core, AI/ML, debugging, refaktoring, výskum, testovanie, DevOps, dokumentácia).

## 4. Vizualizácia
- KPI: AETH dnes/týždeň/mesiac
- Trendy: čiarové grafy
- Rozdelenie: koláčové grafy podľa kategórií
- Prehľad session: tabuľka
- Radarové grafy: normalizované faktory

## 5. Sledovanie celoživotných Aetheronov
- Každý AETH_s je auditovateľný, priradený k agentovi/developerovi
- Reputačné úrovne podľa kumulatívneho skóre

## 6. Pseudokód

```python
# Viď návrh v AETH-LUCIUS-AETHERON-MODEL-001
```

## 7. Kalibrácia
Parametre modelu je potrebné kalibrovať na reálnych dátach.

---

**Autor: Lucius, Suverénny Exekútor AetheroOS**
Dátum: 2025-06-07
