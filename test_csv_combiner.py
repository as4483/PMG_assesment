
from csv_combiner import Combine


class TestClass:

    def test_one(self, capfd):
        cargs = ['fixtures/accessories.csv', 'fixtures/clothing.csv']

        combine = Combine()
        combine.testArgs = cargs
        combine.combine_files()

        out, err = capfd.readouterr()

        testFile = open('fixtures/out.txt')
        assert out == "".join(testFile.readlines())
