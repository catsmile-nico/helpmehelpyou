# Commands Collection
| Description                         | Example                                                                                                                       |
| ----------------------------------- | ----------------------------------------------------------------------------------------------------------------------------- |
| bulk replace filename               | ```Get-ChildItem -Filter "partial_filename" -Recurse \| Rename-Item -NewName {$_.name -replace 'part_to_change','change' }``` |
| bulk execute command to files       | ```Get-ChildItem  .\*.tgz -Name \| Foreach-Object {tar -xvf $PSItem}```                                                       |
| set execution policy to run scripts | ```Set-ExecutionPolicy unrestricted```                                                                                        |
