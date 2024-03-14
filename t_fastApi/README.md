# fastapi
- [官网](https://fastapi.tiangolo.com/zh/#_3)

## 安装
```shell
pip install fastapi

你还会需要一个 ASGI 服务器，生产环境可以使用 Uvicorn 或者 Hypercorn
pip install "uvicorn[standard]"
```


## 运行命令
```shell
uvicorn main:app --reload
```

## 文档
```shell
swagger: http://127.0.0.1:8000/docs

Redoc: http://127.0.0.1:8000/redoc
```