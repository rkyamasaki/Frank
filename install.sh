mkdir tmp

sudo apt-get install make build-essential zlib1g-dev libbz2-dev libreadline-dev
sudo apt-get update
sudo apt-get install sqlite3 libsqlite3-dev
sudo apt-get install libssl-dev

cd tmp
wget http://python.org/ftp/python/2.7.5/Python-2.7.5.tgz
tar -xvf Python-2.7.5.tgz
cd Python-2.7.5
./configure
make
sudo checkinstall

cd ..
rm -r tmp/
