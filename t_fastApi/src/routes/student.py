# -*- coding: utf-8 -*-
"""
@author 仔仔
@date 2024-03-15 14:21:25
@describe TODO
"""
from typing import List
from fastapi import APIRouter, Query
from pydantic import BaseModel
from ..exception import UnicornException


router = APIRouter()


@router.get("/student/detail")
async def student_detail():
    return {"id": "1", "name": "仔仔"}


@router.get("/student/search")
async def student_search(q: str = "123", q1: str = None, short: bool = False):
    # bool: 1,True,yes,on 等都会转成True接收
    # bool: 0,False,no 等会转成False接收
    return {"q": q, "q1": q1, "short": short}


@router.get("/student/query")
async def student_query(q: str = Query(default='', max_length=5), q1: List[str] = Query(default=["1", "2"])):
    # 默认值不会经过校验
    # 正则校验，min_length，max_length，默认值
    # ... 表示参数是必须的
    # 默认值的类型必须得对得上
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    if q1:
        results.update({"q1": q1})
    return results


class StudentCreateItem(BaseModel):
    name: str = "asdasd"
    age: int


@router.post("/student/create")
async def student_create(item: StudentCreateItem):
    print("item:", item)
    results = {"item": item}
    return [1, 2, 3]


@router.get("/student/exception")
async def student_exception():
    raise UnicornException(name="asdasd")
