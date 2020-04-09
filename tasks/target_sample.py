import luigi


class Greet(luigi.Task):
    def output(self):
        return luigi.LocalTarget("greeting.txt")
    
    def run(self):
        out = self.output()
        with out.open('w') as f:
            f.write('Hello, World!')

if __name__ == "__main__":
    luigi.run(main_task_cls=Greet, local_scheduler=True)