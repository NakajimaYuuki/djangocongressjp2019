### メモ

#### 伝えたいこと(45分)
- 前処理(3分)  
  - 自己紹介 
  - アジェンダ
- 本編（35分）
  - 基礎編(20分)　−＞　この辺はゆっくりやる 
    - model定義と実際のデータベース、特にFKとmany to many　について 
    - filterとexclude 実際のsqlも提示しつつ
    - order_by と limit
    - コラム(single objectとquery set)
    - Qオブジェクト(or　検索や条件でフィルターを変えたいとき)
    - 配列やJSONフィールドに対するクエリ(postgresやMYSQLの違いに注意)
　- 応用編(15分)
　  - annotateやwindow関数などの応用的なクエリ発行方法
    - Custom managersの紹介
    - selected_related,prefetch_relatedについて
      -　おまけ:最速のクエリはキャッシュ
    - postgres/mysql/sqlite3での違いについて

###　伝え方をどうする
- ストーリーモード、要件に合わせてどんどん実装していく感じ
- tipsモード；queryをひたすら紹介していく、面白みはない・・


###　ストーリーモード
-　○○データーベース
- アイドルマスタ(not アイドルマスター) 
  − 周りに通じるか不安。。。タイトルとあまり繋がりがない、知らない人にも笑って貰えるようにするには？
-　政治ネタは御法度！（トランプ大統領ネタ）
- ミュージシャンマスタ
  - というふりをしたアイドルマスタ？
- 狂気を感じるものが良いな・・
- モデルはシンプルなのがいい。。 A ,　B, C many to many ぐらい
- 知識にたよらないもの、誰かを傷つけないもの
- オカルトネタとか？（今オカルト少年とかいなくね？）
- 
###　入れたい小ネタ
 - make query great again -> yes we can!
 