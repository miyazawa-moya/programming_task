課題１-当たり判定
====
## 考え方
### 入力データ  
自身のクラスであるheroクラスと敵クラスであるenemyクラスをx座標,y座標,高さ,横幅,キャラ番号を引数に生成。    
  
hero_main = new hero(120,100,70,100,1);  
enemy_data[0]= new enemy(50,60,100,50,1);  
enemy_data[1]= new enemy(10,120,100,50,2);  
enemy_data[2]= new enemy(165,115,70,70,3);  
  
### 判定アルゴリズム  
自身のオブジェクトと敵のオブジェクトの縦と横の重なりを判定する。  
  
自身のy座標 < 敵の高さ && 敵のy座標 < 自身の高さ　だった場合縦の重なりはありと判定  
hero_main.ydata < enemy_data[i].hdata && enemy_data[i].ydata < hero_main.hdata  
  
自身のx座標 < 敵の横幅　&&　敵のx座標 < 自身の横幅　だった場合横の重なりはありと判定  
hero_main.xdata < enemy_data[i].wdata && enemy_data[i].xdata < hero_main.wdata  
  
両方の判定がTrueだった場合出力を実行  
  
### 出力データ  
オブジェクトの番号データを元にconsole.logで出力  
console.log(enemy_data[i].type + "が当たり");  
  
  
  
  
課題２-ポーカーの役判定
====
## 考え方  
### 入力データ  
カード自身のクラスを用意。  
フィールドは現在カードが渡っているかを表す物,カードの数字を表す物,スートを表す物を準備  
use,number,symbol  (useフラグは1がカードを使用していない0がカードを使用している)
  
全カードデータを生成しオブジェクトを二次元配列に入れる。  
その際ジョーカーは1枚とする。  
card_data[i][13] = (i == 0)?new card(1,14,"JOKER"):new card(0,14,"JOKER");  
  
生成後ランダムに5枚カードを取り出し一次元配列に入れる。  
card_select[]  
その際スートとナンバーが全く同じカードは取り出さない処理をする。  
card_select[i] = card_data[a][b];  
card_data[a][b].card_use = 0;  
  
その後カードを昇順にソート。
  
### 判定アルゴリズム  
一番最初は数字が同じだった時の役判定をする。(ワンペア、ツーペア、スリーカード、フルハウス、フォーカード)  
配列の隣同士の数字が同じだった場合フラグに対し1を加算する。  
jokerが配列にある場合はとなり同士の同じカードがなくなった後フラグに数字を加算。  
same_number_flg++;(+=2は役の重み調整のため)  
その後フラグを元に役判定を行う。役のフラグを取り扱う変数に結果を代入。  
same_number_set_flg  
  
次にスートが同じだった時の役判定をする。(ストレート、フラッシュ、ストレートフラッシュ、ロイヤルストレートフラッシュ)  
この際フルハウスとフォーカードの判定が出ていた場合はここのスート判定は行わない。  
判定の際の利用変数  
連番判定変数 same_number_flg  
同一スート判定変数 same_symbole_flg  
その他役判定フラグ royal_flg,straight_flg,flash_flg  
その後フラグを元に役判定を行う。役のフラグを取り扱う変数に結果を代入。  
same_number_set_flg  
  
### 出力データ 
役のフラグを元に役の名前を出力。  
0:ハイカード、1:ワンペア、2:ツーペア、3:スリーペア、4:ストレート、5:フラッシュ、6:フルハウス、7:フォーカード、8:ストレートフラッシュ、9:ロイヤルストレートフラッシュ  
(スート判定の所にバグあり)
  
  
  
  
  
課題３-8Queen
====
## 考え方
### 入力データ  
タイルの配置を二次元のリストで表す。  
tile_list (0:塗りなし,1:塗りあり)
  
### 判定アルゴリズム 
マウスでクリックしたx,y座標を元にタイルのQを描画する場所を決定。(既に塗られている場所に描画は不可)  
Q描画位置を元に縦横斜めへ赤色を塗る。  
塗られたタイルのリストを更新。(リストの中身が1のタイルには塗らない)  
塗りとリスト更新後Qの数をカウントする。  
  
クリア判定  
Qのカウントが8個になった場合ゲームクリア。  
  
ゲームオーバー判定  
Qの数が4より大きくなった場合判定を始める。  
ループでリストの中身を取り出す。  
0が発見された場合塗られてない箇所があるとしてループを抜ける。  
1がリスト全部に代入されていた場合ゲームオーバーフラグがリストのy分加算され8になる。  
ゲームオーバーフラグが8だった場合ゲームオーバー。  

### 出力データ 
ゲームクリアの場合、fandare.wavを流す。  
ゲームオーバーの場合、GameOver.mp3を流す。
