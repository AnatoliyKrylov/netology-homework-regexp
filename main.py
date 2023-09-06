import csv
import re

with open("phonebook_raw.csv", encoding="utf-8") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)


def format_phone(phone):
    pattern = re.compile(r"(\+7|8)\D*(\d{3})\D*(\d{3})\D*(\d{2})\D*(\d{2})")
    subst_pattern = r"+7(\2)\3-\4-\5"
    return pattern.sub(subst_pattern, phone)


def format_phone_ext(phone):
    pattern = re.compile(r"(\+7|8)\D*(\d{3})\D*(\d{3})\D*(\d{2})\D*(\d{2})\D*доб\D*(\d+)\)?")
    subst_pattern = r"+7(\2)\3-\4-\5 доб.\6"
    return pattern.sub(subst_pattern, phone)


def check_exist(format_row):
    if exist_dict.get(f'{format_row[0]} {format_row[1]}'):
        exist_index = exist_dict.get(f'{format_row[0]} {format_row[1]}')
        if final_list[exist_index][2] == '':
            final_list[exist_index][2] = format_row[2]
        if final_list[exist_index][3] == '':
            final_list[exist_index][3] = format_row[3]
        if final_list[exist_index][4] == '':
            final_list[exist_index][4] = format_row[4]
        if final_list[exist_index][5] == '':
            final_list[exist_index][5] = format_row[5]
        if final_list[exist_index][6] == '':
            final_list[exist_index][6] = format_row[6]
    else:
        final_list.append(format_row)
        exist_dict.update({f'{format_row[0]} {format_row[1]}': final_list.index(format_row)})


def formatting_rows(row):
    format_row = []
    for some_name in row[0:3]:
        if some_name == '':
            continue
        else:
            format_row.extend(some_name.split(sep=' '))
    if len(format_row) < 3:
        format_row.append('')
    format_row.extend(row[3:5])
    if row[5].find('доб') == -1:
        format_row.append(format_phone(row[5]))
    else:
        format_row.append(format_phone_ext(row[5]))
    format_row.append(row[6])
    return format_row


if __name__ == '__main__':
    final_list = [contacts_list[0]]
    exist_dict = {}
    for row in contacts_list[1:]:
        format_row = formatting_rows(row)
        check_exist(format_row)

    with open("phonebook.csv", "w", encoding="utf-8", newline="") as f:
        datawriter = csv.writer(f, delimiter=',')
        datawriter.writerows(final_list)
