# ジャンル推定
DialogueActTypePredictorで行なっている
ジャンル自体は、あらかじめトレーニングしたものから推定

# トレーニングデータ
training_dataディレクトリに入っている
この中にtemplatesとかもあるので、質問用のテンプレートも入ってる

# 流れ
language_understandingが呼ばれて、そこから
predictorのsent2features_
で形態素解析
surfaces_でmecab使ってうまいことして
bowの辞書を初期化
to_featuresでベクトルに変換
RandomForestClassifierを使って、act_typeを推定している
上記モデルがどうやって作られたか


## モデルの元データ
training_data_dirにある
DialogueActTypePredictorで使ってるモデルもあらかじめ訓練されたもの
それをどうやって作っているか。

### ジャンルデータや、位置情報データのモデル作成
ontologyのgenre.yamlがベース
genre_maker.pyで、genre.txtを作っている
そこから、
training_data_factory.pyで、genreや位置、お金のモデルを作っている
例えば、

words/genre.txtにワードが
templates/genre.txtにテンプレートがあり
その２つを組み合わせて、例えば、
「ラーメンが食べたい」という文章を作成して、
形態素解析で、分析
さらに、IOB2でタグ付け。
それを、モデルとして、保存する。
