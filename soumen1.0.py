#全体のプログラム
#ウィンドウを作るモジュールを呼び出す
from tkinter import*

#ランダムモジュールを読み込む
import random
import copy


#ウィンドウの作成
win = Tk()
cv = Canvas(win, width = 720, height = 480)
cv.pack()
win.title(u"流しそうめん")

#画面の描画
def draw_screen():
    #画面クリア
    cv.delete('all')
    #キャンバスの作成
    cv.create_rectangle(  0,  0, 720, 480, fill="white", width = 0 )

#背景描画
def haikei():
    cv.create_line     ( 0, 175, 800, 175, fill='gray', width = 5 ) #LINE1
    cv.create_line     ( 0, 225, 800, 225, fill='gray', width = 5 ) #LINE2
    cv.create_line     ( 0, 275, 800, 275, fill='gray', width = 5 ) #LINE3
    cv.create_line     ( 0, 325, 800, 325, fill='gray', width = 5 ) #LINE4
    cv.create_line     ( 0, 375, 800, 375, fill='gray', width = 5 ) #LINE5
    cv.create_line     ( 0, 425, 800, 425, fill='gray', width = 5 ) #LINE6
    cv.create_text     ( 100, 30, text="SCORE", font=("Helvetica", 35, "bold") )
    cv.create_text     ( 300, 30, text=score  , font=("Helvetica", 35, "bold") )
    if life>=1:
        cv.create_text     ( 480, 30, text="LIFE" , font=("Helvetica", 35, "bold") )
    elif life<=0:
        cv.create_text     ( 540, 30, text="GAME OVER" , font=("Helvetica", 35, "bold") )

    
def life_draw():
    global life
    if life == 3:
        heart(550)
        heart(600)
        heart(650)
    if life == 2:
        heart(550)
        heart(600)
    if life == 1:
        heart(550)

def heart(kokoro):
    cv.create_rectangle (   8+kokoro,   4+5,  16+kokoro,   8+5, fill='black' ) #ハートのドット絵描画
    cv.create_rectangle (  28+kokoro,   4+5,  36+kokoro,   8+5, fill='black' ) 
    cv.create_rectangle (   4+kokoro,   8+5,  20+kokoro,  12+5, fill='black' )
    cv.create_rectangle (  24+kokoro,   8+5,  40+kokoro,  12+5, fill='black' ) 
    cv.create_rectangle (   0+kokoro,  12+5,  44+kokoro,  24+5, fill='black' )
    cv.create_rectangle (   4+kokoro,  24+5,  40+kokoro,  28+5, fill='black' ) 
    cv.create_rectangle (   8+kokoro,  28+5,  36+kokoro,  32+5, fill='black' )
    cv.create_rectangle (  12+kokoro,  32+5,  32+kokoro,  36+5, fill='black' ) 
    cv.create_rectangle (  16+kokoro,  36+5,  28+kokoro,  40+5, fill='black' )
    cv.create_rectangle (  20+kokoro,  40+5,  24+kokoro,  44+5, fill='black' ) 
    
Amap =[ [ 0, 1, 2, 1, 0,   1, 0, 2, 0, 2,    3, 1, 0, 1, 2,   0, 0, 2, 0, 1,    0, 0, 0, 1, 2, ],
[ 0, 1, 1, 0, 0,   0, 1, 0, 0, 0,    1, 1, 2, 1, 0,   0, 0, 2, 2, 0,    0, 1, 3, 1, 0, ],
[ 2, 1, 2, 3, 2,   1, 1, 2, 3, 2,    3, 1, 3, 2, 2,   3, 1, 0, 0, 0,    0, 0, 1, 1, 0, ],
[ 0, 0, 1, 2, 0,   0, 1, 2, 0, 0,    1, 0, 1, 0, 1,   2, 1, 0, 2, 1,    1, 3, 0, 1, 3, ],
[ 2, 0, 0, 1, 2,   1, 3, 2, 3, 2,    1, 1, 3, 2, 2,   3, 2, 2, 2, 2,    2, 2, 2, 1, 2, ],

[ 1, 0, 1, 0, 1,   1, 0, 0, 0, 0,    0, 1, 3, 1, 0,   0, 0, 0, 1, 3,    0, 2, 0, 0, 1, ],
[ 0, 1, 2, 1, 0,   1, 0, 2, 0, 2,    3, 1, 0, 1, 2,   0, 0, 2, 0, 1,    0, 0, 0, 1, 2, ],
[ 0, 1, 1, 0, 0,   0, 1, 0, 0, 0,    1, 1, 2, 1, 0,   0, 0, 1, 2, 0,    0, 1, 3, 1, 0, ],
[ 2, 1, 2, 3, 2,   1, 1, 2, 3, 2,    3, 1, 1, 2, 1,   3, 1, 0, 0, 0,    0, 0, 1, 1, 0, ],
[ 0, 0, 1, 2, 0,   0, 1, 2, 0, 0,    1, 0, 1, 0, 1,   2, 1, 0, 2, 1,    1, 3, 0, 1, 3, ],

[ 2, 2, 2, 2, 2,   1, 1, 0, 1, 1,    2, 0, 0, 0, 2,   1, 1, 0, 1, 1,    2, 2, 2, 2, 2, ], #10
[ 0, 1, 1, 0, 0,   1, 0, 0, 1, 1,    0, 1, 3, 1, 1,   0, 0, 1, 0, 3,    0, 2, 1, 0, 1, ],
[ 2, 1, 2, 1, 2,   1, 2, 1, 2, 1,    2, 1, 2, 1, 2,   1, 2, 1, 2, 1,    2, 1, 2, 1, 2, ],
[ 0, 1, 1, 0, 0,   0, 1, 0, 0, 2,    1, 0, 2, 1, 0,   1, 0, 2, 2, 0,    0, 1, 3, 1, 3, ],
[ 2, 0, 2, 0, 2,   1, 0, 1, 3, 2,    3, 1, 1, 0, 2,   3, 1, 0, 0, 1,    0, 1, 0, 1, 0, ],

[ 3, 0, 1, 2, 0,   0, 3, 2, 0, 0,    1, 1, 0, 0, 1,   2, 1, 0, 2, 1,    0, 3, 1, 1, 0, ],
[ 1, 0, 0, 0, 1,   1, 0, 2, 3, 2,    0, 1, 3, 2, 2,   1, 2, 2, 2, 2,    2, 0, 2, 1, 2, ],
[ 0, 0, 1, 0, 0,   1, 3, 0, 0, 0,    0, 0, 3, 1, 1,   2, 0, 1, 1, 3,    0, 1, 0, 0, 1, ],
[ 0, 3, 2, 1, 0,   3, 0, 2, 0, 1,    1, 2, 0, 1, 2,   1, 0, 2, 0, 1,    0, 3, 0, 1, 2, ],
[ 0, 1, 1, 0, 2,   2, 1, 0, 1, 0,    3, 1, 2, 1, 0,   2, 0, 2, 2, 0,    0, 1, 3, 1, 0, ],

[ 2, 1, 2, 1, 2,   0, 1, 2, 1, 2,    1, 1, 3, 2, 2,   1, 1, 0, 0, 0,    0, 0, 1, 1, 2, ], #20
[ 1, 0, 1, 2, 1,   0, 1, 2, 1, 0,    1, 0, 1, 0, 1,   2, 1, 0, 1, 2,    1, 3, 0, 1, 3, ],
[ 2, 3, 3, 1, 2,   1, 3, 2, 3, 2,    3, 1, 1, 2, 1,   3, 2, 2, 2, 2,    2, 2, 1, 1, 2, ],
[ 1, 0, 1, 0, 0,   1, 0, 0, 0, 0,    0, 1, 3, 0, 0,   1, 0, 0, 1, 3,    1, 2, 0, 0, 3, ],
[ 2, 1, 0, 1, 0,   2, 0, 2, 1, 2,    3, 1, 0, 1, 2,   3, 0, 2, 0, 1,    3, 0, 0, 1, 2, ],

[ 0, 2, 1, 0, 3,   1, 2, 0, 0, 0,    0, 3, 1, 1, 0,   0, 0, 2, 1, 0,    0, 1, 3, 1, 0, ],
[ 2, 1, 2, 0, 0,   0, 1, 2, 3, 2,    0, 1, 0, 2, 2,   3, 1, 0, 0, 2,    0, 0, 1, 1, 0, ],
[ 1, 0, 1, 2, 1,   1, 1, 2, 0, 0,    1, 0, 1, 0, 1,   2, 1, 0, 1, 1,    1, 3, 0, 1, 1, ],
[ 1, 0, 0, 1, 2,   1, 3, 2, 3, 1,    3, 1, 1, 2, 2,   1, 2, 2, 2, 2,    2, 2, 2, 1, 2, ],
[ 1, 0, 1, 0, 1,   1, 0, 0, 1, 0,    0, 1, 3, 1, 0,   2, 0, 0, 1, 3,    0, 2, 1, 0, 1, ],]

Zmap = [ 0, 2, 0, 0, 0,   0, 0, 2, 0, 0,    0, 0, 0, 3, 0,   0, 0, 2, 0, 0,    0, 2, 0, 0, 0, ]

#マップ描画
def map():
    global Zmap
    for i in range(25):
        if Zmap[i] == 1:
            bar(int(i%5)*120+50,int(i/5)*50+150)
        elif Zmap[i] == 2:
            pt5(int(i%5)*120+50,int(i/5)*50+150)
        elif Zmap[i] == 3:
            pt10(int(i%5)*120+50,int(i/5)*50+150)

#接触
def touch():
    global mode
    global tekuteku
    global score
    global Zmap
    if (line==1)and(-30<a_yoko< 10):
        if (Zmap[0]==1)and(mode == 1):
            mode = 3
            tekuteku = 21
        if Zmap[0]==2:
            score = score +5
            Zmap[0]=0
        if Zmap[0]==3:
            score = score +10
            Zmap[0]=0

    if (line==1)and( 90<a_yoko<130):
        if (Zmap[1]==1)and(mode == 1):
            mode = 3
            tekuteku = 21
        if Zmap[1]==2:
            score = score +5
            Zmap[1]=0
        if Zmap[1]==3:
            score = score +10
            Zmap[1]=0

    if (line==1)and(210<a_yoko<250):
        if (Zmap[2]==1)and(mode == 1):
            mode = 3
            tekuteku = 21
        if Zmap[2]==2:
            score = score +5
            Zmap[2]=0
        if Zmap[2]==3:
            score = score +10
            Zmap[2]=0

    if (line==1)and(330<a_yoko<370):
        if (Zmap[3]==1)and(mode == 1):
            mode = 3
            tekuteku = 21
        if Zmap[3]==2:
            score = score +5
            Zmap[3]=0
        if Zmap[3]==3:
            score = score +10
            Zmap[3]=0

    if (line==1)and(450<a_yoko<490):
        if (Zmap[4]==1)and(mode == 1):
            mode = 3
            tekuteku = 21
        if Zmap[4]==2:
            score = score +5
            Zmap[4]=0
        if Zmap[4]==3:
            score = score +10
            Zmap[4]=0

    if (line==2)and(-30<a_yoko< 10):
        if (Zmap[5]==1)and(mode == 1):
            mode = 3
            tekuteku = 21
        if Zmap[5]==2:
            score = score +5
            Zmap[5]=0
        if Zmap[5]==3:
            score = score +10
            Zmap[5]=0

    if (line==2)and( 90<a_yoko<130):
        if (Zmap[6]==1)and(mode == 1):
            mode = 3
            tekuteku = 21
        if Zmap[6]==2:
            score = score +5
            Zmap[6]=0
        if Zmap[6]==3:
            score = score +10
            Zmap[6]=0

    if (line==2)and(210<a_yoko<250):
        if (Zmap[7]==1)and(mode == 1):
            mode = 3
            tekuteku = 21
        if Zmap[7]==2:
            score = score +5
            Zmap[7]=0
        if Zmap[7]==3:
            score = score +10
            Zmap[7]=0

    if (line==2)and(330<a_yoko<370):
        if (Zmap[8]==1)and(mode == 1):
            mode = 3
            tekuteku = 21
        if Zmap[8]==2:
            score = score +5
            Zmap[8]=0
        if Zmap[8]==3:
            score = score +10
            Zmap[8]=0

    if (line==2)and(450<a_yoko<490):
        if (Zmap[9]==1)and(mode == 1):
            mode = 3
            tekuteku = 21
        if Zmap[9]==2:
            score = score +5
            Zmap[9]=0
        if Zmap[9]==3:
            score = score +10
            Zmap[9]=0

    if (line==3)and(-30<a_yoko< 10):
        if (Zmap[10]==1)and(mode == 1):
            mode = 3
            tekuteku = 21
        if Zmap[10]==2:
            score = score +5
            Zmap[10]=0
        if Zmap[10]==3:
            score = score +10
            Zmap[10]=0

    if (line==3)and( 90<a_yoko<130):
        if (Zmap[11]==1)and(mode == 1):
            mode = 3
            tekuteku = 21
        if Zmap[11]==2:
            score = score +5
            Zmap[11]=0
        if Zmap[11]==3:
            score = score +10
            Zmap[11]=0

    if (line==3)and(210<a_yoko<250):
        if (Zmap[12]==1)and(mode == 1):
            mode = 3
            tekuteku = 21
        if Zmap[12]==2:
            score = score +5
            Zmap[12]=0
        if Zmap[12]==3:
            score = score +10
            Zmap[12]=0

    if (line==3)and(330<a_yoko<370):
        if (Zmap[13]==1)and(mode == 1):
            mode = 3
            tekuteku = 21
        if Zmap[13]==2:
            score = score +5
            Zmap[13]=0
        if Zmap[13]==3:
            score = score +10
            Zmap[13]=0

    if (line==3)and(450<a_yoko<490):
        if (Zmap[14]==1)and(mode == 1):
            mode = 3
            tekuteku = 21
        if Zmap[14]==2:
            score = score +5
            Zmap[14]=0
        if Zmap[14]==3:
            score = score +10
            Zmap[14]=0

    if (line==4)and(-30<a_yoko< 10):
        if (Zmap[15]==1)and(mode == 1):
            mode = 3
            tekuteku = 21
        if Zmap[15]==2:
            score = score +5
            Zmap[15]=0
        if Zmap[15]==3:
            score = score +10
            Zmap[15]=0

    if (line==4)and( 90<a_yoko<130):
        if (Zmap[16]==1)and(mode == 1):
            mode = 3
            tekuteku = 21
        if Zmap[16]==2:
            score = score +5
            Zmap[16]=0
        if Zmap[16]==3:
            score = score +10
            Zmap[16]=0

    if (line==4)and(210<a_yoko<250):
        if (Zmap[17]==1)and(mode == 1):
            mode = 3
            tekuteku = 21
        if Zmap[17]==2:
            score = score +5
            Zmap[17]=0
        if Zmap[17]==3:
            score = score +10
            Zmap[17]=0

    if (line==4)and(330<a_yoko<370):
        if (Zmap[18]==1)and(mode == 1):
            mode = 3
            tekuteku = 21
        if Zmap[18]==2:
            score = score +5
            Zmap[18]=0
        if Zmap[18]==3:
            score = score +10
            Zmap[18]=0

    if (line==4)and(450<a_yoko<490):
        if (Zmap[19]==1)and(mode == 1):
            mode = 3
            tekuteku = 21
        if Zmap[19]==2:
            score = score +5
            Zmap[19]=0
        if Zmap[19]==3:
            score = score +10
            Zmap[19]=0

    if (line==5)and(-30<a_yoko< 10):
        if (Zmap[20]==1)and(mode == 1):
            mode = 3
            tekuteku = 21
        if Zmap[20]==2:
            score = score +5
            Zmap[20]=0
        if Zmap[20]==3:
            score = score +10
            Zmap[20]=0

    if (line==5)and( 90<a_yoko<130):
        if (Zmap[21]==1)and(mode == 1):
            mode = 3
            tekuteku = 21
        if Zmap[21]==2:
            score = score +5
            Zmap[21]=0
        if Zmap[21]==3:
            score = score +10
            Zmap[21]=0

    if (line==5)and(210<a_yoko<250):
        if (Zmap[22]==1)and(mode == 1):
            mode = 3
            tekuteku = 21
        if Zmap[22]==2:
            score = score +5
            Zmap[22]=0
        if Zmap[22]==3:
            score = score +10
            Zmap[22]=0

    if (line==5)and(330<a_yoko<370):
        if (Zmap[23]==1)and(mode == 1):
            mode = 3
            tekuteku = 21
        if Zmap[23]==2:
            score = score +5
            Zmap[23]=0
        if Zmap[23]==3:
            score = score +10
            Zmap[23]=0

    if (line==5)and(450<a_yoko<490):
        if (Zmap[24]==1)and(mode == 1):
            mode = 3
            tekuteku = 21
        if Zmap[24]==2:
            score = score +5
            Zmap[24]=0
        if Zmap[24]==3:
            score = score +10
            Zmap[24]=0

#ハードル描画
def bar(map_yoko,map_tate):
        cv.create_line     ( 10 +map_yoko, 40 +map_tate, 10+map_yoko, 75+map_tate, fill='black', width = 3 )
        cv.create_line     ( 40 +map_yoko,-10 +map_tate, 40+map_yoko, 25+map_tate, fill='black', width = 3 )
        cv.create_line     ( 10 +map_yoko, 50 +map_tate, 40+map_yoko,  0+map_tate, fill='black', width = 5 )
        cv.create_line     ( 10 +map_yoko, 45 +map_tate, 40+map_yoko, -5+map_tate, fill='black', width = 5 )

#アイテム2描画
def pt5(map_yoko,map_tate):
        cv.create_line     ( 26 +map_yoko,  2 +32+map_tate, 40+map_yoko,  2+32+map_tate, fill='black', width = 5 ) #5
        cv.create_line     ( 26 +map_yoko,  2 +32+map_tate, 19+map_yoko, 14+32+map_tate, fill='black', width = 5 )
        cv.create_line     ( 19 +map_yoko, 14 +32+map_tate, 33+map_yoko, 14+32+map_tate, fill='black', width = 5 )
        cv.create_line     ( 33 +map_yoko, 14 +32+map_tate, 26+map_yoko, 26+32+map_tate, fill='black', width = 5 )
        cv.create_line     ( 26 +map_yoko, 26 +32+map_tate, 12+map_yoko, 26+32+map_tate, fill='black', width = 5 )
        cv.create_line     ( 43 +map_yoko, 14 +32+map_tate, 29+map_yoko, 38+32+map_tate, fill='black', width = 5 ) #p
        cv.create_line     ( 43 +map_yoko, 14 +32+map_tate, 57+map_yoko, 14+32+map_tate, fill='black', width = 5 )
        cv.create_line     ( 57 +map_yoko, 14 +32+map_tate, 50+map_yoko, 26+32+map_tate, fill='black', width = 5 )
        cv.create_line     ( 50 +map_yoko, 26 +32+map_tate, 34+map_yoko, 26+32+map_tate, fill='black', width = 5 )

#アイテム3描画
def pt10(map_yoko,map_tate):
        cv.create_line     ( 16 +map_yoko,  2 +32+map_tate,  2+map_yoko, 25+32+map_tate, fill='black', width = 5 ) #10
        cv.create_line     ( 26 +map_yoko,  2 +32+map_tate, 12+map_yoko, 25+32+map_tate, fill='black', width = 5 )
        cv.create_line     ( 26 +map_yoko,  2 +32+map_tate, 40+map_yoko,  2+32+map_tate, fill='black', width = 5 )
        cv.create_line     ( 40 +map_yoko,  2 +32+map_tate, 26+map_yoko, 25+32+map_tate, fill='black', width = 5 )
        cv.create_line     ( 12 +map_yoko, 25 +32+map_tate, 26+map_yoko, 25+32+map_tate, fill='black', width = 5 )
        cv.create_line     ( 43 +map_yoko, 14 +32+map_tate, 29+map_yoko, 38+32+map_tate, fill='black', width = 5 ) #p
        cv.create_line     ( 43 +map_yoko, 14 +32+map_tate, 57+map_yoko, 14+32+map_tate, fill='black', width = 5 )
        cv.create_line     ( 57 +map_yoko, 14 +32+map_tate, 50+map_yoko, 26+32+map_tate, fill='black', width = 5 )
        cv.create_line     ( 50 +map_yoko, 26 +32+map_tate, 34+map_yoko, 26+32+map_tate, fill='black', width = 5 )

