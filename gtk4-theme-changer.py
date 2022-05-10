#!/usr/bin/python3

import argparse
import subprocess
import os

home_dir = os.environ['HOME']

parser = argparse.ArgumentParser()
parser.add_argument('--themes', type=str, default=home_dir+"/.themes", help="use custom themes directory")
parser.add_argument('--config', type=str, default=home_dir+"/.config", help="use custom config directory")
parser.add_argument('--link', action="store_true", help='use symlinks instead of copy')
parser.add_argument('--reset', action="store_true", help='reset gtk4 configuration')
args = parser.parse_args()

themes_dir = args.themes
config_dir = args.config
theme_dirs = ["gtk-4.0", "assets"]

if args.reset:
	for directory in theme_dirs:
		if directory in os.listdir(config_dir):
			subprocess.call(["rm", "-r", config_dir+"/"+directory])
	exit()

available_themes = []
for theme in os.listdir(themes_dir):
	if theme_dirs[0] in os.listdir(themes_dir+"/"+theme):
		available_themes += [theme]
if available_themes != []:
	print("Available themes:")
	print()
	i=1
	for theme in available_themes:
		print(str(i)+".", theme)
		i+=1
	print()
	used_theme_dir = themes_dir+"/"+available_themes[int(input("Which theme do you want to use? "))-1]
	for directory in theme_dirs:
		if directory in os.listdir(used_theme_dir):
			if directory in os.listdir(config_dir):
				subprocess.call(["rm", "-r", config_dir+"/"+directory])
			if args.link:
				subprocess.call(["ln", "-s", used_theme_dir+"/"+directory, config_dir+"/"+directory])
			else:
				subprocess.call(["cp", "-r", used_theme_dir+"/"+directory, config_dir+"/"+directory])
else:
	print("No supported gtk4 themes found.")
