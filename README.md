# raspberry_pi_os_torrents_fetcher
check for a new raspberry pi os image, download the raspberry pi os torrent file to a local folder

## purpose:
i use it in combination with a cronscript, to check every monday
if there is a new raspberry pi os image, the torrent file is downloaded
the dl_folder is watched by my torrent client who will auto downloads & seeds the file

## how it works:
the script checks the servers 302 response, get the new location and extract the filename from it
if a file with the same name isn't already in the local folder, the torrent file will be downloaded

## requirements:
python3, requests
install requests via: ```pip3 install requests```
