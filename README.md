# ytwrap

YouTube Data API v3用Pythonラッパーです。

## インストール
```
pip install ytwrap
```

## 使い方
```python
import ytwrap

video = ytwrap.YTVideoClient()
comment = ytwrap.YTCommentClient()

# 例: 最新動画の取得
latest = video.get_latest_video('チャンネルID')

# 例: コメント集計
stats = comment.count_comments_and_replies('動画ID')
```

## 必要な環境変数
- `YOUTUBE_API_KEY` : Google Cloud Consoleで取得したAPIキー

## ライセンス
MIT
