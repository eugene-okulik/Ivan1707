import os
import argparse


def parse_arguments():
    parser = argparse.ArgumentParser(
        description="Поиск текста в логах с выводом блока ошибки и контекста."
    )
    parser.add_argument("path", help="Путь к папке с логами или к одному файлу лога")
    parser.add_argument(
        "--text", required=True, help="Текст, который нужно найти в логах"
    )
    parser.add_argument(
        "--first",
        action="store_true",
        help="Выводить только первое найденное вхождение "
        "(по умолчанию выводятся все)",
    )
    return parser.parse_args()


def collect_files(path):
    if os.path.isfile(path):
        return [path]
    elif os.path.isdir(path):
        log_files = []
        for root, dirs, files in os.walk(path):
            for file in files:
                if file.endswith(".log"):
                    log_files.append(os.path.join(root, file))
        return log_files
    else:
        raise ValueError(f"Указанный путь не существует или недоступен: {path}")


def extract_timestamp(line):
    stripped = line.strip()
    if len(stripped) < 19:
        return None
    date_part = stripped[:19]
    if (date_part[4] == '-' and date_part[7] == '-' and
        date_part[10] == ' ' and date_part[13] == ':' and date_part[16] == ':'):
        if (date_part[0:4].isdigit() and date_part[5:7].isdigit() and
            date_part[8:10].isdigit() and date_part[11:13].isdigit() and
            date_part[14:16].isdigit() and date_part[17:19].isdigit()):
            pos = 19
            if len(stripped) > 19 and stripped[19] == '.':
                end = 19
                while end < len(stripped) and (stripped[end].isdigit() or stripped[end] == '.'):
                    end += 1
                return stripped[:end]
            else:
                return stripped[:19]
    return None


def is_timestamp_line(line):
    return extract_timestamp(line) is not None


def split_into_blocks_with_numbers(lines):
    blocks = []
    i = 0
    while i < len(lines):
        line = lines[i]
        timestamp = extract_timestamp(line)
        if timestamp is not None:
            start = i
            block_lines = [line]
            i += 1
            while i < len(lines) and extract_timestamp(lines[i]) is None:
                block_lines.append(lines[i])
                i += 1
            blocks.append(
                {"timestamp": timestamp, "start": start, "lines": block_lines}
            )
        else:
            i += 1
    return blocks


def extract_context(line, search_text, timestamp):
    stripped_line = line.strip()
    if stripped_line.startswith(timestamp):
        content = stripped_line[len(timestamp):].lstrip()
    else:
        content = stripped_line

    search_lower = search_text.lower()
    content_lower = content.lower()
    pos = content_lower.find(search_lower)
    if pos == -1:
        return content[:200]

    start = max(0, pos - 100)
    end = min(len(content), pos + len(search_text) + 100)

    context = content[start:end]
    if start > 0:
        context = "..." + context
    if end < len(content):
        context = context + "..."

    return context


def process_file(file_path, search_text, first_only=False):
    results = []
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            lines = f.readlines()
    except (IOError, UnicodeDecodeError) as e:
        print(f"Ошибка чтения файла {file_path}: {e}")
        return results

    blocks = split_into_blocks_with_numbers(lines)

    for block in blocks:
        timestamp = block["timestamp"]
        start_line = block["start"]
        block_lines = block["lines"]

        for i, line in enumerate(block_lines):
            if search_text.lower() in line.lower():
                context = extract_context(line, search_text, timestamp)
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
