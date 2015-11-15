# source https://pythonhosted.org/testfixtures/files.html

from testfixtures import TempDirectory
with TempDirectory() as d:
  d.write('test.txt', b'some foo thing')
  foo2bar(d.path, 'test.txt')
  d.read('test.txt')
...
b'some bar thing

or

from testfixtures import tempdir, compare

@tempdir()
def test_function(d):
    d.write('test.txt', b'some foo thing')
    foo2bar(d.path, 'test.txt')
    compare(d.read('test.txt'), b'some bar thing')