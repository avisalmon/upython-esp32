import machine, display, time, math, network, utime


tft = display.TFT()
tft.init(tft.ST7789,bgr=False,rot=tft.LANDSCAPE, miso=17,backl_pin=4,backl_on=1, mosi=19, clk=18, cs=5, dc=16)

tft.setwin(40,52,320,240)

for i in range(0,241):
    color=0xFFFFFF-tft.hsb2rgb(i/241*360, 1, 1)
  
   # color=tft.hsb2rgb(i/241*360, 1, 1)
    tft.line(i,0,i,135,color)

tft.set_bg(0xFFFFFF)
tft.set_fg(0x000000)

tft.ellipse(120,67,120,67)

tft.line(0,0,240,135)

text="ST7789 with micropython!"

tft.text(120-int(tft.textWidth(text)/2),67-int(tft.fontSize()[1]/2),text,0x000000)



#wifi=network.WLAN(network.STA_IF) wifi.active(True) wifi.connect("yourWlan","yourPassword") utime.sleep_ms(3000) network.telnet.start(user="m",password="m")