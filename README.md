# JA2JA
声を変換するだけの簡単なプログラムです。

日本語で何か言うと、それをSpeechRecognitionで文字に書き出して、それをVoiceVoxに読ませます。

python ファイルを開いて、コメントで「キャラ変更」と書いてあるところに下記キャラクターの番号を入れて下さい。（26行目）

そのままだと14になっております。（冥鳴ひまり）

```py
#文の設定とキャラ変更と
params = (
    ("text", output),
    ("speaker", 14)        #キャラ変更
)
```

スペックが低いpcだと出力に時間がかかります。

# キャラ変更
注意！

キャラごとに利用規約が違います。

何かに使いたいのであれば、

https://voicevox.hiroshiba.jp/　

でご確認ください。


0	四国めたん	あまあま

1	ずんだもん	あまあま

2	四国めたん	四国めたん

3	ずんだもん	ずんだもん

4	四国めたん	セクシー

5	ずんだもん	セクシー

6	四国めたん	ツンツン

7	ずんだもん	ツンツン

8	春日部つむぎ	春日部つむぎ

9	波音リツ	波音リツ

10	雨晴はう	雨晴はう

11	玄野武宏	玄野武宏

12	白上虎太郎	ふつう

13	青山龍星	青山龍星

14	冥鳴ひまり	冥鳴ひまり

15	九州そら	あまあま

16	九州そら	九州そら

17	九州そら	セクシー

18	九州そら	ツンツン

19	九州そら	ささやき

20	もち子さん	もち子さん

21	剣崎雌雄	剣崎雌雄

22	ずんだもん	ささやき

23	WhiteCUL	WhiteCUL

24	WhiteCUL	たのしい

25	WhiteCUL	かなしい

26	WhiteCUL	びえーん

27	後鬼	人間ver.

28	後鬼	ぬいぐるみver.

29	No.7	No.7

30	No.7	アナウンス

31	No.7	読み聞かせ

32	白上虎太郎	わーい

33	白上虎太郎	びくびく

34	白上虎太郎	おこ

35	白上虎太郎	びえーん

36	四国めたん	ささやき

37	四国めたん	ヒソヒソ

38	ずんだもん	ヒソヒソ


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
VoiceVoxを開いたまま実行が必要です

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
