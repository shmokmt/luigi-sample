import luigi

class TaskA(luigi.Task):
    def run(self):
        print("Hello, I'm TaskA.")

class TaskB(luigi.Task):
    def requires(self):
        return TaskA()
    
    def run(self):
        print("Hello, I'm TaskB.")


if __name__ == '__main__':
    luigi.run()