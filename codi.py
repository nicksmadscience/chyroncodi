import serial, time
# ser = serial.Serial('/dev/tty.usbserial-1120')  # open serial port
# print(ser.name)         # check which port was really used


# # for i in range(-255, 255):
# #     rofl = "\\\\VH\\\\{n}\\\\\\\\".format(n=i).encode()
# #     ser.write(rofl)
# #     print (rofl)
# #     time.sleep(0.05)
# ser.write(b'\\VB\\\\')     # write a string
# ser.write(b'\\DB\\2\\R\\1\\200\\0\\0\\0\\50\\0\\0\\200\\0\\\\')
# ser.close()             # close port


ser = serial.Serial('/dev/tty.usbserial-110', baudrate=38400, bytesize=8, parity='N', stopbits=1, timeout=None, xonxoff=0, rtscts=0)  # open serial port
print(ser.name)         # check which port was really used


def bg(serial, start, r1, g1, b1, k1, end, r2, g2, b2, k2):
    bg_out = '\\DB\\2\\R\\{start}\\{r1}\\{g1}\\{b1}\\{k1}\\{end}\\{r2}\\{g2}\\{b2}\\{k2}\\\\'.format(start=start, r1=r1, g1=g1, b1=b1, k1=k1, end=end, r2=r2, g2=g2, b2=b2, k2=k2)
    serial.write(bg_out.encode("utf-8"))
    
    
def tab(serial, name, x, y, color, font, justification):
    tab_out = '\\DT\\{name}\\{x}\\{y}\\{color}\\{font}\\{justification}\\\\'.format(name=name, x=x, y=y, color=color, font=font, justification=justification)
    serial.write(tab_out.encode("utf-8"))
    
def tabtext(serial, name, x, y, color, font, justification, text):
    tab_out = '\\DT\\{name}\\{x}\\{y}\\{color}\\{font}\\{justification}\\\\\\TU\\{name}\{text}\\\\'.format(name=name, x=x, y=y, color=color, font=font, justification=justification, text=text)
    serial.write(tab_out.encode("utf-8"))
    
def pageblank(serial):
    serial.write(b'\\PB\\\\')
    
def videoblank(serial):
    ser.write(b'\\VB\\\\')


# Video Blank (turn on background).

# background
bg(serial=ser, start=1, r1=24, g1=0, b1=48, k1=0, end=256, r2=96, g2=0, b2=192, k2=0)

# header
bg(serial=ser, start=1, r1=200, g1=100, b1=0, k1=0, end=42, r2=0, g2=0, b2=200, k2=0)

# highlight backgrounds
bg(serial=ser, start=48, r1=36, g1=60, b1=86, k1=0, end=96, r2=90, g2=0, b2=162, k2=0)
bg(serial=ser, start=197, r1=36, g1=120, b1=48, k1=0, end=224, r2=112, g2=180, b2=192, k2=0)


time.sleep(0.5)

# bg(1, 256, 128, 0, 0, 42, 0, 128, 256, 0)\
# Download shaded background (from red to blue); scan- line 1 is red, scanline 50 is blue.


tabtext(serial=ser, name="title", x=20, y=20, color=3, font=5, justification='L', text='Cool aircraft nearby!')
tabtext(serial=ser, name="icao-l", x=20, y=115, color=2, font=1, justification='L', text='ICAO')
tabtext(serial=ser, name="icao", x=75, y=100, color=2, font=3, justification='L', text='AS65')
tabtext(serial=ser, name="reg-l", x=20, y=165, color=2, font=1, justification='L', text='REG.')
tabtext(serial=ser, name="reg", x=75, y=150, color=2, font=3, justification='L', text='N600LL')
time.sleep(0.25)

tabtext(serial=ser, name="lat-l", x=20, y=235, color=2, font=1, justification='L', text='LAT')
tabtext(serial=ser, name="lat", x=75, y=220, color=2, font=3, justification='L', text='37.15')
tabtext(serial=ser, name="lon-l", x=200, y=235, color=2, font=1, justification='L', text='LON')
tabtext(serial=ser, name="lon", x=255, y=220, color=2, font=3, justification='L', text='-75.19')
time.sleep(0.25)



tabtext(serial=ser, name="head-l", x=20, y=285, color=2, font=1, justification='L', text='HEAD')
tabtext(serial=ser, name="head", x=84, y=270, color=2, font=3, justification='L', text='1.3\xae')
tabtext(serial=ser, name="alt-l", x=200, y=285, color=2, font=1, justification='L', text='ALT')
tabtext(serial=ser, name="alt", x=250, y=270, color=2, font=3, justification='L', text='1500ft')



