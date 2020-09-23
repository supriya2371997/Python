import zipfile

#create context manager. They are specifically used to close the file after the operation is done
#E:\PYTHONTEMP\TARGET1.ZIP is the path to output folder/directory along with file name and extension
#w will make the output file writable
#compression=zipfile.ZIP_DEFLATED will reduce the size of the output file
with zipfile.ZipFile('E:\PYTHONTEMP\TARGET1.ZIP','w',compression=zipfile.ZIP_DEFLATED) as zipo:
    
    #perform write operation
    zipo.write('E:\PYTHONTEMP\DEMO.zip')
    zipo.write('E:\PYTHONTEMP\MUSIC.mp3')