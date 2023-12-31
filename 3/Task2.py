import re
from collections import Counter

# Заменяем все символы пунктуации на пробелы и переводим текст в нижний регистр
текст = """
Поясняя своё определение, Джон Маккарти указывает: «Проблема состоит в том, что пока мы не можем в целом определить, какие вычислительные процедуры мы хотим называть интеллектуальными. Мы понимаем некоторые механизмы интеллекта и не понимаем остальные. Поэтому под интеллектом в пределах этой науки понимается только вычислительная составляющая способности достигать целей в мире».
"""

текст = re.sub(r'[^\w\s]', ' ', текст.lower())

# Разбиваем текст на слова и подсчитываем их частоту
слова = текст.split()
частоты = Counter(слова)

# Получаем 3 самых частых слов
самые_частые = частоты.most_common(3)

# Выводим результат
for слово, частота in самые_частые:
    print(f"{слово}: {частота}")
