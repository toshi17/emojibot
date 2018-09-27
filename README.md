# Slack emojibot
これはテキストから自動的に絵文字を作成する絵文字ぼっとです。

# セットアップ

dockerが入っている場合には不要です。

```
git clone https://github.com/toshi17/emojibot.git
cd emojibot
pip install -r requirements.txt
```

以下の操作を終えたら、以下に示す「セッションのクッキーの獲得」を行なってください。

- https://{teamname}.slack.com/customize/emojiを開く
- 開発者ツールを起動し、ネットワークタブを開く
- ページをリロードし、"name"が"emoji"の項目を開く
- 新たに開いたタブから"Headers"を選ぶ
- "Request-Headers"までスクロールし、"Cookie"の値をコピーし，slackbot_settings.pyに追加する

# 起動
上記のセットアップを終えたら

```
python run.py
```
で動きます。dockerが入っている場合には上記のセットアップをしなくとも

```
docker build -t <img_name>
docker run -it --rm <img_name>
```

で動きます。


