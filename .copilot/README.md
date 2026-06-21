# GitHub Copilot Configuration for Mailer

## Instrukcje (Instructions)
- `copilot-instructions.md` – Globalne standardy projektu

## Skills (Umiejętności)
1. email-validation – Walidacja adresów email
2. mailer-complete-testing – Kompletne testowanie
3. email-templates – Szablony email (HTML i plain-text)

Użycie:
```
@copilot use email-validation skill
```

## Agenci (Agents)
1. docs-generator-agent – Generowanie dokumentacji

Użycie:
```
Generate API documentation for mailer.subscribers module
```

## Workflow
1. Developer pisze kod
2. Copilot sugeruje pattern z odpowiedniego skill
3. Dev generuje testy używając skill
4. Docs generator tworzy dokumentację

## Best Practices
- Zawsze sprawdź `copilot-instructions.md` przed rozpoczęciem
- Użyj skill jeśli dostępny
- Agenci dla złożonych, wieloetapowych zadań
