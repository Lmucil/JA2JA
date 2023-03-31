import requests, simpleaudio, tempfile, json
import speech_recognition as sr
import pykakasi

#音声を聞き取る
mic = sr.Recognizer()
try:
    with sr.Microphone() as source:
        print(u"聞き取り中...")
        voice = mic.listen(source)
        text = mic.recognize_google(voice, language="ja-JP")
except:
    print(u"聞き取れませんでした。")

#全部カタカナに変換する
kks = pykakasi.kakasi()
kks.setMode("J", "K")  # 漢字からカタカナ
kks.setMode("H", "K")  # ひらがなからカタカナ
kks.setMode("K","K")   #カタカナはそのまま
result = kks.convert(text)
hiragana = set([chr(i) for i in range(12353, 12436)])  
output = ''.join([r['hira'] if r['orig'] in hiragana else r['kana'] for r in result])

#HTTP リクエスト
host = "127.0.0.1" 
port = 50021

#文の設定とキャラ変更と
params = (
    ("text", output),
    ("speaker", 14) 
)

#POST
response1 = requests.post(
    f"http://{host}:{port}/audio_query",
    params=params
)

#もいっかい
response2 = requests.post(
    f"http://{host}:{port}/synthesis",
    headers={"Content-Type": "application/json"},
    params=params,
    data=json.dumps(response1.json())
)

#WAVのダウンロード
with tempfile.TemporaryDirectory() as tmp:
    with open(f"{tmp}/audi.wav", "wb") as f:
        f.write(response2.content)
        result = simpleaudio.WaveObject.from_wave_file(f"{tmp}/audi.wav")
        play = result.play()
        play.wait_done()



# VOICEVOXエンジンを開いておいてください。
# VOICEVOXエンジンを開いておいてください。
# VOICEVOXエンジンを開いておいてください。
# VOICEVOXエンジンを開いておいてください。
# VOICEVOXエンジンを開いておいてください。
# VOICEVOXエンジンを開いておいてください。
# VOICEVOXエンジンを開いておいてください。
# VOICEVOXエンジンを開いておいてください。
# VOICEVOXエンジンを開いておいてください。
# VOICEVOXエンジンを開いておいてください。
