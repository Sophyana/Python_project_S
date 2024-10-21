def separator(line):
    arra = []
    for word in line:
        war = ""
        for i in range(0, len(word)) :
            if not word[i].isalpha():
                arra.append(war)
                war = ""
                i += 1
            else:
                war += word[i].lower()
        if war != "":
            arra.append(war)
    return arra


def find_all(set_w, words):
    count_arra = []
    for word in set_w:
        i = 0
        count = 0
        while i < len(words):
            if word == words[i]:
                count += 1
                # words.remove(words[i])
            i += 1
        count_arra.append((word, count))
    return count_arra


def sorting(out_array):
    for i in range(0, len(out_array)):
        for j in range(0, len(out_array) - 1):
            if out_array[j][1] > out_array[j + 1][1]:
                out_array[j], out_array[j + 1] = out_array[j + 1], out_array[j]
    return out_array


# main

w = int(input())
words = []
while str := input():
    line = [war for war in str.split(" ")]
    words += separator(line)

# print("words", words)

words_length = [word for word in words if len(word) == w]
set_words = {w for w in words_length}

output_array = find_all(set_words, words_length)
# print(*output_array)
output_array = sorting(output_array)
# print(*output_array)
output_array.reverse()
# print(*output_array)

n = output_array[0][1]
for wr in output_array:
    if wr[1] >= n:
        print(wr[0], end = " ")


"""
5
cerebral atrophy, n:
        The phenomena which occurs as brain cells become weak and sick, and
impair the brain's performance.  An abundance of these "bad" cells can cause
symptoms related to senility, apathy, depression, and overall poor academic
performance.  A certain small number of brain cells will deteriorate due to
everday activity, but large amounts are weakened by intense mental effort
and the assimilation of difficult concepts.  Many college students become
victims of this dread disorder due to poor habits such as overstudying.
-
cerebral darwinism, n:
        The theory that the effects of cerebral atrophy can be reversed
through the purging action of heavy alcohol consumption.  Large amounts of
alcohol cause many brain cells to perish due to oxygen deprivation.  Through
the process of natural selection, the weak and sick brain cells will die
first, leaving only the healthy cells.  This wonderful process leaves the
imbiber with a healthier, more vibrant brain, and increases mental capacity.
Thus, the devastating effects of cerebral atrophy are reversed, and academic
performance actually increases beyond previous levels.
"""