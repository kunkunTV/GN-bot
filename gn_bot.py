import os, random
from datetime import datetime

# 簡単なG&Nテンプレート
gn_templates = [
    "今日のG&N：80歳の患者さんが『歯が痛くなくなって、孫とおせんべい食べられる！』と涙ぐんでくれた。船橋市で予防歯科を続けてきてよかった。",
    "今日の嬉しかったこと：小学生の男の子が『歯医者さん、将来なりたい！』と言ってくれた。キャンディをくれる患者さんも嬉しいけど、これが一番のご褒美😭",
    "グッド＆ニュー：スタッフが自主的に新しい予防器具の練習をしていた。『先生、これ楽しいです！』って。こんなチームを持てて私は幸せ者です。"
]

gn_text = random.choice(gn_templates)
today = datetime.now().strftime("%Y/%m/%d")
gn_text = f"📅 {today}\n{gn_text}\n#グッドアンドニュー #歯科医院地域一番実践会 #船橋歯科"

# 顔画像を取得（後でfacesフォルダを作ります）
try:
    face_files = [f for f in os.listdir("faces") if f.endswith((".jpg", ".png"))]
    if face_files:
        selected_face = random.choice(face_files)
        print(f"使用画像: {selected_face}")
    else:
        print("⚠️ facesフォルダに画像がありません")
except:
    print("⚠️ facesフォルダがまだありません")

print(f"投稿内容:\n{gn_text}")
print("✅ 処理完了")
