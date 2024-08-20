import helper


first_filename = input('enter first file name:')
second_filename = input('enter second file name:')
x = int(input('enter number of similar words displayed'))
# first_filename = 'donald_speech.txt'
# second_filename = 'melina_trump_speech.txt'
# x = 10

first_text = helper.initialize_txt(first_filename)
second_text = helper.initialize_txt(second_filename)

print('get')
print(first_text)

first_text = helper.clean_txt(first_text)
second_text = helper.clean_txt(second_text)

print('clean')
print(first_text)

first_text = helper.remove_support_words(first_text)
second_text = helper.remove_support_words(second_text)

print('remove')
print(first_text)

similar_words = helper.check_similarity(first_text, second_text, x)

print(similar_words)
for i,word in enumerate(similar_words):
    print(f'Word {i+1} is {word[0]}, similarity coeffeciant is {word[1][2]}')

print(similar_words[9][0] in helper.stop_words)
print(similar_words[9][0] == 'are')


