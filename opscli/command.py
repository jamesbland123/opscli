
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
        mod = importlib.import_module('.account', package='opscli.provider')
        function = getattr(mod, "Account")
        instance_of_class = function()
        return instance_of_class.get()

    def help(self):
        return "Please helpme"