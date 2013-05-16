HDViet save
===========

This is simple python script for downloading stream from HDViet (include HD quality). 
Maded in 15 minutes.

How it's work
=============

HDViet make a lot of chunks with 5-10 seconds of video in it. Each file - is separate videoclip, you can download each file separately.

I don't know how to get url from web page, so you need any sniffer to get starting url. For example, for Zambezia: http://movies.hdviet.com/zambezia_3266.html

I use fiddler2 (http://fiddler2.com/) as sniffer to catch main url. Just start video to playing, wait while advertisement ended and look in sniffer for a lot of very similar request.

It's looks like:
http://acs06.vn-hd.com/03052013/zambezia_2012_1080p_bluray_dts_x264_publichd/800/zambezia_2012_1080p_bluray_dts_x264_publichd_800_1.ts

So, starting from 0 and count up till get 404 error we can get all part of video. To get HD video you must change in url "800" to "1024".

Actually video have 4 variants of quality: 480, 640, 800, 1024. Just replace in 2 places and get the quality you are interesting in.

For example, link to get HD videoclip:
http://acs06.vn-hd.com/03052013/zambezia_2012_1080p_bluray_dts_x264_publichd/1024/zambezia_2012_1080p_bluray_dts_x264_publichd_1024_1.ts

After all chunk download complete it's need to merge it all together. I use ffmpeg (http://www.ffmpeg.org/) to do this.

How to use
==========
In hdviet.py change path_template to url you get with sniffer without .ts extension and number in the end.
Don't forget to change quality in url.

Then run script: python hdviet.py

I make a sleep(3) timeout to prevent problem with server, just in case. If you want - you can change it.

After script end working - you will get a lot of NNNN.ts files and merge_all.bat file. You need ffmpeg.exe to merge all files together. 
Just put ffmpeg.exe near .bat and video files and run merge_all.bat

Notice: linux and Mac user know what to do in step, where i describe a Windows way working ;) This is detailed instruction for Windows.