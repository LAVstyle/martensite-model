import pandas as pd
import re

def format_gost_2018(row):
    # Извлекаем данные из строки Excel
    authors = [a.strip() for a in str(row['authors']).split(';')]
    title = str(row['title'])
    journal = str(row['journal'])
    year = str(row['year'])

    # Автоопределение языка
    is_english = not bool(re.search('[а-яА-Я]', title))

    def fix_author(author_str, reverse=False):
        parts = [p.strip() for p in author_str.split(',')]
        surname = parts[0]
        initials = parts[1] if len(parts) > 1 else ""
        initials = re.sub(r'(\w)\.(?!\s)', r'\1. ', initials).strip()
        return f"{initials} {surname}".strip() if reverse else f"{surname}, {initials}".strip()

    lang = {
        'et_al': '[et al.]' if is_english else '[и др.]',
        'vol': 'Vol. ' if is_english else 'Т. ',
        'no': 'No. ' if is_english else '№ ',
        'p': 'P. ' if is_english else 'С. ',
        'text_type': 'Текст : электронный' if (pd.notna(row.get('doi')) or is_english) else 'Текст : непосредственный'
    }

    # Сборка авторов
    first_author_header = fix_author(authors[0])
    responsibility = (f"{fix_author(authors[0], True)} {lang['et_al']}" if len(authors) > 3
                      else ", ".join([fix_author(a, True) for a in authors]))

    # Формирование строки
    res = f"{first_author_header} {title} / {responsibility} // {journal}. – {year}."

    if pd.notna(row.get('volume')):
        res += f" – {lang['vol']}{str(row['volume']).replace('.0','')}"
    if pd.notna(row.get('number')):
        sep = ", " if pd.notna(row.get('volume')) else " – "
        res += f"{sep}{lang['no']}{str(row['number']).replace('.0','')}"
    if pd.notna(row.get('pages')):
        p_val = str(row['pages']).strip()
        # Если это Article ID (есть "Art", "e", или просто длинное число без тире)
        if "Art" in p_val or (not any(char in p_val for char in ['-', '–']) and len(p_val) > 3):
            val = p_val if "Art" in p_val else f"Art. {p_val}"
            res += f". – {val}"
        else:
            # Обычный диапазон страниц
            res += f". – {lang['p']}{p_val.replace('-', '–')}"
    if pd.notna(row.get('doi')):
        res += f". – DOI: {row['doi']}"

    return f"{res}. – {lang['text_type']}."

# --- ОБРАБОТКА ФАЙЛА ---
try:
    df = pd.read_excel("references.xlsx", sheet_name="Review")

    # Добавляем признак языка для сортировки
    df['is_eng'] = df['title'].apply(lambda x: not bool(re.search('[а-яА-Я]', str(x))))

    # Сортировка: сначала по языку (False < True), затем по автору (алфавит)
    #df = df.sort_values(by=['is_eng', 'authors'])

    formatted_list = [format_gost_2018(row) for _, row in df.iterrows()]

    # Сохранение в текстовый файл
    with open("ref_Review.txt", "w", encoding="utf-8") as f:
        for i, entry in enumerate(formatted_list, 1):
            f.write(f"{i}. {entry}\n")

    print(f"Готово! Список из {len(formatted_list)} источников сохранен в 'ref_Review.txt'")

except Exception as e:
    print(f"Ошибка: {e}. Проверьте наличие 'references.xlsx' и названия колонок.")
