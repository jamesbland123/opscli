""" Command class """
import argparse
import sys
import importlib
import pprint

class Command():
    """
    This is a Command class to process subcommands for the cli.

    Attributes:
        None
    """
    def __init__(self): 
        """
        Constructor for Command class that parses cli subcommands
        and validates input.
        """
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
            pprint.pprint(result)

    def get(self):
        """
        Processes the get subcommand, loads the requested module, and 
        runs the get method of the class.

        Args:
            (string) module name passed through command args.

        Returns 
            (dict) class module get.
        """
        parser = argparse.ArgumentParser(description='Provider service subcommand')
        parser.add_argument('provider')
        args = parser.parse_args(sys.argv[2:3])

        try: 
            mod = importlib.import_module('.' + args.provider, package='opscli.provider')

        except ImportError as error:
            print("Error: ", error.msg)
            parser.print_help()
            sys.exit(1)

        function = getattr(mod, str.capitalize(args.provider))
        instance_of_class = function()
        return instance_of_class.get()