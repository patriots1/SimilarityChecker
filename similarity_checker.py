import helper


# first_filename = input('enter first file name:')
# second_filename = input('enter second file name:')
# x = int(input('enter number of similar words displayed'))
first_filename = 'donald_speech.txt'
second_filename = 'melina_trump_speech.txt'
x = 10

first_text = helper.initialize_txt(first_filename)
second_text = helper.initialize_txt(second_filename)

first_text_ls = helper.remove_support_words(first_text)
second_text_ls = helper.remove_support_words(second_text)

print(first_text_ls)

similar_words = helper.check_similarity(first_text_ls, second_text_ls, x)

print(similar_words)
for i,word in enumerate(similar_words):
    print(f'Word {i+1} is {word[0]}, similarity coeffeciant is {word[1][2]}')

print(similar_words[9][0] in helper.stop_words)
print(similar_words[9][0] == 'are')





# ex = 'abcde'
# for i,char in enumerate(ex):
#     print('i', i, 'char', char)

# str = '\\n'
# print(str)

