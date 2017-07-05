import sys
import math
from textblob import TextBlob as tb
import os
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize,word_tokenize

##typ=sys.argv[2]
dirc=sys.argv[1]
directory=dirc.replace("\\","\\\\")
typ='0'
#directory="C:\\InputFiles\\Input6\\"
os.chdir(directory)
c=""
for path,subdirs,files in os.walk(directory):
        #print files
        for filename in files:
            if filename.endswith('.txt'):
                #x=2
                #print filename
                f=open(filename,"r")
                b=f.read().decode('latin-1')
                c=c+b
                f.close()
                #a.write(filename+"\n")
stop_words=set(stopwords.words("english"))
words=word_tokenize(c)
import string
filtered_sent=[]
for w in words:
    if w.lower() not in stop_words:
        filtered_sent.append(w)
d=" ".join(filtered_sent).lower()
import re
d = re.sub(r'[^\w\s]','',d)
list1=d.split()
#print d
from collections import Counter
import operator

counts = Counter(list1)
A=counts
if len(A)>80:
    newA = dict(sorted(A.iteritems(), key=operator.itemgetter(1), reverse=True)[:80])
else:
    newA = dict(sorted(A.iteritems(), key=operator.itemgetter(1), reverse=True))
#print newA
if typ=='0':
    from sklearn.cluster import KMeans
    from sklearn.feature_extraction.text import TfidfVectorizer
    t=' '.join(newA.keys())    

    dire="/Users/adityakhetarpal/Downloads/textpool/InputFiles/corpus/"
    os.chdir(dire)
    c=""
    maxs=0
    maxn=''
    vectorizer = TfidfVectorizer(min_df=1,lowercase=True)
    for path,subdirs,files in os.walk(dire):
        for filename in files:
            if filename.endswith('.txt'):
                f=open(filename,'r')
                b=f.read().decode('latin-1')
                f.close()
                b.replace('\n',' ')
                texts=[t,b]
                tfidf = vectorizer.fit_transform(texts)
                score=(tfidf*tfidf.T).A[0,1]
                #print filename,(tfidf*tfidf.T).A[0,1]
                if score>maxs:
                    maxs=score
                    maxn=filename
    if maxs>0.05:
        
        print maxn.split("_")[0]
        b=open("/Users/adityakhetarpal/Downloads/textpool/webapp/loaded.html","r")
        ft=b.read()
        #print ft
        b.close()
        a=open("/Users/adityakhetarpal/Downloads/textpool/webapp/loaded.html","w")
        ind=ft.find('<div class="ntext">')
        a.write(ft[:ind])
        a.write('<div class="ntext">TextPool thinks that this corpus is about '+maxn.split('_')[0]+'.')
        ind2=ft.find('</div>',ind)
        a.write(ft[ind2:])
        a.close()

        b=open("/Users/adityakhetarpal/Downloads/textpool/webapp/loaded.html","r")
        ft=b.read()
        #print ft
        b.close()
        a=open("/Users/adityakhetarpal/Downloads/textpool/webapp/loaded.html","w")
        ind=ft.find('<div id="imgs">')
        a.write(ft[:ind])
        a.write('<div id="imgs"><img src="http://localhost:8081/images/'+maxn.split('_')[0]+'/2.png" height="750px" width="800px">')
        ind2=ft.find('</div>',ind)
        a.write(ft[ind2:])
        a.close()

    else:
        print maxn.split("_")[0]
        b=open("/Users/adityakhetarpal/Downloads/textpool/webapp/loaded.html","r")
        ft=b.read()
        #print ft
        b.close()
        a=open("/Users/adityakhetarpal/Downloads/textpool/webapp/loaded.html","w")
        ind=ft.find('<div class="ntext">')
        a.write(ft[:ind])
        a.write('<div class="ntext">We think this corpus is about '+maxn.split('_')[0]+'. But we are not sure.')
        ind2=ft.find('</div>',ind)
        a.write(ft[ind2:])
        a.close()

        b=open("/Users/adityakhetarpal/Downloads/textpool/webapp/loaded.html","r")
        ft=b.read()
        #print ft
        b.close()
        a=open("/Users/adityakhetarpal/Downloads/textpool/webapp/loaded.html","w")
        ind=ft.find('<div id="imgs">')
        a.write(ft[:ind])
        a.write('<div id="imgs">')
        ind2=ft.find('</div>',ind)
        a.write(ft[ind2:])
        a.close()


else:
    fname="/Users/adityakhetarpal/Downloads/textpool/InputFiles/corpus/"+typ+"_corpus.txt"
    f=open(fname,"w")
    for k in newA:
        f.write(k+'\n')
    f.close()
  

