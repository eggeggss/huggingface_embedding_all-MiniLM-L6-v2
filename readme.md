 
##hugging face的sentence-transformers/all-MiniLM-L6-v2 

###換掉config/config.ini
```
[DEFAULT]
qdrant_url = 自己qdrant server的url
```

###換成自己程式的路徑
```
docker run -v C:\Users\rogerroan-superdesk\source\all-MiniLM-L6-v2\:/tmp -ti python:3.11 bash
```

###進入容器
```
 cd /tmp
 pip install -r requirements.txt
```

###建立vector database
```
python embedding.py
```

###搜尋資料
```
python retreive.py
```