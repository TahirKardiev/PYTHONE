import os
import json
import csv
import pickle

def get_size(path):
    # Возвращает размер файла или директории
    if os.path.isfile(path):
        return os.path.getsize(path)
    elif os.path.isdir(path):
        total_size = 0
        for dirpath, dirnames, filenames in os.walk(path):
            for filename in filenames:
                filepath = os.path.join(dirpath, filename)
                total_size += os.path.getsize(filepath)
        return total_size

def traverse_directory(directory_path, output_folder):
    # Проверяем, существует ли директория для сохранения результатов
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Создаем списки для хранения данных
    data_list = []

    # Рекурсивная функция для обхода директории
    def recursive_traverse(current_path, parent_dir):
        nonlocal data_list

        for item in os.listdir(current_path):
            item_path = os.path.join(current_path, item)

            if os.path.isfile(item_path):
                # Если это файл, добавляем информацию о файле
                relative_path = os.path.relpath(item_path, parent_dir)
                size = get_size(item_path)
                data_list.append({'type': 'file', 'path': relative_path, 'size': size})
            elif os.path.isdir(item_path):
                # Если это директория, добавляем информацию о директории и вызываем функцию рекурсивно
                relative_path = os.path.relpath(item_path, parent_dir)
                size = get_size(item_path)
                data_list.append({'type': 'directory', 'path': relative_path, 'size': size})
                recursive_traverse(item_path, parent_dir)

    # Начинаем обход с переданной директории
    recursive_traverse(directory_path, directory_path)

    # Сохраняем результаты в JSON
    json_path = os.path.join(output_folder, 'result.json')
    with open(json_path, 'w') as json_file:
        json.dump(data_list, json_file, indent=2)

    # Сохраняем результаты в CSV
    csv_path = os.path.join(output_folder, 'result.csv')
    with open(csv_path, 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(['Type', 'Path', 'Size'])
        for data in data_list:
            csv_writer.writerow([data['type'], data['path'], data['size']])

    # Сохраняем результаты в pickle
    pickle_path = os.path.join(output_folder, 'result.pickle')
    with open(pickle_path, 'wb') as pickle_file:
        pickle.dump(data_list, pickle_file)


directory_to_traverse = 'C:/Users/mrfes/OneDrive/Документы/P+/HW3'
output_directory = 'C:/Users/mrfes/OneDrive/Документы/P+/HW3'

traverse_directory(directory_to_traverse, output_directory)
