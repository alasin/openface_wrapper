from subprocess import call
import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument("--exe_dir", help="directory for OpenFace executable")
parser.add_argument("--src", help="input video")
parser.add_argument("--out_dir", help="output directory")

args = parser.parse_args()

src_filename = os.path.realpath(os.path.join(os.getcwd(), args.src))
exe_filename = os.path.realpath(os.path.join(args.exe_dir, "FeatureExtraction"))
out_full_dir = os.path.realpath(os.path.join(os.getcwd(), args.out_dir))

cmd_str = exe_filename 

ret = call([cmd_str, '-simalign', '-2Dfp', '-tracked', '-f', src_filename, '-out_dir', out_full_dir])
ret = call(['mv', 'R.txt', 'T.txt', 'bboxes.txt', out_full_dir + '/'])
