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
フィールドは現在カードが渡っているかを表すuse,カードの数字を表すnumber,スートを表すsymbolを準備
