## *Installing Windows Subsystem for Linux + Change WSL's directory to another Drive other than Window C:/*

*The [Windows Subsystem for Linux](https://docs.microsoft.com/en-us/windows/wsl/about) lets developers run a GNU/Linux environment -- including most command-line tools, utilities, and applications -- directly on Windows, unmodified, without the overhead of a traditional virtual machine or dualboot setup.*

1. [Installing WSL](https://youtu.be/D7Em1wjMiak)
2. [Change WSL's directory](https://youtu.be/ON_dPAO4KZs) so you can peacefully install packages as much as you want without having to worry about the limited storage of the Windows active partition C:\\!

> ***View files in ubuntu system using windows file explorer***

```
// type following address in the address bar of the file explorer

\\wsl$\Ubuntu-20.04\usr\share\doc\verilator\examples

```
> ***Open with atom editor for better view : showing open with atom when right clicking file or folder in windows 10***

[Guide](https://www.radishlogic.com/atom-text-editor/showing-open-with-atom-when-right-clicking-file-or-folder-in-windows-10/)

*Steps*

1. Open Atom Text Editor
2. Go to FILES --> SETTINGS --> SYSTEM
3. Check the following boxes

```
✅ Show in file context menus
✅ Show in folder context menus
```
