 # Реализовать RLE алгоритм. реализовать модуль сжатия и восстановления данных. 
 # Входные и выходные данные хранятся в отдельных файлах (в одном файлике 
 # отрывок из какой-то книги, а втором файлике — сжатая версия этого текста). 

# # importing the collections
# import collections
# # function
# def run_length_encoding(string):
#    # initialzing the count dict
#    count_dict = collections.OrderedDict.fromkeys(string, 0)
#    # iterating over the string
#    print(count_dict)
#    for char in string:
#       # incrementing the frequency
#       count_dict[char] += 1
#    # initializing the empty encoded string
#    encoded_string = ""
#    # joining all the chars and their frequencies
#    for key, value in count_dict.items():
#       # joining
#       encoded_string += key + str(value)
#       # printing the encoded string
#       print(encoded_string)

# # initializing the strings
# string = "tutorialspoint"
# # invoking the function
# #run_length_encoding(string)
# # another string
# string = "aaaaaaaaaaaabbbbbccccccczzzzzz"
# run_length_encoding(string)

def RleZip(text):
    # ret = {i:0 for i in text}
    # for char in text:
    #     ret[char] += 1
    # s = []
    # for key in ret:
    #     while ret[key]>9:
    #         s.append(key + '9')
    #         ret[key] -= 9
    #     s.append(key + str(ret[key]))
    # return "".join(s)
    s = ''
    prev_char= text[0]
    count = 0
    for char in text:
        if prev_char != char:
            s += prev_char+str(count)
            prev_char = char
            count = 1
        else:
            if count == 9:
                s += prev_char+str(count)
                count = 1
            else:    
                count += 1
    s += char+str(count)
    return s

def RleUnZip(text):
    ret = [text[i:i+2] for i in range(0, len(text), 2)]
    return "".join(ret[i][0]*int(ret[i][1]) for i in range(len(ret)))

# string = 'aaaaaaaaaaaabbbbbccccccczzzzzz'
# print(string)
# print(RleZip(string))
# print(RleUnZip(RleZip(string)))

with open('kolobok_orig.txt','r', encoding='UTF-8') as f:
    text = f.read()

# print(text)
# print('====================')
# print(RleZip(text))
# print(RleUnZip(RleZip(text)))

with open('kolobok.rle','w', encoding='UTF-8') as f:
    f.write(RleZip(text))

with open('kolobok.rle','r', encoding='UTF-8') as f:
    text = RleUnZip(f.read())

with open('kolobok_unzip.txt','w', encoding='UTF-8') as f:
    f.write(text)




