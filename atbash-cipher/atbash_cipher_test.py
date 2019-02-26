import unittest

from atbash_cipher import Atbash


# Tests adapted from `problem-specifications//canonical-data.json` @ v1.2.0

class AtbashCipherTest(unittest.TestCase):

    def setUp(self):
        self.atbash = Atbash()

    def test_encode_no(self):
        self.assertMultiLineEqual(self.atbash.encode("no"), "ml")

    def test_encode_yes(self):
        self.assertMultiLineEqual(self.atbash.encode("yes"), "bvh")

    def test_encode_OMG(self):
        self.assertMultiLineEqual(self.atbash.encode("OMG"), "lnt")

    def test_encode_O_M_G(self):
        self.assertMultiLineEqual(self.atbash.encode("O M G"), "lnt")

    def test_encode_long_word(self):
        self.assertMultiLineEqual(self.atbash.encode("mindblowingly"), "nrmwy oldrm tob")

    def test_encode_numbers(self):
        self.assertMultiLineEqual(
            self.atbash.encode("Testing, 1 2 3, testing."), "gvhgr mt123 gvhgr mt")

    def test_encode_sentence(self):
        self.assertMultiLineEqual(
            self.atbash.encode("Truth is fiction."), "gifgs rhurx grlm")

    def test_encode_all_things(self):
        plaintext = "The quick brown fox jumps over the lazy dog."
        ciphertext = "gsvjf rxpyi ldmul cqfnk hlevi gsvoz abwlt"
        self.assertMultiLineEqual(self.atbash.encode(plaintext), ciphertext)

    def test_decode_word(self):
        self.assertMultiLineEqual(self.atbash.decode("vcvix rhn"), "exercism")

    def test_decode_sentence(self):
        self.assertMultiLineEqual(
            self.atbash.decode("zmlyh gzxov rhlug vmzhg vkkrm thglm v"),
            "anobstacleisoftenasteppingstone")

    def test_decode_numbers(self):
        self.assertMultiLineEqual(
            self.atbash.decode("gvhgr mt123 gvhgr mt"), "testing123testing")

    def test_decode_all_the_letters(self):
        ciphertext = "gsvjf rxpyi ldmul cqfnk hlevi gsvoz abwlt"
        plaintext = "thequickbrownfoxjumpsoverthelazydog"
        self.assertMultiLineEqual(self.atbash.decode(ciphertext), plaintext)

    def test_decode_with_too_many_spaces(self):
        self.assertMultiLineEqual(self.atbash.decode("vc vix    r hn"), "exercism")
    #
    def test_decode_with_no_spaces(self):
        ciphertext = "zmlyhgzxovrhlugvmzhgvkkrmthglmv"
        plaintext = "anobstacleisoftenasteppingstone"
        self.assertMultiLineEqual(self.atbash.decode(ciphertext), plaintext)

    # additional track specific test
    def test_encode_decode(self):
        self.assertMultiLineEqual(
            self.atbash.decode(self.atbash.encode("Testing, 1 2 3, testing.")), "testing123testing")


if __name__ == '__main__':
    unittest.main()
