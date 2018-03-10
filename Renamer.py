import os
from tvdb_api import Tvdb
import re


def get_files(path):
    fileNames = os.listdir(path)
    return fileNames


def get_episode_number(fileName):
    episodeNumber = None
    try:
        episode = re.findall(r'[Ss]..[Ee](..)', fileName)[0]
        episodeNumber = int(episode)
    except:
        pass
    return episodeNumber


def get_file_extension(fileName):
    fileExtension = fileName[-4:]
    return fileExtension


def rename(showName, seasonNumber, path):
    tvdb = Tvdb()
    fileNames = get_files(path)
    os.chdir(path)
    flag = False
    for fileName in fileNames:
        episodeNumber = get_episode_number(fileName)
        if episodeNumber:
            episode = tvdb[showName][seasonNumber][episodeNumber]
            fileExtension = get_file_extension(fileName)
            episodeName = str(episodeNumber) + " - " + episode['episodename'] + fileExtension
            os.rename(fileName, episodeName)
            flag = True
    if flag:
        print("Rename Complete")
    else:
        print("No files changed")


if __name__ == "__main__":
    showName = input("Enter the name of the show ")
    seasonNumber = int(input("Enter the season number "))
    path = input("Enter path to the " + showName + " season " + str(seasonNumber) + " folder ")
    rename(showName, seasonNumber, path)

