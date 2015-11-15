import math

class Solver:
    def faa(self):
        return

    def foo(self, nom, den):
        if den > 0:
            return nom / den
        else:
            raise Exception


if __name__ == "__main__":
    s = Solver()
    print str(s.foo(2.0,3.0))

    try:
        print str(s.foo(2.0, 0))
    except Exception:
        print 'Zero division'
