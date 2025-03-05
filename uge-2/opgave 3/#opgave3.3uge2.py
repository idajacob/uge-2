#opgave3.3uge2

import csv
import os
import logging

logging.basicConfig(
    filename="error_log.txt",
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

source_file = r"C:\Users\spac-27\uge-2\opgave 3"
destination_file = "destination_data.csv"

data = []


try:
    if not os.path.exists(source_file):
        raise FileNotFoundError(f"Kildefilen '{source_file}' findes ikke.")
except FileNotFoundError as e:
    logging.error(e)
    print(e)

try:
    with open(source_file, "r", encoding="utf-8") as src:
        reader = csv.reader(src)
        headers = next(reader, None)

        if headers is None:
            raise ValueError("Filen har ingen overskrifter eller er tom.")

        for row in reader:
            if not any(row): 
                continue
            if len(row) != len(headers):
                raise ValueError(f"Uventet dataformat i filen. Tjek række: {row}")
            data.append(row)

except ValueError as e:
    logging.error(e)
    print(e)

except Exception as e:
    logging.error(e)
    print(f"Uventet fejl under læsning af filen: {e}")


try:
    if os.path.exists(destination_file) and not os.access(destination_file, os.W_OK):
        raise PermissionError(f"Filen '{destination_file}' er skrivebeskyttet.")
except PermissionError as e:
    logging.error(e)
    print(e)


try:
    with open(destination_file, "w", encoding="utf-8", newline="") as dest:
        writer = csv.writer(dest)
        writer.writerow(headers)
        writer.writerows(data)

    print(f"Data er kopieret fra '{source_file}' til '{destination_file}'.")

except PermissionError as e:
    logging.error(e)
    print(f"Kan ikke skrive til '{destination_file}'. Tjek om filen er skrivebeskyttet.")

except Exception as e:
    logging.error(e)
    print(f"Uventet fejl under skrivning til filen: {e}")


print("Script afsluttet.")
