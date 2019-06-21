var enemy_data = [];
var hero_main;

//キャラクター全体のクラス
class character{
    constructor(x,y,width,height,number){
    this.x = x;
    this.y = y;
    this.width = width;
    this.height = height;
    this.number = number;
    }

    draw(){
    var canvas = document.getElementById("canvas");
    var context = canvas.getContext("2d");
    if(this.type == "hero"){
        context.fillStyle = "red";
    }else{
        context.fillStyle = "blue";
    }
    context.fillRect(this.x,this.y,this.width,this.height);
    }

    get xdata(){return this.x;}
    get ydata(){return this.y;}
    get wdata(){return this.width + this.x;}
    get hdata(){return this.height + this.y;}

}

//自分クラス
class hero extends character{
    type = "hero";
}

class enemy extends character{
    type = "enemy" + this.number;
}

//ループ関数
function update(){
    for(var i=0; i<3; i++){
        if((hero_main.ydata < enemy_data[i].hdata && enemy_data[i].ydata < hero_main.hdata) && (hero_main.xdata < enemy_data[i].wdata && enemy_data[i].xdata < hero_main.wdata)){
            console.log(enemy_data[i].type + "が当たり");
        }
    }
    requestAnimationFrame(update);
}

//メイン関数
var main =function main(){
    //ここから初期設定

    //自機データを入力
    hero_main = new hero(120,100,70,100,1);
    //敵機データ入力
    enemy_data[0]= new enemy(50,60,100,50,1);
    enemy_data[1]= new enemy(10,120,100,50,2);
    enemy_data[2]= new enemy(165,115,70,70,3);
    
    //自機と敵機を描画
    hero_main.draw();
    for(var i=0; i<3; i++){
        enemy_data[i].draw();
    }

    //ここまで初期設定

    //ここからループ
    requestAnimationFrame(update);

}

main();
