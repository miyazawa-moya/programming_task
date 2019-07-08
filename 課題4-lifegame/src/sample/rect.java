package sample;
import javafx.scene.canvas.GraphicsContext;
import javafx.scene.paint.Color;

class rect {
    //今現在のrectの状態を表す変数
    private rectState myState;
    private int posX;
    private int posY;

    //初期状態はdeathに設定
    public rect(int x,int y){
        myState = deathState.getInstance();
        this.posX = x;
        this.posY = y;
    }

    //death状態の時にlive状態に変更するメソッド
    public void revival(GraphicsContext gc){
        myState.live(this);
        //コンテキストを取得し黒色を塗る
        gc.setFill(Color.BLACK);
        gc.fillRect(this.posX,this.posY,20,20);
    }

    //live状態の時death状態にするメソッド
    public void dead(GraphicsContext gc){
        myState.death(this);
        //コンテキストを取得し白色を塗る
        gc.setFill(Color.WHITE);
        gc.fillRect(this.posX,this.posY,20,20);
    }

    //状態を変更
    public void changeState(rectState d){
        myState = d;
    }

    //四角がliveしてるかのチェック
    public boolean checkState(){
        return myState instanceof liveState;
    }

    public void print(){
        System.out.println(myState.toString());
    }
}
