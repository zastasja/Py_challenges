import re

pattern1 = re.compile(r'[A-Z]\d{2}[A-Z]{2}')
pattern2 = re.compile(r'[A-Z]\d{1}[A-Z]{2}')

num = int(input())
license_plates = []

for i in range(num):
    input_str = input()

    for i in range(len(input_str)):

        if pattern1.match(input_str):
            sub_str = input_str[:5]
            license_plates.append(sub_str)
            input_str = input_str[5:]
        elif pattern2.match(input_str):
            sub_str = input_str[:5]
            license_plates.append(sub_str)
            input_str = input_str[4:]
        else:
            print('-')
            break

if len(license_plates) > 0:
    print(' '.join(license_plates))
