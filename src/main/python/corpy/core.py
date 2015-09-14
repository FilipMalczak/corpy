import types

class CorpyRuntime: 
    def __init__(self, configuration):
        self.configuration = configuration

    def get_components(self):
        return dict(self.configuration.__dict__)

def component(class_or_foo):
    if isinstance(class_or_foo, type):
        clazz = class_or_foo
    elif isinstance(class_or_foo, (types.MethodType, types.FunctionType, types.LambdaType):
        foo = class_or_foo

class Configuration(types.SimpleNamespace):
    
    current_runtime = None
    
    def get_not_overloaded_main_msg(self):
        return "Overload main method of your configuration ("+str(type(self))")!"
    
    def main(self):
        print(get_not_overloaded_main_msg(self))
    
    def run(self):
        last_runtime = Configuration.current_runtime
        Configuration.current_runtime = CorpyRuntime(self)
        try:
            kwargs = {
                "a": 3,
                "b": 4
            }
            self.main(**kwargs)
        finally:
            Configuration.current_runtime = last_runtime
    
Configuration().run()
