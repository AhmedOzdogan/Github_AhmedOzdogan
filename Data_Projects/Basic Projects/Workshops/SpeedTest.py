# -*- coding: utf-8 -*-
import speedtest

st = speedtest.Speedtest()

opt = int(input('''Please choosen an option :
                1 = Download
                2 = Upload
                3= All
                Your Choice = '''))

if opt == 1:
    print(int(st.download()/131072), 'mbps')
    
elif opt == 2:
    print(int(st.upload()/1310723), 'mbps')

elif opt == 3:
    print("Download : ", int(st.download()/131072), 'mbps')
    print("Upload : ", int(st.upload()/1310723), 'mbps')
    
else:
    print("Please enter correct number!")
