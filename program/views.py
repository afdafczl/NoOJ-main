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
    print(type)
    test = Test.objects.create(Test_file_addr=file_addr, Test_type=type, program=program, result_file_loc="/static")
    test.save()
    return JsonResponse({"errno": "0", "msg": "cre test success"})


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
    test = Test.objects.filter(program=program)

    return JsonResponse({"errno": "0", "msg": "query test success"})