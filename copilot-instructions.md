# GitHub Copilot Instructions - Mailer Project

## 1. Python i zależności
- Python 3.9+
- Linting: `flake8`, formatowanie: `black`
- Type hints obowiązkowe
- Aktualizuj `requirements.txt` przy zmianie zależności

## 2. Style i konwencje
- Przestrzegaj PEP 8
- Funkcje: max 50 linii
- Moduły: zalecenie < 500 linii
- Docstringi w formacie Google

## 3. Testy
- Używaj `pytest` i `pytest-cov`
- Minimum 80% code coverage
- Mockuj zewnętrzne usługi (SMTP, DB)
- Każda istotna funkcjonalność: testy pozytywne i negatywne
- Korzystaj ze skilla `mailer-complete-testing` dla kompleksowych wzorców testowych

## 4. Bezpieczeństwo
- Nie commituj credentials i secretów
- Używaj environment variables dla kluczy
- Waliduj wszystkie dane wejściowe (np. adresy email)
- Chroń przed XSS w szablonach HTML

## 5. Architektura
- Separacja logiki biznesowej od UI (Flask: routes vs service layer)
- MVC dla warstwy web
- Unikaj side-effectów w funkcjach pomocniczych

## 6. Git i workflow
- Commit messages: conventional commits
- Branch naming: `feature/*`, `bugfix/*`, `docs/*`
- PR: opis, kroki do uruchomienia, testy

## 7. Skills i Agents
- Umieść skills w `.copilot/skills/`
- Agenci w katalogu `.agents/`
- Opisz skills w `SKILL.md` i dodaj `.promptyaml` dla metadanych

## 8. Dokumentacja
- Generuj dokumentację w `docs/`
- Aktualizuj README dla nowych funkcji

