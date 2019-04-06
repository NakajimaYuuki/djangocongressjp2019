# メモ

## 伝えたいこと(45分)

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

## 伝え方をどうする

- ストーリーモード、要件に合わせてどんどん実装していく感じ
- tipsモード；queryをひたすら紹介していく、面白みはない・・

## ストーリーモード

-　システムを動かして実演しつつは大変、実際にとても（スクショで対応か）
- スライドは英語で作ろうかな(英語圏向けにもなる)

##　ストーリー詳細

- 簡単な一覧画面だけ用意
- 普通のモデル、fk、M2Mは宣言させたい
- PresidentM@ster

## Presidentマスター

## DjangoConのプレゼン一覧

アイドル情報データベースを作ろう

- Idle
  - user (one to one)
  - idle_group(m2m, blank=True)
  - features(json)
  - is_retired(default=False)

- IdleGroup
  - name
  - start_date
  - end_date(null=True)
  - genre(m2m)
  - features(json)

- Genre
  - name

## 入れたい小ネタ

## 課題　スライドは何で作る？

- Google　slideが楽？
- 普通のスライド(google slide) 
- Reveal.jsとか？

### Presentationの方法

- 参考　https://www.youtube.com/watch?v=7fGdwBd_Yuk
  - 最初に目的を言う
  - 信頼性を担保する話し方をする、長く話すパートと短く話すパートを分ける
  - コアメッセージは短くする
  -　説明だけでプレゼンをする意味はない
  - 未来のことを話さないと意味はない
  - 自分事にする
  - 相手を幸せにする
  - カリスマっぽく見えるプレゼン(フレーズを入れる：これからは○○の時代です！など)
  - 自分のプレゼンス型をビデオに撮って欲しい
    - 自分の立ち方を理解する
    - 手の位置を理解する(手は胸の前に置いておく)
    - 声の出し方(鼻腔共鳴)
    - カラオケボックスで練習する