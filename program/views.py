from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from program.models import *
from user.models import *
# Create your views here.


def index(request):
    return HttpResponse("This is the index page")




def cre_program(request):
    print(request.session['username'])

    if request.session['username'] is None:
        return JsonResponse({"errno": "1002", "msg": "not login in"})

    username = request.session['username']
    user = User.objects.get(username=username)

    program_name = request.POST.get('program_name')
    program_giturl = request.POST.get('program_giturl')
    existed_program = Program.objects.filter(Program_name=program_name)

    if not existed_program.exists():
        program = Program.objects.create(Program_name=program_name, Program_giturl=program_giturl, user=user)
        program.save()
        return JsonResponse({"errno": "0", "msg": "cre success"})
    else:
        existed_program = existed_program[0]
        print(existed_program)
        return JsonResponse({"errno": "1001", "msg": "program already exist"})


def query_program(request):
    print(request.session['username'])

    if request.session['username'] is None:
        return JsonResponse({"errno": "1002", "msg": "not login in"})

    username = request.session['username']
    user = User.objects.get(username=username)

    program_name = request.POST.get('program_name')
    existed_program = Program.objects.filter(Program_name=program_name)
    print(program_name)
    if not existed_program.exists():
        return JsonResponse({"errno": "1001", "msg": "query fail"})
    else:
        existed_program = existed_program[0]
        print(existed_program)
        return JsonResponse({"errno": "0", "msg": "query success"})


#submit and judge
def submit(program_giturl, type):

    check_method = int(type)
    print(check_method)
    print(program_giturl)
    #os.system('~/CI/scripts/pull.sh '+gitlink)

    if(check_method==1):
        #os.system('~/CI/checkstyle/check.sh')
        with open("/home/duanu/CI/workspace/res/checkstyle.xml",'r',encoding='utf-8') as f:
            res = f.read()
#       print(res)
        return res

    elif(check_method==2):
        #os.system('~/CI/findbugs/findbugsscript.sh')
        with open("findbugs.html", 'r',encoding='utf-8') as f:
            res = f.read()
        return res

    elif(check_method==3):
        #os.system('~/OJ/OJ.sh')
        return  "Accepted"

#file_addr is the addr of program directory
def cre_test(request):
    print(request.session['username'])

    if request.session['username'] is None:
        return JsonResponse({"errno": "1002", "msg": "not login in"})

    username = request.session['username']
    user = User.objects.get(username=username)

    program_name = request.POST.get('program_name')
    program = Program.objects.filter(Program_name=program_name)
    if not program.exists():
        return JsonResponse({"errno": "1001", "msg": "项目不存在"})
    program = program[0]
    file_addr = request.POST.get('file_addr')
    type = request.POST.get('type')
    type=int(type)

    text = submit(program_giturl=program.Program_giturl,type=type)

    #print(type)
    test = Test.objects.create(Test_file_addr=file_addr, Test_type=type, program=program, result_file_loc="/static", Test_text =text)
    test.save()
    return JsonResponse({"errno": "0", "msg": "cre test success"})


def get_text_list(program ):
    tests = Test.objects.filter(program=program)
    result = []
    for test in tests:
        #print(test)
        result.append({"test_id": test.Test_id, "test_tyoe": test.Test_type, "test_text": test.Test_text})
    return result

def query_test(request):

    print(request.session['username'])
    if request.session['username'] is None:
        return JsonResponse({"errno": "1002", "msg": "not login in"})

    username = request.session['username']
    user = User.objects.get(username=username)

    program_name = request.POST.get('program_name')
    program = Program.objects.filter(Program_name=program_name)

    if not program.exists():
        return JsonResponse({"errno": "1001", "msg": "项目不存在"})

    program = program[0]

    return JsonResponse({"errno": "0", "msg": "query test success", "res":get_text_list(program) })