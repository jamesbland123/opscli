
import importlib
import argparse
import sys

class Command():
    def __init__(self, func=None): 
        parser = argparse.ArgumentParser(description='Opscli',
                 usage='opscli <command> [<service>] [<options>]')
        parser.add_argument('command')
        args = parser.parse_args(sys.argv[1:2])
        
        if not hasattr(self, args.command):
            print('Unrecognized command')
            parser.print_help()
            sys.exit(1)

        if args.command:
            result = getattr(self, args.command)()
            print(result)

    def get(self):
        parser = argparse.ArgumentParser(description='Provider service subcommand')
        parser.add_argument('provider')
        args = parser.parse_args(sys.argv[2:3])

        try: 
            mod = importlib.import_module('.' + args.provider, package='opscli.provider')

        except ImportError as error:
            print("Error: ", error.msg)
            parser.print_help()
            sys.exit(1)

        function = getattr(mod, "Account")
        instance_of_class = function()
        return instance_of_class.get()

    def help(self):
        return "Please helpme"