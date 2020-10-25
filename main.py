# This is a sample Python script.

# Press Umschalt+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from textblob import TextBlob
import re
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Strg+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
with open(r'C:\Users\Melvin Wolf\PycharmProjects\pythonProject\THG.txt') as file:
    data = file.read().replace('', '')
blob = TextBlob(data)
print(sorted(blob.word_counts.items(), key=lambda item: item[1])[-11:-1])
print((blob.sentiment))

chapters = re.split("\\n[0-9]+\.\\n", data)
i = 0
for chapter in chapters:
    # print(chapter)
    i += 1
    chapterBlob = TextBlob(chapter)
    print("For Chapter "+ str(i) + "Most common words are:" + str(sorted(chapterBlob.word_counts.items(), key=lambda item: item[1])[-11:-1]))

# for s in blob.sentences:
#     if s.sentiment.polarity < -0.4 or s.sentiment.polarity > 0.5:
#         print(s, s.sentiment)