#ランニング　アニメーション
def runman():
    if tekuteku == 1:
        cv.create_oval     ( (15)*3 +a_yoko, (66)*3 +a_tate, (45)*3 +a_yoko, (70)*3 +a_tate, fill='black', width=0 ) #影
        cv.create_polygon  ( (20)*3 +a_yoko, (17)*3 +a_tate, (23)*3 +a_yoko, (44)*3 +a_tate, (32)*3 +a_yoko, (41)*3 +a_tate ) #体
        cv.create_line     ( (25)*3 +a_yoko, (31)*3 +a_tate, (19)*3 +a_yoko, (37)*3 +a_tate, fill='black', width = 5 ) #右腕上
        cv.create_line     ( (19)*3 +a_yoko, (37)*3 +a_tate, (13)*3 +a_yoko, (40)*3 +a_tate, fill='black', width = 5 ) #右腕下
        cv.create_oval     ( (11-3)*3 +a_yoko, (40-3)*3 +a_tate, (11+3)*3 +a_yoko, (40+3)*3 +a_tate, fill='black') #右拳
        cv.create_line     ( (23)*3 +a_yoko, (30)*3 +a_tate, (30)*3 +a_yoko, (35)*3 +a_tate, fill='black', width = 5 ) #左腕上
        cv.create_line     ( (30)*3 +a_yoko, (35)*3 +a_tate, (30)*3 +a_yoko, (41)*3 +a_tate, fill='black', width = 5 ) #左腕下
        cv.create_oval     ( (30-3)*3 +a_yoko, (43-3)*3 +a_tate, (30+3)*3 +a_yoko, (43+3)*3 +a_tate, fill='black') #左拳
        cv.create_line     ( (26)*3 +a_yoko, (40)*3 +a_tate, (32)*3 +a_yoko, (52)*3 +a_tate, fill='black', width = 5 ) #右脚上
        cv.create_line     ( (32)*3 +a_yoko, (52)*3 +a_tate, (39)*3 +a_yoko, (60)*3 +a_tate, fill='black', width = 5 ) #右脚下
        cv.create_oval     ( (39-3)*3 +a_yoko, (62-3)*3 +a_tate, (39+3)*3 +a_yoko, (62+3)*3 +a_tate, fill='black') #右甲
        cv.create_line     ( (26)*3 +a_yoko, (41)*3 +a_tate, (14)*3 +a_yoko, (47)*3 +a_tate, fill='black', width = 5 ) #左脚上
        cv.create_line     ( (14)*3 +a_yoko, (47)*3 +a_tate, (21)*3 +a_yoko, (55)*3 +a_tate, fill='black', width = 5 ) #左脚下
        cv.create_oval     ( (20-3)*3 +a_yoko, (56-3)*3 +a_tate, (20+3)*3 +a_yoko, (56+3)*3 +a_tate, fill='black') #左甲
        cv.create_oval     ( (20-12)*3 +a_yoko, (17-12)*3 +a_tate, (20+12)*3 +a_yoko, (17+12)*3 +a_tate, fill='black') #頭
        cv.create_oval     ( (20-10)*3 +a_yoko, (17-10)*3 +a_tate, (20+10)*3 +a_yoko, (17+10)*3 +a_tate, fill='white') #頭    
        cv.create_text     ( (20   )*3 +a_yoko, (17   )*3 +a_tate, text="そ",     font=("Helvetica", 45,"bold" ) ) #そ

    if tekuteku == 2:
        cv.create_oval     ( (15)*3 +a_yoko, (66)*3 +a_tate, (45)*3 +a_yoko, (70)*3 +a_tate, fill='black', width=0 ) #影
        cv.create_polygon  ( (76-55)*3 +a_yoko, (21)*3 +a_tate, (77-55)*3 +a_yoko, (48)*3 +a_tate, (87-55)*3 +a_yoko, (46)*3 +a_tate ) #体
        cv.create_line     ( (78-55)*3 +a_yoko, (34)*3 +a_tate, (73-55)*3 +a_yoko, (39)*3 +a_tate, fill='black', width = 5 ) #右腕上
        cv.create_line     ( (73-55)*3 +a_yoko, (39)*3 +a_tate, (68-55)*3 +a_yoko, (37)*3 +a_tate, fill='black', width = 5 ) #右腕下
        cv.create_oval     ( (69-55-3)*3 +a_yoko, (37-3)*3 +a_tate, (69-55+3)*3 +a_yoko, (37+3)*3 +a_tate, fill='black') #右拳
        cv.create_line     ( (80-55)*3 +a_yoko, (32)*3 +a_tate, (88-55)*3 +a_yoko, (33)*3 +a_tate, fill='black', width = 5 ) #左腕上
        cv.create_line     ( (88-55)*3 +a_yoko, (33)*3 +a_tate, (88-55)*3 +a_yoko, (40)*3 +a_tate, fill='black', width = 5 ) #左腕下
        cv.create_oval     ( (89-55-3)*3 +a_yoko, (42-3)*3 +a_tate, (89-55+3)*3 +a_yoko, (42+3)*3 +a_tate, fill='black') #左拳
        cv.create_line     ( (82-55)*3 +a_yoko, (44)*3 +a_tate, (87-55)*3 +a_yoko, (51)*3 +a_tate, fill='black', width = 5 ) #右脚上
        cv.create_line     ( (87-55)*3 +a_yoko, (51)*3 +a_tate, (95-55)*3 +a_yoko, (47)*3 +a_tate, fill='black', width = 5 ) #右脚下
        cv.create_oval     ( (95-55-3)*3 +a_yoko, (47-3)*3 +a_tate, (95-55+3)*3 +a_yoko, (47+3)*3 +a_tate, fill='black') #右甲
        cv.create_line     ( (80-55)*3 +a_yoko, (42)*3 +a_tate, (76-55)*3 +a_yoko, (55)*3 +a_tate, fill='black', width = 5 ) #左脚上
        cv.create_line     ( (76-55)*3 +a_yoko, (55)*3 +a_tate, (74-55)*3 +a_yoko, (63)*3 +a_tate, fill='black', width = 5 ) #左脚下
        cv.create_oval     ( (72-55-3)*3 +a_yoko, (64-3)*3 +a_tate, (72-55+3)*3 +a_yoko, (64+3)*3 +a_tate, fill='black') #左甲
        cv.create_oval     ( (74-55-12)*3 +a_yoko, (19-12)*3 +a_tate, (74-55+12)*3 +a_yoko, (19+12)*3 +a_tate, fill='black') #頭
        cv.create_oval     ( (74-55-10)*3 +a_yoko, (19-10)*3 +a_tate, (74-55+10)*3 +a_yoko, (19+10)*3 +a_tate, fill='white') #頭  
        cv.create_text     ( (19      )*3 +a_yoko, (19   )*3 +a_tate, text="そ",     font=("Helvetica", 45,"bold" ) ) #そ

    if tekuteku == 3:
        cv.create_oval     ( (15)*3 +a_yoko, (66)*3 +a_tate, (45)*3 +a_yoko, (70)*3 +a_tate, fill='black', width=0 ) #影
        cv.create_polygon  ( (63-36)*3 +a_yoko, (24)*3 +a_tate, (65-36)*3 +a_yoko, (51)*3 +a_tate, (75-36)*3 +a_yoko, (49)*3 +a_tate ) #体
        cv.create_line     ( (0)*3 +a_yoko, (0)*3 +a_tate, (0)*3 +a_yoko, (0)*3 +a_tate, fill='black', width = 5 ) #右腕上
        cv.create_line     ( (66-36)*3 +a_yoko, (41)*3 +a_tate, (62-36)*3 +a_yoko, (44)*3 +a_tate, fill='black', width = 5 ) #右腕下
        cv.create_oval     ( (62-36-3)*3 +a_yoko, (44-3)*3 +a_tate, (62-36+3)*3 +a_yoko, (44+3)*3 +a_tate, fill='black') #右拳
        cv.create_line     ( (65-36)*3 +a_yoko, (34)*3 +a_tate, (71-36)*3 +a_yoko, (40)*3 +a_tate, fill='black', width = 5 ) #左腕上
        cv.create_line     ( (71-36)*3 +a_yoko, (40)*3 +a_tate, (68-36)*3 +a_yoko, (48)*3 +a_tate, fill='black', width = 5 ) #左腕下
        cv.create_oval     ( (66-36-3)*3 +a_yoko, (49-3)*3 +a_tate, (66-36+3)*3 +a_yoko, (49+3)*3 +a_tate, fill='black') #左拳
        cv.create_line     ( (69-36)*3 +a_yoko, (48)*3 +a_tate, (60-36)*3 +a_yoko, (54)*3 +a_tate, fill='black', width = 5 ) #右脚上
        cv.create_line     ( (60-36)*3 +a_yoko, (54)*3 +a_tate, (72-36)*3 +a_yoko, (55)*3 +a_tate, fill='black', width = 5 ) #右脚下
        cv.create_oval     ( (73-36-3)*3 +a_yoko, (56-3)*3 +a_tate, (73-36+3)*3 +a_yoko, (56+3)*3 +a_tate, fill='black') #右甲
        cv.create_line     ( (71-36)*3 +a_yoko, (48)*3 +a_tate, (66-36)*3 +a_yoko, (55)*3 +a_tate, fill='black', width = 5 ) #左脚上
        cv.create_line     ( (66-36)*3 +a_yoko, (55)*3 +a_tate, (73-36)*3 +a_yoko, (62)*3 +a_tate, fill='black', width = 5 ) #左脚下
        cv.create_oval     ( (72-36-3)*3 +a_yoko, (61-3)*3 +a_tate, (72-36+3)*3 +a_yoko, (61+3)*3 +a_tate, fill='black') #左甲
        cv.create_oval     ( (61-36-12)*3 +a_yoko, (21-12)*3 +a_tate, (61-36+12)*3 +a_yoko, (21+12)*3 +a_tate, fill='black') #頭
        cv.create_oval     ( (61-36-10)*3 +a_yoko, (21-10)*3 +a_tate, (61-36+10)*3 +a_yoko, (21+10)*3 +a_tate, fill='white') #頭  
        cv.create_text     ( (25      )*3 +a_yoko, (21   )*3 +a_tate, text="そ",     font=("Helvetica", 45,"bold" ) ) #そ

    if tekuteku == 4:
        cv.create_oval     ( (15)*3 +a_yoko, (66)*3 +a_tate, (45)*3 +a_yoko, (70)*3 +a_tate, fill='black', width=0 ) #影
        cv.create_polygon  ( (54-27)*3 +a_yoko, (20)*3 +a_tate, (58-27)*3 +a_yoko, (48)*3 +a_tate, (66-27)*3 +a_yoko, (44)*3 +a_tate ) #体
        cv.create_line     ( (56-27)*3 +a_yoko, (31)*3 +a_tate, (65-27)*3 +a_yoko, (35)*3 +a_tate, fill='black', width = 5 ) #右腕上
        cv.create_line     ( (65-27)*3 +a_yoko, (35)*3 +a_tate, (65-27)*3 +a_yoko, (41)*3 +a_tate, fill='black', width = 5 ) #右腕下
        cv.create_oval     ( (65-27-3)*3 +a_yoko, (43-3)*3 +a_tate, (65-27+3)*3 +a_yoko, (43+3)*3 +a_tate, fill='black') #右拳
        cv.create_line     ( (56-27)*3 +a_yoko, (33)*3 +a_tate, (52-27)*3 +a_yoko, (40)*3 +a_tate, fill='black', width = 5 ) #左腕上
        cv.create_line     ( (52-27)*3 +a_yoko, (40)*3 +a_tate, (49-27)*3 +a_yoko, (40)*3 +a_tate, fill='black', width = 5 ) #左腕下
        cv.create_oval     ( (49-27-3)*3 +a_yoko, (41-3)*3 +a_tate, (49-27+3)*3 +a_yoko, (41+3)*3 +a_tate, fill='black') #左拳
        cv.create_line     ( (62-27)*3 +a_yoko, (42)*3 +a_tate, (50-27)*3 +a_yoko, (50)*3 +a_tate, fill='black', width = 5 ) #右脚上
        cv.create_line     ( (50-27)*3 +a_yoko, (50)*3 +a_tate, (57-27)*3 +a_yoko, (55)*3 +a_tate, fill='black', width = 5 ) #右脚下
        cv.create_oval     ( (56-27-3)*3 +a_yoko, (56-3)*3 +a_tate, (56-27+3)*3 +a_yoko, (56+3)*3 +a_tate, fill='black') #右甲
        cv.create_line     ( (61-27)*3 +a_yoko, (42)*3 +a_tate, (66-27)*3 +a_yoko, (54)*3 +a_tate, fill='black', width = 5 ) #左脚上
        cv.create_line     ( (66-27)*3 +a_yoko, (54)*3 +a_tate, (73-27)*3 +a_yoko, (63)*3 +a_tate, fill='black', width = 5 ) #左脚下
        cv.create_oval     ( (72-27-3)*3 +a_yoko, (61-3)*3 +a_tate, (72-27+3)*3 +a_yoko, (61+3)*3 +a_tate, fill='black') #左甲
        cv.create_oval     ( (54-27-12)*3 +a_yoko, (19-12)*3 +a_tate, (54-27+12)*3 +a_yoko, (19+12)*3 +a_tate, fill='black') #頭
        cv.create_oval     ( (54-27-10)*3 +a_yoko, (19-10)*3 +a_tate, (54-27+10)*3 +a_yoko, (19+10)*3 +a_tate, fill='white') #頭  
        cv.create_text     ( (27      )*3 +a_yoko, (19   )*3 +a_tate, text="そ",     font=("Helvetica", 45,"bold" ) ) #そ

    if tekuteku == 5:
        cv.create_oval     ( (15)*3 +a_yoko, (66)*3 +a_tate, (45)*3 +a_yoko, (70)*3 +a_tate, fill='black', width=0 ) #影
        cv.create_polygon  ( (43-18)*3 +a_yoko, (21)*3 +a_tate, (44-18)*3 +a_yoko, (49)*3 +a_tate, (53-18)*3 +a_yoko, (47)*3 +a_tate ) #体
        cv.create_line     ( (45-18)*3 +a_yoko, (33)*3 +a_tate, (55-18)*3 +a_yoko, (33)*3 +a_tate, fill='black', width = 5 ) #右腕上
        cv.create_line     ( (55-18)*3 +a_yoko, (33)*3 +a_tate, (58-18)*3 +a_yoko, (41)*3 +a_tate, fill='black', width = 5 ) #右腕下
        cv.create_oval     ( (57-18-3)*3 +a_yoko, (42-3)*3 +a_tate, (57-18+3)*3 +a_yoko, (42+3)*3 +a_tate, fill='black') #右拳
        cv.create_line     ( (44-18)*3 +a_yoko, (33)*3 +a_tate, (38-18)*3 +a_yoko, (40)*3 +a_tate, fill='black', width = 5 ) #左腕上
        cv.create_line     ( (38-18)*3 +a_yoko, (40)*3 +a_tate, (40-18)*3 +a_yoko, (38)*3 +a_tate, fill='black', width = 5 ) #左腕下
        cv.create_oval     ( (41-18-3)*3 +a_yoko, (40-3)*3 +a_tate, (41-18+3)*3 +a_yoko, (40+3)*3 +a_tate, fill='black') #左拳
        cv.create_line     ( (49-18)*3 +a_yoko, (43)*3 +a_tate, (43-18)*3 +a_yoko, (55)*3 +a_tate, fill='black', width = 5 ) #右脚上
        cv.create_line     ( (43-18)*3 +a_yoko, (55)*3 +a_tate, (40-18)*3 +a_yoko, (64)*3 +a_tate, fill='black', width = 5 ) #右脚下
        cv.create_oval     ( (39-18-3)*3 +a_yoko, (64-3)*3 +a_tate, (39-18+3)*3 +a_yoko, (64+3)*3 +a_tate, fill='black') #右甲
        cv.create_line     ( (46-18)*3 +a_yoko, (45)*3 +a_tate, (52-18)*3 +a_yoko, (54)*3 +a_tate, fill='black', width = 5 ) #左脚上
        cv.create_line     ( (52-18)*3 +a_yoko, (54)*3 +a_tate, (62-18)*3 +a_yoko, (51)*3 +a_tate, fill='black', width = 5 ) #左脚下
        cv.create_oval     ( (62-18-3)*3 +a_yoko, (52-3)*3 +a_tate, (62-18+3)*3 +a_yoko, (52+3)*3 +a_tate, fill='black') #左甲
        cv.create_oval     ( (41-18-12)*3 +a_yoko, (20-12)*3 +a_tate, (41-18+12)*3 +a_yoko, (20+12)*3 +a_tate, fill='black') #頭
        cv.create_oval     ( (41-18-10)*3 +a_yoko, (20-10)*3 +a_tate, (41-18+10)*3 +a_yoko, (20+10)*3 +a_tate, fill='white') #頭  
        cv.create_text     ( (23      )*3 +a_yoko, (20   )*3 +a_tate, text="そ",     font=("Helvetica", 45,"bold" ) ) #そ

    if tekuteku == 6:
        cv.create_oval     ( (15)*3 +a_yoko, (66)*3 +a_tate, (45)*3 +a_yoko, (70)*3 +a_tate, fill='black', width=0 ) #影
        cv.create_polygon  ( (32-9)*3 +a_yoko, (23)*3 +a_tate, (33-9)*3 +a_yoko, (50)*3 +a_tate, (42-9)*3 +a_yoko, (49)*3 +a_tate ) #体
        cv.create_line     ( (33-9)*3 +a_yoko, (34)*3 +a_tate, (39-9)*3 +a_yoko, (42)*3 +a_tate, fill='black', width = 5 ) #右腕上
        cv.create_line     ( (39-9)*3 +a_yoko, (42)*3 +a_tate, (35-9)*3 +a_yoko, (47)*3 +a_tate, fill='black', width = 5 ) #右腕下
        cv.create_oval     ( (34-9-3)*3 +a_yoko, (48-3)*3 +a_tate, (34-9+3)*3 +a_yoko, (48+3)*3 +a_tate, fill='black') #右拳
        cv.create_line     ( (34-9)*3 +a_yoko, (34)*3 +a_tate, (36-9)*3 +a_yoko, (37)*3 +a_tate, fill='black', width = 5 ) #左腕上
        cv.create_line     ( (36-9)*3 +a_yoko, (37)*3 +a_tate, (31-9)*3 +a_yoko, (41)*3 +a_tate, fill='black', width = 5 ) #左腕下
        cv.create_oval     ( (30-9-3)*3 +a_yoko, (44-3)*3 +a_tate, (30-9+3)*3 +a_yoko, (44+3)*3 +a_tate, fill='black') #左拳
        cv.create_line     ( (40-9)*3 +a_yoko, (46)*3 +a_tate, (33-9)*3 +a_yoko, (57)*3 +a_tate, fill='black', width = 5 ) #右脚上
        cv.create_line     ( (33-9)*3 +a_yoko, (57)*3 +a_tate, (41-9)*3 +a_yoko, (64)*3 +a_tate, fill='black', width = 5 ) #右脚下
        cv.create_oval     ( (39-9-3)*3 +a_yoko, (64-3)*3 +a_tate, (39-9+3)*3 +a_yoko, (64+3)*3 +a_tate, fill='black') #右甲
        cv.create_line     ( (37-9)*3 +a_yoko, (46)*3 +a_tate, (28-9)*3 +a_yoko, (53)*3 +a_tate, fill='black', width = 5 ) #左脚上
        cv.create_line     ( (28-9)*3 +a_yoko, (53)*3 +a_tate, (38-9)*3 +a_yoko, (55)*3 +a_tate, fill='black', width = 5 ) #左脚下
        cv.create_oval     ( (40-9-3)*3 +a_yoko, (56-3)*3 +a_tate, (40-9+3)*3 +a_yoko, (56+3)*3 +a_tate, fill='black') #左甲
        cv.create_oval     ( (30-9-12)*3 +a_yoko, (22-12)*3 +a_tate, (30-9+12)*3 +a_yoko, (22+12)*3 +a_tate, fill='black') #頭
        cv.create_oval     ( (30-9-10)*3 +a_yoko, (22-10)*3 +a_tate, (30-9+10)*3 +a_yoko, (22+10)*3 +a_tate, fill='white') #頭  
        cv.create_text     ( (21     )*3 +a_yoko, (22   )*3 +a_tate, text="そ",     font=("Helvetica", 45,"bold" ) ) #そ

