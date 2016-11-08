# Filename: dest_path.py
#
# Set destination folder
#
# Based on the location of CSVs and on the
# location of the web page's adjunct files.
#
# Returns :The path where the generate html files must be located.
# Example:
# if csv files are located under:
# Dropbox/Cluster1/Data
# and the web page store its files on
# Web/drupal/files
# then the destination path must be
# Web/drupal/files/Cluster1/Data

from pathlib import Path


def get_path(src_folder, root_folder):
    path = Path(src_folder)
    parent = path.parts[-2:]
    dest_folder = Path(root_folder, parent[0], parent[1])
    if not dest_folder.is_dir():
        dest_folder.mkdir(parents=True)
    return str(dest_folder)

