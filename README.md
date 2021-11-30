# Browser Tracking Demos: v0.1 beta

A simple App to show user browsing tracking methods used in internet.

Made with ![Love](https://cloud.githubusercontent.com/assets/4301109/16754758/82e3a63c-4813-11e6-9430-6015d98aeaab.png) in Spain

[![python](https://img.shields.io/badge/python-3.8-blue.svg?logo=python&labelColor=yellow)](https://www.python.org/downloads/)
[![platform](https://img.shields.io/badge/platform-osx%2Flinux%2Fwindows-green.svg)](https://github.com/EU-EDPS/website-evidence-collector)


## Install from sources

1. Install dependencies:

```
sudo apt-get update
sudo apt-get upgrade
sudo apt-get install python3 python3-pip python3-venv
```

2. Install  from Github:

```    
git clone https://github.com/mercaderd/privacydemos.git
cd privacydemos
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py createcachetable
python manage.py collecstatic
chmod +x run.sh
```

3. Launch web server:
``` 
./run.sh
``` 

4.- Browse to http://127.0.0.1:8000 and enjoy it!
