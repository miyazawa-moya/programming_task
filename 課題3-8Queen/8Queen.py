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
                    tile_pointX = mouse_x // 40 #クリックしたタイルの指標配置X
                    tile_pointY = mouse_y // 40 #クリックしたタイルの指標配置Y
                    print(tile_pointX)
                    print(tile_pointY)
                    font1 = font_type.render("Q",True,(0,0,0))
                    screen.blit(font1,(112 + (tile_pointX * 40),112 + (tile_pointY * 40)))
                    for square in range(TileNum):
                        pygame.draw.rect(screen,(255,0,0),(100 + square * 40 , 100 + tile_pointY * 40,TileSize + 1,TileSize +1))
                        pygame.draw.rect(screen,(255,0,0),(100 + tile_pointX * 40 , 100 + square * 40, TileSize + 1,TileSize +1))
                        
                    ####  斜めのプログラムが汚いので綺麗にしたい　####
                    count = 1
                    while(tile_pointX + count < 8 and tile_pointY + count < 8):
                        pygame.draw.rect(screen,(255,0,0),(100 + (tile_pointX + count) * 40   , 100 + (tile_pointY + count) * 40 ,TileSize + 1,TileSize +1))
                        count+=1
                    count = -1
                    while(tile_pointX + count >= 0 and tile_pointY + count >= 0):
                        pygame.draw.rect(screen,(255,0,0),(100 + (tile_pointX + count) * 40   , 100 + (tile_pointY + count) * 40 ,TileSize + 1,TileSize +1))
                        count-=1
                    count = -1
                    while(tile_pointX + count >= 0 and tile_pointY - count < 8):
                        pygame.draw.rect(screen,(255,0,0),(100 + (tile_pointX + count) * 40   , 100 + (tile_pointY - count) * 40 ,TileSize + 1,TileSize +1))
                        count-=1
                    count = -1
                    while(tile_pointX - count < 8 and tile_pointY + count >= 0):
                        pygame.draw.rect(screen,(255,0,0),(100 + (tile_pointX - count) * 40   , 100 + (tile_pointY + count) * 40 ,TileSize + 1,TileSize +1))
                        count-=1
                    ####  斜めのプログラムが汚いので綺麗にしたい　####
            
        clock.tick(framerate)
    
        pygame.display.flip()
    
    pygame.quit()
    
if __name__ == '__main__': main()