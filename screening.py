import os

def txt(source,chg_file_name=False,replace_string=False,replace_content=False):
    
    if chg_file_name == True:
        try:
            dest = input('Enter dest that will replace')
            os.rename(source,dest) 
            print('File name changed to '+dest)
        except Exception as e:
            print('Error in change in file name : ',e)
            
    if replace_string == True:
        try:
            x = input("Enter text to be replaced:")
            y = input("Enter text that will replace:")  
            if chg_file_name == True:
                f = open(dest,'r+')
            if chg_file_name == False:
                f = open(source,'r+')
            l = f.readlines()
            if x in l[0]:
                c = 0
                for i in l:
                    if x in i:
                        Replacement = i.replace(x, y)
                        l = Replacement
                    c += 1
                f.truncate(0)
                f.writelines(l)
                f.close()
                print("Text successfully replaced")
            else:
                print(x+" is not present, Invalid input")
        except Exception as e:
            print('Error in replacing the string : ',e)
        finally:
            f.close()
            
    if replace_content == True:
        replace_string == False
        try:
            s = input("Enter text to replace the existing content:")
            if chg_file_name == True:
                f = open(dest,'r+')
            if chg_file_name == False:
                f = open(source,'r+')
            f.truncate(0)
            f.write(s)
            f.close()
            replace_string == False
            print("Text successfully replaced")
        except Exception as e:
            print('Error in replacing the content : ',e)
        finally:
            f.close()
            
            
txt(source = 'C:\\Users\\hp\\Desktop\\example1.txt',
    chg_file_name=True,
    replace_string=True,
    replace_content=True)