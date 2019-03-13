
import importlib

class Command():
    def __init__(self, func=None): 
        if func:
            result = getattr(self, "get")()
            print(result)

    def get(self):
        mod = importlib.import_module('.account', package='opscli.provider')
        function = getattr(mod, "Account")
        instance_of_class = function()
        return instance_of_class.get()

    def help(self):
        return "Please helpme"