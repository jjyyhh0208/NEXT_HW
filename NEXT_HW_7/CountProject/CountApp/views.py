from django.shortcuts import render

# Create your views here.
def count(request):
    return render(request, 'count.html')

def result(request):
    text = request.POST['text']
    newText = text.replace(" ", "")
    wordCountList = text.split(' ')
    text_len = len(text)
    noSpaceLen = len(newText)
    wordCount = len(wordCountList)
    
    
    
    ctx = {
        'text': text,
        'text_len': text_len,
        'noSpaceLen' : noSpaceLen,
        'wordCount' : wordCount,
        
    }
    return render(request, 'result.html', ctx)