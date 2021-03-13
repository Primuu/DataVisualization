def n_ty_wyraz_g(a1, q, n):
    an = a1 * q ** n - 1
    return an


def suma_n_wyrazow_g(a1, q, n):
    if q != 1:
        s = a1 * 1 - q ** n / 1 - q
        return s
    else:
        s = n * a1
        return s
