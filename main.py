def get_key(d):
    return list(d.keys())[0]

def count_words(text):
    return len(text.split())

def chars_in_string(string):
    chars_dict = {}
    for char in string:
        if char.isalpha():
            char = char.lower()
            if char not in chars_dict:
                chars_dict[char] = 1
            elif char in chars_dict:
                chars_dict[char] += 1
    return chars_dict

def format_result(filename, word_count, chars_dict):
    print(f"--- Beging report of {filename} ---")
    print(f"{word_count} words found in the document")
    print()
    print()


    list_of_dicts = [{k: v} for k, v in chars_dict.items()]
    list_of_dicts.sort(reverse=False, key=get_key)
    # for k,v in chars_dict.items():
        # print(f"The '{k} character was found {v} times")
    
    for item in list_of_dicts:
        (key, value), = item.items()
        print(f"The '{key}' character was found {value} times")

    print("--- End report ---")

def main():
    filename = 'books/frankenstein.txt'
    with open(filename) as f:
        file_contents = f.read()
        word_count = count_words(file_contents)
        chars_dict = chars_in_string(file_contents)
        format_result(filename, word_count, chars_dict)

main()