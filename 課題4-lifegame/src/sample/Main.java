package sample;

import javafx.animation.PauseTransition;
import javafx.application.Application;
import javafx.scene.Group;
import javafx.scene.Scene;
import javafx.scene.canvas.Canvas;
import javafx.scene.canvas.GraphicsContext;
import javafx.stage.Stage;
import javafx.util.Duration;

import java.util.Random;


public class Main extends Application {
    //一マスの状態を入れる二次元配列
    private rect[][] rectInstance = new rect[25][25];

    private boolean continueFlag = true;

    @Override
    public void start(Stage primaryStage) throws Exception{
        //シーングラフの根となるインスタンス生成
        Group root = new Group();
        //キャンバス生成
        Canvas canvas = new Canvas(645,645);
        //canvasのコンテキスと取得
        GraphicsContext gc = canvas.getGraphicsContext2D();

        //画面に25*25個の四角を描画
        for(int i=0; i<rectInstance.length; i++) {
            for(int j=0; j<rectInstance.length; j++) {
                int x = 10 + (j * 25); //四角を配置するx座標
                int y = 10 + (i * 25); //四角を配置するy座標
                //縦横20の四角を隙間20で25個配置
                gc.strokeRect(x, y, 20, 20);
                //二次元配列で一マスの状態を表現
                rectInstance[i][j] = new rect(x,y);

                // 1/8の確率でランダムに生物を発生
                Random rand = new Random();
                int r = rand.nextInt(8);
                if(r == 1) rectInstance[i][j].revival(gc);

                //マスの状態を出力　rectInstance[i][j].print();
            }
        }

        //rootの下にcanvasを追加
        root.getChildren().add(canvas);
        //rootを元にシーンを追加
        Scene scene = new Scene(root);
        //StageにSceneを追加
        primaryStage.setScene(scene);
        //Stageを表示
        primaryStage.show();

        //3秒ごとにliveの周りを確認
        showMessage();
    }


    private void showMessage() {
        // 3000ミリ秒ごとに実行する
        PauseTransition p = new PauseTransition(Duration.millis(3000));
        p.setOnFinished(e->{

            for(int i=0; i<rectInstance.length; i++) {
                for (int j = 0; j < rectInstance.length; j++) {
                    if (rectInstance[i][j].checkState() == true) {
                        rectInstance[i][j].print();
                    }
                }
            }
            if(continueFlag) {
                //continueFlagがtrueであれば、またこのメソッドを呼び出す
                showMessage();
            }
        });
        p.play();
    }


    public static void main(String[] args) {
        launch(args);
    }
}
