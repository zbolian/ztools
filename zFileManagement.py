import shutil

def copyAndPasteFile(fromFilePath, toFilePath):
    shutil.copy2(fromFilePath, toFilePath)

copyAndPasteFile(r'/Users/zach.bolian/Desktop/P&G brands.xlsx',r'/Users/zach.bolian/Documents/P&G brands.xlsx')

__author__ = 'zach.bolian'
