import pygame


pygame.init()
screen = pygame.display.set_mode((640, 640))
clock = pygame.time.Clock()
running = True

Matrix = [["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR"],  
    ["bP", "bP", "bP", "bP", "bP", "bP", "bP", "bP"],  
    ["--", "--", "--", "--", "--", "--", "--", "--"],  
    ["--", "--", "--", "--", "--", "--", "--", "--"],  
    ["--", "--", "--", "--", "--", "--", "--", "--"],  
    ["--", "--", "--", "--", "--", "--", "--", "--"],  
    ["wP", "wP", "wP", "wP", "wP", "wP", "wP", "wP"],
    ["wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"]]



OG_blackRock = pygame.image.load("assets/B_Rook.png")
scaled_BRock = pygame.transform.scale(OG_blackRock , ( 40 , 80))

OG_blcackKnight = pygame.image.load("assets/B_Knight.png")
scaleB_Knight = pygame.transform.scale(OG_blcackKnight , (40 , 80 ))

OG_B_bishop = pygame.image.load("assets/B_Bishop.png")
scaleB_Bishop = pygame.transform.scale(OG_B_bishop , (40 , 80 ))

OG_B_queen = pygame.image.load("assets/B_Queen.png")
scaleB_Queen = pygame.transform.scale(OG_B_queen , (40 , 80 ))

OG_B_King = pygame.image.load("assets/B_King.png")
scaleB_King = pygame.transform.scale(OG_B_King , (40 , 80 ))

OG_B_pawn = pygame.image.load("assets/B_Pawn.png")
scaleB_Pawn = pygame.transform.scale(OG_B_pawn , (40 , 80 ))

OG_WightRook = pygame.image.load("assets/W_Rook.png")
scaleW_Rook = pygame.transform.scale(OG_WightRook , (40 , 80 ))

OG_WightKnight = pygame.image.load("assets/W_Knight.png")
scaleW_Knight = pygame.transform.scale(OG_WightKnight , (40 , 80 ))

OG_WightBishop = pygame.image.load("assets/W_Bishop.png")
scaleW_Bishop = pygame.transform.scale(OG_WightBishop , (40 , 80 ))

OG_WightQueen = pygame.image.load("assets/W_Queen.png")
scaleW_Queen = pygame.transform.scale(OG_WightQueen , (40 , 80 ))

OG_WightKing = pygame.image.load("assets/W_King.png")
scaleW_King = pygame.transform.scale(OG_WightKing , (40 , 80 ))

OG_WightPawn = pygame.image.load("assets/W_Pawn.png")
scaleW_Pawn = pygame.transform.scale(OG_WightPawn , (40 , 80 ))




def pieces(P,currentX , currentY):
    match P:
        case "bR":
            screen.blit(scaled_BRock , (currentX+18 , currentY-15))
        case "bN":
            screen.blit(scaleB_Knight , (currentX+18 , currentY-15))
        case "bB":
            screen.blit(scaleB_Bishop , (currentX+18 , currentY-15))
        case "bQ":
            screen.blit(scaleB_Queen , (currentX+18 , currentY-15))
        case "bK":
            screen.blit(scaleB_King , (currentX+18 , currentY-15))
        case "bP":
            screen.blit(scaleB_Pawn , (currentX+18 , currentY-15))
        case "wR":
            screen.blit(scaleW_Rook , (currentX+18 , currentY-15))
        case "wN":
            screen.blit(scaleW_Knight , (currentX+18 , currentY-15))
        case "wB":
            screen.blit(scaleW_Bishop , (currentX+18 , currentY-15))
        case "wQ":
            screen.blit(scaleW_Queen , (currentX+18 , currentY-15))
        case "wK":
            screen.blit(scaleW_King , (currentX+18 , currentY-15))
        case "wP":
            screen.blit(scaleW_Pawn , (currentX+18 , currentY-15))

def BoardInit(): # to init the board outside of the game loop 
    
    weigth = 80 
    height = 80
    currentX = 0
    currentY = 0
    switch1=1

    for i in range(8):
        currentX = 0
        switch1+=1

        for j in range(8):
            if  switch1%2==0: # even
                pygame.draw.rect(screen, (240, 217, 181), (currentX , currentY , weigth ,height))
            else:
                pygame.draw.rect(screen, (118, 150, 86), (currentX , currentY , weigth ,height))
    
            pieces( Matrix[i][j] , currentX , currentY )

            currentX += 80
            switch1+=1
    
        currentY += 80



# def move(name,x,y):
#     match name:
#         case "bR":
#             MoveRock(x,y)
#         case "bN":
#             MoveKnight(x,y)
#         case "bB":
#             MoveBishop(x,y)
#         case "bQ":
#             MoveQueen(x,y)
#         case "bK":
#             MoveKing(x,y)
#         case "bP":
#             MovePawn(x,y)
        
    
   



    

    
while running:
     
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type==pygame.MOUSEBUTTONDOWN:
            x,y=pygame.mouse.get_pos()
            
           
            

    screen.fill("gray")
    BoardInit()

    
    pygame.display.flip()

    clock.tick(60)  # FPS 

pygame.quit()
