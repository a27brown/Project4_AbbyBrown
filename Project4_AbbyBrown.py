#Abby Brown Project 4
#["Massachusetts", "Connecticut", "Rhode Island","North Dakota", "Iowa"] The states I will be doing.
#if the state is affordable for housing draw its rectangle in a shade of blue
#if the state is marginally affordable, draw it in yellow
#if the state is not affordable, draw it in red.
#the rectangle should be labeled
#the height of the rectangle should be scaled to thousands of dollars of house price
#(so Hawaii's $760,000 median house price should be 760 pixels high.
#2Massachusetts;25000;62_270;113_900;580_000 = 580 pixels high
#6;Connecticut;09000;58_400;99_240;380_000 = 380 pixels high
#10;Rhode Island;44000;54_040;92_290;450_000 = 450 pixels high
#29;Iowa;19000;47_670;85_480;230_000 = 230 pixels high
#18;North Dakota;38000;50_320;88_080;277_000 = 230 pixels high
import dearpygui.dearpygui as gui
import comp151Colors

gui.create_context()
gui.create_viewport(title="Comp151 Window",width=800,height=800)
with gui.window(label="Affordable Housing",width=800,height=800):
    with gui.drawlist(width=800,height=800):
        #Origin plan
        gui.draw_rectangle((0,0),(775,775),color = comp151Colors.WHITE,fill = comp151Colors.WHITE)
        gui.draw_arrow((700,700),(50,700),color = comp151Colors.BLACK)
        gui.draw_arrow((50,100),(50,700),color = comp151Colors.BLACK)
        #Connecticut: 380 pixels high
        gui.draw_rectangle((75,320),(150,700),fill = comp151Colors.YELLOW)
        #Iowa: 230 pixels high
        gui.draw_rectangle((200,470),(275,700),fill = comp151Colors.GREEN)
        #Massachusetts: 580 pixels high
        gui.draw_rectangle((325,120),(400,700),fill = comp151Colors.RED)
        #North Dakota: 230 pixels high
        gui.draw_rectangle((450,470),(525,700),fill = comp151Colors.GREEN)
        #Rhode Island: 450 pixels high
        gui.draw_rectangle((575,250),(650,700),fill = comp151Colors.YELLOW)
        gui.draw_text((75,700),"Connectitcut",color = comp151Colors.BLACK,size=17)
        gui.draw_text((215,700),"Iowa",color = comp151Colors.BLACK,size=17)
        gui.draw_text((300,700),"Massachusetts",color = comp151Colors.BLACK,size=17)
        gui.draw_text((450,700),"North Dakota",color = comp151Colors.BLACK,size=17)
        gui.draw_text((575, 700), "Rhode Island", color=comp151Colors.BLACK,size=17)
        gui.draw_text((300,750),"State Name",color = comp151Colors.BLACK,size=25)






gui.setup_dearpygui()
gui.show_viewport()
gui.start_dearpygui()
gui.destroy_context()