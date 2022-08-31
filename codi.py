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


# def bg(start, r1, g1, b1, k1, end, r2, g2, b2, k2):
#     return b'\\DB\\2\\R\\{start}\\{r1}\\{g1}\\{b1}\\{k1}\\{end}\\{r2}\\{g2}\\{b2}\\{k2}\\\\'.format(start=start, r1=r1, g1=g1, b1=b1, end=end, r2=r2, g2=g2, b2=b2, k2=k2)


ser.write(b'\\VB\\\\')
# Video Blank (turn on background).
# ser.write(b'\\DB\\2\\R\\1\\64\\0\\128\\0\\200\\0\\192\\256\\0\\\\')


# background
ser.write(b'\\DB\\2\\R\\1\\24\\0\\48\\0\\256\\96\\0\\192\\0\\\\')

# header
ser.write(b'\\DB\\2\\R\\1\\200\\100\\0\\0\\42\\0\\0\\200\\0\\\\')

# highlight background
ser.write(b'\\DB\\2\\R\\48\\36\\60\\86\\0\\96\\90\\0\\162\\0\\\\')
ser.write(b'\\DB\\2\\R\\197\\36\\120\\48\\0\\224\\112\\180\\192\\0\\\\')

time.sleep(0.5)

# bg(1, 256, 128, 0, 0, 42, 0, 128, 256, 0)\
# Download shaded background (from red to blue); scan- line 1 is red, scanline 50 is blue.


ser.write(b'\\DT\\title\\20\\20\\3\\5\\L\\\\')
ser.write(b'\\DT\\icao-l\\20\\115\\2\\1\\L\\\\')
ser.write(b'\\DT\\icao\\75\\100\\2\\3\\L\\\\')
ser.write(b'\\DT\\reg-l\\20\\165\\2\\1\\L\\\\')
ser.write(b'\\DT\\reg\\75\\150\\2\\3\\L\\\\')
time.sleep(0.25)

ser.write(b'\\DT\\lat-l\\20\\235\\2\\1\\L\\\\')
ser.write(b'\\DT\\lat\\75\\220\\2\\3\\L\\\\')
ser.write(b'\\DT\\lon-l\\200\\235\\2\\1\\L\\\\')
ser.write(b'\\DT\\lon\\255\\220\\2\\3\\L\\\\')
ser.write(b'\\DT\\head-l\\20\\285\\2\\1\\L\\\\')
ser.write(b'\\DT\\head\\84\\270\\2\\3\\L\\\\')
ser.write(b'\\DT\\alt-l\\200\\285\\2\\1\\L\\\\')
ser.write(b'\\DT\\alt\\250\\270\\2\\3\\L\\\\')
time.sleep(0.25)

ser.write(b'\\DT\\ang-l\\20\\415\\2\\1\\L\\\\')
ser.write(b'\\DT\\ang\\82\\400\\2\\3\\L\\\\')
ser.write(b'\\DT\\eta-l\\200\\415\\2\\1\\L\\\\')
ser.write(b'\\DT\\eta\\250\\400\\2\\3\\L\\\\')

time.sleep(0.25)

ser.write(b'\\TU\\title\\Cool aircraft nearby!\\\\')
ser.write(b'\\TU\\icao-l\\ICAO\\\\')
ser.write(b'\\TU\\icao\\AS65\\\\')
ser.write(b'\\TU\\reg-l\\REG.\\\\')
ser.write(b'\\TU\\reg\\N600LL\\\\')
time.sleep(0.25)
ser.write(b'\\TU\\lat-l\\LAT\\\\')
ser.write(b'\\TU\\lat\\-37.15\\\\')
ser.write(b'\\TU\\lon-l\\LON\\\\')
ser.write(b'\\TU\\lon\\75.19\\\\')
ser.write(b'\\TU\\head-l\\HEAD\\\\')
ser.write(b'\\TU\\head\\1.3\xae\\\\')
ser.write(b'\\TU\\alt-l\\ALT\\\\')
ser.write(b'\\TU\\alt\\1500ft\\\\')
time.sleep(0.25)

ser.write(b'\\TU\\ang-l\\ANG.\\\\')
ser.write(b'\\TU\\ang\\15.2\xae\\\\')
ser.write(b'\\TU\\eta-l\\ETA\\\\')
ser.write(b'\\TU\\eta\\4m5s\\\\')
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