time.sleep(0.25)

tabtext(serial=ser, name="ang-l", x=20, y=415, color=2, font=1, justification='L', text='ANG.')
tabtext(serial=ser, name="ang", x=84, y=400, color=2, font=3, justification='L', text='15.2\xae')
tabtext(serial=ser, name="eta-l", x=200, y=415, color=2, font=1, justification='L', text='ETA')
tabtext(serial=ser, name="eta", x=250, y=400, color=2, font=3, justification='L', text='4m5s')



time.sleep(0.25)

# \ES\xaddr\yaddr\color\font\format\mode[\pad\type]\\
ser.write(b'\\ES\\470\\400\\3\\3\\MM:SS.TH\\1\\\\')
ser.write(b'\\ET\\000405\\\\')
ser.write(b'\\ED\\1\\\\')
ser.write(b'\\EB\\1\\\\')



# time.sleep(3)
# ser.write(b'\\MJ\\2\\20\\20\\\\')

# ser.write(b'\\DT\\1\\160\\10\\2\\6\\L\\\\')
# # Download tab 1 to X position 160, y position 10, color 2, font 6, left-justified.
# ser.write(b'\\DT\\2\\50\\100\\5\\4\\L\\3\\400\\100\\5\\4\\L\\\\')
# # Download tab 2 to X position 50, y position 100, color 5, font 4, left-justified.
# # Download tab 3 to X position 400, y position 100, color 5, font 4, left justified.
# # These two tabs were set up in the same command. They could have been typed separately.
# ser.write(b'\\DT\\4\\110\\150\\1\\3\\L\\5\\420\\150\\5\\3\\L\\\\')
# # Download tab 4 to X position 110, y position 150, color 1, font 3, left-justified.
# # Download tab 5 to X position 420, y position 150, color 5, font 4, left justified.
# # These two tabs were set up in the same command. They could have been typed separately.
# #  Sample Screen Set-Up 3-4 Revision E
# # [ ] 6. Define the remaining tabs as follows:
# ser.write(b'\\DT\\6\\110\\200\\1\\3\\L\\8\\110\\250\\1\\3\\L\\10\\110\\300\\1\\3\\L\\12\\110\\350\\1\\3\\L\\\\')
# ser.write(b'\\DT\\7\\420\\200\\1\\3\\L\\9\\420\\250\\1\\3\\L\\11\\420\\300\\1\\3\\L\\13\\420\\350\\1\\3\\L\\\\')

# ser.write(b'\\TU\\1\\ChyronTV\\2\\Channel\\3\\Listing\\\\')
# ser.write(b'\\TU\\4\\2\\5\\CBS\\6\\3\\7\\ESPN\\8\\4\\9\\NBC\\10\\5\\11\\FOX\\12\\6\\13\\HBO\\\\')




# ser.write(b'\\WS\\450\\400\\4\\3\\HH:MM:SS\\1\\\\')
# Watch set-up, X coordinate 450, Y coordinate 400, color 4, font 3, with a
# 12-hour clock display., no A.M. or P.M., and no seconds displayed.
# ser.write(b'\\WD\\\\')# Watch display.

# These commands send the tab data to the tab fields.

# ser.write(b'\\MS\\1\\\\')
# Message save as message 1.
# [ ] 12. To create the next screen, repeat the command lines in step 10, but change the tab data to "7," "ABC," and so on (refer to Figure 3-2 ).
# CODI Handbook
  

# ser.write(b'\\TU\\4\\7\\5\\ABC\\6\\8\\7\\CINEMAX\\8\\9\\9\\WOR\\10\\10\\11\\USA\\12\\11\\13\\WPIX\\\\')
# ser.write(b'\\MS\\2\\\\')
# Message save as message 2.
# Effects:

# while True:
#     try:
#         # Random Matrix Wipe, message 1:
#         ser.write(b'\\ME\\MW\\1\\0\\5\\5\\10\\\\')

#         time.sleep(7)
#         # Message effect, matrix wipe, message 1, effect 0 (random matrix wipe), 5 X 5 pixel
#         # block, at speed 10.
#         # Push message 2 onto the screen: 
#         # ser.write(b'\\ME\\PU\\2\\L\\8\\\\')
#         # time.sleep(7)
#         # Push message 2, from the left, at speed 4.
#     except KeyboardInterrupt:
#         break




# print (ser.read(10))
ser.close()             # close port
