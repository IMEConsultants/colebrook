""" Provides various functions for calculating the Darcy friction factor based on Colebrook-White approximations.
https://en.wikipedia.org/wiki/Darcy_friction_factor_formulae

"""
__author__ = "Rob Markoski, IME Consultants"
__status__ = "Development"
__version__ = "20190215"

import math
import argparse


def sjFriction(reynolds, roughness, sigfig=4):
    """
    Model: Swamee, Jain
    Year: 1976
    Paper: https://cedb.asce.org/CEDBsearch/record.jsp?dockey=0006693
    Suitable Range:
        5000 < Reyonolds < 10^8 and e/D = 0.00001 - 0.5
    """
    friction = 0.25 / (math.log10(roughness / 3.7 + 5.74 / (reynolds**0.9)))**2
    return round(friction, sigfig)


def bntFriction(reynolds, roughness, sigfig=4):
    """
    Model: Bellos, Nalbantis, Tsakris
    Year: 2018
    Paper: https://www.sciencedirect.com/science/article/pii/S0029549311000173
    Suitable Range:
        All Flow Regimes
    """
    inv_roughness = 1 / roughness
    param_a = 1 / (1 + (reynolds / 2712)**8.4)
    param_b = 1 / (1 + (reynolds / (150 * inv_roughness))**1.8)
    exponent_a = 2 * (param_a - 1) * param_b
    exponent_b = 2 * (param_a - 1) * (1 - param_b)
    friction = (64 / reynolds)**param_a * (0.75 * math.log(reynolds / 5.37))**exponent_a * (0.88 * math.log(6.82 *inv_roughness))**exponent_b
    return round(friction, sigfig)


def fngFriction(reynolds, roughness, sigfig=4):
    """
    Model: Fang
    Year: 2011
    Paper: https://www.sciencedirect.com/science/article/pii/S0029549311000173
    Suitable Range:
        Reynolds > 2300 (I.E. Turbulent and Transition Range only)
    """

    friction = 1.613 * (math.log(0.234 * roughness ** 1.1007 - 60.525 / reynolds**1.1105 + 56.291 / reynolds**1.0712))**-2
    return round(friction, sigfig)


def eptFriction(reynolds, roughness, sigfig=4):
    """
    Model: Evangelides, Papaevangelou, Tzimopoulos
    Year: 2010
    Paper: http://blogs.sch.gr/geopapaevan/files/2010/07/full-paper_pre1128act.pdf
    Suitable Range:
        Reynolds > 2300 (I.E. Turbulent and Transition Range only)

    Rel
    """
    friction = (0.2479 - 0.0000947 * (7 - math.log10(reynolds))**4) / (math.log10(roughness / 3.615 + 7.366 / reynolds**0.9142))**2
    return round(friction, sigfig)


def akFriction(reynolds, roughness, sigfig=4):
    """
    Model: Avci, Kargoz
    Year: 2009
    Paper: http://dx.doi.org/10.1115/1.3129132
    Suitable Range:
        Reynolds > 2300 (I.E. Turbulent and Transition Range only)

    """
    friction = 6.4 / (math.log(reynolds) - math.log(1 + 0.01 * reynolds * roughness * (1 + 10 * math.sqrt(roughness))))**2.4
    return round(friction, sigfig)


def bkcFriction(reynolds, roughness, sigfig=4):
    """
    Model: Brkic
    Year: 2011
    Paper: https://doi.org/10.1080%2F10916461003620453
    Suitable Range:
        Reynolds > 2300 (I.E. Turbulent and Transition Range only)
    """
    beta = math.log(reynolds / (1.816 * math.log((1.1 * reynolds) / math.log(1 + 1.1 * reynolds))))
    friction = (-2 * math.log10((2.18 * beta) / reynolds + roughness / 3.71))**-2
    return round(friction, sigfig)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("reynolds", help="Reynolds Number", type=int)
    parser.add_argument("relroughness", help="Relative Roughness of pipe", type=float)
    parser.add_argument("sigfig", nargs="?", help="OPTIONAL - Number of Significant Figures (Default=4)", default=4, type=int)
    args = parser.parse_args()
    reynolds = args.reynolds
    roughness = args.relroughness

    table_format = "|{:<15} | {:<7}|"
    fric_headers = ["METHOD", "VALUE"]

    factors = []
    factors.append(["sjFriction", sjFriction(reynolds, roughness)])
    factors.append(["bntFriction", bntFriction(reynolds, roughness)])
    factors.append(["fngFriction", fngFriction(reynolds, roughness)])
    factors.append(["akFriction", akFriction(reynolds, roughness)])
    factors.append(["bkcFriction", bkcFriction(reynolds, roughness)])
    factors.append(["eptFriction", eptFriction(reynolds, roughness)])
    print("Ensure values are within range of applicability for equations (specifically around transition and laminar region)!")
    print(table_format.format(*fric_headers))
    print("---------------------------")
    for row in factors:
        print(table_format.format(*row))
    print("DISCLAIMER: Use secondary verification. No guarantee of accuracy")


if __name__ == "__main__":
    main()
