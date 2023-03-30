from django.shortcuts import render
from django.http import HttpResponse
import os

def index(request):
    return HttpResponse("测试response")

def show(request):
    return render(request, 'show.html')

def submitpage(request):
    return render(request, 'submitpage.html')

def submit(request):
    gitlink = request.GET['git_link']
    check_method = request.GET['check_method']
    check_method = int(check_method)
    print(check_method)
    print(gitlink)
    os.system('~/CI/scripts/pull.sh '+gitlink)
    if(check_method==1):
        os.system('~/CI/checkstyle/check.sh')
        with open("/home/duanu/CI/workspace/res/checkstyle.xml",'r',encoding='utf-8') as f:
            res = f.read()
#       print(res)
        return HttpResponse(res, content_type="text/plain")
    elif(check_method==2):
        os.system('~/CI/findbugs/findbugsscript.sh')
        return render(request, 'findbugs.html')
    elif(check_method==3):
        os.system('~/OJ/OJ.sh')
        return HttpResponse("Accepted", content_type="text/plain")