#ジャンプ　アニメーション
    if tekuteku == 11:
        cv.create_oval     ( (15)*3 +a_yoko, (66)*3 +a_tate, (45)*3 +a_yoko, (70)*3 +a_tate, fill='black', width=0 ) #影
        cv.create_polygon  ( (19)*3 +a_yoko, (22)*3 +a_tate, (33)*3 +a_yoko, (46)*3 +a_tate, (40)*3 +a_yoko, (39)*3 +a_tate ) #体
        cv.create_line     ( (26)*3 +a_yoko, (30)*3 +a_tate, (22)*3 +a_yoko, (38)*3 +a_tate, fill='black', width = 5 ) #右腕上
        cv.create_line     ( (22)*3 +a_yoko, (38)*3 +a_tate, (16)*3 +a_yoko, (38)*3 +a_tate, fill='black', width = 5 ) #右腕下
        cv.create_oval     ( (15-3)*3 +a_yoko, (37-3)*3 +a_tate, (15+3)*3 +a_yoko, (37+3)*3 +a_tate, fill='black') #右拳
        cv.create_line     ( (26)*3 +a_yoko, (30)*3 +a_tate, (27)*3 +a_yoko, (39)*3 +a_tate, fill='black', width = 5 ) #左腕上
        cv.create_line     ( (27)*3 +a_yoko, (39)*3 +a_tate, (20)*3 +a_yoko, (41)*3 +a_tate, fill='black', width = 5 ) #左腕下
        cv.create_oval     ( (19-3)*3 +a_yoko, (41-3)*3 +a_tate, (19+3)*3 +a_yoko, (41+3)*3 +a_tate, fill='black') #左拳
        cv.create_line     ( (35)*3 +a_yoko, (40)*3 +a_tate, (26)*3 +a_yoko, (50)*3 +a_tate, fill='black', width = 5 ) #右脚上
        cv.create_line     ( (26)*3 +a_yoko, (50)*3 +a_tate, (35)*3 +a_yoko, (56)*3 +a_tate, fill='black', width = 5 ) #右脚下
        cv.create_oval     ( (34-3)*3 +a_yoko, (56-3)*3 +a_tate, (34+3)*3 +a_yoko, (56+3)*3 +a_tate, fill='black') #右甲
        cv.create_line     ( (35)*3 +a_yoko, (40)*3 +a_tate, (23)*3 +a_yoko, (47)*3 +a_tate, fill='black', width = 5 ) #左脚上
        cv.create_line     ( (23)*3 +a_yoko, (47)*3 +a_tate, (30)*3 +a_yoko, (56)*3 +a_tate, fill='black', width = 5 ) #左脚下
        cv.create_oval     ( (28-3)*3 +a_yoko, (56-3)*3 +a_tate, (28+3)*3 +a_yoko, (56+3)*3 +a_tate, fill='black') #左甲
        cv.create_oval     ( (17-12)*3 +a_yoko, (20-12)*3 +a_tate, (17+12)*3 +a_yoko, (20+12)*3 +a_tate, fill='black') #頭
        cv.create_oval     ( (17-10)*3 +a_yoko, (20-10)*3 +a_tate, (17+10)*3 +a_yoko, (20+10)*3 +a_tate, fill='white') #頭  
        cv.create_text     ( (17   )*3 +a_yoko, (20   )*3 +a_tate, text="そ",     font=("Helvetica", 45,"bold" ) ) #そ
    
    if tekuteku == 12:
        cv.create_oval     ( (15)*3 +a_yoko, (66)*3 +a_tate, (45)*3 +a_yoko, (70)*3 +a_tate, fill='black', width=0 ) #影
        cv.create_polygon  ( (19)*3 +a_yoko, (24)*3 +a_tate, (46)*3 +a_yoko, (28)*3 +a_tate, (46)*3 +a_yoko, (18)*3 +a_tate ) #体
        cv.create_line     ( (31)*3 +a_yoko, (26)*3 +a_tate, (26)*3 +a_yoko, (34)*3 +a_tate, fill='black', width = 5 ) #右腕上
        cv.create_line     ( (26)*3 +a_yoko, (34)*3 +a_tate, (20)*3 +a_yoko, (34)*3 +a_tate, fill='black', width = 5 ) #右腕下
        cv.create_oval     ( (20-3)*3 +a_yoko, (33-3)*3 +a_tate, (20+3)*3 +a_yoko, (33+3)*3 +a_tate, fill='black') #右拳
        cv.create_line     ( (30)*3 +a_yoko, (26)*3 +a_tate, (31)*3 +a_yoko, (35)*3 +a_tate, fill='black', width = 5 ) #左腕上
        cv.create_line     ( (31)*3 +a_yoko, (35)*3 +a_tate, (25)*3 +a_yoko, (38)*3 +a_tate, fill='black', width = 5 ) #左腕下
        cv.create_oval     ( (23-3)*3 +a_yoko, (37-3)*3 +a_tate, (23+3)*3 +a_yoko, (37+3)*3 +a_tate, fill='black') #左拳
        cv.create_line     ( (45)*3 +a_yoko, (24)*3 +a_tate, (35)*3 +a_yoko, (34)*3 +a_tate, fill='black', width = 5 ) #右脚上
        cv.create_line     ( (35)*3 +a_yoko, (34)*3 +a_tate, (46)*3 +a_yoko, (33)*3 +a_tate, fill='black', width = 5 ) #右脚下
        cv.create_oval     ( (46-3)*3 +a_yoko, (34-3)*3 +a_tate, (46+3)*3 +a_yoko, (34+3)*3 +a_tate, fill='black') #右甲
        cv.create_line     ( (44)*3 +a_yoko, (23)*3 +a_tate, (34)*3 +a_yoko, (32)*3 +a_tate, fill='black', width = 5 ) #左脚上
        cv.create_line     ( (34)*3 +a_yoko, (32)*3 +a_tate, (45)*3 +a_yoko, (37)*3 +a_tate, fill='black', width = 5 ) #左脚下
        cv.create_oval     ( (45-3)*3 +a_yoko, (36-3)*3 +a_tate, (45+3)*3 +a_yoko, (36+3)*3 +a_tate, fill='black') #左甲
        cv.create_oval     ( (15-12)*3 +a_yoko, (27-12)*3 +a_tate, (15+12)*3 +a_yoko, (27+12)*3 +a_tate, fill='black') #頭
        cv.create_oval     ( (15-10)*3 +a_yoko, (27-10)*3 +a_tate, (15+10)*3 +a_yoko, (27+10)*3 +a_tate, fill='white') #頭  
        cv.create_text     ( (15   )*3 +a_yoko, (27   )*3 +a_tate, text="そ",     font=("Helvetica", 45,"bold" ) ) #そ

    if tekuteku == 13:
        cv.create_oval     ( (15)*3 +a_yoko, (66)*3 +a_tate, (45)*3 +a_yoko, (70)*3 +a_tate, fill='black', width=0 ) #影
        cv.create_polygon  ( (12)*3 +a_yoko, (29)*3 +a_tate, (25)*3 +a_yoko, (6)*3 +a_tate, (16)*3 +a_yoko, (3)*3 +a_tate ) #体
        cv.create_line     ( (0)*3 +a_yoko, (0)*3 +a_tate, (0)*3 +a_yoko, (0)*3 +a_tate, fill='black', width = 5 ) #右腕上
        cv.create_line     ( (16)*3 +a_yoko, (18)*3 +a_tate, (22)*3 +a_yoko, (20)*3 +a_tate, fill='black', width = 5 ) #右腕下
        cv.create_oval     ( (23-3)*3 +a_yoko, (21-3)*3 +a_tate, (23+3)*3 +a_yoko, (21+3)*3 +a_tate, fill='black') #右拳
        cv.create_line     ( (0)*3 +a_yoko, (0)*3 +a_tate, (0)*3 +a_yoko, (0)*3 +a_tate, fill='black', width = 5 ) #左腕上
        cv.create_line     ( (16)*3 +a_yoko, (18)*3 +a_tate, (22)*3 +a_yoko, (21)*3 +a_tate, fill='black', width = 5 ) #左腕下
        cv.create_oval     ( (22-3)*3 +a_yoko, (23-3)*3 +a_tate, (22+3)*3 +a_yoko, (23+3)*3 +a_tate, fill='black') #左拳
        cv.create_line     ( (19)*3 +a_yoko, (5)*3 +a_tate, (22)*3 +a_yoko, (18)*3 +a_tate, fill='black', width = 5 ) #右脚上
        cv.create_line     ( (22)*3 +a_yoko, (18)*3 +a_tate, (26)*3 +a_yoko, (7)*3 +a_tate, fill='black', width = 5 ) #右脚下
        cv.create_oval     ( (26-3)*3 +a_yoko, (8-3)*3 +a_tate, (26+3)*3 +a_yoko, (8+3)*3 +a_tate, fill='black') #右甲
        cv.create_line     ( (19)*3 +a_yoko, (5)*3 +a_tate, (23)*3 +a_yoko, (18)*3 +a_tate, fill='black', width = 5 ) #左脚上
        cv.create_line     ( (23)*3 +a_yoko, (18)*3 +a_tate, (30)*3 +a_yoko, (10)*3 +a_tate, fill='black', width = 5 ) #左脚下
        cv.create_oval     ( (31-3)*3 +a_yoko, (11-3)*3 +a_tate, (31+3)*3 +a_yoko, (11+3)*3 +a_tate, fill='black') #左甲
        cv.create_oval     ( (19-12)*3 +a_yoko, (31-12)*3 +a_tate, (19+12)*3 +a_yoko, (31+12)*3 +a_tate, fill='black') #頭
        cv.create_oval     ( (19-10)*3 +a_yoko, (31-10)*3 +a_tate, (19+10)*3 +a_yoko, (31+10)*3 +a_tate, fill='white') #頭  
        cv.create_text     ( (19   )*3 +a_yoko, (31   )*3 +a_tate, text="そ",     font=("Helvetica", 45,"bold" ) ) #そ

    if tekuteku == 14:
        cv.create_oval     ( (15)*3 +a_yoko, (66)*3 +a_tate, (45)*3 +a_yoko, (70)*3 +a_tate, fill='black', width=0 ) #影
        cv.create_polygon  ( (27)*3 +a_yoko, (31)*3 +a_tate, (12)*3 +a_yoko, (9)*3 +a_tate, (5)*3 +a_yoko, (16)*3 +a_tate ) #体
        cv.create_line     ( (0)*3 +a_yoko, (0)*3 +a_tate, (0)*3 +a_yoko, (0)*3 +a_tate, fill='black', width = 5 ) #右腕上
        cv.create_line     ( (16)*3 +a_yoko, (18)*3 +a_tate, (22)*3 +a_yoko, (21)*3 +a_tate, fill='black', width = 5 ) #右腕下
        cv.create_oval     ( (23-3)*3 +a_yoko, (21-3)*3 +a_tate, (23+3)*3 +a_yoko, (21+3)*3 +a_tate, fill='black') #右拳
        cv.create_line     ( (0)*3 +a_yoko, (0)*3 +a_tate, (0)*3 +a_yoko, (0)*3 +a_tate, fill='black', width = 5 ) #左腕上
        cv.create_line     ( (16)*3 +a_yoko, (19)*3 +a_tate, (22)*3 +a_yoko, (22)*3 +a_tate, fill='black', width = 5 ) #左腕下
        cv.create_oval     ( (22-3)*3 +a_yoko, (23-3)*3 +a_tate, (22+3)*3 +a_yoko, (23+3)*3 +a_tate, fill='black') #左拳
        cv.create_line     ( (9)*3 +a_yoko, (14)*3 +a_tate, (22)*3 +a_yoko, (12)*3 +a_tate, fill='black', width = 5 ) #右脚上
        cv.create_line     ( (22)*3 +a_yoko, (12)*3 +a_tate, (14)*3 +a_yoko, (5)*3 +a_tate, fill='black', width = 5 ) #右脚下
        cv.create_oval     ( (14-3)*3 +a_yoko, (5-3)*3 +a_tate, (14+3)*3 +a_yoko, (5+3)*3 +a_tate, fill='black') #右甲
        cv.create_line     ( (10)*3 +a_yoko, (12)*3 +a_tate, (23)*3 +a_yoko, (8)*3 +a_tate, fill='black', width = 5 ) #左脚上
        cv.create_line     ( (23)*3 +a_yoko, (8)*3 +a_tate, (13)*3 +a_yoko, (5)*3 +a_tate, fill='black', width = 5 ) #左脚下
        cv.create_oval     ( (13-3)*3 +a_yoko, (6-3)*3 +a_tate, (13+3)*3 +a_yoko, (6+3)*3 +a_tate, fill='black') #左甲
        cv.create_oval     ( (19-12)*3 +a_yoko, (31-12)*3 +a_tate, (19+12)*3 +a_yoko, (31+12)*3 +a_tate, fill='black') #頭
        cv.create_oval     ( (19-10)*3 +a_yoko, (31-10)*3 +a_tate, (19+10)*3 +a_yoko, (31+10)*3 +a_tate, fill='white') #頭  
        cv.create_text     ( (19   )*3 +a_yoko, (31   )*3 +a_tate, text="そ",     font=("Helvetica", 45,"bold" ) ) #そ

    if tekuteku == 15:
        cv.create_oval     ( (15)*3 +a_yoko, (66)*3 +a_tate, (45)*3 +a_yoko, (70)*3 +a_tate, fill='black', width=0 ) #影
        cv.create_polygon  ( (36)*3 +a_yoko, (25)*3 +a_tate, (12)*3 +a_yoko, (39)*3 +a_tate, (19)*3 +a_yoko, (46)*3 +a_tate ) #体
        cv.create_line     ( (25)*3 +a_yoko, (32)*3 +a_tate, (19)*3 +a_yoko, (33)*3 +a_tate, fill='black', width = 5 ) #右腕上
        cv.create_line     ( (19)*3 +a_yoko, (33)*3 +a_tate, (16)*3 +a_yoko, (27)*3 +a_tate, fill='black', width = 5 ) #右腕下
        cv.create_oval     ( (17-3)*3 +a_yoko, (27-3)*3 +a_tate, (17+3)*3 +a_yoko, (27+3)*3 +a_tate, fill='black') #右拳
        cv.create_line     ( (24)*3 +a_yoko, (34)*3 +a_tate, (31)*3 +a_yoko, (37)*3 +a_tate, fill='black', width = 5 ) #左腕上
        cv.create_line     ( (31)*3 +a_yoko, (37)*3 +a_tate, (29)*3 +a_yoko, (43)*3 +a_tate, fill='black', width = 5 ) #左腕下
        cv.create_oval     ( (29-3)*3 +a_yoko, (43-3)*3 +a_tate, (29+3)*3 +a_yoko, (43+3)*3 +a_tate, fill='black') #左拳
        cv.create_line     ( (18)*3 +a_yoko, (42)*3 +a_tate, (10)*3 +a_yoko, (29)*3 +a_tate, fill='black', width = 5 ) #右脚上
        cv.create_line     ( (10)*3 +a_yoko, (29)*3 +a_tate, (6)*3 +a_yoko, (40)*3 +a_tate, fill='black', width = 5 ) #右脚下
        cv.create_oval     ( (5-3)*3 +a_yoko, (39-3)*3 +a_tate, (5+3)*3 +a_yoko, (39+3)*3 +a_tate, fill='black') #右甲
        cv.create_line     ( (19)*3 +a_yoko, (42)*3 +a_tate, (7)*3 +a_yoko, (49)*3 +a_tate, fill='black', width = 5 ) #左脚上
        cv.create_line     ( (7)*3 +a_yoko, (49)*3 +a_tate, (12)*3 +a_yoko, (60)*3 +a_tate, fill='black', width = 5 ) #左脚下
        cv.create_oval     ( (10-3)*3 +a_yoko, (60-3)*3 +a_tate, (10+3)*3 +a_yoko, (60+3)*3 +a_tate, fill='black') #左甲
        cv.create_oval     ( (34-12)*3 +a_yoko, (20-12)*3 +a_tate, (34+12)*3 +a_yoko, (20+12)*3 +a_tate, fill='black') #頭
        cv.create_oval     ( (34-10)*3 +a_yoko, (20-10)*3 +a_tate, (34+10)*3 +a_yoko, (20+10)*3 +a_tate, fill='white') #頭  
        cv.create_text     ( (34   )*3 +a_yoko, (20   )*3 +a_tate, text="そ",     font=("Helvetica", 45,"bold" ) ) #そ

    if tekuteku == 16:
        cv.create_oval     ( (15)*3 +a_yoko, (66)*3 +a_tate, (45)*3 +a_yoko, (70)*3 +a_tate, fill='black', width=0 ) #影
        cv.create_polygon  ( (18)*3 +a_yoko, (36)*3 +a_tate, (32)*3 +a_yoko, (59)*3 +a_tate, (39)*3 +a_yoko, (52)*3 +a_tate ) #体
        cv.create_line     ( (24)*3 +a_yoko, (43)*3 +a_tate, (34)*3 +a_yoko, (40)*3 +a_tate, fill='black', width = 5 ) #右腕上
        cv.create_line     ( (34)*3 +a_yoko, (40)*3 +a_tate, (36)*3 +a_yoko, (46)*3 +a_tate, fill='black', width = 5 ) #右腕下
        cv.create_oval     ( (37-3)*3 +a_yoko, (48-3)*3 +a_tate, (37+3)*3 +a_yoko, (48+3)*3 +a_tate, fill='black') #右拳
        cv.create_line     ( (24)*3 +a_yoko, (44)*3 +a_tate, (19)*3 +a_yoko, (53)*3 +a_tate, fill='black', width = 5 ) #左腕上
        cv.create_line     ( (19)*3 +a_yoko, (53)*3 +a_tate, (11)*3 +a_yoko, (57)*3 +a_tate, fill='black', width = 5 ) #左腕下
        cv.create_oval     ( (10-3)*3 +a_yoko, (58-3)*3 +a_tate, (10+3)*3 +a_yoko, (58+3)*3 +a_tate, fill='black') #左拳
        cv.create_line     ( (35)*3 +a_yoko, (54)*3 +a_tate, (21)*3 +a_yoko, (53)*3 +a_tate, fill='black', width = 5 ) #右脚上
        cv.create_line     ( (21)*3 +a_yoko, (53)*3 +a_tate, (20)*3 +a_yoko, (63)*3 +a_tate, fill='black', width = 5 ) #右脚下
        cv.create_oval     ( (18-3)*3 +a_yoko, (64-3)*3 +a_tate, (18+3)*3 +a_yoko, (64+3)*3 +a_tate, fill='black') #右甲
        cv.create_line     ( (35)*3 +a_yoko, (54)*3 +a_tate, (31)*3 +a_yoko, (65)*3 +a_tate, fill='black', width = 5 ) #左脚上
        cv.create_line     ( (31)*3 +a_yoko, (65)*3 +a_tate, (42)*3 +a_yoko, (63)*3 +a_tate, fill='black', width = 5 ) #左脚下
        cv.create_oval     ( (42-3)*3 +a_yoko, (64-3)*3 +a_tate, (42+3)*3 +a_yoko, (64+3)*3 +a_tate, fill='black') #左甲
        cv.create_oval     ( (14-12)*3 +a_yoko, (34-12)*3 +a_tate, (14+12)*3 +a_yoko, (34+12)*3 +a_tate, fill='black') #頭
        cv.create_oval     ( (14-10)*3 +a_yoko, (34-10)*3 +a_tate, (14+10)*3 +a_yoko, (34+10)*3 +a_tate, fill='white') #頭  
        cv.create_text     ( (14   )*3 +a_yoko, (34   )*3 +a_tate, text="そ",     font=("Helvetica", 45,"bold" ) ) #そ

