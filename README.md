# SYMM
Discordのチャンネルに送信された直近の画像をシンメトリー化する

## Installation
<br>

- `sample.env` を `.env`にリネームし、ファイル内の`DISCORD_TOKEN`に自分のDiscord Botトークンを記述してください

```
DISCORD_TOKEN=typing_your_discord_bot_token
```
<br>

- 動作に必要なライブラリをインストールします
```
pip install -r requirements.txt
```
<br>

- 実行
```
py symm.py
```


## 使い方
<br>

- s!syml

```
チャンネル内で送信された直近の画像の左側を使用したシンメトリー画像の送信
```

<br>

- s!symr

```
チャンネル内で送信された直近の画像の右側を使用したシンメトリー画像の送信
```

<br>

- s!sym

```
s!syml、s!symrの両方の実行結果を送信
```

<br>

- s!sym 1-10
- s!syml 1-10
- s!symr 1-10

```
画像の変化量を1-10の数値で指定（デフォルトは5）
```

<br>

- s!help sym

```
コマンドの一覧と説明を表示
```

## 協力
<br>

- maguro869 様

<br>

- nyanmi-1828 様


