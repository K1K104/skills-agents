# Email Templates Skill

## Cel umiejętności
Celem tego skilla jest dostarczenie praktycznych wskazówek i wzorców dla projektowania, wdrażania oraz testowania szablonów email w projekcie Mailer. Skill obejmuje dobre praktyki dotyczące HTML, plain-text, dziedziczenia szablonów i bezpiecznego podstawiania zmiennych.

## Kontekst
- Projekt: Mailer
- Cel: Wiadomości email do subskrybentów
- Platforma: Flask + Jinja2
- Wymagania: zgodność z klientami pocztowymi, bezpieczeństwo, testowalność

## Dlaczego to ważne
Wiadomości email muszą poprawnie wyświetlać się w różnych klientach, zawierać dynamiczne dane oraz być odporne na XSS i nieprawidłowe podstawienia.
Szablony powinny być łatwe do utrzymania, minimalizować powielanie kodu i umożliwiać testy regresyjne.

## Template inheritance
Zalecane jest użycie mechanizmu dziedziczenia Jinja2, aby oddzielić wspólną strukturę wiadomości od treści specyficznych dla danego typu email.
Przykład:
- `base_email.html` zawiera nagłówek, stopkę, sekcję `content`
- `welcome.html` dziedziczy `base_email.html` i wstawia treść powitania
- `newsletter.html` dziedziczy `base_email.html` i dostarcza listę elementów

Dzięki temu łatwiej aktualizować wspólny layout i zachować spójność stylów.

## Variable substitution i bezpieczeństwo
Zmienne muszą być walidowane po stronie aplikacji i przekazywane do renderowania w postaci sformatowanej danych.
W szablonach HTML używaj automatycznego escape'owania Jinja2 lub filtru `|e`, by zabezpieczyć się przed XSS.
Dla plain-text wystarczy wygenerować czysty tekst z tych samych pól, np. z użyciem `render_template('welcome.txt', name=name)`.

Nie umieszczaj logiki biznesowej w samych szablonach — tylko prostą interpolację danych i warunki prezentacyjne.

## HTML i plain-text
Przygotuj równoległe wersje:
- HTML: bogata treść dla klientów obsługujących stylizację
- plain-text: kompatybilny z prostymi klientami i systemami dostarczającymi tekst

Obie wersje powinny bazować na tych samych danych wejściowych, a nie na oddzielnej logice backendowej.

## Przykładowe szablony
1. `welcome.html` / `welcome.txt` — wiadomość powitalna z imieniem i linkiem
2. `confirmation.html` / `confirmation.txt` — potwierdzenie subskrypcji z linkiem aktywacyjnym
3. `newsletter.html` / `newsletter.txt` — lista artykułów lub aktualności

## Testowanie szablonów
Testy muszą renderować szablony z przykładowymi danymi i sprawdzać kluczowe elementy:
- obecność imienia użytkownika
- poprawność linków
- brak błędów renderowania
- prawidłowe escape'owanie danych

Wzorzec testowy:
```python
def test_welcome_template_renders():
    rendered = render_template('welcome.html', name='Anna', link='https://example.com')
    assert 'Witaj, Anna' in rendered
    assert 'https://example.com' in rendered
```

Dodatkowo testuj plain-text:
```python
def test_welcome_text_template_renders():
    rendered = render_template('welcome.txt', name='Anna', link='https://example.com')
    assert 'Witaj, Anna' in rendered
    assert 'https://example.com' in rendered
```

## Reguły
- Unikaj logiki biznesowej w szablonach
- Waliduj dane przed przekazaniem do szablonu
- Używaj dziedziczenia szablonów dla layoutu
- Renderuj i testuj zarówno HTML, jak i plain-text
- Zabezpieczaj dynamiczne dane przed XSS

