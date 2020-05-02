
import docx


def docx_to_plain_text(docx_path, plain_text_path):
    """
    Convert a .docx file into plain text file. This plain text will be further used to build indexes.

    :param docx_path: Full path of the .docx document to be converted to plain text
    :param plain_text_path: Full path of a temporary test.txt file where the converted plain text will be stored for
     later use to build indexes
    :return: None
    """
    f1_doc = docx.opendocx(docx_path)
    f1_para_list = docx.getdocumenttext(f1_doc)

    plain_text = open(plain_text_path, 'w')
    for para in f1_para_list:
        para = remove_punctuations(para)
        plain_text.write('\n' + para)
    plain_text.close()


def remove_punctuations(text):
    """
    Filter and remove all the unwanted punctuations and special characters from the given text.

    :param text: The text (of type string) to be filtered.
    :return: Filtered text (of type string)
    """
    bad_char = ['[', '.', ',', '/', ';', "'", '[', ']', '-', '=', '(', ')', '<', '>', '?', ':', '"', '{', '}', '_', '+',
                '!', '@', '#', '$', '%', '^', '&', '*', '~', '`', ']', '\\']
    text = list(filter(lambda char: char not in bad_char, text))
    return ''.join([str(elem) for elem in text])


file_list = []
indexes = {}


def start_indexing(*files):
    """
    Build inverted indexes of given text files.

    :param files: Tuple of files where each file is a dictionary with 1 key: filename and 1 value: file content
    :return: None
    """

    global indexes, file_list

    for each_file in files:
        file_list.append(each_file)

    for each_file in files:
        file_text_list = list(each_file.values())
        file_text_list[0] = remove_punctuations(file_text_list[0])
        file_text_list = file_text_list[0].lower().split()
        text_set = {''}
        # print(file_text_list)
        for word in file_text_list:
            # print(word)
            # print(indexes)
            if word not in text_set:
                text_set.add(word)
                if word in list(indexes.keys()):
                    indexes[word].append((list(each_file.keys())[0], file_text_list.count(word)))
                else:
                    indexes[word] = [(list(each_file.keys())[0], file_text_list.count(word))]


def search():
    """
    Search for a word or a phrase in the files using inverted index.
    Search result show: filename and frequency of occurrence of search item
    :return: None
    """
    search_item = input('What would you like to search for? ')
    word_list = search_item.lower().split()

    for i, word in enumerate(word_list):
        word_list[i] = remove_punctuations(word)

    print(f'\nSearch results for \'{search_item}\': ')
    for word in word_list:
        if word in indexes:
            word_index_tuple_list = indexes[word]
            for i, tpl in enumerate(word_index_tuple_list):
                if len(word_index_tuple_list) >= 2:
                    while i < len(word_index_tuple_list) - 1:
                        a1, a2 = word_index_tuple_list[i], word_index_tuple_list[i + 1]
                        if a2[1] > a1[1]:
                            word_index_tuple_list[i] = a2
                            word_index_tuple_list[i + 1] = a1
                        i += 1
            print(f'Occurrences of \'{word}\': ')
            for i in range(len(word_index_tuple_list)):
                print(f'In {word_index_tuple_list[i][0]}: {word_index_tuple_list[i][1]} times')
        else:
            print(f'Zero occurrences of \'{word}\': ')


def main():
    """
    Execute full text search (based on inverted index) in the given files and provide search results for user defined
     search items.
    """
    file1 = {'file1': 'I live in Pune, India.'}
    file2 = {'file2': 'Pune is the best city to live in India. I love Pune.'}

    start_indexing(file1, file2)

    search()


if __name__ == '__main__':
    main()
