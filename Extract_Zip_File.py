#Extract files from any directory to ant directly
#import package
import zipfile
#zip file location
target='E:\\DEMO.zip'
#make target file readable
handle=zipfile.ZipFile(target,mode='r')
#output folder location
handle.extractall('E:\\EXTRACTED')
handle.close()