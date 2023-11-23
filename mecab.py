import MeCab
import jaconv
import random

m = MeCab.Tagger()
text = input()
node = m.parseToNode(text)
words = []
while node:
    feature = node.feature.split(",")
    print(feature)
    if len(feature) == 6 or feature[0] =="補助記号": #英単語
        words.append(node.surface)
    elif len(feature) > 19: #日本語
        hira = jaconv.kata2hira(feature[20])
        if len(hira) > 2:
            hira_naka = hira[1:]
            hira = hira[0] + "".join(random.sample(hira_naka, len(hira_naka)))
        words.append(hira)
    node = node.next
print("".join(words))