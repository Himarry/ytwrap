# ytwrap

ytwrap is a general-purpose Python wrapper library for the YouTube Data API v3. It allows you to easily retrieve and analyze YouTube video and comment data, and access various YouTube Data API v3 features from Python.

## Features
- Retrieve YouTube video and channel information
- Fetch and analyze comments and replies
- Simple interface for YouTube Data API v3

## Installation
```
pip install ytwrap
```

## Usage Example
```python
import ytwrap

video = ytwrap.YTVideoClient()
comment = ytwrap.YTCommentClient()

# Get latest video
latest = video.get_latest_video('CHANNEL_ID')

# Analyze comments
stats = comment.count_comments_and_replies('VIDEO_ID')
```

## License
MIT
