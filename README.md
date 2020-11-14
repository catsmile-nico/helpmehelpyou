# GIT MARKDOWN
Description | Example | Detailed example
----------- | ------- | ---- 
New line | line1 \<br/> line2 | tbd

# POWERSHELL
Description | Example | Detailed example
----------- | ------- | ----
bulk replace filename | Get-ChildItem -Filter "partial_filename" -Recurse \| Rename-Item -NewName {$_.name -replace 'part_to_change','change' } | tbd
bulk execute command to files | Get-ChildItem  .\*.tgz -Name \| Foreach-Object {tar -xvf $PSItem}  | tbd
