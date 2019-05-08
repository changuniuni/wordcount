from django.shortcuts import render

# Create your views here.
def home (request) :
    return render(request, 'home.html')

def about(request) :
    return render(request, 'about.html')

def result(request) :
   text= request.GET['fulltext']
   words= text.split()
   
   word_dictionary={}

   for word in words :
        if word in word_dictionary:
           #increase
           word_dictionary[word]+=1

        else :
            #add to dictionary  
            word_dictionary[word]=1
   return render(request, 'result.html', {'full':text, 'total': len(words), 'dictionary': word_dictionary.items()})
   #사전의 키값과 VALUE값의 쌍을 반환함



def mainmain (request) :
       year_list= {'첫번째': '2014' ,
       '두번째': '2018',
       '세번째': '2019'}
       return render(request,'mainmain.html',year_list)  
