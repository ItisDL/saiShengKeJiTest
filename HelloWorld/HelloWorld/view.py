from django.http import HttpResponse
from common.MysqlHelperClass import pythonMysqlHepler

def put(request):
    return
    # pythonMysqlHepler
    # return HttpResponse("first")

def get(request):
    res = pythonMysqlHepler().getAll(sql='select * from user_shop')
    print(res)
    return HttpResponse('second')