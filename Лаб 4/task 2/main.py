# TODO импортировать необходимые молули

import csv
import json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    ...  # TODO считать содержимое csv файла
    with open(INPUT_FILENAME, "r") as input_file:
        reader = csv.DictReader(input_file)
        output_file = open(OUTPUT_FILENAME, "w")
        arr = []
        for row in reader:
            arr.append(row)
        output_file.write(json.dumps(arr, indent=4))

    ...  # TODO Сериализовать в файл с отступами равными 4


if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
