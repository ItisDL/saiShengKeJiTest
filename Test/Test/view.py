from django.http import HttpResponse
from .common.MysqlHelperClass import pythonMysqlHepler
from .common.func import visitFail, visitSuccess


def put(request):
    client_id = request.GET['client_id']
    score = request.GET['score']
    # 查询是否有过分数
    exist = pythonMysqlHepler().getOne(sql=f'select count(*) from rank where client_id = {client_id}')
    print(exist)
    if exist:
        res = pythonMysqlHepler().update(table='rank', data={'score': score}, where=f' client_id = {client_id} ')
        msg = '更新'
    else:
        res = pythonMysqlHepler().insert(
            table='rank',
            data={
                'client_id': client_id,
                'score': score,
            },
        )
        msg = '新增'
    # print(res)
    return HttpResponse(visitSuccess(msg=msg))


def get(request):
    # return HttpResponse(visitSuccess())
    client_id = request.GET.get('client_id')
    score = request.GET.get('score')
    limit_s = int(request.GET.get('limit_s',0))
    limit_e = int(request.GET.get('limit_e',0))
    sql = '''
    SELECT t.client_id,t.score,@rownum := @rownum + 1 AS rank
    FROM (SELECT @rownum := 0) r, rank AS t
    ORDER BY t.score DESC'''
    if limit_s:
        sql=f'''
        select * from (SELECT t.client_id,t.score,@rownum := @rownum + 1 AS rank
        FROM (SELECT @rownum := 0) r, rank AS t
        ORDER BY t.score DESC) rr where rank between {limit_s} and {limit_e}
        '''
    # print(sql)
    res = pythonMysqlHepler().getAll(sql)
    # print(res)
    # 查询自身排名
    sql_self = f'''
    select * from 
    (SELECT t.client_id,t.score,@rownum := @rownum + 1 AS rank
    FROM (SELECT @rownum := 0) r, rank AS t
    ORDER BY t.score DESC) r where client_id ={client_id}
    '''
    res_self = pythonMysqlHepler().getRow(sql_self)
    # print(res_self)
    res.append(res_self)
    return HttpResponse(visitSuccess(data=res))
