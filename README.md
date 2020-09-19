# inu

動作環境
Python `3.8.5`
Poetry `1.0.10`

Vercelでのサーバ起動
```
$ vercel dev
```


### uvicornでのサーバ起動
**vercel.jsonのあるディレクトリから** api/index.pyを指定してuvicornを起動すること
```
$ poetry run uvicorn api.index:app --reload --host 0.0.0.0 --port 4000
```



##### ☆注意点  
インポート文は`vercel.json` からの絶対パスで記載すること  
```
from  api._utils.hoge import 〜
```
