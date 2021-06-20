import argparse
from anytree import Node as AnyNode


class ArgumentParserNode(AnyNode):
    def __init__(
        self,
        module,
        parser=None,
        parent=None,
        argument_adder="add_argument",
        starter="start",
    ):
        super().__init__(name=self.get_suffix(module.__name__), parent=parent)
        self.parser = parser or argparse.ArgumentParser()
        self.module = module
        self.argument_adder = argument_adder
        self.starter = starter
        self.build()

    def build(self):
        if hasattr(self.module, self.argument_adder):
            submodules = getattr(self.module, self.argument_adder)(self.parser)
            if submodules:
                self.subparsers = self.parser.add_subparsers(
                    dest=self.name + "_command", required=True
                )
            for submodule in submodules or []:
                parser = self.subparsers.add_parser(self.get_suffix(submodule.__name__))
                ArgumentParserNode(submodule, parser, parent=self)

    @property
    def parse_args(self):
        return self.parser.parse_args

    def start(self, args):
        subparsers = getattr(self, "subparsers", None)
        if subparsers is None:
            getattr(self.module, self.starter)(args)
        else:
            value = getattr(args, subparsers.dest)
            for child in self.children:
                if child.name == value:
                    child.start(args)

    @staticmethod
    def get_suffix(module_name):
        return module_name.split(".")[-1]

    def __repr__(self):
        return f"ArgumentParserNode(name={self.name}, module={self.module.__name__})"
