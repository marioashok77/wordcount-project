from django.shortcuts import render
from django.http import  HttpResponse
import operator

def home(request):

    return render(request,'home.html')

def eggs(request):
    return render(request,'eggs.html')

def count(request):
    userText = request.GET['fulltext']
    x=userText.lower()
    splitUserText = x.split()
    countSplitUserText = len(splitUserText)
    wordDictionary = {}

    for word in splitUserText:
         
        if word in wordDictionary:
            wordDictionary[word]+=1
        else:
            wordDictionary[word]=1



    sortedWords= sorted(wordDictionary.items(),key=operator.itemgetter(1),reverse=True)

    maximum = sortedWords[0][0]

    return render(request,'count.html',{'text':userText,'count':countSplitUserText,'sorted':sortedWords,'max':maximum})


























































    # fulltext=request.GET['fulltext']
    # wordlist = fulltext.split()
    # worddictionary={}
    # for word in wordlist:
    #     if word in worddictionary:
    #         worddictionary[word]+=1
    #     else:
    #         #add to worddictionary
    #         worddictionary[word]=1
    # sortedWords=sorted(worddictionary.items(),key=operator.itemgetter(1),reverse=True)
    #
    # return render(request,'count.html',{'fulltext':fulltext,'wordlist':len(wordlist),'worddictionary':sortedWords})
