import nltk
import re

file = open('comment.txt', 'r')
text = file.read()
sentences = nltk.sent_tokenize(text)
print(sentences)
words = [nltk.word_tokenize(sentence)for sentence in sentences]
print(words)
pos_tags = [nltk.pos_tag(sentence) for sentence in words]
print(pos_tags)
new_sentences = []
for sentence in pos_tags:
 new_sentence = []
 for tag in sentence:
  word = tag[0]
  print(word)
  pos = tag[1]
  print(pos)
  if re.match('[Nn]|[Nn][Nn][Ss]',pos):
#    new_sentence.append(word)
#    new_sentences.append(new_sentence)
   new_sentence.append('NEW_NOUN')
  else:
#    new_sentence.append('NEW_NOUN')
   new_sentence.append(word)
   new_sentences.append(new_sentence)
new_text = ''
print (new_sentence + ['\n'])
print (new_sentences)
for sentence in new_sentences:
 new_text += ''.join(sentence)+'.'
print (new_text)
