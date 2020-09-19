# inu

Vercelでのサーバ起動
```
$ vercel dev
```


uvicornでのサーバ起動
```
$ poetry run uvicorn api.index:app --reload --host 0.0.0.0 --port 4000
```



##### ☆注意点  
インポート文は`vercel.json` からの絶対パスで記載すること  
Dockerコンテナを実行する際もvercel.jsonのあるディレクトリからapi/index.pyを指定してuvicornを起動すること
```
from  api._utils.typeDefs import type_defs
```
