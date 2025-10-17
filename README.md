# view-mob

## Debian dependencies
```
apt install git build-essential pkg-config python3-dev libgirepository-2.0-dev libcairo2-dev gir1.2-gtk-3.0 libcanberra-gtk3-module python3-venv libgirepository1.0-dev
```

## Start environment
```
python3 -m venv venv
source venv/bin/activate
pip install flask
pip install toga
pip install briefcase
```

## Running APP on browser
```
flask --app app run
```

## Running APP on Android
```
briefcase run android -r
```