#スリップ　アニメーション
    if tekuteku == 21:
        cv.create_oval     ( (15)*3 +a_yoko, (66)*3 +a_tate, (45)*3 +a_yoko, (70)*3 +a_tate, fill='black', width=0 ) #影
        cv.create_polygon  ( (14)*3 +a_yoko, (23)*3 +a_tate, (27)*3 +a_yoko, (47)*3 +a_tate, (35)*3 +a_yoko, (41)*3 +a_tate ) #体
        cv.create_line     ( (24)*3 +a_yoko, (35)*3 +a_tate, (18)*3 +a_yoko, (42)*3 +a_tate, fill='black', width = 5 ) #右腕上
        cv.create_line     ( (18)*3 +a_yoko, (42)*3 +a_tate, (12)*3 +a_yoko, (42)*3 +a_tate, fill='black', width = 5 ) #右腕下
        cv.create_oval     ( (12-3)*3 +a_yoko, (42-3)*3 +a_tate, (12+3)*3 +a_yoko, (42+3)*3 +a_tate, fill='black') #右拳
        cv.create_line     ( (23)*3 +a_yoko, (33)*3 +a_tate, (25)*3 +a_yoko, (42)*3 +a_tate, fill='black', width = 5 ) #左腕上
        cv.create_line     ( (25)*3 +a_yoko, (42)*3 +a_tate, (21)*3 +a_yoko, (46)*3 +a_tate, fill='black', width = 5 ) #左腕下
        cv.create_oval     ( (20-3)*3 +a_yoko, (46-3)*3 +a_tate, (20+3)*3 +a_yoko, (46+3)*3 +a_tate, fill='black') #左拳
        cv.create_line     ( (30)*3 +a_yoko, (43)*3 +a_tate, (38)*3 +a_yoko, (56)*3 +a_tate, fill='black', width = 5 ) #右脚上
        cv.create_line     ( (38)*3 +a_yoko, (56)*3 +a_tate, (39)*3 +a_yoko, (56)*3 +a_tate, fill='black', width = 5 ) #右脚下
        cv.create_oval     ( (38-3)*3 +a_yoko, (57-3)*3 +a_tate, (38+3)*3 +a_yoko, (57+3)*3 +a_tate, fill='black') #右甲
        cv.create_line     ( (30)*3 +a_yoko, (43)*3 +a_tate, (41)*3 +a_yoko, (51)*3 +a_tate, fill='black', width = 5 ) #左脚上
        cv.create_line     ( (41)*3 +a_yoko, (51)*3 +a_tate, (51)*3 +a_yoko, (52)*3 +a_tate, fill='black', width = 5 ) #左脚下
        cv.create_oval     ( (51-3)*3 +a_yoko, (53-3)*3 +a_tate, (51+3)*3 +a_yoko, (53+3)*3 +a_tate, fill='black') #左甲
        cv.create_oval     ( (15-12)*3 +a_yoko, (21-12)*3 +a_tate, (15+12)*3 +a_yoko, (21+12)*3 +a_tate, fill='black') #頭
        cv.create_oval     ( (15-10)*3 +a_yoko, (21-10)*3 +a_tate, (15+10)*3 +a_yoko, (21+10)*3 +a_tate, fill='white') #頭  
        cv.create_text     ( (15   )*3 +a_yoko, (21   )*3 +a_tate, text="そ",     font=("Helvetica", 45,"bold" ) ) #そ
    
    if tekuteku == 22:
        cv.create_oval     ( (15)*3 +a_yoko, (66)*3 +a_tate, (45)*3 +a_yoko, (70)*3 +a_tate, fill='black', width=0 ) #影
        cv.create_polygon  ( (10)*3 +a_yoko, (30)*3 +a_tate, (29)*3 +a_yoko, (49)*3 +a_tate, (34)*3 +a_yoko, (41)*3 +a_tate ) #体
        cv.create_line     ( (20)*3 +a_yoko, (38)*3 +a_tate, (15)*3 +a_yoko, (45)*3 +a_tate, fill='black', width = 5 ) #右腕上
        cv.create_line     ( (15)*3 +a_yoko, (45)*3 +a_tate, (8)*3 +a_yoko, (46)*3 +a_tate, fill='black', width = 5 ) #右腕下
        cv.create_oval     ( (9-3)*3 +a_yoko, (45-3)*3 +a_tate, (9+3)*3 +a_yoko, (45+3)*3 +a_tate, fill='black') #右拳
        cv.create_line     ( (20)*3 +a_yoko, (37)*3 +a_tate, (22)*3 +a_yoko, (46)*3 +a_tate, fill='black', width = 5 ) #左腕上
        cv.create_line     ( (22)*3 +a_yoko, (46)*3 +a_tate, (18)*3 +a_yoko, (50)*3 +a_tate, fill='black', width = 5 ) #左腕下
        cv.create_oval     ( (16-3)*3 +a_yoko, (50-3)*3 +a_tate, (16+3)*3 +a_yoko, (50+3)*3 +a_tate, fill='black') #左拳
        cv.create_line     ( (29)*3 +a_yoko, (43)*3 +a_tate, (41)*3 +a_yoko, (50)*3 +a_tate, fill='black', width = 5 ) #右脚上
        cv.create_line     ( (41)*3 +a_yoko, (50)*3 +a_tate, (50)*3 +a_yoko, (43)*3 +a_tate, fill='black', width = 5 ) #右脚下
        cv.create_oval     ( (50-3)*3 +a_yoko, (45-3)*3 +a_tate, (50+3)*3 +a_yoko, (45+3)*3 +a_tate, fill='black') #右甲
        cv.create_line     ( (29)*3 +a_yoko, (43)*3 +a_tate, (45)*3 +a_yoko, (55)*3 +a_tate, fill='black', width = 5 ) #左脚上
        cv.create_line     ( (45)*3 +a_yoko, (55)*3 +a_tate, (46)*3 +a_yoko, (55)*3 +a_tate, fill='black', width = 5 ) #左脚下
        cv.create_oval     ( (46-3)*3 +a_yoko, (56-3)*3 +a_tate, (46+3)*3 +a_yoko, (56+3)*3 +a_tate, fill='black') #左甲
        cv.create_oval     ( (14-12)*3 +a_yoko, (24-12)*3 +a_tate, (14+12)*3 +a_yoko, (24+12)*3 +a_tate, fill='black') #頭
        cv.create_oval     ( (14-10)*3 +a_yoko, (24-10)*3 +a_tate, (14+10)*3 +a_yoko, (24+10)*3 +a_tate, fill='white') #頭  
        cv.create_text     ( (14   )*3 +a_yoko, (24   )*3 +a_tate, text="そ",     font=("Helvetica", 45,"bold" ) ) #そ

    if tekuteku == 23:
        cv.create_oval     ( (15)*3 +a_yoko, (66)*3 +a_tate, (45)*3 +a_yoko, (70)*3 +a_tate, fill='black', width=0 ) #影
        cv.create_polygon  ( (12)*3 +a_yoko, (44)*3 +a_tate, (38)*3 +a_yoko, (53)*3 +a_tate, (40)*3 +a_yoko, (43)*3 +a_tate ) #体
        cv.create_line     ( (22)*3 +a_yoko, (46)*3 +a_tate, (15)*3 +a_yoko, (52)*3 +a_tate, fill='black', width = 5 ) #右腕上
        cv.create_line     ( (15)*3 +a_yoko, (52)*3 +a_tate, (5)*3 +a_yoko, (52)*3 +a_tate, fill='black', width = 5 ) #右腕下
        cv.create_oval     ( (4-3)*3 +a_yoko, (52-3)*3 +a_tate, (4+3)*3 +a_yoko, (52+3)*3 +a_tate, fill='black') #右拳
        cv.create_line     ( (23)*3 +a_yoko, (46)*3 +a_tate, (20)*3 +a_yoko, (54)*3 +a_tate, fill='black', width = 5 ) #左腕上
        cv.create_line     ( (20)*3 +a_yoko, (54)*3 +a_tate, (13)*3 +a_yoko, (58)*3 +a_tate, fill='black', width = 5 ) #左腕下
        cv.create_oval     ( (12-3)*3 +a_yoko, (58-3)*3 +a_tate, (12+3)*3 +a_yoko, (58+3)*3 +a_tate, fill='black') #左拳
        cv.create_line     ( (36)*3 +a_yoko, (47)*3 +a_tate, (50)*3 +a_yoko, (49)*3 +a_tate, fill='black', width = 5 ) #右脚上
        cv.create_line     ( (50)*3 +a_yoko, (49)*3 +a_tate, (58)*3 +a_yoko, (41)*3 +a_tate, fill='black', width = 5 ) #右脚下
        cv.create_oval     ( (57-3)*3 +a_yoko, (42-3)*3 +a_tate, (57+3)*3 +a_yoko, (42+3)*3 +a_tate, fill='black') #右甲
        cv.create_line     ( (36)*3 +a_yoko, (48)*3 +a_tate, (48)*3 +a_yoko, (55)*3 +a_tate, fill='black', width = 5 ) #左脚上
        cv.create_line     ( (48)*3 +a_yoko, (55)*3 +a_tate, (59)*3 +a_yoko, (52)*3 +a_tate, fill='black', width = 5 ) #左脚下
        cv.create_oval     ( (59-3)*3 +a_yoko, (53-3)*3 +a_tate, (59+3)*3 +a_yoko, (53+3)*3 +a_tate, fill='black') #左甲
        cv.create_oval     ( (15-12)*3 +a_yoko, (38-12)*3 +a_tate, (15+12)*3 +a_yoko, (38+12)*3 +a_tate, fill='black') #頭
        cv.create_oval     ( (15-10)*3 +a_yoko, (38-10)*3 +a_tate, (15+10)*3 +a_yoko, (38+10)*3 +a_tate, fill='white') #頭  
        cv.create_text     ( (15   )*3 +a_yoko, (38   )*3 +a_tate, text="そ",     font=("Helvetica", 45,"bold" ) ) #そ

    if tekuteku == 24:
        cv.create_oval     ( (15)*3 +a_yoko, (66)*3 +a_tate, (45)*3 +a_yoko, (70)*3 +a_tate, fill='black', width=0 ) #影
        cv.create_polygon  ( (16)*3 +a_yoko, (58)*3 +a_tate, (43)*3 +a_yoko, (62)*3 +a_tate, (43)*3 +a_yoko, (52)*3 +a_tate ) #体
        cv.create_line     ( (0)*3 +a_yoko, (0)*3 +a_tate, (0)*3 +a_yoko, (0)*3 +a_tate, fill='black', width = 5 ) #右腕上
        cv.create_line     ( (0)*3 +a_yoko, (0)*3 +a_tate, (0)*3 +a_yoko, (0)*3 +a_tate, fill='black', width = 5 ) #右腕下
        cv.create_oval     ( (5-3)*3 +a_yoko, (58-3)*3 +a_tate, (5+3)*3 +a_yoko, (58+3)*3 +a_tate, fill='black') #右拳
        cv.create_line     ( (26)*3 +a_yoko, (56)*3 +a_tate, (18)*3 +a_yoko, (63)*3 +a_tate, fill='black', width = 5 ) #左腕上
        cv.create_line     ( (18)*3 +a_yoko, (63)*3 +a_tate, (9)*3 +a_yoko, (62)*3 +a_tate, fill='black', width = 5 ) #左腕下
        cv.create_oval     ( (7-3)*3 +a_yoko, (61-3)*3 +a_tate, (7+3)*3 +a_yoko, (61+3)*3 +a_tate, fill='black') #左拳
        cv.create_line     ( (41)*3 +a_yoko, (57)*3 +a_tate, (55)*3 +a_yoko, (58)*3 +a_tate, fill='black', width = 5 ) #右脚上
        cv.create_line     ( (55)*3 +a_yoko, (58)*3 +a_tate, (63)*3 +a_yoko, (50)*3 +a_tate, fill='black', width = 5 ) #右脚下
        cv.create_oval     ( (63-3)*3 +a_yoko, (51-3)*3 +a_tate, (63+3)*3 +a_yoko, (51+3)*3 +a_tate, fill='black') #右甲
        cv.create_line     ( (41)*3 +a_yoko, (58)*3 +a_tate, (55)*3 +a_yoko, (60)*3 +a_tate, fill='black', width = 5 ) #左脚上
        cv.create_line     ( (55)*3 +a_yoko, (60)*3 +a_tate, (67)*3 +a_yoko, (58)*3 +a_tate, fill='black', width = 5 ) #左脚下
        cv.create_oval     ( (67-3)*3 +a_yoko, (59-3)*3 +a_tate, (67+3)*3 +a_yoko, (59+3)*3 +a_tate, fill='black') #左甲
        cv.create_oval     ( (16-12)*3 +a_yoko, (50-12)*3 +a_tate, (16+12)*3 +a_yoko, (50+12)*3 +a_tate, fill='black') #頭
        cv.create_oval     ( (16-10)*3 +a_yoko, (50-10)*3 +a_tate, (16+10)*3 +a_yoko, (50+10)*3 +a_tate, fill='white') #頭  
        cv.create_text     ( (16   )*3 +a_yoko, (50   )*3 +a_tate, text="そ",     font=("Helvetica", 45,"bold" ) ) #そ
        
    if tekuteku == 25:
        cv.create_oval     ( (15)*3 +a_yoko, (66)*3 +a_tate, (45)*3 +a_yoko, (70)*3 +a_tate, fill='black', width=0 ) #影
        cv.create_polygon  ( (16)*3 +a_yoko, (62)*3 +a_tate, (43)*3 +a_yoko, (66)*3 +a_tate, (43)*3 +a_yoko, (56)*3 +a_tate ) #体
        cv.create_line     ( (0)*3 +a_yoko, (0)*3 +a_tate, (0)*3 +a_yoko, (0)*3 +a_tate, fill='black', width = 5 ) #右腕上
        cv.create_line     ( (0)*3 +a_yoko, (0)*3 +a_tate, (0)*3 +a_yoko, (0)*3 +a_tate, fill='black', width = 5 ) #右腕下
        cv.create_oval     ( (5-3)*3 +a_yoko, (62-3)*3 +a_tate, (5+3)*3 +a_yoko, (62+3)*3 +a_tate, fill='black') #右拳
        cv.create_line     ( (26)*3 +a_yoko, (60)*3 +a_tate, (18)*3 +a_yoko, (67)*3 +a_tate, fill='black', width = 5 ) #左腕上
        cv.create_line     ( (18)*3 +a_yoko, (67)*3 +a_tate, (9)*3 +a_yoko, (66)*3 +a_tate, fill='black', width = 5 ) #左腕下
        cv.create_oval     ( (7-3)*3 +a_yoko, (65-3)*3 +a_tate, (7+3)*3 +a_yoko, (65+3)*3 +a_tate, fill='black') #左拳
        cv.create_line     ( (41)*3 +a_yoko, (61)*3 +a_tate, (55)*3 +a_yoko, (62)*3 +a_tate, fill='black', width = 5 ) #右脚上
        cv.create_line     ( (55)*3 +a_yoko, (62)*3 +a_tate, (63)*3 +a_yoko, (54)*3 +a_tate, fill='black', width = 5 ) #右脚下
        cv.create_oval     ( (63-3)*3 +a_yoko, (55-3)*3 +a_tate, (63+3)*3 +a_yoko, (55+3)*3 +a_tate, fill='black') #右甲
        cv.create_line     ( (41)*3 +a_yoko, (62)*3 +a_tate, (55)*3 +a_yoko, (64)*3 +a_tate, fill='black', width = 5 ) #左脚上
        cv.create_line     ( (55)*3 +a_yoko, (64)*3 +a_tate, (67)*3 +a_yoko, (62)*3 +a_tate, fill='black', width = 5 ) #左脚下
        cv.create_oval     ( (67-3)*3 +a_yoko, (63-3)*3 +a_tate, (67+3)*3 +a_yoko, (63+3)*3 +a_tate, fill='black') #左甲
        cv.create_oval     ( (16-12)*3 +a_yoko, (54-12)*3 +a_tate, (16+12)*3 +a_yoko, (54+12)*3 +a_tate, fill='black') #頭
        cv.create_oval     ( (16-10)*3 +a_yoko, (54-10)*3 +a_tate, (16+10)*3 +a_yoko, (54+10)*3 +a_tate, fill='white') #頭  
        cv.create_text     ( (16   )*3 +a_yoko, (54   )*3 +a_tate, text="そ",     font=("Helvetica", 45,"bold" ) ) #そ

    if tekuteku == 26:
        cv.create_oval     ( (15)*3 +a_yoko, (66)*3 +a_tate, (45)*3 +a_yoko, (70)*3 +a_tate, fill='black', width=0 ) #影
        cv.create_polygon  ( (16)*3 +a_yoko, (62)*3 +a_tate, (43)*3 +a_yoko, (66)*3 +a_tate, (43)*3 +a_yoko, (56)*3 +a_tate ) #体
        cv.create_line     ( (0)*3 +a_yoko, (0)*3 +a_tate, (0)*3 +a_yoko, (0)*3 +a_tate, fill='black', width = 5 ) #右腕上
        cv.create_line     ( (0)*3 +a_yoko, (0)*3 +a_tate, (0)*3 +a_yoko, (0)*3 +a_tate, fill='black', width = 5 ) #右腕下
        cv.create_oval     ( (5-3)*3 +a_yoko, (62-3)*3 +a_tate, (5+3)*3 +a_yoko, (62+3)*3 +a_tate, fill='black') #右拳
        cv.create_line     ( (26)*3 +a_yoko, (60)*3 +a_tate, (18)*3 +a_yoko, (67)*3 +a_tate, fill='black', width = 5 ) #左腕上
        cv.create_line     ( (18)*3 +a_yoko, (67)*3 +a_tate, (9)*3 +a_yoko, (66)*3 +a_tate, fill='black', width = 5 ) #左腕下
        cv.create_oval     ( (7-3)*3 +a_yoko, (65-3)*3 +a_tate, (7+3)*3 +a_yoko, (65+3)*3 +a_tate, fill='black') #左拳
        cv.create_line     ( (41)*3 +a_yoko, (61)*3 +a_tate, (55)*3 +a_yoko, (62)*3 +a_tate, fill='black', width = 5 ) #右脚上
        cv.create_line     ( (55)*3 +a_yoko, (62)*3 +a_tate, (63)*3 +a_yoko, (54)*3 +a_tate, fill='black', width = 5 ) #右脚下
        cv.create_oval     ( (63-3)*3 +a_yoko, (55-3)*3 +a_tate, (63+3)*3 +a_yoko, (55+3)*3 +a_tate, fill='black') #右甲
        cv.create_line     ( (41)*3 +a_yoko, (62)*3 +a_tate, (55)*3 +a_yoko, (64)*3 +a_tate, fill='black', width = 5 ) #左脚上
        cv.create_line     ( (55)*3 +a_yoko, (64)*3 +a_tate, (67)*3 +a_yoko, (62)*3 +a_tate, fill='black', width = 5 ) #左脚下
        cv.create_oval     ( (67-3)*3 +a_yoko, (63-3)*3 +a_tate, (67+3)*3 +a_yoko, (63+3)*3 +a_tate, fill='black') #左甲
        cv.create_oval     ( (16-12)*3 +a_yoko, (54-12)*3 +a_tate, (16+12)*3 +a_yoko, (54+12)*3 +a_tate, fill='black') #頭
        cv.create_oval     ( (16-10)*3 +a_yoko, (54-10)*3 +a_tate, (16+10)*3 +a_yoko, (54+10)*3 +a_tate, fill='white') #頭  
        cv.create_text     ( (16   )*3 +a_yoko, (54   )*3 +a_tate, text="そ",     font=("Helvetica", 45,"bold" ) ) #そ

