import os
from pyunpack import Archive
import re

default_folder = '/home/data/torrent/Shows/King.Of.The.Hill.S01-S12.DVDRip.x264-SCENE/'
# The folder to start in
pattern = 'r$'
# RegEx pattern for locating rar files

os.chdir(default_folder)
# cd into aforementioned folder

choice = input('Select the folder (from {} to {}): '.format(os.listdir()[0], os.listdir()[-1]))

os.chdir(default_folder + choice)
# cd into selected folder

for i in range(0, len(os.listdir())):
    os.chdir(default_folder + choice)
    # For loop that does stuff for every folder

    os.chdir(default_folder + choice + '/' + os.listdir()[i])
    # cd into selected episode

    for episode_list in range(0, len(os.listdir())):

        result = re.search(pattern, os.listdir()[episode_list])
        # RegEx result for .rar files

        if result:
            try:
                print(os.listdir()[episode_list])
                Archive(os.listdir()[episode_list]).extractall('.')
                # Extract .rar file to current folder
            except:
                print('Error')
        else:
            pass
print('Done')
