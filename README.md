# JA2JA
声を変換するだけの簡単なプログラムです。

日本語で何か言うと、それをSpeechRecognitionで文字に書き出して、それをVoiceVoxに読ませます。

**python ファイルを開いて、コメントで「キャラ変更」と書いてあるところにキャラクターの番号を入れて下さい。（26行目）**

キャラ番号はcharacterlistのファイルに乗っております。

そのままだと14になっております。（冥鳴ひまり）

```py
#文の設定とキャラ変更と
params = (
    ("text", output),
    ("speaker", 14)        #キャラ変更
)
```

スペックが低いpcだと出力に時間がかかります。

# キャラ
注意！

キャラごとに利用規約が違います。

何かに使いたいのであれば、

https://voicevox.hiroshiba.jp/　

でご確認ください。


# 必要事項

VoiceVox, Python3, pyaudio, SpeechRecognition

VoiceVoxについては、

https://voicevox.hiroshiba.jp/

からダウンロードしてください。

二つのライブラリは python3があれば、batch file の 'Requirements'を開くとインストールできます。（ふつうにpipでいけます）

# 開発環境
参考までに

Windows 11 Home

Python 3.7.0

VScode

# 注意事項
**VoiceVoxを開いたまま実行が必要です**

スペックが低いpcだと出力に時間がかかります。

何かに使うのならばキャラごとに違う利用規約の確認も必要です。

このプログラムは宿題に追われている中学生が暇つぶしに書いたものであり、本格的なものではありません。

疑問形の文章には対応していません。

また、細かいイントネーションの調節もしておりません。不自然な発音をたまにします。


# 追記（2023年3月30日）
Pythonライブラリのpykakasiを使うことで、漢字をカタカナに変換するようにしました。

多分精度は上がってると思います。

# さらに追記
カタカナに変換したら、こんにちは、をkonnnichiHAと文字通り発音したので変換は諦めました。

#English to Japanese
I am planning to make repo of English to Japanese version.
