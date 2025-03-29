# CoSeMnou

> **CoSeMnou** je webová aplikace určená pro žáky, kteří se připravují na přijímací zkoušky na střední školy. Pomáhá porovnat výsledky z češtiny a matematiky s požadovaným minimálním skóre jednotlivých škol, a tím zodpovědět klíčovou otázku: **Stačí mi body pro přijetí?**

![Logo projektu](https://github.com/gyarab/2024-4e-eiselt-CoSeMnou/blob/master/frontend/static/images/file.png)  


## Hlavní funkce

- **Porovnání výsledků**  
  Uživatel zadá své bodové skóre z češtiny a matematiky a vybere školy (první, druhá, třetí volba). Aplikace porovná zadané body s minimálními požadavky jednotlivých škol a ihned zobrazí výsledek.

- **Seznam škol**  
  Aplikace obsahuje detailní přehled středních škol, včetně informací o adrese, kontaktech, minimálních požadovaných bodech, popisu a užitečných odkazech.

- **Tipy pro přípravu**  
  Pokud uživatel nesplňuje požadavky, aplikace nabídne tipy na zlepšení a odkazy na cvičné testy, doporučené materiály a návody, jak se efektivně učit.

## Jak to funguje

1. **Vyplnění bodů:**  
   Uživatel zadá počet bodů z češtiny a matematiky (například 35 z 50).

2. **Výběr škol:**  
   Uživatel si vybere, na které školy by se chtěl přihlásit (první, druhá a volitelně třetí volba).

3. **Porovnání:**  
   Aplikace porovná zadané body s minimálními požadavky jednotlivých škol.

4. **Výsledek:**  
   Pokud uživatel splňuje požadavky, zobrazí se zpráva „✅ Přijat!“. V opačném případě se zobrazí zpráva „❌ Nepřijat.“ spolu s tipy na zlepšení.

## Technologie

- **Django** (Python) – Backend a zpracování formulářů.
- **Bootstrap 5** – Responsivní layout a styling.
- **SQLite** – Výchozí databáze (možno přejít na PostgreSQL či MySQL).
- **HTML, CSS** – Frontendová logika a šablony.

## Lokální spuštění

1. **Naklonujte** repozitář:
   ```bash
   cd cosemnou
   python -m venv venv
   source venv/bin/activate   # Na Windows: venv\Scripts\activate

2. **Přejděte** do složky projektu a vytvořte virtuální prostředí:
   ```bash
   git clone https://github.com/uzivatel/cosemnou.git

3. **Nainstalujte** závislosti:
   ```bash
   pip install -r requirements.txt

4. **Spusťte** databázové migrace a vývojový server:
   ```bash
   python manage.py migrate
   python manage.py runserver

5. **Otevřete** prohlížeč a přejděte na:
   ```bash
   (http://127.0.0.1:8000/)