#起き上がり　アニメーション
    if tekuteku == 31:
        cv.create_oval     ( (15)*3 +a_yoko, (66)*3 +a_tate, (45)*3 +a_yoko, (70)*3 +a_tate, fill='black', width=0 ) #影
        cv.create_polygon  ( (18)*3 +a_yoko, (55)*3 +a_tate, (44)*3 +a_yoko, (59)*3 +a_tate, (44)*3 +a_yoko, (50)*3 +a_tate ) #体
        cv.create_line     ( (29)*3 +a_yoko, (53)*3 +a_tate, (22)*3 +a_yoko, (61)*3 +a_tate, fill='black', width = 5 ) #右腕上
        cv.create_line     ( (22)*3 +a_yoko, (61)*3 +a_tate, (14)*3 +a_yoko, (63)*3 +a_tate, fill='black', width = 5 ) #右腕下
        cv.create_oval     ( (13-3)*3 +a_yoko, (61-3)*3 +a_tate, (13+3)*3 +a_yoko, (61+3)*3 +a_tate, fill='black') #右拳
        cv.create_line     ( (28)*3 +a_yoko, (54)*3 +a_tate, (34)*3 +a_yoko, (60)*3 +a_tate, fill='black', width = 5 ) #左腕上
        cv.create_line     ( (34)*3 +a_yoko, (60)*3 +a_tate, (29)*3 +a_yoko, (64)*3 +a_tate, fill='black', width = 5 ) #左腕下
        cv.create_oval     ( (28-3)*3 +a_yoko, (62-3)*3 +a_tate, (28+3)*3 +a_yoko, (62+3)*3 +a_tate, fill='black') #左拳
        cv.create_line     ( (43)*3 +a_yoko, (54)*3 +a_tate, (34)*3 +a_yoko, (63)*3 +a_tate, fill='black', width = 5 ) #右脚上
        cv.create_line     ( (34)*3 +a_yoko, (63)*3 +a_tate, (45)*3 +a_yoko, (62)*3 +a_tate, fill='black', width = 5 ) #右脚下
        cv.create_oval     ( (62-3)*3 +a_yoko, (63-3)*3 +a_tate, (62+3)*3 +a_yoko, (63+3)*3 +a_tate, fill='black') #右甲
        cv.create_line     ( (43)*3 +a_yoko, (54)*3 +a_tate, (50)*3 +a_yoko, (64)*3 +a_tate, fill='black', width = 5 ) #左脚上
        cv.create_line     ( (50)*3 +a_yoko, (64)*3 +a_tate, (61)*3 +a_yoko, (64)*3 +a_tate, fill='black', width = 5 ) #左脚下
        cv.create_oval     ( (45-3)*3 +a_yoko, (62-3)*3 +a_tate, (45+3)*3 +a_yoko, (62+3)*3 +a_tate, fill='black') #左甲
        cv.create_oval     ( (13-12)*3 +a_yoko, (50-12)*3 +a_tate, (13+12)*3 +a_yoko, (50+12)*3 +a_tate, fill='black') #頭
        cv.create_oval     ( (13-10)*3 +a_yoko, (50-10)*3 +a_tate, (13+10)*3 +a_yoko, (50+10)*3 +a_tate, fill='white') #頭  
        cv.create_text     ( (13   )*3 +a_yoko, (50   )*3 +a_tate, text="そ",     font=("Helvetica", 45,"bold" ) ) #そ
    
    if tekuteku == 32:
        cv.create_oval     ( (15)*3 +a_yoko, (66)*3 +a_tate, (45)*3 +a_yoko, (70)*3 +a_tate, fill='black', width=0 ) #影
        cv.create_polygon  ( (18)*3 +a_yoko, (52)*3 +a_tate, (45)*3 +a_yoko, (57)*3 +a_tate, (45)*3 +a_yoko, (47)*3 +a_tate ) #体
        cv.create_line     ( (29)*3 +a_yoko, (52)*3 +a_tate, (23)*3 +a_yoko, (59)*3 +a_tate, fill='black', width = 5 ) #右腕上
        cv.create_line     ( (23)*3 +a_yoko, (59)*3 +a_tate, (16)*3 +a_yoko, (64)*3 +a_tate, fill='black', width = 5 ) #右腕下
        cv.create_oval     ( (15-3)*3 +a_yoko, (64-3)*3 +a_tate, (15+3)*3 +a_yoko, (64+3)*3 +a_tate, fill='black') #右拳
        cv.create_line     ( (29)*3 +a_yoko, (52)*3 +a_tate, (34)*3 +a_yoko, (58)*3 +a_tate, fill='black', width = 5 ) #左腕上
        cv.create_line     ( (34)*3 +a_yoko, (58)*3 +a_tate, (30)*3 +a_yoko, (64)*3 +a_tate, fill='black', width = 5 ) #左腕下
        cv.create_oval     ( (30-3)*3 +a_yoko, (64-3)*3 +a_tate, (30+3)*3 +a_yoko, (64+3)*3 +a_tate, fill='black') #左拳
        cv.create_line     ( (43)*3 +a_yoko, (52)*3 +a_tate, (37)*3 +a_yoko, (65)*3 +a_tate, fill='black', width = 5 ) #右脚上
        cv.create_line     ( (37)*3 +a_yoko, (65)*3 +a_tate, (48)*3 +a_yoko, (63)*3 +a_tate, fill='black', width = 5 ) #右脚下
        cv.create_oval     ( (49-3)*3 +a_yoko, (64-3)*3 +a_tate, (49+3)*3 +a_yoko, (60+3)*3 +a_tate, fill='black') #右甲
        cv.create_line     ( (43)*3 +a_yoko, (53)*3 +a_tate, (49)*3 +a_yoko, (64)*3 +a_tate, fill='black', width = 5 ) #左脚上
        cv.create_line     ( (49)*3 +a_yoko, (64)*3 +a_tate, (60)*3 +a_yoko, (62)*3 +a_tate, fill='black', width = 5 ) #左脚下
        cv.create_oval     ( (60-3)*3 +a_yoko, (64-3)*3 +a_tate, (60+3)*3 +a_yoko, (64+3)*3 +a_tate, fill='black') #左甲
        cv.create_oval     ( (15-12)*3 +a_yoko, (43-12)*3 +a_tate, (15+12)*3 +a_yoko, (43+12)*3 +a_tate, fill='black') #頭
        cv.create_oval     ( (15-10)*3 +a_yoko, (43-10)*3 +a_tate, (15+10)*3 +a_yoko, (43+10)*3 +a_tate, fill='white') #頭  
        cv.create_text     ( (15   )*3 +a_yoko, (43   )*3 +a_tate, text="そ",     font=("Helvetica", 45,"bold" ) ) #そ

    if tekuteku == 33:
        cv.create_oval     ( (15)*3 +a_yoko, (66)*3 +a_tate, (45)*3 +a_yoko, (70)*3 +a_tate, fill='black', width=0 ) #影
        cv.create_polygon  ( (23)*3 +a_yoko, (37)*3 +a_tate, (41)*3 +a_yoko, (57)*3 +a_tate, (47)*3 +a_yoko, (50)*3 +a_tate ) #体
        cv.create_line     ( (33)*3 +a_yoko, (44)*3 +a_tate, (30)*3 +a_yoko, (54)*3 +a_tate, fill='black', width = 5 ) #右腕上
        cv.create_line     ( (30)*3 +a_yoko, (54)*3 +a_tate, (25)*3 +a_yoko, (62)*3 +a_tate, fill='black', width = 5 ) #右腕下
        cv.create_oval     ( (24-3)*3 +a_yoko, (63-3)*3 +a_tate, (24+3)*3 +a_yoko, (63+3)*3 +a_tate, fill='black') #右拳
        cv.create_line     ( (33)*3 +a_yoko, (44)*3 +a_tate, (36)*3 +a_yoko, (53)*3 +a_tate, fill='black', width = 5 ) #左腕上
        cv.create_line     ( (36)*3 +a_yoko, (53)*3 +a_tate, (37)*3 +a_yoko, (57)*3 +a_tate, fill='black', width = 5 ) #左腕下
        cv.create_oval     ( (37-3)*3 +a_yoko, (59-3)*3 +a_tate, (37+3)*3 +a_yoko, (59+3)*3 +a_tate, fill='black') #左拳
        cv.create_line     ( (43)*3 +a_yoko, (52)*3 +a_tate, (36)*3 +a_yoko, (64)*3 +a_tate, fill='black', width = 5 ) #右脚上
        cv.create_line     ( (36)*3 +a_yoko, (64)*3 +a_tate, (48)*3 +a_yoko, (62)*3 +a_tate, fill='black', width = 5 ) #右脚下
        cv.create_oval     ( (60-3)*3 +a_yoko, (64-3)*3 +a_tate, (60+3)*3 +a_yoko, (64+3)*3 +a_tate, fill='black') #右甲
        cv.create_line     ( (43)*3 +a_yoko, (52)*3 +a_tate, (49)*3 +a_yoko, (64)*3 +a_tate, fill='black', width = 5 ) #左脚上
        cv.create_line     ( (49)*3 +a_yoko, (64)*3 +a_tate, (60)*3 +a_yoko, (62)*3 +a_tate, fill='black', width = 5 ) #左脚下
        cv.create_oval     ( (49-3)*3 +a_yoko, (64-3)*3 +a_tate, (49+3)*3 +a_yoko, (64+3)*3 +a_tate, fill='black') #左甲
        cv.create_oval     ( (23-12)*3 +a_yoko, (35-12)*3 +a_tate, (23+12)*3 +a_yoko, (35+12)*3 +a_tate, fill='black') #頭
        cv.create_oval     ( (23-10)*3 +a_yoko, (35-10)*3 +a_tate, (23+10)*3 +a_yoko, (35+10)*3 +a_tate, fill='white') #頭  
        cv.create_text     ( (23   )*3 +a_yoko, (35   )*3 +a_tate, text="そ",     font=("Helvetica", 45,"bold" ) ) #そ

    if tekuteku == 34:
        cv.create_oval     ( (15)*3 +a_yoko, (66)*3 +a_tate, (45)*3 +a_yoko, (70)*3 +a_tate, fill='black', width=0 ) #影
        cv.create_polygon  ( (23)*3 +a_yoko, (37)*3 +a_tate, (41)*3 +a_yoko, (57)*3 +a_tate, (47)*3 +a_yoko, (50)*3 +a_tate ) #体
        cv.create_line     ( (33)*3 +a_yoko, (44)*3 +a_tate, (30)*3 +a_yoko, (51)*3 +a_tate, fill='black', width = 5 ) #右腕上
        cv.create_line     ( (30)*3 +a_yoko, (51)*3 +a_tate, (25)*3 +a_yoko, (59)*3 +a_tate, fill='black', width = 5 ) #右腕下
        cv.create_oval     ( (24-3)*3 +a_yoko, (60-3)*3 +a_tate, (24+3)*3 +a_yoko, (60+3)*3 +a_tate, fill='black') #右拳
        cv.create_line     ( (34)*3 +a_yoko, (44)*3 +a_tate, (38)*3 +a_yoko, (51)*3 +a_tate, fill='black', width = 5 ) #左腕上
        cv.create_line     ( (38)*3 +a_yoko, (51)*3 +a_tate, (37)*3 +a_yoko, (56)*3 +a_tate, fill='black', width = 5 ) #左腕下
        cv.create_oval     ( (36-3)*3 +a_yoko, (57-3)*3 +a_tate, (36+3)*3 +a_yoko, (57+3)*3 +a_tate, fill='black') #左拳
        cv.create_line     ( (43)*3 +a_yoko, (52)*3 +a_tate, (29)*3 +a_yoko, (54)*3 +a_tate, fill='black', width = 5 ) #右脚上
        cv.create_line     ( (29)*3 +a_yoko, (54)*3 +a_tate, (36)*3 +a_yoko, (63)*3 +a_tate, fill='black', width = 5 ) #右脚下
        cv.create_oval     ( (57-3)*3 +a_yoko, (64-3)*3 +a_tate, (57+3)*3 +a_yoko, (64+3)*3 +a_tate, fill='black') #右甲
        cv.create_line     ( (43)*3 +a_yoko, (52)*3 +a_tate, (45)*3 +a_yoko, (64)*3 +a_tate, fill='black', width = 5 ) #左脚上
        cv.create_line     ( (45)*3 +a_yoko, (64)*3 +a_tate, (56)*3 +a_yoko, (63)*3 +a_tate, fill='black', width = 5 ) #左脚下
        cv.create_oval     ( (36-3)*3 +a_yoko, (64-3)*3 +a_tate, (36+3)*3 +a_yoko, (64+3)*3 +a_tate, fill='black') #左甲
        cv.create_oval     ( (23-12)*3 +a_yoko, (35-12)*3 +a_tate, (23+12)*3 +a_yoko, (35+12)*3 +a_tate, fill='black') #頭
        cv.create_oval     ( (23-10)*3 +a_yoko, (35-10)*3 +a_tate, (23+10)*3 +a_yoko, (35+10)*3 +a_tate, fill='white') #頭  
        cv.create_text     ( (23   )*3 +a_yoko, (35   )*3 +a_tate, text="そ",     font=("Helvetica", 45,"bold" ) ) #そ

    if tekuteku == 35:
        cv.create_oval     ( (15)*3 +a_yoko, (66)*3 +a_tate, (45)*3 +a_yoko, (70)*3 +a_tate, fill='black', width=0 ) #影
        cv.create_polygon  ( (18)*3 +a_yoko, (36)*3 +a_tate, (32)*3 +a_yoko, (59)*3 +a_tate, (39)*3 +a_yoko, (52)*3 +a_tate ) #体
        cv.create_line     ( (24)*3 +a_yoko, (43)*3 +a_tate, (34)*3 +a_yoko, (40)*3 +a_tate, fill='black', width = 5 ) #右腕上
        cv.create_line     ( (34)*3 +a_yoko, (40)*3 +a_tate, (36)*3 +a_yoko, (46)*3 +a_tate, fill='black', width = 5 ) #右腕下
        cv.create_oval     ( (37-3)*3 +a_yoko, (48-3)*3 +a_tate, (37+3)*3 +a_yoko, (48+3)*3 +a_tate, fill='black') #右拳
        cv.create_line     ( (24)*3 +a_yoko, (44)*3 +a_tate, (19)*3 +a_yoko, (53)*3 +a_tate, fill='black', width = 5 ) #左腕上
        cv.create_line     ( (19)*3 +a_yoko, (53)*3 +a_tate, (11)*3 +a_yoko, (57)*3 +a_tate, fill='black', width = 5 ) #左腕下
        cv.create_oval     ( (10-3)*3 +a_yoko, (58-3)*3 +a_tate, (10+3)*3 +a_yoko, (58+3)*3 +a_tate, fill='black') #左拳
        cv.create_line     ( (35)*3 +a_yoko, (54)*3 +a_tate, (21)*3 +a_yoko, (53)*3 +a_tate, fill='black', width = 5 ) #右脚上
        cv.create_line     ( (21)*3 +a_yoko, (53)*3 +a_tate, (20)*3 +a_yoko, (63)*3 +a_tate, fill='black', width = 5 ) #右脚下
        cv.create_oval     ( (18-3)*3 +a_yoko, (64-3)*3 +a_tate, (18+3)*3 +a_yoko, (64+3)*3 +a_tate, fill='black') #右甲
        cv.create_line     ( (35)*3 +a_yoko, (54)*3 +a_tate, (31)*3 +a_yoko, (65)*3 +a_tate, fill='black', width = 5 ) #左脚上
        cv.create_line     ( (31)*3 +a_yoko, (65)*3 +a_tate, (42)*3 +a_yoko, (63)*3 +a_tate, fill='black', width = 5 ) #左脚下
        cv.create_oval     ( (42-3)*3 +a_yoko, (64-3)*3 +a_tate, (42+3)*3 +a_yoko, (64+3)*3 +a_tate, fill='black') #左甲
        cv.create_oval     ( (14-12)*3 +a_yoko, (34-12)*3 +a_tate, (14+12)*3 +a_yoko, (34+12)*3 +a_tate, fill='black') #頭
        cv.create_oval     ( (14-10)*3 +a_yoko, (34-10)*3 +a_tate, (14+10)*3 +a_yoko, (34+10)*3 +a_tate, fill='white') #頭  
        cv.create_text     ( (14   )*3 +a_yoko, (34   )*3 +a_tate, text="そ",     font=("Helvetica", 45,"bold" ) ) #そ


#オープニング　アニメーション
    if tekuteku == 41:  #上に２行く(-2)
#        cv.create_oval     ( (15)*3 +a_yoko, (66)*3 +a_tate, (45)*3 +a_yoko, (70)*3 +a_tate, fill='black', width=0 ) #影
        cv.create_polygon  ( (37)*3 +a_yoko, (11)*3 +a_tate, (22)*3 +a_yoko, (34)*3 +a_tate, (31)*3 +a_yoko, (38)*3 +a_tate ) #体
        cv.create_line     ( (31)*3 +a_yoko, (24)*3 +a_tate, (21)*3 +a_yoko, (20)*3 +a_tate, fill='black', width = 5 ) #右腕上
        cv.create_line     ( (21)*3 +a_yoko, (20)*3 +a_tate, (12)*3 +a_yoko, (17)*3 +a_tate, fill='black', width = 5 ) #右腕下
        cv.create_oval     ( (10-3)*3 +a_yoko, (15-3)*3 +a_tate, (10+3)*3 +a_yoko, (15+3)*3 +a_tate, fill='black') #右拳
        cv.create_line     ( (33)*3 +a_yoko, (26)*3 +a_tate, (39)*3 +a_yoko, (29)*3 +a_tate, fill='black', width = 5 ) #左腕上
        cv.create_line     ( (39)*3 +a_yoko, (29)*3 +a_tate, (37)*3 +a_yoko, (32)*3 +a_tate, fill='black', width = 5 ) #左腕下
        cv.create_oval     ( (37-3)*3 +a_yoko, (35-3)*3 +a_tate, (39+3)*3 +a_yoko, (44+3)*3 +a_tate, fill='black') #左拳
        cv.create_line     ( (39)*3 +a_yoko, (35)*3 +a_tate, (39)*3 +a_yoko, (35)*3 +a_tate, fill='black', width = 5 ) #右脚上
        cv.create_line     ( (39)*3 +a_yoko, (31)*3 +a_tate, (35)*3 +a_yoko, (43)*3 +a_tate, fill='black', width = 5 ) #右脚下
        cv.create_oval     ( (34-3)*3 +a_yoko, (34-3)*3 +a_tate, (34+3)*3 +a_yoko, (34+3)*3 +a_tate, fill='black') #右甲
        cv.create_line     ( (28)*3 +a_yoko, (35)*3 +a_tate, (42)*3 +a_yoko, (35)*3 +a_tate, fill='black', width = 5 ) #左脚上
        cv.create_line     ( (42)*3 +a_yoko, (35)*3 +a_tate, (37)*3 +a_yoko, (45)*3 +a_tate, fill='black', width = 5 ) #左脚下
        cv.create_oval     ( (36-3)*3 +a_yoko, (46-3)*3 +a_tate, (36+3)*3 +a_yoko, (46+3)*3 +a_tate, fill='black') #左甲
        cv.create_oval     ( (41-12)*3 +a_yoko, (14-12)*3 +a_tate, (41+12)*3 +a_yoko, (14+12)*3 +a_tate, fill='black') #頭
        cv.create_oval     ( (41-10)*3 +a_yoko, (14-10)*3 +a_tate, (41+10)*3 +a_yoko, (14+10)*3 +a_tate, fill='white') #頭  
        cv.create_text     ( (41   )*3 +a_yoko, (14   )*3 +a_tate, text="そ",     font=("Helvetica", 45,"bold" ) ) #そ

    if tekuteku == 42:
#        cv.create_oval     ( (15)*3 +a_yoko, (66)*3 +a_tate, (45)*3 +a_yoko, (70)*3 +a_tate, fill='black', width=0 ) #影
        cv.create_polygon  ( (37)*3 +a_yoko, (16)*3 +a_tate, (22)*3 +a_yoko, (39)*3 +a_tate, (31)*3 +a_yoko, (43)*3 +a_tate ) #体
        cv.create_line     ( (33)*3 +a_yoko, (28)*3 +a_tate, (22)*3 +a_yoko, (24)*3 +a_tate, fill='black', width = 5 ) #右腕上
        cv.create_line     ( (22)*3 +a_yoko, (24)*3 +a_tate, (13)*3 +a_yoko, (20)*3 +a_tate, fill='black', width = 5 ) #右腕下
        cv.create_oval     ( (12-3)*3 +a_yoko, (19-3)*3 +a_tate, (12+3)*3 +a_yoko, (19+3)*3 +a_tate, fill='black') #右拳
        cv.create_line     ( (33)*3 +a_yoko, (29)*3 +a_tate, (40)*3 +a_yoko, (31)*3 +a_tate, fill='black', width = 5 ) #左腕上
        cv.create_line     ( (40)*3 +a_yoko, (31)*3 +a_tate, (37)*3 +a_yoko, (35)*3 +a_tate, fill='black', width = 5 ) #左腕下
        cv.create_oval     ( (36-3)*3 +a_yoko, (36-3)*3 +a_tate, (36+3)*3 +a_yoko, (36+3)*3 +a_tate, fill='black') #左拳
        cv.create_line     ( (28)*3 +a_yoko, (39)*3 +a_tate, (33)*3 +a_yoko, (51)*3 +a_tate, fill='black', width = 5 ) #右脚上
        cv.create_line     ( (33)*3 +a_yoko, (51)*3 +a_tate, (31)*3 +a_yoko, (62)*3 +a_tate, fill='black', width = 5 ) #右脚下
        cv.create_oval     ( (31-3)*3 +a_yoko, (64-3)*3 +a_tate, (31+3)*3 +a_yoko, (64+3)*3 +a_tate, fill='black') #右甲
        cv.create_line     ( (24)*3 +a_yoko, (38)*3 +a_tate, (29)*3 +a_yoko, (51)*3 +a_tate, fill='black', width = 5 ) #左脚上
        cv.create_line     ( (29)*3 +a_yoko, (51)*3 +a_tate, (28)*3 +a_yoko, (62)*3 +a_tate, fill='black', width = 5 ) #左脚下
        cv.create_oval     ( (27-3)*3 +a_yoko, (64-3)*3 +a_tate, (27+3)*3 +a_yoko, (64+3)*3 +a_tate, fill='black') #左甲
        cv.create_oval     ( (42-12)*3 +a_yoko, (17-12)*3 +a_tate, (42+12)*3 +a_yoko, (17+12)*3 +a_tate, fill='black') #頭
        cv.create_oval     ( (42-10)*3 +a_yoko, (17-10)*3 +a_tate, (42+10)*3 +a_yoko, (17+10)*3 +a_tate, fill='white') #頭  
        cv.create_text     ( (42   )*3 +a_yoko, (17   )*3 +a_tate, text="そ",     font=("Helvetica", 45,"bold" ) ) #そ

    if tekuteku == 43:
#        cv.create_oval     ( (15)*3 +a_yoko, (66)*3 +a_tate, (45)*3 +a_yoko, (70)*3 +a_tate, fill='black', width=0 ) #影
        cv.create_polygon  ( (37)*3 +a_yoko, (16)*3 +a_tate, (22)*3 +a_yoko, (39)*3 +a_tate, (31)*3 +a_yoko, (43)*3 +a_tate ) #体
        cv.create_line     ( (33)*3 +a_yoko, (28)*3 +a_tate, (22)*3 +a_yoko, (24)*3 +a_tate, fill='black', width = 5 ) #右腕上
        cv.create_line     ( (22)*3 +a_yoko, (24)*3 +a_tate, (13)*3 +a_yoko, (20)*3 +a_tate, fill='black', width = 5 ) #右腕下
        cv.create_oval     ( (12-3)*3 +a_yoko, (19-3)*3 +a_tate, (12+3)*3 +a_yoko, (19+3)*3 +a_tate, fill='black') #右拳
        cv.create_line     ( (33)*3 +a_yoko, (29)*3 +a_tate, (40)*3 +a_yoko, (31)*3 +a_tate, fill='black', width = 5 ) #左腕上
        cv.create_line     ( (40)*3 +a_yoko, (31)*3 +a_tate, (37)*3 +a_yoko, (35)*3 +a_tate, fill='black', width = 5 ) #左腕下
        cv.create_oval     ( (36-3)*3 +a_yoko, (36-3)*3 +a_tate, (36+3)*3 +a_yoko, (36+3)*3 +a_tate, fill='black') #左拳
        cv.create_line     ( (28)*3 +a_yoko, (39)*3 +a_tate, (42)*3 +a_yoko, (39)*3 +a_tate, fill='black', width = 5 ) #右脚上
        cv.create_line     ( (42)*3 +a_yoko, (39)*3 +a_tate, (39)*3 +a_yoko, (50)*3 +a_tate, fill='black', width = 5 ) #右脚下
        cv.create_oval     ( (40-3)*3 +a_yoko, (51-3)*3 +a_tate, (40+3)*3 +a_yoko, (51+3)*3 +a_tate, fill='black') #右甲
        cv.create_line     ( (24)*3 +a_yoko, (38)*3 +a_tate, (29)*3 +a_yoko, (51)*3 +a_tate, fill='black', width = 5 ) #左脚上
        cv.create_line     ( (29)*3 +a_yoko, (51)*3 +a_tate, (28)*3 +a_yoko, (62)*3 +a_tate, fill='black', width = 5 ) #左脚下
        cv.create_oval     ( (27-3)*3 +a_yoko, (64-3)*3 +a_tate, (27+3)*3 +a_yoko, (64+3)*3 +a_tate, fill='black') #左甲
        cv.create_oval     ( (42-12)*3 +a_yoko, (17-12)*3 +a_tate, (42+12)*3 +a_yoko, (17+12)*3 +a_tate, fill='black') #頭
        cv.create_oval     ( (42-10)*3 +a_yoko, (17-10)*3 +a_tate, (42+10)*3 +a_yoko, (17+10)*3 +a_tate, fill='white') #頭  
        cv.create_text     ( (42   )*3 +a_yoko, (17   )*3 +a_tate, text="そ",     font=("Helvetica", 45,"bold" ) ) #そ

    if tekuteku == 44:
#        cv.create_oval     ( (15)*3 +a_yoko, (66)*3 +a_tate, (45)*3 +a_yoko, (70)*3 +a_tate, fill='black', width=0 ) #影
        cv.create_polygon  ( (37)*3 +a_yoko, (17)*3 +a_tate, (22)*3 +a_yoko, (40)*3 +a_tate, (31)*3 +a_yoko, (44)*3 +a_tate ) #体
        cv.create_line     ( (33)*3 +a_yoko, (29)*3 +a_tate, (22)*3 +a_yoko, (25)*3 +a_tate, fill='black', width = 5 ) #右腕上
        cv.create_line     ( (22)*3 +a_yoko, (25)*3 +a_tate, (13)*3 +a_yoko, (21)*3 +a_tate, fill='black', width = 5 ) #右腕下
        cv.create_oval     ( (12-3)*3 +a_yoko, (20-3)*3 +a_tate, (12+3)*3 +a_yoko, (20+3)*3 +a_tate, fill='black') #右拳
        cv.create_line     ( (33)*3 +a_yoko, (30)*3 +a_tate, (40)*3 +a_yoko, (32)*3 +a_tate, fill='black', width = 5 ) #左腕上
        cv.create_line     ( (40)*3 +a_yoko, (32)*3 +a_tate, (37)*3 +a_yoko, (36)*3 +a_tate, fill='black', width = 5 ) #左腕下
        cv.create_oval     ( (36-3)*3 +a_yoko, (37-3)*3 +a_tate, (36+3)*3 +a_yoko, (37+3)*3 +a_tate, fill='black') #左拳
        cv.create_line     ( (29)*3 +a_yoko, (39)*3 +a_tate, (38)*3 +a_yoko, (49)*3 +a_tate, fill='black', width = 5 ) #右脚上
        cv.create_line     ( (38)*3 +a_yoko, (49)*3 +a_tate, (35)*3 +a_yoko, (60)*3 +a_tate, fill='black', width = 5 ) #右脚下
        cv.create_oval     ( (34-3)*3 +a_yoko, (60-3)*3 +a_tate, (34+3)*3 +a_yoko, (60+3)*3 +a_tate, fill='black') #右甲
        cv.create_line     ( (24)*3 +a_yoko, (39)*3 +a_tate, (19)*3 +a_yoko, (51)*3 +a_tate, fill='black', width = 5 ) #左脚上
        cv.create_line     ( (19)*3 +a_yoko, (51)*3 +a_tate, (13)*3 +a_yoko, (61)*3 +a_tate, fill='black', width = 5 ) #左脚下
        cv.create_oval     ( (12-3)*3 +a_yoko, (64-3)*3 +a_tate, (12+3)*3 +a_yoko, (64+3)*3 +a_tate, fill='black') #左甲
        cv.create_oval     ( (42-12)*3 +a_yoko, (18-12)*3 +a_tate, (42+12)*3 +a_yoko, (18+12)*3 +a_tate, fill='black') #頭
        cv.create_oval     ( (42-10)*3 +a_yoko, (18-10)*3 +a_tate, (42+10)*3 +a_yoko, (18+10)*3 +a_tate, fill='white') #頭  
        cv.create_text     ( (42   )*3 +a_yoko, (18   )*3 +a_tate, text="そ",     font=("Helvetica", 45,"bold" ) ) #そ

    if tekuteku == 45:
