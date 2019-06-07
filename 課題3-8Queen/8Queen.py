import pygame

framerate = 60
TileNum = 8 #タイルの数
TileSize = 40 #タイルの大きさ

TileWidth = TileNum * TileSize  #タイル全体の最終的な横幅
TileHeight = TileNum * TileSize #タイル全体の最終的な縦幅

def main():
    pygame.init()
    pygame.font.init()
    screen = pygame.display.set_mode((520,520)) #画面幅
    clock = pygame.time.Clock()
    
    font_type = pygame.font.Font(None,10)
    font1 = font_type.render("Q",True,(0,0,0))

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
                    print(mouse_x // 40)
                    print(mouse_y // 40)
                    #screen.blit(font1,450,450)
                    pygame.draw.rect(screen,(255,0,0),(100 + (mouse_x // 40 * 40),100 + (mouse_y // 40 * 40),TileSize + 1,TileSize +1))
                    
            
        clock.tick(framerate)
    
        pygame.display.flip()
    
    pygame.quit()
    
if __name__ == '__main__': main()