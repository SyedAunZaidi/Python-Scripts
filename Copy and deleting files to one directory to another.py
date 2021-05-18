#! usr/bin/python

import time
import schedule

def createFolder_move():
    from datetime import datetime
    import os
    
    today = datetime.now()
    date_str = str(today.date())

    if os.path.exists("C:\\Users\\Aun\\Music\\"+date_str +"\\"):
        import shutil
        source_dir  = "C:\\Users\\Aun\Music"
        target_dir  = "C:\\Users\\Aun\Music\\"+date_str

        # file_names = os.listdir(source_dir)
        file_names = [f for f in os.listdir(source_dir) if os.path.isfile(os.path.join(source_dir, f))]   # Selects files only from directory
            
        print(file_names)
        for file_name in file_names:
            shutil.copy(os.path.join(source_dir, file_name), target_dir) # Copy only files to target directory
            os.remove(os.path.join(source_dir, file_name))  # Delete that file from parent directory
    else:
        os.mkdir("C:\\Users\\Aun\\Music\\" + today.strftime('%Y-%m-%d'))
        

schedule.every(1).seconds.do(createFolder_move)

while 1:
    schedule.run_pending()
    time.sleep(1)

