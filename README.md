# pythonLedOpen
=========20190527============================
使用openRaspberryPi.py 作為開啟檔 來呼叫 LedTest.py & GetAddressIP.py
GetAddressIP.py 可以獲取local ip 並使用espeak 唸出來


=========20190523============================
使用 espeak 執行 文字轉語音 tts 
安裝 sudo apt-get install espeak
測試
espeak -ven+f3 -k5 -s150 "I've just picked up a fault in the AE35 unit"
執行方式為 
import os
os.system("espeak 'The quick brown fox'")

ref.
1.https://www.ncnynl.com/archives/201609/867.html
2.https://pythonspot.com/speech-engines-with-python-tutorial/


raspberry pi 開機執行 py ：
cd /home/pi                  //cd  到pi目錄
sudo nano test.py        //隨便打個print測試
sudo nano .bashrc      //編輯.bashrc
python test.py              //在.bashrc最後一行新增

or

set rc.local that when system open can run this.py file
#sudo nano /ext/rc.local
#write python /home/pi/LedOpen.py before exit 0

sudo nano /etc/rc.local
在exit 0 之前 新增一行如下
python /home/pi/LedOpen.py 

