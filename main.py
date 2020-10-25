# This is a sample Python script.

# Press Umschalt+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from textblob import TextBlob
import re

included_tags = {"NN", "VB", "AD"}

with open(r'C:\Users\Melvin Wolf\PycharmProjects\pythonProject\THG.txt') as file:
    data = file.read().replace('', '')
blob = TextBlob(data)
print(sorted(blob.word_counts.items(), key=lambda item: item[1])[-11:-1])
print((blob.sentiment))

chapters = re.split("\\n[0-9]+\.\\n", data)
i = 0
for chapter in chapters:
    realChapterWords = ""
    # print(chapter)
    i += 1
    chapterBlob = TextBlob(chapter)
    # chapterBlob.tokenize()
    for (word, tag) in chapterBlob.tags:
        if tag in included_tags:
            # print(word, tag)

            realChapterWords += word + " "
    realChapterWords = TextBlob(realChapterWords)
    # print(realChapterWords)
    print("For Chapter "+ str(i) + "Most common words are:" + str(sorted(realChapterWords.word_counts.items(), key=lambda item: item[1])[-11:-1]))

# for s in blob.sentences:
#     if s.sentiment.polarity < -0.4 or s.sentiment.polarity > 0.5:
#         print(s, s.sentiment)
