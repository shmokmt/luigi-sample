import luigi
from luigi.mock import MockTarget


class OnMemoryTask(luigi.Task):

    def output(self):
        return MockTarget(self.__class__.__name__)


class Greet(OnMemoryTask):

    def run(self):
        out = self.output()
        with out.open('w') as f:
            f.write('Hello, World!\n')


class Eat(OnMemoryTask):

    def run(self):
        out = self.output()
        with out.open('w') as f:
            f.write('Mog, Mog\n')


class Sleep(OnMemoryTask):

    def run(self):
        out = self.output()
        with out.open('w') as f:
            f.write('Zzz...\n')


class RequiresOnly(luigi.WrapperTask):

    def requires(self):
        # 依存している Task は複数書ける
        return [Greet(), Eat(), Sleep()]
        # あるいは
        # yield Greet()
        # yield Eat()
        # yield Sleep()
        # としても良い


def main():
    luigi.run(main_task_cls=RequiresOnly, local_scheduler=True)


if __name__ == '__main__':
    main()