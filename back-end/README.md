# Back-end

## Framework

Flask, Python 마이크로 프레임워크에서 가장 유명한 프레임워크. 미니멀하고 직관적인 장점을 가지고 있으나 한번에 많은 트래픽을 처리할수 없는 WSGI 태생적 한계 존재. 내부적으로 사용할 용도이기에 경험이 많은 Flask를 사용. 만약 이를 외부로 공개하려고 한다면, ASGI 기반인 `FastAPI` 을 추천.

## Install

python 3.6 requires.

```bash
touch .env

python3 -m venv venv

source venv/bin/acrivate

pip3 install -r requirements.txt

flask run
```

```python
db.execute("""CREATE TABLE `user` (
  `id`           INTEGER        not null,
  `email`        varchar(30)    not null,
  `created_time` datetime       DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id` AUTOINCREMENT)
)""")
db.execute(INSERT INTO user (email) VALUES ('test@test.com'))
db.commit()
db.close()
```
