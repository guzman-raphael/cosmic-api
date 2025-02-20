# docker run --rm -v /home/raphael/Documents/github/cosmic-api/test:/tmp/test --workdir /tmp/test python:slim bash run.sh
set -e

apt update
apt install curl wget -y
wget -q https://packages.mozilla.org/apt/repo-signing-key.gpg -O- | tee /etc/apt/keyrings/packages.mozilla.org.asc > /dev/null
echo "deb [signed-by=/etc/apt/keyrings/packages.mozilla.org.asc] https://packages.mozilla.org/apt mozilla main" | tee -a /etc/apt/sources.list.d/mozilla.list > /dev/null
echo '
Package: *
Pin: origin packages.mozilla.org
Pin-Priority: 1000
' | tee /etc/apt/preferences.d/mozilla
apt-get update && apt-get install firefox -y

# curl -LO https://github.com/mozilla/geckodriver/releases/download/v0.35.0/geckodriver-v0.35.0-linux64.tar.gz --output-dir /tmp
# tar -xvzf ../geckodriver-v0.35.0-linux64.tar.gz -C /usr/local/bin
# chown root:root /usr/local/bin/geckodriver
# rm ../geckodriver-v0.35.0-linux64.tar.gz

pip install selenium
python verify.py
