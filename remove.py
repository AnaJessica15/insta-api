import os 
from os import listdir

folder_path = '/home/ana/Desktop/tact/Download Insta pics/food52'


for file_name in listdir(folder_path):
    
    if file_name.endswith('.txt'):
        
        os.remove(folder_path +'/'+ file_name)

    elif file_name.endswith('.json.xz'):

         os.remove(folder_path +'/'+ file_name)

    elif file_name.endswith('.mp4.temp' and '.mp4'):

         os.remove(folder_path +'/'+ file_name)

    elif file_name.endswith('.'):

         os.remove(folder_path +'/'+ file_name)
    
    elif file_name.endswith('_profile_pic.jpg'):

         os.remove(folder_path +'/'+ file_name)

    os.remove(folder_path +'/'+ 'id' )


    

   


         
