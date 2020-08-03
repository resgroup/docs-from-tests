import samples.hello as hello
import samples.world as world

class HelloWorldCombiner:
    def combine(self) -> str:
        return f'{hello.hello()} {world.world()}' 