#        cv.create_oval     ( (15)*3 +a_yoko, (66)*3 +a_tate, (45)*3 +a_yoko, (70)*3 +a_tate, fill='black', width=0 ) #影
        cv.create_polygon  ( (37)*3 +a_yoko, (16)*3 +a_tate, (22)*3 +a_yoko, (39)*3 +a_tate, (31)*3 +a_yoko, (43)*3 +a_tate ) #体
        cv.create_line     ( (33)*3 +a_yoko, (28)*3 +a_tate, (22)*3 +a_yoko, (24)*3 +a_tate, fill='black', width = 5 ) #右腕上
        cv.create_line     ( (22)*3 +a_yoko, (24)*3 +a_tate, (13)*3 +a_yoko, (20)*3 +a_tate, fill='black', width = 5 ) #右腕下
        cv.create_oval     ( (12-3)*3 +a_yoko, (19-3)*3 +a_tate, (12+3)*3 +a_yoko, (19+3)*3 +a_tate, fill='black') #右拳
        cv.create_line     ( (33)*3 +a_yoko, (29)*3 +a_tate, (40)*3 +a_yoko, (31)*3 +a_tate, fill='black', width = 5 ) #左腕上
        cv.create_line     ( (40)*3 +a_yoko, (31)*3 +a_tate, (37)*3 +a_yoko, (35)*3 +a_tate, fill='black', width = 5 ) #左腕下
        cv.create_oval     ( (36-3)*3 +a_yoko, (36-3)*3 +a_tate, (36+3)*3 +a_yoko, (36+3)*3 +a_tate, fill='black') #左拳
        cv.create_line     ( (28)*3 +a_yoko, (39)*3 +a_tate, (33)*3 +a_yoko, (51)*3 +a_tate, fill='black', width = 5 ) #右脚上
        cv.create_line     ( (33)*3 +a_yoko, (51)*3 +a_tate, (31)*3 +a_yoko, (62)*3 +a_tate, fill='black', width = 5 ) #右脚下
        cv.create_oval     ( (31-3)*3 +a_yoko, (64-3)*3 +a_tate, (31+3)*3 +a_yoko, (64+3)*3 +a_tate, fill='black') #右甲
        cv.create_line     ( (24)*3 +a_yoko, (38)*3 +a_tate, (29)*3 +a_yoko, (51)*3 +a_tate, fill='black', width = 5 ) #左脚上
        cv.create_line     ( (29)*3 +a_yoko, (51)*3 +a_tate, (28)*3 +a_yoko, (62)*3 +a_tate, fill='black', width = 5 ) #左脚下
        cv.create_oval     ( (27-3)*3 +a_yoko, (64-3)*3 +a_tate, (27+3)*3 +a_yoko, (64+3)*3 +a_tate, fill='black') #左甲
        cv.create_oval     ( (42-12)*3 +a_yoko, (17-12)*3 +a_tate, (42+12)*3 +a_yoko, (17+12)*3 +a_tate, fill='black') #頭
        cv.create_oval     ( (42-10)*3 +a_yoko, (17-10)*3 +a_tate, (42+10)*3 +a_yoko, (17+10)*3 +a_tate, fill='white') #頭  
        cv.create_text     ( (42   )*3 +a_yoko, (17   )*3 +a_tate, text="そ",     font=("Helvetica", 45,"bold" ) ) #そ

    if tekuteku == 46:
#        cv.create_oval     ( (15)*3 +a_yoko, (66)*3 +a_tate, (45)*3 +a_yoko, (70)*3 +a_tate, fill='black', width=0 ) #影
        cv.create_polygon  ( (37)*3 +a_yoko, (16)*3 +a_tate, (22)*3 +a_yoko, (39)*3 +a_tate, (31)*3 +a_yoko, (43)*3 +a_tate ) #体
        cv.create_line     ( (33)*3 +a_yoko, (28)*3 +a_tate, (22)*3 +a_yoko, (24)*3 +a_tate, fill='black', width = 5 ) #右腕上
        cv.create_line     ( (22)*3 +a_yoko, (24)*3 +a_tate, (13)*3 +a_yoko, (20)*3 +a_tate, fill='black', width = 5 ) #右腕下
        cv.create_oval     ( (12-3)*3 +a_yoko, (19-3)*3 +a_tate, (12+3)*3 +a_yoko, (19+3)*3 +a_tate, fill='black') #右拳
        cv.create_line     ( (33)*3 +a_yoko, (29)*3 +a_tate, (40)*3 +a_yoko, (31)*3 +a_tate, fill='black', width = 5 ) #左腕上
        cv.create_line     ( (40)*3 +a_yoko, (31)*3 +a_tate, (37)*3 +a_yoko, (35)*3 +a_tate, fill='black', width = 5 ) #左腕下
        cv.create_oval     ( (36-3)*3 +a_yoko, (36-3)*3 +a_tate, (36+3)*3 +a_yoko, (36+3)*3 +a_tate, fill='black') #左拳
        cv.create_line     ( (26)*3 +a_yoko, (41)*3 +a_tate, (20)*3 +a_yoko, (52)*3 +a_tate, fill='black', width = 5 ) #右脚上
        cv.create_line     ( (20)*3 +a_yoko, (52)*3 +a_tate, (14)*3 +a_yoko, (62)*3 +a_tate, fill='black', width = 5 ) #右脚下
        cv.create_oval     ( (13-3)*3 +a_yoko, (64-3)*3 +a_tate, (13+3)*3 +a_yoko, (64+3)*3 +a_tate, fill='black') #右甲
        cv.create_line     ( (29)*3 +a_yoko, (41)*3 +a_tate, (39)*3 +a_yoko, (50)*3 +a_tate, fill='black', width = 5 ) #左脚上
        cv.create_line     ( (39)*3 +a_yoko, (50)*3 +a_tate, (32)*3 +a_yoko, (60)*3 +a_tate, fill='black', width = 5 ) #左脚下
        cv.create_oval     ( (32-3)*3 +a_yoko, (62-3)*3 +a_tate, (32+3)*3 +a_yoko, (62+3)*3 +a_tate, fill='black') #左甲
        cv.create_oval     ( (42-12)*3 +a_yoko, (17-12)*3 +a_tate, (42+12)*3 +a_yoko, (17+12)*3 +a_tate, fill='black') #頭
        cv.create_oval     ( (42-10)*3 +a_yoko, (17-10)*3 +a_tate, (42+10)*3 +a_yoko, (17+10)*3 +a_tate, fill='white') #頭  
        cv.create_text     ( (42   )*3 +a_yoko, (17   )*3 +a_tate, text="そ",     font=("Helvetica", 45,"bold" ) ) #そ
        
    if tekuteku == 47:
#        cv.create_oval     ( (15)*3 +a_yoko, (66)*3 +a_tate, (45)*3 +a_yoko, (70)*3 +a_tate, fill='black', width=0 ) #影
        cv.create_polygon  ( (37)*3 +a_yoko, (16)*3 +a_tate, (22)*3 +a_yoko, (39)*3 +a_tate, (31)*3 +a_yoko, (43)*3 +a_tate ) #体
        cv.create_line     ( (33)*3 +a_yoko, (28)*3 +a_tate, (22)*3 +a_yoko, (24)*3 +a_tate, fill='black', width = 5 ) #右腕上
        cv.create_line     ( (22)*3 +a_yoko, (24)*3 +a_tate, (13)*3 +a_yoko, (20)*3 +a_tate, fill='black', width = 5 ) #右腕下
        cv.create_oval     ( (12-3)*3 +a_yoko, (19-3)*3 +a_tate, (12+3)*3 +a_yoko, (19+3)*3 +a_tate, fill='black') #右拳
        cv.create_line     ( (33)*3 +a_yoko, (29)*3 +a_tate, (40)*3 +a_yoko, (31)*3 +a_tate, fill='black', width = 5 ) #左腕上
        cv.create_line     ( (40)*3 +a_yoko, (31)*3 +a_tate, (37)*3 +a_yoko, (35)*3 +a_tate, fill='black', width = 5 ) #左腕下
        cv.create_oval     ( (36-3)*3 +a_yoko, (36-3)*3 +a_tate, (36+3)*3 +a_yoko, (36+3)*3 +a_tate, fill='black') #左拳
        cv.create_line     ( (28)*3 +a_yoko, (39)*3 +a_tate, (42)*3 +a_yoko, (39)*3 +a_tate, fill='black', width = 5 ) #右脚上
        cv.create_line     ( (42)*3 +a_yoko, (39)*3 +a_tate, (39)*3 +a_yoko, (50)*3 +a_tate, fill='black', width = 5 ) #右脚下
        cv.create_oval     ( (40-3)*3 +a_yoko, (51-3)*3 +a_tate, (40+3)*3 +a_yoko, (51+3)*3 +a_tate, fill='black') #右甲
        cv.create_line     ( (24)*3 +a_yoko, (38)*3 +a_tate, (29)*3 +a_yoko, (51)*3 +a_tate, fill='black', width = 5 ) #左脚上
        cv.create_line     ( (29)*3 +a_yoko, (51)*3 +a_tate, (28)*3 +a_yoko, (62)*3 +a_tate, fill='black', width = 5 ) #左脚下
        cv.create_oval     ( (27-3)*3 +a_yoko, (64-3)*3 +a_tate, (27+3)*3 +a_yoko, (64+3)*3 +a_tate, fill='black') #左甲
        cv.create_oval     ( (42-12)*3 +a_yoko, (17-12)*3 +a_tate, (42+12)*3 +a_yoko, (17+12)*3 +a_tate, fill='black') #頭
        cv.create_oval     ( (42-10)*3 +a_yoko, (17-10)*3 +a_tate, (42+10)*3 +a_yoko, (17+10)*3 +a_tate, fill='white') #頭  
        cv.create_text     ( (42   )*3 +a_yoko, (17   )*3 +a_tate, text="そ",     font=("Helvetica", 45,"bold" ) ) #そ

    if tekuteku == 48:
#        cv.create_oval     ( (15)*3 +a_yoko, (66)*3 +a_tate, (45)*3 +a_yoko, (70)*3 +a_tate, fill='black', width=0 ) #影
        cv.create_polygon  ( (37)*3 +a_yoko, (17)*3 +a_tate, (22)*3 +a_yoko, (40)*3 +a_tate, (31)*3 +a_yoko, (44)*3 +a_tate ) #体
        cv.create_line     ( (33)*3 +a_yoko, (29)*3 +a_tate, (22)*3 +a_yoko, (25)*3 +a_tate, fill='black', width = 5 ) #右腕上
        cv.create_line     ( (22)*3 +a_yoko, (25)*3 +a_tate, (13)*3 +a_yoko, (21)*3 +a_tate, fill='black', width = 5 ) #右腕下
        cv.create_oval     ( (12-3)*3 +a_yoko, (20-3)*3 +a_tate, (12+3)*3 +a_yoko, (20+3)*3 +a_tate, fill='black') #右拳
        cv.create_line     ( (33)*3 +a_yoko, (30)*3 +a_tate, (40)*3 +a_yoko, (32)*3 +a_tate, fill='black', width = 5 ) #左腕上
        cv.create_line     ( (40)*3 +a_yoko, (32)*3 +a_tate, (37)*3 +a_yoko, (36)*3 +a_tate, fill='black', width = 5 ) #左腕下
        cv.create_oval     ( (36-3)*3 +a_yoko, (37-3)*3 +a_tate, (36+3)*3 +a_yoko, (37+3)*3 +a_tate, fill='black') #左拳
        cv.create_line     ( (29)*3 +a_yoko, (39)*3 +a_tate, (38)*3 +a_yoko, (49)*3 +a_tate, fill='black', width = 5 ) #右脚上
        cv.create_line     ( (38)*3 +a_yoko, (49)*3 +a_tate, (35)*3 +a_yoko, (60)*3 +a_tate, fill='black', width = 5 ) #右脚下
        cv.create_oval     ( (34-3)*3 +a_yoko, (60-3)*3 +a_tate, (34+3)*3 +a_yoko, (60+3)*3 +a_tate, fill='black') #右甲
        cv.create_line     ( (24)*3 +a_yoko, (39)*3 +a_tate, (19)*3 +a_yoko, (51)*3 +a_tate, fill='black', width = 5 ) #左脚上
        cv.create_line     ( (19)*3 +a_yoko, (51)*3 +a_tate, (13)*3 +a_yoko, (61)*3 +a_tate, fill='black', width = 5 ) #左脚下
        cv.create_oval     ( (12-3)*3 +a_yoko, (64-3)*3 +a_tate, (12+3)*3 +a_yoko, (64+3)*3 +a_tate, fill='black') #左甲
        cv.create_oval     ( (42-12)*3 +a_yoko, (18-12)*3 +a_tate, (42+12)*3 +a_yoko, (18+12)*3 +a_tate, fill='black') #頭
        cv.create_oval     ( (42-10)*3 +a_yoko, (18-10)*3 +a_tate, (42+10)*3 +a_yoko, (18+10)*3 +a_tate, fill='white') #頭  
        cv.create_text     ( (42   )*3 +a_yoko, (18   )*3 +a_tate, text="そ",     font=("Helvetica", 45,"bold" ) ) #そ

    if tekuteku == 49:
#        cv.create_oval     ( (15)*3 +a_yoko, (66)*3 +a_tate, (45)*3 +a_yoko, (70)*3 +a_tate, fill='black', width=0 ) #影
        cv.create_polygon  ( (37)*3 +a_yoko, (16)*3 +a_tate, (22)*3 +a_yoko, (39)*3 +a_tate, (31)*3 +a_yoko, (43)*3 +a_tate ) #体
        cv.create_line     ( (33)*3 +a_yoko, (28)*3 +a_tate, (22)*3 +a_yoko, (24)*3 +a_tate, fill='black', width = 5 ) #右腕上
        cv.create_line     ( (22)*3 +a_yoko, (24)*3 +a_tate, (13)*3 +a_yoko, (20)*3 +a_tate, fill='black', width = 5 ) #右腕下
        cv.create_oval     ( (12-3)*3 +a_yoko, (19-3)*3 +a_tate, (12+3)*3 +a_yoko, (19+3)*3 +a_tate, fill='black') #右拳
        cv.create_line     ( (33)*3 +a_yoko, (29)*3 +a_tate, (40)*3 +a_yoko, (31)*3 +a_tate, fill='black', width = 5 ) #左腕上
        cv.create_line     ( (40)*3 +a_yoko, (31)*3 +a_tate, (37)*3 +a_yoko, (35)*3 +a_tate, fill='black', width = 5 ) #左腕下
        cv.create_oval     ( (36-3)*3 +a_yoko, (36-3)*3 +a_tate, (36+3)*3 +a_yoko, (36+3)*3 +a_tate, fill='black') #左拳
        cv.create_line     ( (28)*3 +a_yoko, (39)*3 +a_tate, (33)*3 +a_yoko, (51)*3 +a_tate, fill='black', width = 5 ) #右脚上
        cv.create_line     ( (33)*3 +a_yoko, (51)*3 +a_tate, (31)*3 +a_yoko, (62)*3 +a_tate, fill='black', width = 5 ) #右脚下
        cv.create_oval     ( (31-3)*3 +a_yoko, (64-3)*3 +a_tate, (31+3)*3 +a_yoko, (64+3)*3 +a_tate, fill='black') #右甲
        cv.create_line     ( (24)*3 +a_yoko, (38)*3 +a_tate, (29)*3 +a_yoko, (51)*3 +a_tate, fill='black', width = 5 ) #左脚上
        cv.create_line     ( (29)*3 +a_yoko, (51)*3 +a_tate, (28)*3 +a_yoko, (62)*3 +a_tate, fill='black', width = 5 ) #左脚下
        cv.create_oval     ( (27-3)*3 +a_yoko, (64-3)*3 +a_tate, (27+3)*3 +a_yoko, (64+3)*3 +a_tate, fill='black') #左甲
        cv.create_oval     ( (42-12)*3 +a_yoko, (17-12)*3 +a_tate, (42+12)*3 +a_yoko, (17+12)*3 +a_tate, fill='black') #頭
        cv.create_oval     ( (42-10)*3 +a_yoko, (17-10)*3 +a_tate, (42+10)*3 +a_yoko, (17+10)*3 +a_tate, fill='white') #頭  
        cv.create_text     ( (42   )*3 +a_yoko, (17   )*3 +a_tate, text="そ",     font=("Helvetica", 45,"bold" ) ) #そ

    if tekuteku == 50:
#        cv.create_oval     ( (15)*3 +a_yoko, (66)*3 +a_tate, (45)*3 +a_yoko, (70)*3 +a_tate, fill='black', width=0 ) #影
        cv.create_polygon  ( (37)*3 +a_yoko, (16)*3 +a_tate, (22)*3 +a_yoko, (39)*3 +a_tate, (31)*3 +a_yoko, (43)*3 +a_tate ) #体
        cv.create_line     ( (33)*3 +a_yoko, (28)*3 +a_tate, (22)*3 +a_yoko, (24)*3 +a_tate, fill='black', width = 5 ) #右腕上
        cv.create_line     ( (22)*3 +a_yoko, (24)*3 +a_tate, (13)*3 +a_yoko, (20)*3 +a_tate, fill='black', width = 5 ) #右腕下
        cv.create_oval     ( (12-3)*3 +a_yoko, (19-3)*3 +a_tate, (12+3)*3 +a_yoko, (19+3)*3 +a_tate, fill='black') #右拳
        cv.create_line     ( (33)*3 +a_yoko, (29)*3 +a_tate, (40)*3 +a_yoko, (31)*3 +a_tate, fill='black', width = 5 ) #左腕上
        cv.create_line     ( (40)*3 +a_yoko, (31)*3 +a_tate, (37)*3 +a_yoko, (35)*3 +a_tate, fill='black', width = 5 ) #左腕下
        cv.create_oval     ( (36-3)*3 +a_yoko, (36-3)*3 +a_tate, (36+3)*3 +a_yoko, (36+3)*3 +a_tate, fill='black') #左拳
        cv.create_line     ( (26)*3 +a_yoko, (41)*3 +a_tate, (20)*3 +a_yoko, (52)*3 +a_tate, fill='black', width = 5 ) #右脚上
        cv.create_line     ( (20)*3 +a_yoko, (52)*3 +a_tate, (14)*3 +a_yoko, (62)*3 +a_tate, fill='black', width = 5 ) #右脚下
        cv.create_oval     ( (13-3)*3 +a_yoko, (64-3)*3 +a_tate, (13+3)*3 +a_yoko, (64+3)*3 +a_tate, fill='black') #右甲
        cv.create_line     ( (29)*3 +a_yoko, (41)*3 +a_tate, (39)*3 +a_yoko, (50)*3 +a_tate, fill='black', width = 5 ) #左脚上
        cv.create_line     ( (39)*3 +a_yoko, (50)*3 +a_tate, (32)*3 +a_yoko, (60)*3 +a_tate, fill='black', width = 5 ) #左脚下
        cv.create_oval     ( (32-3)*3 +a_yoko, (62-3)*3 +a_tate, (32+3)*3 +a_yoko, (62+3)*3 +a_tate, fill='black') #左甲
        cv.create_oval     ( (42-12)*3 +a_yoko, (17-12)*3 +a_tate, (42+12)*3 +a_yoko, (17+12)*3 +a_tate, fill='black') #頭
        cv.create_oval     ( (42-10)*3 +a_yoko, (17-10)*3 +a_tate, (42+10)*3 +a_yoko, (17+10)*3 +a_tate, fill='white') #頭  
        cv.create_text     ( (42   )*3 +a_yoko, (17   )*3 +a_tate, text="そ",     font=("Helvetica", 45,"bold" ) ) #そ
#オープニング　アニメーション
    if tekuteku == 51:  #上に２行く(-2)
