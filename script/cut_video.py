import os
import sys


def main(path):
    os.chdir(path);
    for file in os.listdir(path):
        comd = 'ffmpeg -i {} -ss 15 -codec copy 1.mp4'.format(file, file)
        print(comd)
        os.system(comd)
        os.system('mv 1.mp4 {}'.format(file))


if __name__ == '__main__':
    path = sys.argv[1]
    main(path)
