from os import sep
from subs import getsubs

### Parameters
CRLF = "win"
LANGUAGE = "french"
DOPROMPT = True

FILENAME = "The.Walking.Dead.The.Ones.Who.Live.S01E02.1080p.WEB.H264-NHTFS.srt"

SRCDIR = "src"      # The source directory, to put the raw SRTs in
RESDIR = "res"      # The result directory, the script outputs the raw str selected in pieces
TRADDIR = "trad"    # The traduction directory, the script create as many blank files as the result files, to paste traduction in and fuse back later

STEP = 40
PADDING = 5

TF_PREFIX = "{}-{}_TOTRAD."
L_PREFIX = "%s." % LANGUAGE.upper()
TFP_PREFIX = "{}-{}_" + L_PREFIX

### Don't modify manually
LF = b'\r\n' if CRLF=="win" else b'\n'
PATH = SRCDIR + sep + FILENAME
FINAL_PATH = SRCDIR + sep + L_PREFIX + FILENAME
TARGET_PATH = RESDIR + sep + TF_PREFIX + FILENAME
TARGET_PATH_P = TRADDIR + sep + TFP_PREFIX + FILENAME

_PROMPT = "Translate these subtitles into %s without altering the format, from the {}th to the {}th subtitle." % LANGUAGE


def main(step,padding):
    subs = getsubs(PATH,LF)

    b,e = 0,step
    while b+padding < len(subs):
        print(f"{b}:{e}?")
        input() # to wait for translation with external software and keep track

        open(file=TARGET_PATH_P.format(b,e),mode="wb").close() # just creates the file to paste traduction in
        with open(file=TARGET_PATH.format(b,e),mode="wb") as fstream:
            for sub in subs[b:e]:
                fstream.write(sub["n"]+LF)
                fstream.write(sub["timing"]+LF)

                for subline in sub["sub"]: fstream.write(subline+LF)
                fstream.write(LF)

            if not DOPROMPT: continue
            fstream.write(_PROMPT.format(b+1,e).encode())
            fstream.write(LF)

        b,e = e-padding,e+step

if __name__=="__main__": main(STEP,PADDING)
