package sample;

class deathState extends rectState {
    private static deathState s = new deathState();

    public static rectState getInstance(){
        return s;
    }

    @Override
    public void live(rect livechange) {
        //death状態からlive状態に変更
        livechange.changeState(liveState.getInstance());
    }

    @Override
    public void death(rect deathchange) {
        //death状態なので何もしない
    }

    public String toString(){
        return "死んでいます";
    }
}
