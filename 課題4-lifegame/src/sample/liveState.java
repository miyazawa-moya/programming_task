package sample;

class liveState extends rectState{
    private static liveState s = new liveState();
    public static rectState getInstance(){
        return s;
    }


    @Override
    public void live(rect livechange) {
        //live状態なので何もしない
    }

    @Override
    public void death(rect deathchange) {
        //live状態からdeath状態に変更
        deathchange.changeState(deathState.getInstance());
    }

    public String toString(){
        return "生きています";
    }
}
