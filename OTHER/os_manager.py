import os
import stat
import argparse
from pathlib import Path

parser = argparse.ArgumentParser(description='System management program',
                                 usage='Script options:')
parser.add_argument('-s', '--system',  type=str, help='System command')
parser.add_argument('-c', '--chmod',  type=str, help='Checking access rights')
parser.add_argument('-t', '--tree',  type=str, help='Directory tree')
args = parser.parse_args()


class SystemManagment:
    def __init__(self):
        if args.system == 'system':
            self.shell_command()
        elif args.chmod == 'chmod':
            self.chmod()
        elif args.tree == 'tree':
            self.tree()

    @staticmethod
    def shell_command():
        while cmd := input('Shell command: '):
            if cmd == 'exit':
                print('The work was completed!')
                break
            if os.system(cmd) != 0:
                print('Wrong command, exit!')
                break

    @staticmethod
    def chmod():
        while fdir := input('Enter the path: '):
            if fdir == 'exit':
                print('The file or directory does not exist!')
                break
            if os.path.exists(fdir) == False:
                print('The file or directory does not exist!')
            else:
                print(oct(stat.S_IMODE(os.lstat(fdir).st_mode))[2:])

    def tree(self):
        while fdir := input('Enter the path: '):
            if fdir == 'exit':
                print('The file or directory does not exist!')
                break
            if os.path.exists(fdir) == False:
                print('The file or directory does not exist!')
            else:
                self.print_tree(fdir)

    def print_tree(self, path='.', head='', tail=''):
        path = Path(path)
        print(head + path.name)
        entries = sorted(filter(Path.is_dir, path.iterdir()))

        for i, entry in enumerate(entries):
            if i < len(entries) - 1:
                self.print_tree(entry, tail + '├──', tail + '│  ')
            else:
                self.print_tree(entry, tail + '└──', tail + '   ')


SystemManagment()
