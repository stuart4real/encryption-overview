"""
Author: Situ Feng

This is only meant to be used by students who are taking CSC427 LEC9201.
"""

from tinyec.ec import SubGroup, Curve


def sample_curve_p107():
    """
    This function prints out the ECC points on curve y^2 = x^3 + 7 (mod 17)
    """
    field = SubGroup(p=17, g=(15, 13), n=18, h=1)
    curve = Curve(a=0, b=7, field=field, name='p1707')
    print("curve: ", curve)

    for k in range(0, 25):
        p = k * curve.g
        print(f"{k} * G = ({p.x}, {p.y})")


def sample_curve_p1707():
    """
    This function prints out the ECC points on curve y^2 = x^3 + 7 (mod 17)
    """
    field = SubGroup(p=17, g=(5, 9), n=18, h=1)
    curve = Curve(a=0, b=7, field=field, name='p1707')
    print("curve: ", curve)

    for k in range(0, 25):
        p = k * curve.g
        print(f"{k} * G = ({p.x}, {p.y})")


if __name__ == "__main__":

    # Step 1: Observe the printed out points. What pattern did you notice?
    sample_curve_p107()

    # Step 2: Uncomment the function below. And observe the printed out points.
    #         Did you find a similiar pattern?

    # sample_curve_p1707()
