TEXT = input("Text: ")
def print_occurrences(TEXT):
    words_count = dict()
    longest_word_length = 0
    for word in TEXT.split():
        if word in words_count:
            words_count[word] += 1
        else:
            words_count.update({word: 1})
        if len(word) > longest_word_length:
            longest_word_length = len(word)
    words_count = sort(words_count)
    for line in words_count:
        print("{:{}} : {}".format(line,longest_word_length,words_count[line]))

def sort(words_count):
    temp_list = [word for word in words_count]
    for i in range(len(temp_list)):
        for here in range(0,len(temp_list)-i-1):
            if temp_list[here] > temp_list[here+1]:
                temp_list[here],temp_list[here+1] = temp_list[here+1],temp_list[here]
    return {word: words_count[word] for word in temp_list}

print_occurrences(TEXT)
