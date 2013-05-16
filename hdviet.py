import urllib2
import time

def main():
    path_template = "http://acs06.vn-hd.com/03052013/zambezia_2012_1080p_bluray_dts_x264_publichd/1024/zambezia_2012_1080p_bluray_dts_x264_publichd_1024_"
    concatfile = open('merge_all.bat', mode='w')
    i = 0
    try:
        while(True):
            path = path_template
            path += str(i)
            path += ".ts"
            print "Get url: " + path
            response = urllib2.urlopen(path)
            raw = response.read()
            savefile = open(str(i)+'.ts', mode='wb')
            savefile.write(raw)
            savefile.close()
            time.sleep(3)
            i += 1
    except urllib2.URLError, e:
        if not hasattr(e, "code"):
            raise

    concatfile.write('ffmpeg -i "concat:')
    for x in range(0, i):
        if not x==0:
            concatfile.write('|')
        concatfile.write(str(x) + ".ts")
    concatfile.write('" -c copy -bsf:a aac_adtstoasc res.mp4')
    concatfile.close()

if __name__ == "__main__":
    main()
