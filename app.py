#Flaskとrender_template（HTMLを表示させるための関数）をインポート
#ライブラリを使用する際のお約束
from flask import Flask,render_template, request, url_for
import medication

#Flaskオブジェクトの生成
#Flaskのクラスをインスタンス化している
app = Flask(__name__)

#デコレーターという機能を使ったルーティングの設定
#ルーティングとは、URLと処理を対応づけること、Flaskのルーティングは、URLとfuncitonを紐付けます。ルーティングには、route() を用います。
#「/index」へアクセスがあった場合に、「index.html」を返す
@app.route("/")
def index():
    return render_template('index.html', title='pediatric-med-calculator')

@app.route("/result", methods=['POST'])
def calculation():
    age = int(request.form.get('age'))
    BW = int(request.form.get('BW'))
    asberin_p = request.form.get('asberin_p')
    asberin_s = request.form.get('asberin_s')
    mukodain_p = request.form.get('mukodain_p')
    mukodain_s = request.form.get('mukodain_s')
    hokunarin = request.form.get('hokunarin')

    result = list()

    if asberin_p == "y":
        result.append(medication.asberin_p(BW))
    if asberin_s == "y":
        result.append(medication.asberin_s(BW))
    if mukodain_p == "y":
        result.append(medication.mukodain_p(BW))
    if mukodain_s == "y":
        result.append(medication.mukodain_s(BW))
    if hokunarin == "y":
        result.append(medication.hokunarin(age))

    return render_template('result.html',result=result)

#おまじない
if __name__ == '__main__':
    app.run(debug=True)
