import luigi

class Greet(luigi.Task):
    def output(self):
        return luigi.LocalTarget('greeting.txt')
    
    def run(self):
        out = self.output()
        with out.open('w') as f:
            f.write('Hello, World\n')

class Repeat(luigi.Task):
    def requires(self):
        return Greet()
    
    def output(self):
        return luigi.LocalTarget('repeating.txt')
    
    def run(self):
        # requires() で指定した Task の実行結果(Target)は input() で得られる
        # input_ = yield Greet() のように書くこともできる
        # yield を使う書き方だと複数列挙した場合、必ず直列になる
        input_ = self.input()
        output = self.output()

        with input_.open('r') as r, output.open('w') as w:
            lines = r.readlines()

            for _ in range(3):
                w.writelines(lines)

if __name__ == '__main__':
    luigi.run(main_task_cls=Repeat, local_scheduler=True)