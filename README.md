watchdog-wrapper
================

Directory monitoring wrapper.

dir-watch.py behavior
---------------------
####Linux
#####file deletion 
Action
```
rm /home/user/foo.txt
```
Output
```
deleted: /home/user/foo.txt
modified: /home/user
```

#####file creation
Action
```
cd /home/user/
ls .. > foo.txt
```
Output
```
created: /home/user/foo.txt
modified: /home/user
modified: /home/user/foo.txt
```
#####file renaming
Action
```
cd /home/user/
mv foo.txt bar.txt
```
Output
```
moved/renamed: /home/user/foo.txt destination: /home/user/bar.txt
modified: /home/user
```
#####file modified
Action
```
cd /home/user/
ls
>foo.txt
ls / > foo.txt
```
Output
```
modified: /home/user/foo.txt
```
