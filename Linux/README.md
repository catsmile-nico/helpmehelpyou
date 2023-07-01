# Commands Collection

## General
| Description   | Example                              |
| ------------- | ------------------------------------ |
| Loop commands | for i in {1..50}; do {command}; done |

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

## Process
| Description              | Example             |
| ------------------------ | ------------------- |
| Show PID/CPU/MEM usage   | ```ps -aux```       |
| Kill a process using PID | ```kill -9 {PID}``` |

## Network
| Description                           | Example       |
| ------------------------------------- | ------------- |
| List socket(TCP/UDP/PORT) information | ```lsof -i``` |