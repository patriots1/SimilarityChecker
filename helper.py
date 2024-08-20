stop_words = ['i','me','my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', "you're", "you've", "you'll", "you'd", 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', "she's", 'her', 'hers', 'herself', 'it', "it's", 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', "that'll", 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up','down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', "don't", 'should', "should've", 'now', 'd', 'll', 'm', 'o', 're', 've', 'y', 'ain', 'aren', "aren't", 'couldn', "couldn't", 'didn', "didn't", 'doesn', "doesn't", 'hadn', "hadn't", 'hasn', "hasn't", 'haven', "haven't", 'isn', "isn't", 'ma', 'mightn', "mightn't", 'mustn', "mustn't", 'needn', "needn't", 'shan', "shan't", 'shouldn', "shouldn't", 'wasn', "wasn't", 'weren', "weren't", 'won', "won't", 'wouldn', "wouldn't"]


#extracts text from .txt file
def initialize_txt(filename, per_line = True):
    with open(filename) as r:
        if per_line:
            return r.read().splitlines()
        else:
            return r.read()
        
#cleans text from all non alpha characters
def clean_txt(text: list) -> list:
    ier = 0
    output = []
    for line in text:
        output_ls = []
        word_ls = list(line.split(' '))
        for word in word_ls:
            word_str = ''
            for char in word:
                if char.isalpha():
                    word_str += char
                elif char == '.' or char == ',':
                    print('activated')
                    output_ls.append(word_str)
                    word_str = ''
            output_ls.append(word_str)
        # for word in output_ls:
        #     output.append(word)
        output.append(output_ls)
    return output
    

# non-split
# def clean_txt(text: str) -> str:
#     for i,char in enumerate(text):
#         if text[i:i+2] == '\\n':
#             print('removing new line')
#             text = text[:i] + text[i+2:]
#         if not text[i].isalpha() and text[i] != ' ':
#             text = text[:i] + text[i+1:]
#     return text

#removes all the stop words
def remove_support_words(text: list) -> list:
    output = []
    for line in text:
        output_ls = []
        for word in line:
            if word not in stop_words:
                output_ls.append(word)
        output.append(output_ls)
    return output

# str -> ls
# def remove_support_words(text: str) -> list:
#     print(type(text))
#     words = list(text.split(" "))
#     for word in words:
#         if word in stop_words:
#             words.remove(word)
#             print(word)
#     return words
    
#returns top x words that are the most common between texts (first_text/second_text)
def check_similarity(first_text: list, second_text: list, x: int) -> list:
    #initialize variable
    common_ratio = {}
    most_common_first = {}
    most_common_second = {}
    dummy = {}
    #find occurences of texts
    for line in first_text:
        for word in line:
            if word in most_common_first:
                most_common_first[word] += 1
            else:
                most_common_first[word] = 1
    for line in second_text:
        for word in line:
            if word in most_common_second:
                most_common_second[word] += 1
            else:
                most_common_second[word] = 1
        
    #find the top 10 words most common between texts
    for word in most_common_first:
        if word in most_common_second:
            common_ratio[word] = [most_common_first[word], most_common_second[word], float('{:.2f}'.format(most_common_first[word]/most_common_second[word]))]
    common_ratio = sorted(common_ratio.items(), key = lambda x: x[1][2])
    return common_ratio[len(common_ratio) - x:]
    
    