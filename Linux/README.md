# Commands Collection

## General
| Description   | Example                                    |
| ------------- | ------------------------------------------ |
| Loop commands | ```for i in {1..50}; do {command}; done``` |

<br>

## Files & Folders
| Description                                              | Example                                                                    |
| -------------------------------------------------------- | -------------------------------------------------------------------------- |
| Find word pattern in dir                                 | ```grep -rni '{dir}' -e '{pattern}'```                                     |
| Find file in dir                                         | ```find {dir} -name {file}```                                              |
| Find all extensions type in dir                          | ```find . -type f \| sed -rn 's\|.*/[^/]+\.([^/.]+)$\|\1\|p' \| sort -u``` |
| Show directory size                                      | ```du -sh {dir}```                                                         |
| Show numeric permissions for all files and folder in dir | ```stat -c '%a %n' *```                                                    |
| Watch file changes                                       | ```tail -f {file}```                                                       |
| Rename file extensions for all file in dir               | ```rename 's/\.{old_ext}/\.{new_ext}/' *.{old_ext}```                      |

<br>

## Process
| Description               | Example                  |
| ------------------------- | ------------------------ |
| Show PID/CPU/MEM usage    | ```ps -aux```            |
| Kill a process using PID  | ```kill -9 {PID}```      |
| Kill all user's processes | ```pkill -9 -u {user}``` |

<br>

## Network
| Description                           | Example       |
| ------------------------------------- | ------------- |
| List socket(TCP/UDP/PORT) information | ```lsof -i``` |

<br>

## Bash

### Bash for version increment

```bash
current_version=$(jq -r '.metadata.script_version' test.ipynb)
echo "Current version:" $current_version
new_version=$(python3 -c "version = list(map(int, '$current_version'.split('.'))); version[-1] += 1; print('.'.join(map(str, version)))")
echo "New version:" $new_version

jq ".metadata.script_version = \"$new_version\"" test.ipynb > tmp.ipynb
mv tmp.ipynb test.ipynb
```

<br>

# Package Collection

installer | package | description
--- | --- | ---
apt | nethogs | Network monitoring program

<br>

# WSL

## Miniconda

### Install

```bash
cd ~
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
chmod +x Miniconda3-latest-Linux-x86_64.sh
sh Miniconda3-latest-Linux-x86_64.sh
rm Miniconda3-latest-Linux-x86_64.sh
source .bashrc
conda config --set auto_activate_base false
source .bashrc
```

### Create environment

```bash
conda create -n {env_name} python={python_version}
```


## Configurations

### To increase memory 
At c:\\user\\{name} create .wslconfig and add the following

```
[wsl2]
memory=11GB
```

### Enabled systemd
Inside your Ubuntu instance, add the following modification to /etc/wsl.conf.

```
[boot]
systemd=true
```