import os
import argparse
import re

def parse_arguments():
    parser = argparse.ArgumentParser(
        description="Поиск текста в логах с выводом блока ошибки и контекста."
    )
    parser.add_argument(
        "path",
        help="Путь к папке с логами или к одному файлу лога"
    )
    parser.add_argument(
        "--text",
        required=True,
        help="Текст, который нужно найти в логах"
    )
    parser.add_argument(
        "--first",
        action="store_true",
        help="Выводить только первое найденное вхождение "
             "(по умолчанию выводятся все)"
    )
    return parser.parse_args()

def collect_files(path):
    if os.path.isfile(path):
        return [path]
    elif os.path.isdir(path):
        log_files = []
        for root, dirs, files in os.walk(path):
            for file in files:
                if file.endswith('.log'):
                    log_files.append(os.path.join(root, file))
        return log_files
    else:
        raise ValueError(f"Указанный путь не существует или недоступен: {path}")

def is_timestamp_line(line):
    pattern = r'^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}'
    return re.match(pattern, line.strip()) is not None

def split_into_blocks_with_numbers(lines):
    blocks = []
    i = 0
    while i < len(lines):
        line = lines[i]
        if is_timestamp_line(line):
            timestamp = line.strip()
            start = i
            block_lines = [line]
            i += 1
            while i < len(lines) and not is_timestamp_line(lines[i]):
                block_lines.append(lines[i])
                i += 1
            blocks.append({
                'timestamp': timestamp,
                'start': start,
                'lines': block_lines
            })
        else:
            i += 1
    return blocks

def extract_context(line, search_text):
    words = line.split()
    for i, word in enumerate(words):
        if search_text.lower() in word.lower():
            start = max(0, i - 5)
            end = min(len(words), i + 6)
            context_words = words[start:end]
            return " ".join(context_words)
    return None

def process_file(file_path, search_text, first_only=False):
    results = []
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
    except (IOError, UnicodeDecodeError) as e:
        print(f"Ошибка чтения файла {file_path}: {e}")
        return results

    blocks = split_into_blocks_with_numbers(lines)

    for block in blocks:
        timestamp = block['timestamp']
        start_line = block['start']
        block_lines = block['lines']

        for i, line in enumerate(block_lines):
            if search_text.lower() in line.lower():
                context = extract_context(line, search_text)
                if context:
                    line_number = start_line + i + 1
                    results.append((file_path, timestamp, line_number, context))
                    if first_only:
                        return results
        if first_only and results:
            break
    return results

def main():
    args = parse_arguments()
    try:
        files = collect_files(args.path)
    except ValueError as e:
        print(e)
        return

    if not files:
        print("Не найдено файлов для обработки.")
        return

    all_results = []
    for file in files:
        results = process_file(file, args.text, args.first)
        all_results.extend(results)
        if args.first and results:
            break

    if not all_results:
        print(f"Текст '{args.text}' не найден ни в одном файле.")
        return

    print(f"\nРезультаты поиска для текста '{args.text}':\n")
    for idx, (file_path, timestamp, line_num, context) in enumerate(all_results, 1):
        print(f"--- Находка {idx} ---")
        print(f"Файл: {file_path}")
        print(f"Время ошибки: {timestamp}")
        print(f"Строка: {line_num}")
        print(f"Контекст: {context}\n")

if __name__ == "__main__":
    main()
