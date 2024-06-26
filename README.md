
### main.py 실행
```python
# 터미널 실행
uvicorn main:app --reload
```



### API 응답 호출 방법 아래와 같습니다

```python
import requests
url = '주소:포트번호/query'
payload = {'query': '안녕하세요'}
headers = {'Content-Type': 'application/json'}
response = requests.post(url, json=payload, headers=headers)
print(response.json())```


