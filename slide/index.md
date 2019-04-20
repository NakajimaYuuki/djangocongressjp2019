---

theme　: "Solarized"  
transition: 'default'

---

### Make Query Great Agarin!

- 話すこと
  - DjangoのOR/Mapperでのselect全般
- 対象
  - 初心者
  - select時にfilterやexcludeしか分からない
  - O/RM？SQL書けばいいのでは？

---

## Make Query Great again!

Nakajima Yuuki

---

## 自己紹介

- Django歴3年ぐらい
- Web歴3年ぐらい
- C0B0L歴5年ぐらい
- 日本システム技研
- twitter @propretariat

---

## Purpose

Djanoのselectでもう悩まない！

---

### story
やばい寿司屋さんこと

---

### models

pass

---

#### 全件取得
  
~~~python
Sale.objects.all()
~~~

~~~SQL
select * from sisi_app_sales;
~~~

---

### ソートしてくれ

~~~python
Sale.objects.all().order_by('-sales_date')
~~~

~~~SQL
select * from sisi_app_sales order sales_date DESC;
~~~

---

### 寿司ネタで検索したい

~~~python
Sale.objects.filter(name="マグロ").order_by('-sales_date')
~~~

~~~SQL
select * from sisi_app_sales where name = 'マグロ' order sales_date DESC;
~~~

---

---

### 寿司ネタでand検索したい

~~~python
Sale.objects.filter(name="マグロ", sales_date_="今日").order_by('-sales_date')
~~~

~~~SQL
select * from sisi_app_sales where name = 'マグロ' order sales_date DESC;
~~~


---

### 寿司ネタでor検索したい

Qオブジェクトの使い方
 - 自在にQueyを作れる
 - or もandも作れる
 -　filiterng条件を組み立てるときに使う

~~~python
q = Q(name="マグロ")
q |= Q(name="カルフォルニアロール")
Sale.objects.filter(q).order_by('-sales_date')
~~~

~~~SQL
TODO
~~~
