import os
import sys

from Utilities.filecreator import create_file_if_not_exists

BASKETS_BASE_DIRECTORY = "baskets"
CONFIG_FILE_DEFAULT_NAME = "config.json"
Baskets_Base_Location = None
Config_File_Location = None

if sys.platform in ("linux", "linux2", "darwin"):
    filesystem_location = '/etc/iotcollector'
elif sys.platform == "win32":
    filesystem_location = os.path.dirname(os.path.realpath(__file__))


def set_filesystem_location(new_location):
    global filesystem_location
    filesystem_location = new_location


def init_file_system(new_configfile_location=None):
    global Baskets_Base_Location, Config_File_Location

    try:
        Baskets_Base_Location = os.path.join(filesystem_location, BASKETS_BASE_DIRECTORY)
        if not os.path.exists(Baskets_Base_Location):
            os.makedirs(Baskets_Base_Location)

        if new_configfile_location is not None:
            Config_File_Location = create_file_if_not_exists(new_configfile_location, hidden=False, init_text='[]')
        else:
            Config_File_Location = create_file_if_not_exists(
                os.path.join(filesystem_location, CONFIG_FILE_DEFAULT_NAME), hidden=False, init_text='[]')
    except (Exception, OSError) as ex:
        print >> sys.stderr, ex
        sys.exit(1)


def get_baskets_base_location():
    return Baskets_Base_Location


def get_configfile_location():
    return Config_File_Location
