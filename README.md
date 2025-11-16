# 🧭 Projekt 6 – Tři automatizované testy (Playwright)
**Autor:** Radim Novotný  
**Email:** r.novotny@centrum.cz  

---

Tento projekt je součástí Engeto Python Akademie. Jedná se o tři jednoduché automatizované testy webové stránky [Engeto.cz](https://engeto.cz/) pomocí frameworku **Playwright** a pluginu **pytest-playwright**.

---

## 🗂️ Co projekt umí
Projekt obsahuje testy, které:

- Ověřují, zda se stránka načte se správným titulkem (title)  
- Kontrolují, zda hlavní navigační menu obsahuje odkaz **„Kurzy“**  
- Ověřují, zda je viditelný hlavní nadpis stránky (`<h1>`)

---

## 🧩 Struktura projektu

| Soubor | Popis |
|--------|-------|
| Python.py | Soubor s třemi automatizovanými testy |
| requirements.txt | Seznam balíčků potřebných pro spuštění testů |
| README.md | Tento dokument – návod a informace o projektu |

---

## ▶️ Spuštění testů

1. Nainstalujte potřebné balíčky:
```bash
pip install -r requirements.txt
```

2. Nainstalujte prohlížeče pro Playwright:
```bash
python -m playwright install
```

3. Spusťte testy:
```bash
python -m pytest Python.py
```

Pokud je vše správně, uvidíte:
```
3 passed
```

---

## 🧰 Použité knihovny
- `pytest`  
- `playwright`  
- `pytest-playwright`

---
