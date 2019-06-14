import pygame
from mutagen.mp3 import MP3 as mp3

framerate = 60
TileNum = 8 #タイルの数
TileSize = 40 #タイルの大きさ

TileWidth = TileNum * TileSize  #タイル全体の最終的な横幅
TileHeight = TileNum * TileSize #タイル全体の最終的な縦幅

tile_list = [
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        ]

def draw(screen,TileX,TileY):
    if tile_list[TileY][TileX] == 0:
        tile_list[TileY][TileX] = 1
        pygame.draw.rect(screen,(255,0,0),(100 + TileX * 40,100 + TileY * 40,TileSize + 1,TileSize +1))
        
def playMusic(filename):
    pygame.mixer.init(frequency = 44100, size = -16, channels = 2, buffer = 1024)
    pygame.mixer.music.load(filename)     # 音楽ファイルの読み込み
    pygame.mixer.music.play()             # 音楽の再生回数(ループ再生)

    

def main():
    Qcount = 0 #Qの数カウント変数
    pygame.init()
    pygame.font.init()
    screen = pygame.display.set_mode((520,520)) #画面幅
    clock = pygame.time.Clock()
    
    font_type = pygame.font.Font(None,32)

    endflg = False
    
    screen.fill((255,255,255))
    
    #タイル作成のためrectを8*8描画
    for i in range(0,TileHeight,TileSize):
        for j in range(0,TileWidth,TileSize):
            pygame.draw.rect(screen,(0,0,0),(100 + j,100 + i,TileSize,TileSize),2 ) #x,y=100が基準値

    #メインのプログラム
    while endflg == False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                endflg = True
    
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x = pygame.mouse.get_pos()[0] -100 #マウスx座標から基準値100を引く
                mouse_y = pygame.mouse.get_pos()[1] -100 #マウスy座標から基準値100を引く
                
                if (mouse_x > 0 and mouse_x < TileWidth) and (mouse_y > 0 and mouse_y < TileHeight) : 
                    #マウスダウンがタイル内の時
                    tile_pointX = mouse_x // 40 #クリックしたタイルのインデックス配置X
                    tile_pointY = mouse_y // 40 #クリックしたタイルのインデックス配置Y
                    
                    #タイルリストのフラグが0だった時フラグを立てて色を塗る
                    if tile_list[tile_pointY][tile_pointX] == 0:
                        tile_list[tile_pointY][tile_pointX] = 1
                        Qcount+=1
                        #print(Qcount)
                        #print(tile_pointX)
                        #print(tile_pointY)
                    
                        #Qの文字を印字
                        font1 = font_type.render("Q",True,(0,0,0))
                        screen.blit(font1,(112 + (tile_pointX * 40),112 + (tile_pointY * 40)))
                        
                        #縦と横を赤で塗るループ
                        for square in range(TileNum):
                            draw(screen, square , tile_pointY) #マウスクリック座標を起点に横に色を塗る
                            draw(screen, tile_pointX , square) #マウスクリック座標を起点に縦に色を塗る
                        
                    ####  斜めのプログラムが汚いので綺麗にしたい　####
                        count = 1
                        while(tile_pointX + count < 8 and tile_pointY + count < 8):
                            draw(screen,tile_pointX + count,tile_pointY + count)
                            count+=1
                        count = -1
                        while(tile_pointX + count >= 0 and tile_pointY + count >= 0):
                            draw(screen,tile_pointX + count,tile_pointY + count)
                            count-=1
                        count = -1
                        while(tile_pointX + count >= 0 and tile_pointY - count < 8):
                            draw(screen,tile_pointX + count,tile_pointY - count)
                            count-=1
                        count = -1
                        while(tile_pointX - count < 8 and tile_pointY + count >= 0):
                            draw(screen,tile_pointX - count,tile_pointY + count)
                            count-=1
                    ####  斜めのプログラムが汚いので綺麗にしたい　####
                    
                    ###ゲームクリアフラグ###
                        if Qcount == 8:
                            GameClear = font_type.render("GameClera",True,(0,0,0))
                            screen.blit(GameClear,(210,450))
                            playMusic("sound/fanfare.wav")
                            break
                    
                        GameOverFlag = 0
                        if Qcount > 4:
                            for i in tile_list:
                                for j in i:
                                    if j == 0 : break
                                else:
                                    GameOverFlag+=1
                                    continue
                                break
                        
                        if GameOverFlag == 8:
                            GameOver = font_type.render("GameOver",True,(0,0,0))
                            screen.blit(GameOver,(210,450))
                            playMusic("sound/GameOver.mp3")
                            break
                    ###ゲームクリアフラグ###
                        
        clock.tick(framerate)
    
        pygame.display.flip()
    
    pygame.quit()
    
if __name__ == '__main__': main()