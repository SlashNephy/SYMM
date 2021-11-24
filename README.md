# SYMM

Discordのチャンネルに送信された画像を自動でシンメトリー化する (Cloud Vision API を利用して顔認識するバージョン)

本家同様に画像の添付ファイルと画像 URL に反応し、顔を中心にして左右シンメトリーとした画像を2枚生成します。顔が複数検出された場合には、検出確度が高い順から最大2x3枚まで生成します。

2000 リクエストまで Cloud Vision API では無料で使えますが、レートリミット等は実装されていないためご注意ください。(公開サーバーでの使用はおすすめしません。)

## How to Run

使用にあたっては Cloud Vision API へのアクセス権と資格情報が必要です。詳しくは [GCP](https://cloud.google.com/vision/docs/quickstart-client-libraries?hl=ja) のドキュメントをご確認ください。

```shell
$ docker run \
    -e DISCORD_BOT_TOKEN=xxx \
    -e GOOGLE_APPLICATION_CREDENTIALS=/path.json \
    -v $(PWD)/xxx-xxx.json:/path.json:ro \
    ghcr.io/slashnephy/symm
```

![ScreenShot](https://i.imgur.com/xgMr8Ad.png)

## Special Thanks

- HIKAKIN シンメトリー Bot
