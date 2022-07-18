#!/usr/bin/env python
# -*- coding: utf-8 -*-


""" Module of Periodic table named periodictb

Todo:
    output other information such as regular mass number

    Created in 01/26/2022

"""


class periodic:
    """ class: periodic

    This class is for creating periodic table.

    """

    def __init__(self):
        """ constructor

        List to Elements is based on Periodic table in 2022.

        List divided in new line follow their groups and same characteristics
        (Lanthanide, Actinide)

        """

        self.Elements = ["H", "He",
                         "Li", "Be", "B", "C", "N", "O", "F", "Ne",
                         "Na", "Mg", "Al", "Si", "P", "S", "Cl", "Ar",
                         "K", "Ca", "Sc", "Ti", "V", "Cr", "Mn", "Fe", "Co",
                         "Ni", "Cu", "Zn", "Ga", "Ge", "As", "Se", "Br", "Kr",
                         "Rb", "Sr", "Y", "Zr", "Nb", "Mo", "Tc", "Ru", "Rh",
                         "Pd", "Ag", "Cd", "In", "Sn", "Sb", "Te", "I", "Xe",
                         "Cs", "Ba",
                         "La", "Ce", "Pr", "Nd", "Pm", "Sm", "Eu", "Gd", "Tb",
                         "Dy", "Ho", "Er", "Tm", "Yb", "Lu",
                         "Hf", "Ta", "W", "Re", "Os", "Ir", "Pt", "Au", "Hg",
                         "Tl", "Pb", "Bi", "Po", "At", "Rn",
                         "Fr", "Ra",
                         "Ac", "Th", "Pa", "U", "Np", "Pu", "Am", "Cm", "Bk",
                         "Cf", "Es", "Fm", "Md", "No", "Lr",
                         "Rf", "Db", "Sg", "Bh", "Hs", "Mt", "Ds", "Rg", "Cn",
                         "Nh", "Fl", "Mc", "Lv", "Ts", "Og"
                         ]
        self.Elements_dict = {
            1: "H", 2: "He", 3: "Li", 4: "Be", 5: "B", 6: "C", 7: "N", 8: "O",
            9: "F", 10: "Ne", 11: "Na", 12: "Mg", 13: "Al", 14: "Si", 15: "P",
            16: "S", 17: "Cl", 18: "Ar", 19: "K", 20: "Ca"}

    def SymbolToAtom(self, Symbol, error="ON"):
        """ Symbol to Atom

        This method can exchange symbol of element to atomic number.

        Args:
            Symbol(string) : chemical symbol like H, He, C, etc...
            error(string, optional) : can output error(=ON).

        Raises:
            It causes errors in an invaild string that is not in periodic table.

        Yields:
            i(integer) : this yield is a atomic number in the matched string.

        Examples:
            test = periodic()
            print(test.SymbolToAtom("He"))
            -> 2

        """

        if Symbol in self.Elements:
            for i, e in enumerate(self.Elements, 1):
                if Symbol == e:
                    return i
        else:
            if error == "ON":
                raise ValueError(Symbol+" don't include in Periodic table!")
            else:
                pass

    def AtomToSymbol(self, Atomic, error="ON"):
        """ Atom to Symbol

        This method can exchange atomic number to symbol of elements.

        Args:
            Atomic(integer) : Atomic number (1 ~ 118).
            error(string, optional) : can output error(=ON).

        Raises:
            It causes errors in an invaild number that is not in periodic table.

        Yields:
            e(string) : this yield is chemical symbol in the matched number.

        Examples:
            test = periodic()
            print(test.AtomToSymbol(2))
            -> He

        """

        if 0 < Atomic <= len(self.Elements):
            for i, e in enumerate(self.Elements, 1):
                if i == Atomic:
                    return e
        else:
            if error == "ON":
                raise ValueError("Atomic number has to be from 1 to 118!\n"
                                 + "This case: " + str(Atomic))
            else:
                return str(Atomic)


if __name__ == "__main__":
    element = periodic()
    print(element.SymbolToAtom("Re"))
    print(element.AtomToSymbol(118))
    print(element.Elements_dict)
    print(element.Elements)
