import sys
import getopt
import logging

logging.basicConfig(level=logging.DEBUG,
                    format='[%(levelname)s][%(asctime)s] %(message)s',
                    datefmt='%Y-%m-%d %I:%M:%S')
logger = logging.getLogger()

args, _ = getopt.getopt(sys.argv[2:], 'do:', ['dev', 'output='])

print(args)

is_dev = False
save_log = False
for arg, value in args:
    if arg in ('-d', '--dev'):
        is_dev = True
    elif arg in ('-o', '--output'):
        save_log = True
    else:
        assert False, 'invalid argument'

if is_dev:
  print('This is dev environment')

if save_log:
  print('Saving logs')