#        cv.create_oval     ( (15)*3 +a_yoko, (66)*3 +a_tate, (45)*3 +a_yoko, (70)*3 +a_tate, fill='black', width=0 ) #影
        cv.create_polygon  ( (28)*3 +a_yoko, (11)*3 +a_tate, (35)*3 +a_yoko, (40)*3 +a_tate, (43)*3 +a_yoko, (35)*3 +a_tate ) #体
        cv.create_line     ( (35)*3 +a_yoko, (25)*3 +a_tate, (45)*3 +a_yoko, (21)*3 +a_tate, fill='black', width = 5 ) #右腕上
        cv.create_line     ( (45)*3 +a_yoko, (21)*3 +a_tate, (54)*3 +a_yoko, (14)*3 +a_tate, fill='black', width = 5 ) #右腕下
        cv.create_oval     ( (54-3)*3 +a_yoko, (14-3)*3 +a_tate, (54+3)*3 +a_yoko, (16+3)*3 +a_tate, fill='black') #右拳
        cv.create_line     ( (33)*3 +a_yoko, (26)*3 +a_tate, (26)*3 +a_yoko, (29)*3 +a_tate, fill='black', width = 5 ) #左腕上
        cv.create_line     ( (26)*3 +a_yoko, (29)*3 +a_tate, (24)*3 +a_yoko, (34)*3 +a_tate, fill='black', width = 5 ) #左腕下
        cv.create_oval     ( (24-3)*3 +a_yoko, (35-3)*3 +a_tate, (24+3)*3 +a_yoko, (35+3)*3 +a_tate, fill='black') #左拳
        cv.create_line     ( (39)*3 +a_yoko, (35)*3 +a_tate, (25)*3 +a_yoko, (35)*3 +a_tate, fill='black', width = 5 ) #右脚上
        cv.create_line     ( (25)*3 +a_yoko, (35)*3 +a_tate, (30)*3 +a_yoko, (45)*3 +a_tate, fill='black', width = 5 ) #右脚下
        cv.create_oval     ( (31-3)*3 +a_yoko, (46-3)*3 +a_tate, (31+3)*3 +a_yoko, (46+3)*3 +a_tate, fill='black') #右甲
        cv.create_line     ( (41)*3 +a_yoko, (33)*3 +a_tate, (27)*3 +a_yoko, (32)*3 +a_tate, fill='black', width = 5 ) #左脚上
        cv.create_line     ( (27)*3 +a_yoko, (32)*3 +a_tate, (33)*3 +a_yoko, (43)*3 +a_tate, fill='black', width = 5 ) #左脚下
        cv.create_oval     ( (34-3)*3 +a_yoko, (44-3)*3 +a_tate, (34+3)*3 +a_yoko, (44+3)*3 +a_tate, fill='black') #左甲
        cv.create_oval     ( (25-12)*3 +a_yoko, (14-12)*3 +a_tate, (25+12)*3 +a_yoko, (14+12)*3 +a_tate, fill='black') #頭
        cv.create_oval     ( (25-10)*3 +a_yoko, (14-10)*3 +a_tate, (25+10)*3 +a_yoko, (14+10)*3 +a_tate, fill='white') #頭  
        cv.create_text     ( (25   )*3 +a_yoko, (14   )*3 +a_tate, text="そ",     font=("Helvetica", 45,"bold" ) ) #そ

    if tekuteku == 52:
#        cv.create_oval     ( (15)*3 +a_yoko, (66)*3 +a_tate, (45)*3 +a_yoko, (70)*3 +a_tate, fill='black', width=0 ) #影
        cv.create_polygon  ( (28)*3 +a_yoko, (16)*3 +a_tate, (35)*3 +a_yoko, (43)*3 +a_tate, (44)*3 +a_yoko, (38)*3 +a_tate ) #体
        cv.create_line     ( (34)*3 +a_yoko, (28)*3 +a_tate, (44)*3 +a_yoko, (24)*3 +a_tate, fill='black', width = 5 ) #右腕上
        cv.create_line     ( (44)*3 +a_yoko, (24)*3 +a_tate, (52)*3 +a_yoko, (19)*3 +a_tate, fill='black', width = 5 ) #右腕下
        cv.create_oval     ( (53-3)*3 +a_yoko, (19-3)*3 +a_tate, (53+3)*3 +a_yoko, (19+3)*3 +a_tate, fill='black') #右拳
        cv.create_line     ( (32)*3 +a_yoko, (29)*3 +a_tate, (26)*3 +a_yoko, (32)*3 +a_tate, fill='black', width = 5 ) #左腕上
        cv.create_line     ( (26)*3 +a_yoko, (32)*3 +a_tate, (29)*3 +a_yoko, (36)*3 +a_tate, fill='black', width = 5 ) #左腕下
        cv.create_oval     ( (30-3)*3 +a_yoko, (37-3)*3 +a_tate, (30+3)*3 +a_yoko, (37+3)*3 +a_tate, fill='black') #左拳
        cv.create_line     ( (36)*3 +a_yoko, (39)*3 +a_tate, (32)*3 +a_yoko, (52)*3 +a_tate, fill='black', width = 5 ) #右脚上
        cv.create_line     ( (32)*3 +a_yoko, (52)*3 +a_tate, (34)*3 +a_yoko, (62)*3 +a_tate, fill='black', width = 5 ) #右脚下
        cv.create_oval     ( (34-3)*3 +a_yoko, (64-3)*3 +a_tate, (34+3)*3 +a_yoko, (64+3)*3 +a_tate, fill='black') #右甲
        cv.create_line     ( (41)*3 +a_yoko, (38)*3 +a_tate, (37)*3 +a_yoko, (50)*3 +a_tate, fill='black', width = 5 ) #左脚上
        cv.create_line     ( (37)*3 +a_yoko, (50)*3 +a_tate, (39)*3 +a_yoko, (62)*3 +a_tate, fill='black', width = 5 ) #左脚下
        cv.create_oval     ( (39-3)*3 +a_yoko, (64-3)*3 +a_tate, (39+3)*3 +a_yoko, (64+3)*3 +a_tate, fill='black') #左甲
        cv.create_oval     ( (25-12)*3 +a_yoko, (17-12)*3 +a_tate, (25+12)*3 +a_yoko, (17+12)*3 +a_tate, fill='black') #頭
        cv.create_oval     ( (25-10)*3 +a_yoko, (17-10)*3 +a_tate, (25+10)*3 +a_yoko, (17+10)*3 +a_tate, fill='white') #頭  
        cv.create_text     ( (25   )*3 +a_yoko, (17   )*3 +a_tate, text="そ",     font=("Helvetica", 45,"bold" ) ) #そ

    if tekuteku == 53:
#        cv.create_oval     ( (15)*3 +a_yoko, (66)*3 +a_tate, (45)*3 +a_yoko, (70)*3 +a_tate, fill='black', width=0 ) #影
        cv.create_polygon  ( (28)*3 +a_yoko, (16)*3 +a_tate, (35)*3 +a_yoko, (43)*3 +a_tate, (44)*3 +a_yoko, (38)*3 +a_tate ) #体
        cv.create_line     ( (34)*3 +a_yoko, (28)*3 +a_tate, (44)*3 +a_yoko, (24)*3 +a_tate, fill='black', width = 5 ) #右腕上
        cv.create_line     ( (44)*3 +a_yoko, (24)*3 +a_tate, (52)*3 +a_yoko, (19)*3 +a_tate, fill='black', width = 5 ) #右腕下
        cv.create_oval     ( (53-3)*3 +a_yoko, (19-3)*3 +a_tate, (53+3)*3 +a_yoko, (19+3)*3 +a_tate, fill='black') #右拳
        cv.create_line     ( (32)*3 +a_yoko, (29)*3 +a_tate, (26)*3 +a_yoko, (32)*3 +a_tate, fill='black', width = 5 ) #左腕上
        cv.create_line     ( (26)*3 +a_yoko, (32)*3 +a_tate, (29)*3 +a_yoko, (36)*3 +a_tate, fill='black', width = 5 ) #左腕下
        cv.create_oval     ( (30-3)*3 +a_yoko, (37-3)*3 +a_tate, (30+3)*3 +a_yoko, (37+3)*3 +a_tate, fill='black') #左拳
        cv.create_line     ( (37)*3 +a_yoko, (39)*3 +a_tate, (23)*3 +a_yoko, (39)*3 +a_tate, fill='black', width = 5 ) #右脚上
        cv.create_line     ( (23)*3 +a_yoko, (39)*3 +a_tate, (28)*3 +a_yoko, (50)*3 +a_tate, fill='black', width = 5 ) #右脚下
        cv.create_oval     ( (27-3)*3 +a_yoko, (50-3)*3 +a_tate, (27+3)*3 +a_yoko, (50+3)*3 +a_tate, fill='black') #右甲
        cv.create_line     ( (41)*3 +a_yoko, (38)*3 +a_tate, (37)*3 +a_yoko, (50)*3 +a_tate, fill='black', width = 5 ) #左脚上
        cv.create_line     ( (37)*3 +a_yoko, (50)*3 +a_tate, (39)*3 +a_yoko, (62)*3 +a_tate, fill='black', width = 5 ) #左脚下
        cv.create_oval     ( (39-3)*3 +a_yoko, (64-3)*3 +a_tate, (39+3)*3 +a_yoko, (64+3)*3 +a_tate, fill='black') #左甲
        cv.create_oval     ( (25-12)*3 +a_yoko, (17-12)*3 +a_tate, (25+12)*3 +a_yoko, (17+12)*3 +a_tate, fill='black') #頭
        cv.create_oval     ( (25-10)*3 +a_yoko, (17-10)*3 +a_tate, (25+10)*3 +a_yoko, (17+10)*3 +a_tate, fill='white') #頭  
        cv.create_text     ( (25   )*3 +a_yoko, (17   )*3 +a_tate, text="そ",     font=("Helvetica", 45,"bold" ) ) #そ

    if tekuteku == 54:
#        cv.create_oval     ( (15)*3 +a_yoko, (66)*3 +a_tate, (45)*3 +a_yoko, (70)*3 +a_tate, fill='black', width=0 ) #影
        cv.create_polygon  ( (28)*3 +a_yoko, (17)*3 +a_tate, (35)*3 +a_yoko, (44)*3 +a_tate, (44)*3 +a_yoko, (39)*3 +a_tate ) #体
        cv.create_line     ( (34)*3 +a_yoko, (29)*3 +a_tate, (44)*3 +a_yoko, (25)*3 +a_tate, fill='black', width = 5 ) #右腕上
        cv.create_line     ( (44)*3 +a_yoko, (25)*3 +a_tate, (52)*3 +a_yoko, (20)*3 +a_tate, fill='black', width = 5 ) #右腕下
        cv.create_oval     ( (53-3)*3 +a_yoko, (20-3)*3 +a_tate, (53+3)*3 +a_yoko, (19+3)*3 +a_tate, fill='black') #右拳
        cv.create_line     ( (32)*3 +a_yoko, (30)*3 +a_tate, (26)*3 +a_yoko, (33)*3 +a_tate, fill='black', width = 5 ) #左腕上
        cv.create_line     ( (26)*3 +a_yoko, (33)*3 +a_tate, (29)*3 +a_yoko, (37)*3 +a_tate, fill='black', width = 5 ) #左腕下
        cv.create_oval     ( (30-3)*3 +a_yoko, (38-3)*3 +a_tate, (30+3)*3 +a_yoko, (38+3)*3 +a_tate, fill='black') #左拳
        cv.create_line     ( (38)*3 +a_yoko, (41)*3 +a_tate, (26)*3 +a_yoko, (50)*3 +a_tate, fill='black', width = 5 ) #右脚上
        cv.create_line     ( (26)*3 +a_yoko, (50)*3 +a_tate, (30)*3 +a_yoko, (60)*3 +a_tate, fill='black', width = 5 ) #右脚下
        cv.create_oval     ( (31-3)*3 +a_yoko, (62-3)*3 +a_tate, (31+3)*3 +a_yoko, (62+3)*3 +a_tate, fill='black') #右甲
        cv.create_line     ( (40)*3 +a_yoko, (40)*3 +a_tate, (47)*3 +a_yoko, (52)*3 +a_tate, fill='black', width = 5 ) #左脚上
        cv.create_line     ( (47)*3 +a_yoko, (52)*3 +a_tate, (53)*3 +a_yoko, (62)*3 +a_tate, fill='black', width = 5 ) #左脚下
        cv.create_oval     ( (54-3)*3 +a_yoko, (64-3)*3 +a_tate, (54+3)*3 +a_yoko, (64+3)*3 +a_tate, fill='black') #左甲
        cv.create_oval     ( (25-12)*3 +a_yoko, (18-12)*3 +a_tate, (25+12)*3 +a_yoko, (18+12)*3 +a_tate, fill='black') #頭
        cv.create_oval     ( (25-10)*3 +a_yoko, (18-10)*3 +a_tate, (25+10)*3 +a_yoko, (18+10)*3 +a_tate, fill='white') #頭  
        cv.create_text     ( (25   )*3 +a_yoko, (18   )*3 +a_tate, text="そ",     font=("Helvetica", 45,"bold" ) ) #そ
 
    if tekuteku == 55:
#        cv.create_oval     ( (15)*3 +a_yoko, (66)*3 +a_tate, (45)*3 +a_yoko, (70)*3 +a_tate, fill='black', width=0 ) #影
        cv.create_polygon  ( (28)*3 +a_yoko, (16)*3 +a_tate, (35)*3 +a_yoko, (43)*3 +a_tate, (44)*3 +a_yoko, (38)*3 +a_tate ) #体
        cv.create_line     ( (34)*3 +a_yoko, (28)*3 +a_tate, (44)*3 +a_yoko, (24)*3 +a_tate, fill='black', width = 5 ) #右腕上
        cv.create_line     ( (44)*3 +a_yoko, (24)*3 +a_tate, (52)*3 +a_yoko, (19)*3 +a_tate, fill='black', width = 5 ) #右腕下
        cv.create_oval     ( (53-3)*3 +a_yoko, (19-3)*3 +a_tate, (53+3)*3 +a_yoko, (19+3)*3 +a_tate, fill='black') #右拳
        cv.create_line     ( (32)*3 +a_yoko, (29)*3 +a_tate, (26)*3 +a_yoko, (32)*3 +a_tate, fill='black', width = 5 ) #左腕上
        cv.create_line     ( (26)*3 +a_yoko, (32)*3 +a_tate, (29)*3 +a_yoko, (36)*3 +a_tate, fill='black', width = 5 ) #左腕下
        cv.create_oval     ( (30-3)*3 +a_yoko, (37-3)*3 +a_tate, (30+3)*3 +a_yoko, (37+3)*3 +a_tate, fill='black') #左拳
        cv.create_line     ( (37)*3 +a_yoko, (38)*3 +a_tate, (37)*3 +a_yoko, (52)*3 +a_tate, fill='black', width = 5 ) #右脚上
        cv.create_line     ( (37)*3 +a_yoko, (52)*3 +a_tate, (40)*3 +a_yoko, (62)*3 +a_tate, fill='black', width = 5 ) #右脚下
        cv.create_oval     ( (34-3)*3 +a_yoko, (50-3)*3 +a_tate, (34+3)*3 +a_yoko, (50+3)*3 +a_tate, fill='black') #右甲
        cv.create_line     ( (41)*3 +a_yoko, (38)*3 +a_tate, (28)*3 +a_yoko, (40)*3 +a_tate, fill='black', width = 5 ) #左脚上
        cv.create_line     ( (28)*3 +a_yoko, (40)*3 +a_tate, (33)*3 +a_yoko, (49)*3 +a_tate, fill='black', width = 5 ) #左脚下
        cv.create_oval     ( (40-3)*3 +a_yoko, (64-3)*3 +a_tate, (40+3)*3 +a_yoko, (64+3)*3 +a_tate, fill='black') #左甲
        cv.create_oval     ( (25-12)*3 +a_yoko, (17-12)*3 +a_tate, (25+12)*3 +a_yoko, (17+12)*3 +a_tate, fill='black') #頭
        cv.create_oval     ( (25-10)*3 +a_yoko, (17-10)*3 +a_tate, (25+10)*3 +a_yoko, (17+10)*3 +a_tate, fill='white') #頭  
        cv.create_text     ( (25   )*3 +a_yoko, (17   )*3 +a_tate, text="そ",     font=("Helvetica", 45,"bold" ) ) #そ

    if tekuteku == 56:
#        cv.create_oval     ( (15)*3 +a_yoko, (66)*3 +a_tate, (45)*3 +a_yoko, (70)*3 +a_tate, fill='black', width=0 ) #影
        cv.create_polygon  ( (28)*3 +a_yoko, (19)*3 +a_tate, (35)*3 +a_yoko, (46)*3 +a_tate, (44)*3 +a_yoko, (41)*3 +a_tate ) #体
        cv.create_line     ( (34)*3 +a_yoko, (31)*3 +a_tate, (44)*3 +a_yoko, (27)*3 +a_tate, fill='black', width = 5 ) #右腕上
        cv.create_line     ( (44)*3 +a_yoko, (27)*3 +a_tate, (52)*3 +a_yoko, (22)*3 +a_tate, fill='black', width = 5 ) #右腕下
        cv.create_oval     ( (53-3)*3 +a_yoko, (22-3)*3 +a_tate, (53+3)*3 +a_yoko, (22+3)*3 +a_tate, fill='black') #右拳
        cv.create_line     ( (32)*3 +a_yoko, (32)*3 +a_tate, (26)*3 +a_yoko, (35)*3 +a_tate, fill='black', width = 5 ) #左腕上
        cv.create_line     ( (26)*3 +a_yoko, (35)*3 +a_tate, (29)*3 +a_yoko, (39)*3 +a_tate, fill='black', width = 5 ) #左腕下
        cv.create_oval     ( (30-3)*3 +a_yoko, (40-3)*3 +a_tate, (30+3)*3 +a_yoko, (40+3)*3 +a_tate, fill='black') #左拳
        cv.create_line     ( (38)*3 +a_yoko, (41)*3 +a_tate, (45)*3 +a_yoko, (53)*3 +a_tate, fill='black', width = 5 ) #右脚上
        cv.create_line     ( (45)*3 +a_yoko, (53)*3 +a_tate, (50)*3 +a_yoko, (62)*3 +a_tate, fill='black', width = 5 ) #右脚下
        cv.create_oval     ( (51-3)*3 +a_yoko, (64-3)*3 +a_tate, (51+3)*3 +a_yoko, (64+3)*3 +a_tate, fill='black') #右甲
        cv.create_line     ( (44)*3 +a_yoko, (41)*3 +a_tate, (25)*3 +a_yoko, (51)*3 +a_tate, fill='black', width = 5 ) #左脚上
        cv.create_line     ( (25)*3 +a_yoko, (51)*3 +a_tate, (31)*3 +a_yoko, (61)*3 +a_tate, fill='black', width = 5 ) #左脚下
        cv.create_oval     ( (31-3)*3 +a_yoko, (63-3)*3 +a_tate, (31+3)*3 +a_yoko, (63+3)*3 +a_tate, fill='black') #左甲
        cv.create_oval     ( (25-12)*3 +a_yoko, (20-12)*3 +a_tate, (25+12)*3 +a_yoko, (20+12)*3 +a_tate, fill='black') #頭
        cv.create_oval     ( (25-10)*3 +a_yoko, (20-10)*3 +a_tate, (25+10)*3 +a_yoko, (20+10)*3 +a_tate, fill='white') #頭  
        cv.create_text     ( (25   )*3 +a_yoko, (20   )*3 +a_tate, text="そ",     font=("Helvetica", 45,"bold" ) ) #そ

    if tekuteku == 57:
#        cv.create_oval     ( (15)*3 +a_yoko, (66)*3 +a_tate, (45)*3 +a_yoko, (70)*3 +a_tate, fill='black', width=0 ) #影
        cv.create_polygon  ( (28)*3 +a_yoko, (16)*3 +a_tate, (35)*3 +a_yoko, (43)*3 +a_tate, (44)*3 +a_yoko, (38)*3 +a_tate ) #体
        cv.create_line     ( (34)*3 +a_yoko, (28)*3 +a_tate, (44)*3 +a_yoko, (24)*3 +a_tate, fill='black', width = 5 ) #右腕上
        cv.create_line     ( (44)*3 +a_yoko, (24)*3 +a_tate, (52)*3 +a_yoko, (19)*3 +a_tate, fill='black', width = 5 ) #右腕下
        cv.create_oval     ( (53-3)*3 +a_yoko, (19-3)*3 +a_tate, (53+3)*3 +a_yoko, (19+3)*3 +a_tate, fill='black') #右拳
        cv.create_line     ( (32)*3 +a_yoko, (29)*3 +a_tate, (26)*3 +a_yoko, (32)*3 +a_tate, fill='black', width = 5 ) #左腕上
        cv.create_line     ( (26)*3 +a_yoko, (32)*3 +a_tate, (29)*3 +a_yoko, (36)*3 +a_tate, fill='black', width = 5 ) #左腕下
        cv.create_oval     ( (30-3)*3 +a_yoko, (37-3)*3 +a_tate, (30+3)*3 +a_yoko, (37+3)*3 +a_tate, fill='black') #左拳
        cv.create_line     ( (37)*3 +a_yoko, (39)*3 +a_tate, (23)*3 +a_yoko, (39)*3 +a_tate, fill='black', width = 5 ) #右脚上
        cv.create_line     ( (23)*3 +a_yoko, (39)*3 +a_tate, (28)*3 +a_yoko, (50)*3 +a_tate, fill='black', width = 5 ) #右脚下
        cv.create_oval     ( (27-3)*3 +a_yoko, (50-3)*3 +a_tate, (27+3)*3 +a_yoko, (50+3)*3 +a_tate, fill='black') #右甲
        cv.create_line     ( (41)*3 +a_yoko, (38)*3 +a_tate, (37)*3 +a_yoko, (50)*3 +a_tate, fill='black', width = 5 ) #左脚上
        cv.create_line     ( (37)*3 +a_yoko, (50)*3 +a_tate, (39)*3 +a_yoko, (62)*3 +a_tate, fill='black', width = 5 ) #左脚下
        cv.create_oval     ( (39-3)*3 +a_yoko, (64-3)*3 +a_tate, (39+3)*3 +a_yoko, (64+3)*3 +a_tate, fill='black') #左甲
        cv.create_oval     ( (25-12)*3 +a_yoko, (17-12)*3 +a_tate, (25+12)*3 +a_yoko, (17+12)*3 +a_tate, fill='black') #頭
        cv.create_oval     ( (25-10)*3 +a_yoko, (17-10)*3 +a_tate, (25+10)*3 +a_yoko, (17+10)*3 +a_tate, fill='white') #頭  
        cv.create_text     ( (25   )*3 +a_yoko, (17   )*3 +a_tate, text="そ",     font=("Helvetica", 45,"bold" ) ) #そ

    if tekuteku == 58:
