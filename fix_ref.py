import re

def format_gost_2018(authors, title, journal, year, volume=None, number=None, pages=None, doi=None, is_english=None):
    # Автоопределение языка по наличию кириллицы в названии
    if is_english is None:
        is_english = not bool(re.search('[а-яА-Я]', title))

    # Вспомогательная функция для инверсии и пробелов (Anoop, C.R. -> C. R. Anoop)
    def fix_author(author_str, reverse=False):
        parts = [p.strip() for p in author_str.split(',')]
        surname = parts[0]
        initials = parts[1] if len(parts) > 1 else ""
        # Добавляем пробелы в инициалы (A.B. -> A. B.)
        initials = re.sub(r'(\w)\.(?!\s)', r'\1. ', initials).strip()
        if reverse:
            return f"{initials} {surname}".strip()
        return f"{surname}, {initials}".strip()

    # Настройки языка
    lang = {
        'et_al': '[et al.]' if is_english else '[и др.]',
        'vol': 'Vol. ' if is_english else 'Т. ',
        'no': 'No. ' if is_english else '№ ',
        'p': 'P. ' if is_english else 'С. ',
        'text_type': 'Текст : электронный' if (doi or is_english) else 'Текст : непосредственный'
    }

    # 1. Обработка авторов
    first_author_header = fix_author(authors[0])

    if len(authors) > 3:
        responsibility = f"{fix_author(authors[0], reverse=True)} {lang['et_al']}"
    else:
        responsibility = ", ".join([fix_author(a, reverse=True) for a in authors])

    # 2. Основная сборка
    res = f"{first_author_header} {title} / {responsibility} // {journal}. – {year}."

    # 3. Том и Номер (исправленная логика)
    if volume and number:
        res += f" – {lang['vol']}{volume}, {lang['no']}{number}"
    elif volume:
        res += f" – {lang['vol']}{volume}"
    elif number:
        res += f" – {lang['no']}{number}"

    # 4. Страницы
    if pages:
        res += f". – {lang['p']}{str(pages).replace('-', '–')}"

    # 5. DOI
    if doi:
        res += f". – DOI: {doi}"

    res += f". – {lang['text_type']}."
    return res

# --- ПРОВЕРКА ---
# Статья с Томом и Номером (автоматически определит как English)
print(format_gost_2018(
    authors=["Anoop, C.R.", "Singh, R.K.", "Kumar, R.R.", "Jayalakshmi, M."],
    title="A review on steels for cryogenic applications",
    journal="Materials Performance and Characterization",
    year="2021",
    volume="10",
    number="1", # Добавили номер
    pages="16-88",
    doi="10.1520/MPC20200193"
))
