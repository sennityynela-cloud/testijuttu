from unittest import TestCase
from tv import


class TestTV(TestCase):
    def test_paina_nappia(self):
        tv = TV()
        ennen = tv.päällä
        tv.painaNappia()
        self.assertEqual(ennen, not tv.päällä)

    def test_kanava_ylos1(self):
        tv = TV()
        ennen = tv.kanava
        tv.kanavaYlos()
        self.assertEqual(ennen, tv.kanava)

    def test_kanava_ylos2(self):
        tv = TV()
        tv.painaNappia()
        ennen = tv.kanava
        tv.kanavaYlos()
        self.assertEqual(ennen + 1, tv.kanava)

    def test_kanava_ylos3(self):
        tv = TV()
        tv.painaNappia()
        tv.kanavaYlos()
        ennen = tv.kanava
        for i in range(5):
            tv.kanavaYlos()
        self.assertEqual(ennen, tv.kanava)

#    def test_kanava_alas(self):
#        self.fail() # täydennä kun muut toimivat

    def test_ääni_ylos1(self):
        tv = TV()
        ennen = tv.ääni
        tv.ääniYlos()
        self.assertEqual(ennen, tv.ääni)

    def test_ääni_ylos2(self):
        tv = TV()
        tv.painaNappia()
        ennen = tv.ääni
        tv.ääniYlos()
        self.assertEqual(ennen + 1, tv.ääni)

    def test_ääni_ylos3(self):
        tv = TV()
        tv.painaNappia()
        ennen = tv.ääni
        for i in range(6):
            tv.ääniYlos()
        self.assertEqual(5, tv.ääni)

#    def test_ääni_alas(self):
#        self.fail() # täydennä kun muut toimivat
