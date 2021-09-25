# minecraft_python
Learn Python through Minecraft

[set things up in Windows 10]
1. Install python3.8  
    A. Download and install : https://www.python.org/ftp/python/3.8.10/python-3.8.10-amd64.exe  
        * https://www.python.org/downloads/windows/  
    B. Check :  
        python --version  
    C. Add python path :  
        Add user environment path below, after opening system variable via Control Panel  
            %USERPROFILE%\AppData\local\programs\python\python38\lib\site-packages  
        *  uninstall Anaconda or Miniconda if they are installed, to avoid path confusion,   particularly when running 'pip install XXX'   

2. Install Sublime text  
    A. Download and install : https://www.sublimetext.com/  
    B. Check :   
        Create test.py file and type below  
            print('test')  
        [Ctrl] + [b] to run the above line  
    C. Customize :   
        Preferences > Settings and modify "translate_tabs_to_spaces": true  

