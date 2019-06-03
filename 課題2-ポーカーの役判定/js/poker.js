class card{
    constructor(use,number,symbol){
        this.use = use;
        this.number = number;
        this.symbol = symbol;
    }

    get card_use(){return this.use;}
    get card_number(){return this.number;}
    get card_symbol(){return this.symbol;}
    set card_use(val){this.use = val;}
}

//画像表示関数
var img_show = function img_show(i , symbol, number){
    var card = document.getElementById("card" + i);
    var img = document.createElement("img");
    img.setAttribute("src" ,"img/" + symbol + "_" + number + ".png");
    card.appendChild(img);
}

var text_change = function text_change(text){
    var element = document.getElementById("judge_area");
    element.innerText = text;
}

var main = function main(){
    //カードの初期設定
    var card_data = new Array();　//カード情報の入った配列
    var card_select = new Array(6); //選ばれた5つのカード配列
    var symbol_data = ["spade","club","diamond","heart"];
    var same_number_flg = 0; //同じ数字が何枚続いているかのフラグ
    var same_number_set_flg = 0; //同じ数字のセットが何個あるかのフラグ
    var same_symbole_flg = 0; //同じスートフラグ
    var same_symbole_set_flg =0; //同じスートが5つあるフラグ
    var JOKER_flg = 0;
    var straight_flg = 0; 
    var flash_flg = 0;
    var royal_flg = 0;

    //二次元配列に数字と柄を持ったオブジェクトを生成
    for(var i=0; i<4; i++){
        card_data[i] = new Array();
        for(var j=0; j<13; j++){
            card_data[i][j] = new card(1,j+1,symbol_data[i]);
        }
        card_data[i][13] = (i == 0)?new card(1,14,"JOKER"):new card(0,14,"JOKER"); //配列の最後にJOKER挿入
    }

    //card_select配列にランダムな５つの数字を代入
    for(var i=0; i<5; i++){
        var a = Math.floor(Math.random()*4);
        var b = Math.floor(Math.random()*14);
        //カードの種類が重複しないための処理
        if(card_data[a][b].card_use != 0){
            card_select[i] = card_data[a][b];
            card_data[a][b].card_use = 0;
        }else{
            i--;
        }
    }

    //テストデータ用
    /*
    card_select[0] = card_data[0][10];
    card_select[1] = card_data[0][11];
    card_select[2] = card_data[0][12];
    card_select[3] = card_data[0][5];
    
    card_select[4] = card_data[0][13];
    */

    //最後にダミーを代入
    card_select[5] = new card(100,symbol_data[i]);

    //カードを昇順にソート
    card_select.sort(function(a,b){
        if(a.card_number < b.card_number) return -1;
        if(a.card_number > b.card_number) return 1;
        return 0;
    });

    //カードの画像を表示
    for(var i = 0; i < card_select.length - 1; i++){
        img_show(i , card_select[i].card_symbol , card_select[i].card_number);
    }

    //昇順にした配列を出力
    for(var i=0; i<5; i++){
        console.log(card_select[i].card_number);
        console.log(card_select[i].card_symbol);

        //隣同士の数字が同じだった場合
        if(card_select[i].card_number == card_select[i+1].card_number){
            same_number_flg++;
        }else{
        //同じ数字が続いていた個数をカウント
        if(card_select[4].card_number == 14 && JOKER_flg == 0){
            switch(same_number_flg){
                case 0:
                    if(i == 4) same_number_flg++;
                    break;
                case 1:
                    same_number_flg++;
                    break;
                case 2:
                    same_number_flg += 2;
                    break;
                case 3:
                    same_number_flg++;
                    break;
            }
            if(same_number_flg != 0) JOKER_flg = 1;
        }

        switch(same_number_flg){
            case 1:
                same_number_set_flg++; //ワンペア発見
                break;
            case 2:
                same_number_set_flg += 3; //スリーカード発見
                break;
            case 3:
                same_number_set_flg += 7; //フォーカード発見
                break;
            case 4:
                same_number_set_flg += 7; //フォーカード発見
                break;
        }
            same_number_flg = 0; //フラグを初期化
        }
    }

    //フルハウスの重み調整
    if(same_number_set_flg == 4) same_number_set_flg = 6;

    //ジョーカーフラグ初期化
    JOKER_flg = 0;

    //スリーカードより上の判定
    if(same_number_set_flg <= 3){
        //ストレート判定
        for(var i=0; i<4; i++){
            var number_a = card_select[i]; //比較数値１
            var number_b = card_select[i+1]; //比較数値２
                //連番比較
                console.log("number_a" + number_a.card_number + "== " + number_b.card_number);
                if(number_a.card_number + 1 == number_b.card_number && number_a.card_number != 10){
                    same_number_flg++;
                    console.log("a");
                }else if(number_a.card_number + 9 == number_b.card_number || card_select[4].card_symbol == "JOKER" && JOKER_flg == 0){
                    console.log("b");
                    console.log("JOKER" + JOKER_flg);
                    if(number_a.card_number == 1 && number_b.card_number == 10){
                        royal_flg = 1; //ロイヤルストレートフラッシュフラグを立てる
                    }
                    if(number_a.card_number == 1 && card_select[4].card_symbol == "JOKER" && JOKER_flg == 0 || card_select[4].card_symbol == "JOKER" && number_a.card_number == 10 && JOKER_flg == 0){
                        royal_flg = 1; //ロイヤルストレートフラッシュフラグを立てる
                        JOKER_flg = 1;
                        i--;
                        console.log("i   " +i);
                    }
                    if(card_select[4].card_symbol == "JOKER" && JOKER_flg == 0){
                        JOKER_flg = 1;
                        i--;
                        console.log("i   " +i);
                    }
                    same_number_flg++;
                }else{
                    same_number_flg -- ;
                }
                //スート比較
                if(number_a.card_symbol == number_b.card_symbol || number_b.card_symbol == "JOKER"){
                    same_symbole_flg++
                }
            }

            console.log("same_number_flg " + same_number_flg);
            console.log("same_symbol_flg " + same_symbole_flg);
            if(same_number_flg >= 4){
                same_number_set_flg = 4; //ストレート発見
                straight_flg = 1; //ストレートフラグを立てる
            }
            if(same_symbole_flg >= 4){
                same_number_set_flg = 5; //フラッシュ発見
                flash_flg = 1; //フラッシュフラグを立てる
            }

            if(straight_flg == 1 && flash_flg == 1) same_number_set_flg = 8; //ストレートフラッシュ判定
            if(royal_flg == 1 && flash_flg == 1) same_number_set_flg = 9; //ロイヤルストレートフラッシュ判定
        }

        console.log("same" + same_number_set_flg);
        console.log("straight" + straight_flg);
        console.log("flashu" + flash_flg);

    switch(same_number_set_flg){
        case 0:
            text_change("ハイカード");
            break;
        case 1:
            text_change("ワンペア");
            break;
        case 2:
            text_change("ツーペア");
            break;
        case 3:
            text_change("スリーペア");
            break;
        case 4:
            text_change("ストレート");
            break;
        case 5:
            text_change("フラッシュ");
            break;
        case 6:
            text_change("フルハウス");
            break;
        case 7:
            text_change("フォーカード");
            break;
        case 8:
            text_change("ストレートフラッシュ");
            break;
        case 9:
            text_change("ロイヤルストレートフラッシュ");
            break;
    }
}
window.onload = function(){
    main();
}
