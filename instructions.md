## HOW TO INSTALL
### BlackArch official repository
```
sudo pacman -S hidden-eye
```
to run just use
```
sudo hidden-eye
```
### CLONE
```
git clone https://gitlab.com/hackinter/HiddenEye.git
```

### RUNNING (In Linux)
```
chmod 777 HiddenEye
```

```
sudo apt install python3-pip
```

```
cd HiddenEye
```

```
sudo pip3 install -r requirements.txt
```

```
sudo pip3 install requests
```

```
python3 HiddenEye.py

```
   OR

```
./HiddenEye.py    

```
### RUNNING (Arch Linux or Manjaro)
```
chmod 777 HiddenEye
```

```
sudo pacman -Syu
```
```
sudo pacman -S python-pip
```

```
cd HiddenEye
```

```
sudo pip3 install -r requirements.txt
```

```
sudo python3 HiddenEye.py

```
   OR

```
sudo ./HiddenEye.py    

```
## FOR ANDROID USERS

### 1) INSTALLING IN (USERLAND APP)

```
Install userland app from playstore.

```

```
Set up app and install kali from app.Set ssh username(anyname) and password. 

```

```
When kali will run it'll ask for password type the ssh password.Then do su.After that kali will run on your device wothout root and do apt update For more info read here (https://null-byte.wonderhowto.com/how-to/android-for-hackers-turn-android-phone-into-hacking-device-without-root-0189649/)

```
```
sudo apt install python3 python3-pip unzip php git

```
```
git clone https://gitlab.com/hackinter/HiddenEye.git

```

```
chmod 777 HiddenEye
```

```
cd HiddenEye

```

```
pip3 install -r requirements.txt && pip3 install requests

```

```
python3 HiddenEye.py
```

### 2) INSTALLING IN (TERMUX APP)

```
First install { Termux } from Playstore.

```

```
After opening Follow below commands One by one

```

```
pkg install git python php curl openssh grep

```

```
git clone -b Termux-Support-Branch https://gitlab.com/hackinter/HiddenEye.git
```

```
chmod 777 HiddenEye
```

```
pip install requests
```

```
cd HiddenEye
```
```
python HiddenEye.py

or

./HiddenEye.py

```
### ONE LINE COMMAND TO INSTALL IN TERMUX(ANDROID). Just copy/paste this single command and hit Enter .. ALL DONE


```
First install { Termux } from Playstore.

```

```
After opening Copy and run this Single Command.

```
```
pkg install git python php curl openssh grep && git clone -b Termux-Support-Branch https://gitlab.com/hackintere/HiddenEye.git && chmod 777 HiddenEye && cd HiddenEye && pip install -r requirements.txt && pip install requests && python HiddenEye.py

```
