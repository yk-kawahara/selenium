# 大雑把な使い方一覧

### config.txtにご自身のメールアドレスとパスワードを記載

### イメージの作成
```
docker build -t test .
```

### コンテナを作って入る
```
docker run -it --name test1 test /bin/bash
```
### コンテナ内でこちらのコードを実行
```
python3.6 web-get-ubuntu.py
```
### コンテナから抜ける
```
exit
```
### 最後に起動したコンテナのIDを確認（b71fa45b2e27など）
```
docker ps -l
```
### コンテナ内にある画像ファイルをローカル上に持ってくる
```
docker cp b71fa45b2e27:/home/test/screenshot.png .
```
### コンテナ削除
```
docker rm b71fa45b2e27
```
# イメージ確認
```
docker images
```
### イメージID削除
```
docker rmi 07ed4f27b423
```
