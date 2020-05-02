
# Develop an Inverted Index Search Tool.

##########################
# Existing search capabilities-
##########################
# Create indexes (in-memory) for given files
# search for a word in a file
# search in multiple files
# display search results- files that contain the word and frequency of occurrence in each file
# search results are sorted with most frequent occurrence on the top
# search case-insensitive
# search irrespective of the punctuations
# read files on physical disk and index them --> then search
# search not only for a word but also for a phrase
##########################
# Planned future enhancements-
##########################
# provide a path of files and search within all the files on that path
# develop UI to: give path of text files, enter phrase to search for, search results, open file from results
# store the files as well as indexes in DB
# check if the file is modified or new and only then index it
# run periodic indexation --> can be neglected

import docx
import glob


def docx_to_plain_text(docx_path, plain_text_path):
    f1_doc = docx.opendocx(docx_path)
    f1_para_list = docx.getdocumenttext(f1_doc)

    plain_text = open(plain_text_path, 'w')
    for para in f1_para_list:
        para = remove_punctuations(para)
        plain_text.write('\n' + para)
    plain_text.close()


def remove_punctuations(text):
    bad_char = ['[', '.', ',', '/', ';', "'",  '[', ']', '-', '=', '(', ')', '<', '>', '?', ':', '"', '{', '}', '_',
                '+', '!', '@', '#', '$', '%', '^', '&', '*', '~', '`', ']', '\\']
    text = list(filter(lambda char: char not in bad_char, text))
    return ''.join([str(elem) for elem in text])


files_text_dict = {}
indexes = {}


def start_indexing(path):
    global indexes, files_text_dict
    plain_text_path = 'C:\\Users\\j39\\Desktop\\Python_Learnings\\Capstone_Projects_Udemy\\Data_Structure\\' \
                      'Inverted_Index_Search\\test_file.txt'

    docx_path_list = [f for f in glob.glob(path + "**/*.docx", recursive=True)]

    opened_files = []
    for docx_path in docx_path_list:
        if '~' in docx_path:
            docx_path_list.remove(docx_path)
            opened_files.append(docx_path)
    if len(opened_files) > 0:
        print('WARNING for Indexed data: Some files are currently in Open state. Search tool may not account for the'
              ' latest changes in such files. You can save and close these files to get most up-to-date search results.'
              '\nFollowing files are currently Opened:')
        for file in opened_files:
            print(f'\t{file}')

    for docx_path in docx_path_list:
        docx_to_plain_text(docx_path, plain_text_path)
        f = open(plain_text_path, 'r')
        files_text_dict[docx_path] = f.read()
        f.close()
    # for each_file in files:
    #     file_list.append(each_file)

    for each_file in files_text_dict:
        file_text_list = list(files_text_dict[each_file].lower().split())
        text_set = {''}
        # print(file_text_list)
        for word in file_text_list:
            # print(word)
            # print(indexes)
            if word not in text_set:
                text_set.add(word)
                if word in list(indexes.keys()):
                    indexes[word].append((each_file, file_text_list.count(word)))
                else:
                    indexes[word] = [(each_file, file_text_list.count(word))]

# def start_indexing(*files):
#     global indexes, file_list
#
#     for each_file in files:
#         file_list.append(each_file)
#
#     for each_file in files:
#         file_text_list = list(each_file.values())
#         file_text_list[0] = remove_punctuations(file_text_list[0])
#         file_text_list = file_text_list[0].lower().split()
#         text_set = {''}
#         # print(file_text_list)
#         for word in file_text_list:
#             # print(word)
#             # print(indexes)
#             if word not in text_set:
#                 text_set.add(word)
#                 if word in list(indexes.keys()):
#                     indexes[word].append((list(each_file.keys())[0], file_text_list.count(word)))
#                 else:
#                     indexes[word] = [(list(each_file.keys())[0], file_text_list.count(word))]


def search():
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
                        a1, a2 = word_index_tuple_list[i], word_index_tuple_list[i+1]
                        if a2[1] > a1[1]:
                            word_index_tuple_list[i] = a2
                            word_index_tuple_list[i+1] = a1
                        i += 1
            print(f'Occurrences of \'{word}\': ')
            for i in range(len(word_index_tuple_list)):
                print(f'In {word_index_tuple_list[i][0]}: {word_index_tuple_list[i][1]} times')
        else:
            print(f'Zero occurrences of \'{word}\': ')


def main():

    path = 'C:\\Users\\j39\\Desktop\\localTEMP'
    start_indexing(path)
    print(files_text_dict, '\n', indexes)

    search()


if __name__ == '__main__':
    main()
