import PyInstaller.__main__ 
import os
PyInstaller.__main__.run([  
     'name-%s' % 'hfclpipbinary',
     '--onefile',
     '--windowed',
     os.path.join('/var/lib/jenkins/workspace/hfclpipeline2/', 'app.py')                                        
])
