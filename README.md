# JA2JA
声を変換するだけの簡単なプログラムです。
日本語で何か言うと、それをSpeechRecognitionで文字に書き出して、それをVoiceVoxに読ませます。

**python ファイルを開いて、下記の場所に好きなキャラクターの番号を入れて下さい。（26行目）**

**キャラ番号はcharacterlist.iniのファイルに記載**

```py
#文の設定とキャラ変更と
params = (
    ("text", output),
    ("speaker", 14)        #キャラ変更
)
```

# 必要事項

**VoiceVox, Python3, pyaudio, SpeechRecognition**

VoiceVoxについては、

https://voicevox.hiroshiba.jp/

からダウンロードしてください。

二つのライブラリは python3があれば、batch file の 'Requirements'を開くとインストールできます。

# 注意事項
**VoiceVoxを開いたまま実行が必要です**

キャラごとに利用規約が違います。何かに使いたいのであれば、

https://voicevox.hiroshiba.jp/　

でご確認ください。

スペックが低いpcだと出力に時間がかかります。

# 開発環境
参考までに

Windows 11 Home

Python 3.7.0

VScode
