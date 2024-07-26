def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    text = text.lower()  # Convert the text to lowercase
    char_count = {}
    for char in text:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

def generate_report(file_path, word_count, char_count):
    print(f"--- Begin report of {file_path} ---")
    print(f"{word_count} words found in the document\n")
    
    # Convert char_count dictionary to a sorted list of dictionaries
    char_count_list = [{'char': char, 'num': count} for char, count in char_count.items() if char.isalpha()]
    char_count_list.sort(reverse=True, key=lambda x: x['num'])
    
    for item in char_count_list:
        print(f"The '{item['char']}' character was found {item['num']} times")
    
    print("--- End report ---")

def main():
    file_path = "books/frankenstein.txt"
    with open(file_path) as f:
        file_contents = f.read()
        word_count = count_words(file_contents)
        char_count = count_characters(file_contents)
        
        generate_report(file_path, word_count, char_count)

if __name__ == "__main__":
    main()
