import string


def find_length(str):
    len = 0
    for i in str:
        len += 1
    return len


def is_lower(char):
    if char in string.ascii_lowercase:
        return True

    return False


def is_upper(char):
    if char in string.ascii_uppercase:
        return True

    return False


def find_location_upper(char):

    i = 0
    for ch in string.ascii_uppercase:
        if char == ch:
            return i
        i += 1
    return 26


def find_location_lower(char):

    i = 0
    for ch in string.ascii_lowercase:
        if char == ch:
            return i
        i += 1
    return 26


def convert_lower_upper(char):
    loc = find_location_lower(char)

    return string.ascii_uppercase[loc]


def convert_upper_lower(char):
    loc = find_location_upper(char)

    return string.ascii_lowercase[loc]


def split_string(str):
    final_list = []
    temp = ''
    for ch in str:
        if ch != ' ':
            temp += ch
        else:
            final_list.append(temp)
            temp = ''
    final_list.append(temp)
    return final_list


if __name__ == '__main__':

    text = input('> ')
    final_text = ''
    text_split = split_string(text)

    for str in text_split:
        if is_lower(str[0]):
            final_text += convert_lower_upper(str[0])
        else:
            final_text += str[0]

        for i in range(1, find_length(str)):
            if is_upper(str[i]):
                final_text += convert_upper_lower(str[i])
            else:
                final_text += str[i]
        final_text += ' '

    print(final_text)
