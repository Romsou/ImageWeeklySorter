import os
import sys
import imghdr
import datetime
import calendar
import argparse
import configparser

from PIL import Image
from PIL.ExifTags import TAGS
from pathlib import Path, PureWindowsPath


DEFAULT_CONFIG_FILE = Path('config.ini')
DEFAULT_SECTION_NAME = 'Directories'


def main():
    config_content = parse_config(DEFAULT_CONFIG_FILE, DEFAULT_SECTION_NAME)

    agenda = { day : subject for day, subject in config_content }
    dirs = list(agenda.values())

    create_directories(dirs)
    sort_image(agenda)


def parse_config(conf_file, section):
    check_config_file(conf_file)
    parser = configparser.ConfigParser()
    parser.read(conf_file)
    return parser.items(section)


def check_config_file(conf_file):
    if not conf_file.is_file():
        print('Must specify a config file')
        sys.exit(1)


def create_directories(directories: list):
    for directory in directories:
        create_directory(directory)
    

def create_directory(directory):
    if Path(directory).is_file():
        print(f'Error: {directory} is a file')
        sys.exit(1)
    elif not Path(directory).exists():
        Path(directory).mkdir()


def sort_image(agenda):
    for file in os.listdir():
        if not Path(file).is_dir() and str(imghdr.what(file)) != 'None':
            image = Image.open(file)
            dayname = creation_dayname(image)
            image.close()
            move_in_dir(file, agenda, dayname)


def creation_dayname(image):
    date = parse_date(get_creation_date(image))
    date = datetime.datetime.strptime(date,'%d %m %Y').weekday()
    return calendar.day_name[date].lower()


def parse_date(date):
    return " ".join(date.split(" ")[0].split(":")[::-1])


def get_creation_date(img: Image):
    info = img._getexif()
    for tag in info.keys():
        if TAGS.get(tag, tag) == 'DateTimeOriginal':
            return info[tag] 
    return None


def move_in_dir(imagename, agenda, dayname):
    if Path(agenda[dayname]).is_dir():
        os.rename(Path(imagename), Path(agenda[dayname]) /  Path(imagename))


if __name__ == '__main__':
    main()

