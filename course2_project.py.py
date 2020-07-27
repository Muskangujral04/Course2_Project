"""
Your task is to build a sentiment classifier, which will detect how positive or negative each tweet is. You will create a csv file, which contains columns for the Number of Retweets, Number of Replies, Positive Score (which is how many happy words are in the tweet), Negative Score (which is how many angry words are in the tweet), and the Net Score for each tweet. At the end, you upload the csv file to Excel or Google Sheets, and produce a graph of the Net Score vs Number of Retweets.

To start, define a function called strip_punctuation which takes one parameter, a string which represents a word, and removes characters considered punctuation from everywhere in the word. (Hint: remember the .replace() method for strings.)
"""
punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
def strip_punctuation(s):
    for i in s:
        if i in punctuation_chars:
            s=s.replace(i,"")
    return s

"""
Next, copy in your strip_punctuation function and define a function called get_pos which takes one parameter, a string which represents one or more sentences, and calculates how many words in the string are considered positive words. Use the list, positive_words to determine what words will count as positive. The function should return a positive integer - how many occurrences there are of positive words in the text. Note that all of the words in positive_words are lower cased, so you’ll need to convert all the words in the input string to lower case as well.
"""


positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())

def get_pos(st):
    lst=st.split()
    count=0
    for i in lst:
        word=strip_punctuation(i)
        if word.lower() in positive_words:
            count+=1
    return count

"""
Next, copy in your strip_punctuation function and define a function called get_neg which takes one parameter, a string which represents one or more sentences, and calculates how many words in the string are considered negative words. Use the list, negative_words to determine what words will count as negative. The function should return a positive integer - how many occurrences there are of negative words in the text. Note that all of the words in negative_words are lower cased, so you’ll need to convert all the words in the input string to lower case as well.
"""
negative_words = []
with open("negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())

            
def get_neg(st):
    lst=st.split()
    count=0
    for i in lst:
        word=strip_punctuation(i)
        if word.lower() in negative_words:
            count+=1
    return count



"""
Finally, copy in your previous functions and write code that opens the file project_twitter_data.csv which has the fake generated twitter data (the text of a tweet, the number of retweets of that tweet, and the number of replies to that tweet). Your task is to build a sentiment classifier, which will detect how positive or negative each tweet is. Copy the code from the code windows above, and put that in the top of this code window. Now, you will write code to create a csv file called resulting_data.csv, which contains the Number of Retweets, Number of Replies, Positive Score (which is how many happy words are in the tweet), Negative Score (which is how many angry words are in the tweet), and the Net Score (how positive or negative the text is overall) for each tweet. The file should have those headers in that order. Remember that there is another component to this project. You will upload the csv file to Excel or Google Sheets and produce a graph of the Net Score vs Number of Retweets. 
"""
result=open("resulting_data.csv","w")
st="{},{},{},{},{}".format("Number of Retweets","Number of Replies","Positive Score","Negative Score","Net Score")
result.write(st)
result.write("\n")
files=open("project_twitter_data.csv","r")
st=files.readlines()
for i in st[1:]:
    l=i.strip().split(",")
    tweet=l[0]
    pos=get_pos(tweet)
    neg=get_neg(tweet)
    retweets=l[1]
    replies=l[2]
    st="{},{},{},{},{}".format(retweets,replies,pos,neg,(pos-neg))
    result.write(st)
    result.write("\n")
files.close()
result.close()