#        cv.create_oval     ( (15)*3 +a_yoko, (66)*3 +a_tate, (45)*3 +a_yoko, (70)*3 +a_tate, fill='black', width=0 ) #影
        cv.create_polygon  ( (28)*3 +a_yoko, (17)*3 +a_tate, (35)*3 +a_yoko, (44)*3 +a_tate, (44)*3 +a_yoko, (39)*3 +a_tate ) #体
        cv.create_line     ( (34)*3 +a_yoko, (29)*3 +a_tate, (44)*3 +a_yoko, (25)*3 +a_tate, fill='black', width = 5 ) #右腕上
        cv.create_line     ( (44)*3 +a_yoko, (25)*3 +a_tate, (52)*3 +a_yoko, (20)*3 +a_tate, fill='black', width = 5 ) #右腕下
        cv.create_oval     ( (53-3)*3 +a_yoko, (20-3)*3 +a_tate, (53+3)*3 +a_yoko, (19+3)*3 +a_tate, fill='black') #右拳
        cv.create_line     ( (32)*3 +a_yoko, (30)*3 +a_tate, (26)*3 +a_yoko, (33)*3 +a_tate, fill='black', width = 5 ) #左腕上
        cv.create_line     ( (26)*3 +a_yoko, (33)*3 +a_tate, (29)*3 +a_yoko, (37)*3 +a_tate, fill='black', width = 5 ) #左腕下
        cv.create_oval     ( (30-3)*3 +a_yoko, (38-3)*3 +a_tate, (30+3)*3 +a_yoko, (38+3)*3 +a_tate, fill='black') #左拳
        cv.create_line     ( (38)*3 +a_yoko, (41)*3 +a_tate, (26)*3 +a_yoko, (50)*3 +a_tate, fill='black', width = 5 ) #右脚上
        cv.create_line     ( (26)*3 +a_yoko, (50)*3 +a_tate, (30)*3 +a_yoko, (60)*3 +a_tate, fill='black', width = 5 ) #右脚下
        cv.create_oval     ( (31-3)*3 +a_yoko, (62-3)*3 +a_tate, (31+3)*3 +a_yoko, (62+3)*3 +a_tate, fill='black') #右甲
        cv.create_line     ( (40)*3 +a_yoko, (40)*3 +a_tate, (47)*3 +a_yoko, (52)*3 +a_tate, fill='black', width = 5 ) #左脚上
        cv.create_line     ( (47)*3 +a_yoko, (52)*3 +a_tate, (53)*3 +a_yoko, (62)*3 +a_tate, fill='black', width = 5 ) #左脚下
        cv.create_oval     ( (54-3)*3 +a_yoko, (64-3)*3 +a_tate, (54+3)*3 +a_yoko, (64+3)*3 +a_tate, fill='black') #左甲
        cv.create_oval     ( (25-12)*3 +a_yoko, (18-12)*3 +a_tate, (25+12)*3 +a_yoko, (18+12)*3 +a_tate, fill='black') #頭
        cv.create_oval     ( (25-10)*3 +a_yoko, (18-10)*3 +a_tate, (25+10)*3 +a_yoko, (18+10)*3 +a_tate, fill='white') #頭  
        cv.create_text     ( (25   )*3 +a_yoko, (18   )*3 +a_tate, text="そ",     font=("Helvetica", 45,"bold" ) ) #そ
 
    if tekuteku == 59:
#        cv.create_oval     ( (15)*3 +a_yoko, (66)*3 +a_tate, (45)*3 +a_yoko, (70)*3 +a_tate, fill='black', width=0 ) #影
        cv.create_polygon  ( (28)*3 +a_yoko, (16)*3 +a_tate, (35)*3 +a_yoko, (43)*3 +a_tate, (44)*3 +a_yoko, (38)*3 +a_tate ) #体
        cv.create_line     ( (34)*3 +a_yoko, (28)*3 +a_tate, (44)*3 +a_yoko, (24)*3 +a_tate, fill='black', width = 5 ) #右腕上
        cv.create_line     ( (44)*3 +a_yoko, (24)*3 +a_tate, (52)*3 +a_yoko, (19)*3 +a_tate, fill='black', width = 5 ) #右腕下
        cv.create_oval     ( (53-3)*3 +a_yoko, (19-3)*3 +a_tate, (53+3)*3 +a_yoko, (19+3)*3 +a_tate, fill='black') #右拳
        cv.create_line     ( (32)*3 +a_yoko, (29)*3 +a_tate, (26)*3 +a_yoko, (32)*3 +a_tate, fill='black', width = 5 ) #左腕上
        cv.create_line     ( (26)*3 +a_yoko, (32)*3 +a_tate, (29)*3 +a_yoko, (36)*3 +a_tate, fill='black', width = 5 ) #左腕下
        cv.create_oval     ( (30-3)*3 +a_yoko, (37-3)*3 +a_tate, (30+3)*3 +a_yoko, (37+3)*3 +a_tate, fill='black') #左拳
        cv.create_line     ( (37)*3 +a_yoko, (38)*3 +a_tate, (37)*3 +a_yoko, (52)*3 +a_tate, fill='black', width = 5 ) #右脚上
        cv.create_line     ( (37)*3 +a_yoko, (52)*3 +a_tate, (40)*3 +a_yoko, (62)*3 +a_tate, fill='black', width = 5 ) #右脚下
        cv.create_oval     ( (34-3)*3 +a_yoko, (50-3)*3 +a_tate, (34+3)*3 +a_yoko, (50+3)*3 +a_tate, fill='black') #右甲
        cv.create_line     ( (41)*3 +a_yoko, (38)*3 +a_tate, (28)*3 +a_yoko, (40)*3 +a_tate, fill='black', width = 5 ) #左脚上
        cv.create_line     ( (28)*3 +a_yoko, (40)*3 +a_tate, (33)*3 +a_yoko, (49)*3 +a_tate, fill='black', width = 5 ) #左脚下
        cv.create_oval     ( (40-3)*3 +a_yoko, (64-3)*3 +a_tate, (40+3)*3 +a_yoko, (64+3)*3 +a_tate, fill='black') #左甲
        cv.create_oval     ( (25-12)*3 +a_yoko, (17-12)*3 +a_tate, (25+12)*3 +a_yoko, (17+12)*3 +a_tate, fill='black') #頭
        cv.create_oval     ( (25-10)*3 +a_yoko, (17-10)*3 +a_tate, (25+10)*3 +a_yoko, (17+10)*3 +a_tate, fill='white') #頭  
        cv.create_text     ( (25   )*3 +a_yoko, (17   )*3 +a_tate, text="そ",     font=("Helvetica", 45,"bold" ) ) #そ

    if tekuteku == 60:
#        cv.create_oval     ( (15)*3 +a_yoko, (66)*3 +a_tate, (45)*3 +a_yoko, (70)*3 +a_tate, fill='black', width=0 ) #影
        cv.create_polygon  ( (28)*3 +a_yoko, (19)*3 +a_tate, (35)*3 +a_yoko, (46)*3 +a_tate, (44)*3 +a_yoko, (41)*3 +a_tate ) #体
        cv.create_line     ( (34)*3 +a_yoko, (31)*3 +a_tate, (44)*3 +a_yoko, (27)*3 +a_tate, fill='black', width = 5 ) #右腕上
        cv.create_line     ( (44)*3 +a_yoko, (27)*3 +a_tate, (52)*3 +a_yoko, (22)*3 +a_tate, fill='black', width = 5 ) #右腕下
        cv.create_oval     ( (53-3)*3 +a_yoko, (22-3)*3 +a_tate, (53+3)*3 +a_yoko, (22+3)*3 +a_tate, fill='black') #右拳
        cv.create_line     ( (32)*3 +a_yoko, (32)*3 +a_tate, (26)*3 +a_yoko, (35)*3 +a_tate, fill='black', width = 5 ) #左腕上
        cv.create_line     ( (26)*3 +a_yoko, (35)*3 +a_tate, (29)*3 +a_yoko, (39)*3 +a_tate, fill='black', width = 5 ) #左腕下
        cv.create_oval     ( (30-3)*3 +a_yoko, (40-3)*3 +a_tate, (30+3)*3 +a_yoko, (40+3)*3 +a_tate, fill='black') #左拳
        cv.create_line     ( (38)*3 +a_yoko, (41)*3 +a_tate, (45)*3 +a_yoko, (53)*3 +a_tate, fill='black', width = 5 ) #右脚上
        cv.create_line     ( (45)*3 +a_yoko, (53)*3 +a_tate, (50)*3 +a_yoko, (62)*3 +a_tate, fill='black', width = 5 ) #右脚下
        cv.create_oval     ( (51-3)*3 +a_yoko, (64-3)*3 +a_tate, (51+3)*3 +a_yoko, (64+3)*3 +a_tate, fill='black') #右甲
        cv.create_line     ( (44)*3 +a_yoko, (41)*3 +a_tate, (25)*3 +a_yoko, (51)*3 +a_tate, fill='black', width = 5 ) #左脚上
        cv.create_line     ( (25)*3 +a_yoko, (51)*3 +a_tate, (31)*3 +a_yoko, (61)*3 +a_tate, fill='black', width = 5 ) #左脚下
        cv.create_oval     ( (31-3)*3 +a_yoko, (63-3)*3 +a_tate, (31+3)*3 +a_yoko, (63+3)*3 +a_tate, fill='black') #左甲
        cv.create_oval     ( (25-12)*3 +a_yoko, (20-12)*3 +a_tate, (25+12)*3 +a_yoko, (20+12)*3 +a_tate, fill='black') #頭
        cv.create_oval     ( (25-10)*3 +a_yoko, (20-10)*3 +a_tate, (25+10)*3 +a_yoko, (20+10)*3 +a_tate, fill='white') #頭  
        cv.create_text     ( (25   )*3 +a_yoko, (20   )*3 +a_tate, text="そ",     font=("Helvetica", 45,"bold" ) ) #そ


    if tekuteku == 61:
#        cv.create_oval     ( (15)*3 +a_yoko, (66)*3 +a_tate, (45)*3 +a_yoko, (70)*3 +a_tate, fill='black', width=0 ) #影
        cv.create_polygon  ( (25)*3 +a_yoko, (16)*3 +a_tate, (23)*3 +a_yoko, (44)*3 +a_tate, (33)*3 +a_yoko, (43)*3 +a_tate ) #体
        cv.create_line     ( (25)*3 +a_yoko, (31)*3 +a_tate, (15)*3 +a_yoko, (29)*3 +a_tate, fill='black', width = 5 ) #右腕上
        cv.create_line     ( (15)*3 +a_yoko, (29)*3 +a_tate, ( 8)*3 +a_yoko, (25)*3 +a_tate, fill='black', width = 5 ) #右腕下
        cv.create_oval     ( ( 7-3)*3 +a_yoko, (24-3)*3 +a_tate, ( 7+3)*3 +a_yoko, (24+3)*3 +a_tate, fill='black') #右拳
        cv.create_line     ( (28)*3 +a_yoko, (31)*3 +a_tate, (36)*3 +a_yoko, (27)*3 +a_tate, fill='black', width = 5 ) #左腕上
        cv.create_line     ( (36)*3 +a_yoko, (27)*3 +a_tate, (43)*3 +a_yoko, (21)*3 +a_tate, fill='black', width = 5 ) #左腕下
        cv.create_oval     ( (44-3)*3 +a_yoko, (20-3)*3 +a_tate, (44+3)*3 +a_yoko, (20+3)*3 +a_tate, fill='black') #左拳
        cv.create_line     ( (29)*3 +a_yoko, (40)*3 +a_tate, (31)*3 +a_yoko, (53)*3 +a_tate, fill='black', width = 5 ) #右脚上
        cv.create_line     ( (31)*3 +a_yoko, (53)*3 +a_tate, (37)*3 +a_yoko, (62)*3 +a_tate, fill='black', width = 5 ) #右脚下
        cv.create_oval     ( (37-3)*3 +a_yoko, (63-3)*3 +a_tate, (37+3)*3 +a_yoko, (63+3)*3 +a_tate, fill='black') #右甲
        cv.create_line     ( (26)*3 +a_yoko, (41)*3 +a_tate, (14)*3 +a_yoko, (47)*3 +a_tate, fill='black', width = 5 ) #左脚上
        cv.create_line     ( (14)*3 +a_yoko, (47)*3 +a_tate, (11)*3 +a_yoko, (55)*3 +a_tate, fill='black', width = 5 ) #左脚下
        cv.create_oval     ( (22-3)*3 +a_yoko, (55-3)*3 +a_tate, (22+3)*3 +a_yoko, (55+3)*3 +a_tate, fill='black') #左甲
        cv.create_oval     ( (25-12)*3 +a_yoko, (16-12)*3 +a_tate, (25+12)*3 +a_yoko, (16+12)*3 +a_tate, fill='black') #頭
        cv.create_oval     ( (25-10)*3 +a_yoko, (16-10)*3 +a_tate, (25+10)*3 +a_yoko, (16+10)*3 +a_tate, fill='white') #頭  
        cv.create_text     ( (25   )*3 +a_yoko, (16   )*3 +a_tate, text="そ",     font=("Helvetica", 45,"bold" ) ) #そ

    if tekuteku == 71:
#        cv.create_oval     ( (15)*3 +a_yoko, (66)*3 +a_tate, (45)*3 +a_yoko, (70)*3 +a_tate, fill='black', width=0 ) #影
        cv.create_polygon  ( (25)*3 +a_yoko, (18)*3 +a_tate, (26)*3 +a_yoko, (44)*3 +a_tate, (35)*3 +a_yoko, (42)*3 +a_tate ) #体
        cv.create_line     ( (27)*3 +a_yoko, (28)*3 +a_tate, (28)*3 +a_yoko, (36)*3 +a_tate, fill='black', width = 5 ) #右腕上
        cv.create_line     ( (28)*3 +a_yoko, (36)*3 +a_tate, (24)*3 +a_yoko, (41)*3 +a_tate, fill='black', width = 5 ) #右腕下
        cv.create_oval     ( (14-3)*3 +a_yoko, (42-3)*3 +a_tate, (14+3)*3 +a_yoko, (42+3)*3 +a_tate, fill='black') #右拳
        cv.create_line     ( (29)*3 +a_yoko, (28)*3 +a_tate, (29)*3 +a_yoko, (36)*3 +a_tate, fill='black', width = 5 ) #左腕上
        cv.create_line     ( (29)*3 +a_yoko, (36)*3 +a_tate, (29)*3 +a_yoko, (40)*3 +a_tate, fill='black', width = 5 ) #左腕下
        cv.create_oval     ( (29-3)*3 +a_yoko, (40-3)*3 +a_tate, (29+3)*3 +a_yoko, (40+3)*3 +a_tate, fill='black') #左拳
        cv.create_line     ( (29)*3 +a_yoko, (40)*3 +a_tate, (27)*3 +a_yoko, (50)*3 +a_tate, fill='black', width = 5 ) #右脚上
        cv.create_line     ( (27)*3 +a_yoko, (50)*3 +a_tate, (27)*3 +a_yoko, (61)*3 +a_tate, fill='black', width = 5 ) #右脚下
        cv.create_oval     ( (32-3)*3 +a_yoko, (60-3)*3 +a_tate, (32+3)*3 +a_yoko, (60+3)*3 +a_tate, fill='black') #右甲
        cv.create_line     ( (33)*3 +a_yoko, (40)*3 +a_tate, (32)*3 +a_yoko, (50)*3 +a_tate, fill='black', width = 5 ) #左脚上
        cv.create_line     ( (32)*3 +a_yoko, (50)*3 +a_tate, (32)*3 +a_yoko, (59)*3 +a_tate, fill='black', width = 5 ) #左脚下
        cv.create_oval     ( (28-3)*3 +a_yoko, (61-3)*3 +a_tate, (28+3)*3 +a_yoko, (61+3)*3 +a_tate, fill='black') #左甲
        cv.create_oval     ( (21-12)*3 +a_yoko, (17-12)*3 +a_tate, (21+12)*3 +a_yoko, (27+12)*3 +a_tate, fill='black') #頭
        cv.create_oval     ( (21-10)*3 +a_yoko, (17-10)*3 +a_tate, (21+10)*3 +a_yoko, (27+10)*3 +a_tate, fill='white') #頭  
        cv.create_text     ( (21   )*3 +a_yoko, (17   )*3 +a_tate, text="そ",     font=("Helvetica", 45,"bold" ) ) #そ



#変数
tekuteku = 1
a_tate = 100
a_yoko = 610
a_iti = 1
mode = 1
move = -30
line = 3
hiscore = 0
score = 0
life =3
runspeed = 50
scene = 1
op_count = 1

#リスタート
def re_start():
    global tekuteku
    global a_tate
    global a_yoko
    global a_iti
    global mode
    global move
    global line
    global score
    global life
    global runspeed
    global scene
    global op_count
    global Zmap
    tekuteku = 1
    a_tate = 100
    a_yoko = 610
    a_iti = 1
    mode = 1
    move = -30
    line = 3
    score = 0
    life =3
    runspeed = 1000
    scene = 2
    Zmap = [ 0, 2, 0, 0, 0,   0, 0, 2, 0, 0,    0, 0, 0, 3, 0,   0, 0, 2, 0, 0,    0, 2, 0, 0, 0, ]

#モード（人の動き）を変更する。
def mode_change():
    global tekuteku
    tekuteku = tekuteku + 1
    global mode
    global life
    if tekuteku == 7:
        mode = 1
        tekuteku = 1
    if tekuteku == 17:
        mode = 1
        tekuteku = 1
    if tekuteku == 27:
        mode = 4
        tekuteku = 31
        life = life -1
    if tekuteku == 36:
        mode = 1
        tekuteku = 1

#キー操作
def input_key1(event):
    global tekuteku
    global mode
    global life
    if mode == 1:
        mode = 2
        tekuteku = 11

def input_key2(event):
    global line
    if line >= 2:
        line = line -1

def input_key3(event):
    global line
    if line <= 4:
        line = line +1

def input_key4(event): #リセットボタン
    re_start()

win.bind('<Key-1>',input_key1)
win.bind('<Key-2>',input_key2)
win.bind('<Key-3>',input_key3)
win.bind('<Key-4>',input_key4)

#走るモーションの関数
def hasiru():
    global a_yoko
    global a_tate
    global mode
    global move
    global line
    global Zmap
    if mode ==4:
        move = 0
    elif mode ==1:
        move = -30
    elif mode ==2:
        move = -30
    elif mode ==3:
        move = -30        

#画面端での繰り返し
    a_yoko = a_yoko +move
    if (a_yoko <= -300)and(a_yoko >= -400):
        a_yoko = 700
        Zmap = copy.deepcopy(Amap[(random.randint(0,29))])
        
    if line == 1:
        a_tate = 0
    elif line == 2:
        a_tate = 50
    elif line == 3:
        a_tate = 100
    elif line == 4:
        a_tate = 150
    elif line == 5:
        a_tate = 200

#難易度操作
def nanido():
    global score
    global runspeed
    if (    0 <= score )and(  200 >= score ):
        runspeed = 130
    elif (  201 <= score )and(  400 >= score ):
        runspeed = 110
    elif (  401 <= score )and(  600 >= score ):
        runspeed =  90
    elif (  601 <= score )and(  800 >= score ):
        runspeed =  80
    elif (  801 <= score )and( 1000 >= score ):
        runspeed =  70
    elif ( 1001 <= score )and( 1200 >= score ):
        runspeed =  60
    elif ( 1201 <= score ):
        runspeed =  50

#オープニング
def OP():
    global runspeed
    global tekuteku
    global a_yoko
    global a_tate
    global hiscore
    runspeed = 200
    tekuteku = tekuteku + 1
    a_tate = 250
    a_yoko = 250
    if (tekuteku <=40):
        tekuteku = 41
    elif(tekuteku ==61):
        tekuteku = 41
    runman()
    cv.create_text     ( 110, 120, text="流", font=("Helvetica", 60,"bold" ) )
    cv.create_text     ( 210, 150, text="し", font=("Helvetica", 60,"bold" ) )
    cv.create_text     ( 310, 120, text="そ", font=("Helvetica", 60,"bold" ) )
    cv.create_text     ( 410, 150, text="う", font=("Helvetica", 60,"bold" ) )
    cv.create_text     ( 510, 120, text="め", font=("Helvetica", 60,"bold" ) )
    cv.create_text     ( 610, 150, text="ん", font=("Helvetica", 60,"bold" ) )
    cv.create_text     ( 350, 220, text="PRESS START", font=("Helvetica", 30,"bold" ) )
    cv.create_text     ( 550,  25, text="HI SCORE", font=("Helvetica", 20, "bold") )
    cv.create_text     ( 670,  25, text=hiscore  , font=("Helvetica", 25, "bold") )

#終了後のカウンター
def OP_COUNT():
    global life
    global op_count
    global scene
    global score
    global hiscore
    if life == 0:
        op_count = op_count +1
    if op_count == 50:
        scene = 1
        op_count = 1
    if hiscore <= score:
        hiscore = score

#ゲームの繰り返し処理
def game_loop():
    global scene
    if scene ==1:
        draw_screen()
        OP()
    if scene ==2:
        draw_screen()
        haikei()
        life_draw()
        map()
        if life>=1:
            runman()
            hasiru()    
        mode_change()
        nanido()
        OP_COUNT()
    touch()
    win.after(runspeed, game_loop) #runspeedがディレイ。ここを操作する事でゲームの難易度操作
           
#ドット絵描画関数の実行
game_loop()
#ウィンドウの表示
win.mainloop()
