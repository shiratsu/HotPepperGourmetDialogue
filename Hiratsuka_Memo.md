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

```
---------sys_act_type--------------
{'user_act_type': 'other', 'GENRE': '和食', 'sys_act_type': 'REQUEST_LOCATION'}
```

上記モデルがどうやって作られたか

## その後
act_typeがわかったのち、例えば、act_type=ジャンルがわかったのち、

そのact_typeに沿ったどのキーワードが検索対象になるか、抜き出す。

dialogue_actにセット

## 会話の推定
セットしたものを、DialogueStateの状態情報に使う。



## モデルの元データ
training_data_dirにある

DialogueActTypePredictorで使ってるモデルもあらかじめ訓練されたもの

それをどうやって作っているか。

### 分類用のモデルの作成
DialogueActType/predictor.pyで作っている。
dic.txtをベース

training_dataディレクトリに、３タイプのモデル
genre,location,maximum_amount,otherがある

例えば、genreは、食べ物関連が保存されている
これが、文章から検出されたら、genreですと分類するモデルを作る。

```
[[['1', '名詞', '数', '*', '*', '*', '*', '*', 'B-MAXIMUM_AMOUNT'], [',', '名詞', 'サ変接続', '*', '*', '*', '*', '*', 'I-MAXIMUM_AMOUNT'], ['832', '名詞', '数', '*', '*', '*', '*', '*', 'I-MAXIMUM_AMOUNT'], ['円', '名詞', '接尾', '助数詞', '*', '*', '*', '円', 'エン', 'エン', 'O'], ['くらい', '助詞', '副助詞', '*', '*', '*', '*', 'くらい', 'クライ', 'クライ', 'O']], [['どんな', '連体詞', '*', '*', '*', '*', '*', 'どんな', 'ドンナ', 'ドンナ', 'O'], ['こと', '名詞', '非自立', '一般', '*', '*', '*', 'こと', 'コト', 'コト', 'O'], ['を', '助詞', '格助詞', '一般', '*', '*', '*', 'を', 'ヲ', 'ヲ', 'O'], ['手伝い', '動詞', '自立', '*', '*', '五段・ワ行促音便', '連用形', '手伝う', 'テツダイ', 'テツダイ', 'O'], ['ます', '助動詞', '*', '*', '*', '特殊・マス', '基本形', 'ます', 'マス', 'マス', 'O'], ['か', '助詞', '副助詞／並立助詞／終助詞', '*', '*', '*', '*', 'か', 'カ', 'カ', 'O'], ['？', '記号', '一般', '*', '*', '*', '*', '？', '？', '？', 'O']], [['7', '名詞', '数', '*', '*', '*', '*', '*', 'B-MAXIMUM_AMOUNT'], [',', '名詞', 'サ変接続', '*', '*', '*', '*', '*', 'I-MAXIMUM_AMOUNT'], ['372', '名詞', '数', '*', '*', '*', '*', '*', 'I-MAXIMUM_AMOUNT'], ['円', '名詞', '接尾', '助数詞', '*', '*', '*', '円', 'エン', 'エン', 'O']], [['9715', '名詞', '数', '*', '*', '*', '*', '*', 'B-MAXIMUM_AMOUNT'], ['円', '名詞', '接尾', '助数詞', '*', '*', '*', '円', 'エン', 'エン', 'O'], ['以下', '名詞', '非自立', '副詞可能', '*', '*', '*', '以下', 'イカ', 'イカ', 'O']], [['8347', '名詞', '数', '*', '*', '*', '*', '*', 'B-MAXIMUM_AMOUNT'], ['円', '名詞', '接尾', '助数詞', '*', '*', '*', '円', 'エン', 'エン', 'O'], ['以下', '名詞', '非自立', '副詞可能', '*', '*', '*', '以下', 'イカ', 'イカ', 'O']], [['雨', '名詞', '一般', '*', '*', '*', '*', '雨', 'アメ', 'アメ', 'O'], ['は', '助詞', '係助詞', '*', '*', '*', '*', 'は', 'ハ', 'ワ', 'O'], ['嫌い', '名詞', '形容動詞語幹', '*', '*', '*', '*', '嫌い', 'キライ', 'キライ', 'O'], ['だ', '助動詞', '*', '*', '*', '特殊・ダ', '基本形', 'だ', 'ダ', 'ダ', 'O'], ['けど', '助詞', '接続助詞', '*', '*', '*', '*', 'けど', 'ケド', 'ケド', 'O'], ['ね', '助詞', '終助詞', '*', '*', '*', '*', 'ね', 'ネ', 'ネ', 'O']], [['1927', '名詞', '数', '*', '*', '*', '*', '*', 'B-MAXIMUM_AMOUNT'], ['円', '名詞', '接尾', '助数詞', '*', '*', '*', '円', 'エン', 'エン', 'O']], [['8', '名詞', '数', '*', '*', '*', '*', '*', 'B-MAXIMUM_AMOUNT'], [',', '名詞', 'サ変接続', '*', '*', '*', '*', '*', 'I-MAXIMUM_AMOUNT'], ['579', '名詞', '数', '*', '*', '*', '*', '*', 'I-MAXIMUM_AMOUNT'], ['円', '名詞', '接尾', '助数詞', '*', '*', '*', '円', 'エン', 'エン', 'O']], [['キンキン', '副詞', '一般', '*', '*', '*', '*', 'キンキン', 'キンキン', 'キンキン', 'O'], ['に', '助詞', '副詞化', '*', '*', '*', '*', 'に', 'ニ', 'ニ', 'O'], ['冷やし', '動詞', '自立', '*', '*', '五段・サ行', '連用形', '冷やす', 'ヒヤシ', 'ヒヤシ', 'O'], ['た', '助動詞', '*', '*', '*', '特殊・タ', '基本形', 'た', 'タ', 'タ', 'O'], ['やつ', '名詞', '代名詞', '一般', '*', '*', '*', 'やつ', 'ヤツ', 'ヤツ', 'O'], ['は', '助詞', '係助詞', '*', '*', '*', '*', 'は', 'ハ', 'ワ', 'O'], ['本当に', '副詞', '一般', '*', '*', '*', '*', '本当に', 'ホントウニ', 'ホントーニ', 'O'], ['おいしい', '形容詞', '自立', '*', '*', '形容詞・イ段', '基本形', 'おいしい', 'オイシイ', 'オイシイ', 'O'], ['です', '助動詞', '*', '*', '*', '特殊・デス', '基本形', 'です', 'デス', 'デス', 'O'], ['よ', '助詞', '終助詞', '*', '*', '*', '*', 'よ', 'ヨ', 'ヨ', 'O'], ['ね', '助詞', '終助詞', '*', '*', '*', '*', 'ね', 'ネ', 'ネ', 'O']], [['ゲーム', '名詞', '一般', '*', '*', '*', '*', 'ゲーム', 'ゲーム', 'ゲーム', 'O'], ['で', '助詞', '格助詞', '一般', '*', '*', '*', 'で', 'デ', 'デ', 'O'], ['財布', '名詞', '一般', '*', '*', '*', '*', '財布', 'サイフ', 'サイフ', 'O'], ['が', '助詞', '格助詞', '一般', '*', '*', '*', 'が', 'ガ', 'ガ', 'O'], ['寂しい', '形容詞', '自立', '*', '*', '形容詞・イ段', '基本形', '寂しい', 'サビシイ', 'サビシイ', 'O'], ['です', '助動詞', '*', '*', '*', '特殊・デス', '基本形', 'です', 'デス', 'デス', 'O']]]
-------labels-----------
['maximum_amount', 'other', 'maximum_amount', 'maximum_amount', 'maximum_amount', 'other', 'maximum_amount', 'maximum_amount', 'other', 'other']
```

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
