password_list = []


def pass_gen():
    symbols = '- _@*#&/'

    names = name_variation()

    years = ['DOB YEAR & AGE', '18', '19', '20', '1994', '94', '994']

    phone_numbers = ['ENTER PHONE NO HERE', '+0001234567890', '5654', '890', '00']
    # ------------------------------------------------------------------------- End of Information

    for name in names:
        for doyear in years:
            password = name + doyear
            password_list.append(password)
            password = name + ' ' + doyear
            password_list.append(password)
    # ------------------------------------------------------------------------- Name and Birth Year

    for syms in symbols:
        for name in names:
            for doyear in years:
                password = name + syms + doyear
                password_list.append(password)
    # ------------------------------------------------------------------------- Name, Symbol and Birth Year

    for name in names:
        for number in phone_numbers:
            password = name + number
            password_list.append(password)
            password = name + ' ' + number
            password_list.append(password)
    # ------------------------------------------------------------------------- Name and Phone Number

    for syms in symbols:
        for name in names:
            for number in phone_numbers:
                password = name + syms + number
                password_list.append(password)
    # ------------------------------------------------------------------------- Name, Symbol and Phone Number

    print('\n----------------- Passwords Successfully Generated')
    file_name = input('Enter File Name : \n')
    for i in password_list:
        f = open(file_name + '.txt', 'a')
        f.writelines(i + '\n')
        f.close()

    print('\n--- Passwords Successfully Saved to "' + file_name + '.txt"')


def name_variation():
    name = ['ENTER TARGET NAME HERE']

    names = []
    for na in name:
        na = na.lower()
        names.append(na)

        upper_name = na.upper()
        names.append(upper_name)

        no_space_lower_name = na.replace(' ', '')
        names.append(no_space_lower_name)

        no_space_upper_name = upper_name.replace(' ', '')
        names.append(no_space_upper_name)

        first_letter_upper = na.capitalize()
        names.append(first_letter_upper)

        every_first_letter_upper = na.title()
        names.append(every_first_letter_upper)

        first_letter_upper_no_space = first_letter_upper.replace(' ', '')
        names.append(first_letter_upper_no_space)

        every_first_letter_upper_no_space = every_first_letter_upper.replace(' ', '')
        names.append(every_first_letter_upper_no_space)

        if ' ' in na:
            new_na = na.replace(' ', '-')
            names.append(new_na)
            names.append(new_na.upper())
            names.append(new_na.capitalize())

            new1_every_first_letter_upper = every_first_letter_upper.replace(' ', '-')
            names.append(new1_every_first_letter_upper)

            new2_na = na.replace(' ', '_')
            names.append(new2_na)
            names.append(new2_na.upper())
            names.append(new2_na.capitalize())

            new2_every_first_letter_upper = every_first_letter_upper.replace(' ', '_')
            names.append(new2_every_first_letter_upper)

    final_names = []

    for i in names:
        if i in final_names:
            continue
        else:
            final_names.append(i)

    return final_names


def get_information():
    print('Target Full Name')
    tar_full_names = input()
    tar_full_names = str.split(tar_full_names)

    print('Target Name')
    tar_names = input()
    tar_names = str.split(tar_names)

    print('Target Nik Name')
    tar_nik_names = input()
    tar_nik_names = str.split(tar_nik_names)

    print('Target Pet Name')
    tar_pet_names = input()
    tar_pet_names = str.split(tar_pet_names)

    print('Target Born Year')
    tar_born_year = input()
    tar_born_year = str.split(tar_born_year)

    print('Target Phone Numbers')
    tar_phone_no = input()
    tar_phone_no = str.split(tar_phone_no)

    print('Enter Target Closet Names')
    rel_names = input()
    rel_names = str.split(rel_names)

    print('Enter Target Closet People Born Year')
    rel_born_year = input()
    rel_born_year = str.split(rel_born_year)

    print('Enter Target Closet People Phone Number')
    rel_phone_no = input()
    rel_phone_no = str.split(rel_phone_no)

    print('Any Other Keywords')
    keyword = input()
    keyword = str.split(keyword)


if __name__ == '__main__':
    print('--------------------------------------------------')
    print('|                                                |')
    print('|                                                |')
    print('|              PASSWORD LIST MAKER               |')
    print('|              v 1.0                             |')
    print('|                                                |')
    print('---E-V-I-L--S-H-A-D-E-----------------------------')
    # get_information()
    pass_gen()
    # name_variation()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
