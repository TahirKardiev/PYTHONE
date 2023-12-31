def подходящие_комбинации(вещи, грузоподъемность):
    def рекурсивный_перебор(текущая_комбинация, индекс):
        if индекс == len(вещи):
            # Если дошли до конца списка вещей, проверяем, влезли ли в рюкзак
            сумма_массы = sum(вещь[1] for вещь in текущая_комбинация)
            if сумма_массы <= грузоподъемность:
                допустимые_комбинации.append(текущая_комбинация)
            return
        
        # Рассматриваем два случая: берем текущую вещь или нет
        рекурсивный_перебор(текущая_комбинация, индекс + 1)  # Не берем текущую вещь
        новая_комбинация = текущая_комбинация + [вещи[индекс]]  # Берем текущую вещь
        рекурсивный_перебор(новая_комбинация, индекс + 1)

    допустимые_комбинации = []
    рекурсивный_перебор([], 0)
    
    return допустимые_комбинации

# Пример использования
вещи = [("Книга", 1), ("Фонарик", 2), ("Еда", 3), ("Вода", 2)]
грузоподъемность = 5

результат = подходящие_комбинации(вещи, грузоподъемность)

for комбинация in результат:
    print("Комбинация:")
    for вещь in комбинация:
        print(f"{вещь[0]} (масса: {вещь[1]})")
    print()
