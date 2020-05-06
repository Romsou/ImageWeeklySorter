# Image weekly sorter

A simple python script to sort images out into directories based on the day of the week.

# Usage

For now, you can only use this script by creating a config.ini file in the directory you wish to sort.
You can find a sample in src.

The config.ini file has a very simple syntax. it consists in a Directories section, in which every line follow the same convention:

```
dayname : directory name
```

Notice that the images you want to sort need to use exif metadata. I originally wrote this script to automatically sort
my course photos, hence, it's not a generalist script and it may not be suitable for your own needs. However, feel free to adapt it.

In its current state, the script works on both Linux (tried on a Xubuntu 18.04) and Windows 10 (It should also works on OS X). 
