#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
purpose:
	check the raspberry pi os torrent link for a new version
	if a new version is available, download torrent file to a local folder

usage:
	i use it in combination with a cronscript, to check every monday
	if there is a new raspberry pi os image, the torrent file is downloaded
	the dl_folder is watched by a torrent client and auto downloads / seeds the file

how does it work:
	check the servers 302 answer, get the new location, extract filename from it,
	check if filename is already in local folder, if not: download it

requirements:
	python3, requests
	install requests via: pip3 install requests

raspberry pi os torrent urls:
	Desktop Full:	https://downloads.raspberrypi.org/raspios_full_armhf_latest.torrent
	Desktop:			https://downloads.raspberrypi.org/raspios_armhf_latest.torrent
	Lite:					https://downloads.raspberrypi.org/raspios_lite_armhf_latest.torrent
"""

import sys,os,requests,shutil

dl_folder = "/Users/auckenox/Projects/raspberry_pi_os_torrents_fetcher"
rpi_url = "https://downloads.raspberrypi.org/raspios_lite_armhf_latest.torrent"


def downloadFile(url,target_file):
	try:
		response = requests.get(url, stream=True)
		with open(target_file, 'wb') as out_file:
			shutil.copyfileobj(response.raw, out_file)
		del response
	except Exception as e:
		print("downloadFile failed: %s"%e)
		sys.exit(1)

def getRealDownloadUrl(url):
	try:
		r = requests.get(url, allow_redirects=False)
		rdr_url = r.headers['Location']
		if rdr_url == '':
			return False
		return rdr_url
	except Exception as e:
		print("getRealDownloadUrl failed: %s"%e)
		sys.exit(1)


dl_url = getRealDownloadUrl(rpi_url)
filename = os.path.basename(dl_url)
path = "%s/%s"%(dl_folder,filename)

if os.path.isfile(path):
	print('the file: "%s" already exists, no new version found'%filename)
else:
	print('new file found: "%s" lets download it'%filename)
	downloadFile(dl_url,path)
	print('download from "%s" successful!'%dl_url)

sys.exit(0)
