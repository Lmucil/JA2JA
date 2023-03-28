import requests, simpleaudio, tempfile, json
import speech_recognition as sr

#音声を聞き取る
mic = sr.Recognizer()
try:
    with sr.Microphone() as source:
        print(u"聞き取り中...")
        voice = mic.listen(source)
        text = mic.recognize_google(voice, language="ja-JP")
except:
    print(u"聞き取れませんでした。")

#HTTP リクエスト
host = "127.0.0.1" 
port = 50021

params = (
    ("text", text),
    ("speaker", キャラの数字) #キャラクターの変更
)

response1 = requests.post(
    f"http://{host}:{port}/audio_query",
    params=params
)

response2 = requests.post(
    f"http://{host}:{port}/synthesis",
    headers={"Content-Type": "application/json"},
    params=params,
    data=json.dumps(response1.json())
)

with tempfile.TemporaryDirectory() as tmp:
    with open(f"{tmp}/audi.wav", "wb") as f:
        f.write(response2.content)
        wav_obj = simpleaudio.WaveObject.from_wave_file(f"{tmp}/audi.wav")
        play_obj = wav_obj.play()
        play_obj.wait_done()



# VOICEVOXエンジンを開いておいてください。
