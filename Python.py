"""
Projekt 6 – Tři automatizované testy (Playwright)
Autor: Radim Novotný
E-mail: r.novotny@centrum.cz

Popis:
Tento projekt obsahuje tři automatizované testy webové stránky Engeto.cz
pomocí frameworku Playwright a pluginu pytest-playwright.

Testy:
1. Kontrola, zda stránka načte správný titulek (title).
2. Kontrola, zda hlavní menu obsahuje odkaz "Kurzy".
3. Kontrola, zda je viditelný hlavní nadpis stránky (h1).
"""

import pytest
from playwright.sync_api import Page

# Test 1: Ověření titulku stránky
def test_title(page: Page):
    page.goto("https://engeto.cz/")
    # Ověření, že titulek obsahuje 'engeto' (ignorujeme velikost písmen)
    assert "engeto" in page.title().lower()

# Test 2: Ověření existence odkazu "Kurzy" v navigačním menu
def test_menu_kurzy(page: Page):
    page.goto("https://engeto.cz/")
    menu_items = page.locator("nav a")
    assert menu_items.filter(has_text="Kurzy").count() > 0

# Test 3: Ověření viditelnosti hlavního nadpisu (h1)
def test_banner_visible(page: Page):
    page.goto("https://engeto.cz/")
    banner = page.locator("h1")
    assert banner.is_visible()
