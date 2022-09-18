#Gensim -> based on textrank algorithm, textrank id graph based ranking algorithm for text processing,
# also know as topic modelling, document indexing and similarity retrieal for large text
# pre trained model comes with it

from bs4 import BeautifulSoup
import requests
from gensim.summarization.summarizer import summarize
from gensim.summarization import keywords

# creating a function to extract only text from <p> tags
def get_text(url):
    request = requests.get(url)
    content = request.content
    soup = BeautifulSoup(content,'lxml')
    text = ' '.join(map(lambda p:p.text,soup.find_all('p')))
    title = ' '.join(soup.title.stripped_strings)
    return title, text

# calling the function with desired URl
text = get_text('https://en.wikinews.org/wiki/Global_markets_plunge')

print(len(str.split(text[1]))) ##spliting the string in words

#summarization

print("The title is: ", text[0])
print("Summary of the text: ")
print(summarize(repr(text[1]),word_count=100))
#or we can use
# print(summarize(repr(text[1]),ratio=0.1))


#printing keywords extraction of text that are critcal
print("KeyWords...")
print(keywords(text[1],ratio=0.1,lemmatize=True)) #ration is threshold and lemmatize is stop repetion of words which are similar it convert it into a root word

