# Generic 

## dev packages
```bash
sudo apt update  
sudo apt-get install wget build-essential gcc g++ make byacc vim python3-dev python3-distutils python-setuptools
```

## pip packages
```bash
pip install --upgrade pip setuptools wheel python-dev-tools
```

<br>

# Jupyter

## Install conda python as jupyter kernel
```bash
conda activate cenv
conda install ipykernel
ipython kernel install --user --name={any_name_for_kernel}
```

## DELETE KERNEL
```bash
jupyter kernelspec uninstall {kernel}
```

<br>

# Selenium

## Install chrome

### Linux (apt) (Recommended)

```bash
sudo sh -c 'echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list'
sudo wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | sudo apt-key add -
sudo apt update
sudo apt install google-chrome-stable
google-chrome-stable --version
```

### Linux (deb file)

```bash
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
sudo dpkg -i google-chrome-stable_current_amd64.deb
sudo apt --fix-broken install
google-chrome-stable --version
```

### Centos

```bash
wget https://dl.google.com/linux/direct/google-chrome-stable_current_x86_64.rpm
yum localinstall google-chrome-stable_current_x86_64.rpm
```

### Possible fixes if installation fails

```bash
sudo apt-get install -y chromium-browser
sudo apt-get install libnss3
```

## Install chromedriver

### From python package (Recommended)

```bash
pip install chromedriver-binary
```

### From zip file

```bash
chrome_driver=$(curl "https://chromedriver.storage.googleapis.com/LATEST_RELEASE") && \
echo "$chrome_driver"
curl -Lo chromedriver_linux64.zip "https://chromedriver.storage.googleapis.com/\
${chrome_driver}/chromedriver_linux64.zip"
sudo apt install unzip
mkdir -p "chromedriver/stable" && \
unzip -q "chromedriver_linux64.zip" -d "chromedriver/stable" && \
chmod +x "chromedriver/stable/chromedriver"
```