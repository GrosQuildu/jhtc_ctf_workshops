# https://id0-rsa.pub/problem/11/

import gmpy2

def crt(a, n):
    """Chinese remainder theorem
    from: http://rosettacode.org/wiki/Chinese_remainder_theorem#Python
    
    x = a[0] % n[0]
    x = a[1] % n[1]
    x = a[2] % n[2]
    Args:
        a(list): remainders
        n(list): modules

    Returns:
        long: solution to crt
    """
    if len(a) != len(n):
        log.critical_error("Different number of remainders({}) and modules({})".format(len(a), len(n)))

    sum = 0
    prod = reduce(lambda x, y: x * y, n)

    for n_i, a_i in zip(n, a):
        p = prod / n_i
        sum += a_i * gmpy2.invert(p, n_i) * p
    return long(sum % prod)

e = 3

C1 = 0x94f145679ee247b023b09f917beea7e38707452c5f4dc443bba4d089a18ec42de6e32806cc967e09a28ea6fd2e683d5bb7258bce9e6f972d6a30d7e5acbfba0a85610261fb3e0aac33a9e833234a11895402bc828da3c74ea2979eb833cd644b8ab9e3b1e46515f47a49ee602c608812241e56b94bcf76cfbb13532d9f4ff8ba
N1 = 0xa5d1c341e4837bf7f2317024f4436fb25a450ddabd7293a0897ebecc24e443efc47672a6ece7f9cac05661182f3abbb0272444ce650a819b477fd72bf01210d7e1fbb7eb526ce77372f1aa6c9ce570066deee1ea95ddd22533cbc68b3ba20ec737b002dfc6f33dcb19e6f9b312caa59c81bb80cda1facf16536cb3c184abd1d5
C2 = 0x5ad248df283350558ba4dc22e5ec8325364b3e0b530b143f59e40c9c2e505217c3b60a0fae366845383adb3efe37da1b9ae37851811c4006599d3c1c852edd4d66e4984d114f4ea89d8b2aef45cc531cfa1ab16c7a2e04d8884a071fed79a8d30af66edf1bbbf695ff8670b9fccf83860a06e017d67b1788b19b72d597d7d8d8
N2 = 0xaf4ed50f72b0b1eec2cde78275bcb8ff59deeeb5103ccbe5aaef18b4ddc5d353fc6dc990d8b94b3d0c1750030e48a61edd4e31122a670e5e942ae224ecd7b5af7c13b6b3ff8bcc41591cbf2d8223d32eeb46ba0d7e6d9ab52a728be56cd284842337db037e1a1da246ed1da0fd9bdb423bbe302e813f3c9b3f9414b25e28bda5
C3 = 0x8a9315ee3438a879f8af97f45df528de7a43cd9cf4b9516f5a9104e5f1c7c2cdbf754b1fa0702b3af7cecfd69a425f0676c8c1f750f32b736c6498cac207aa9d844c50e654ceaced2e0175e9cfcc2b9f975e3183437db73111a4a139d48cc6ce4c6fac4bf93b98787ed8a476a9eb4db4fd190c3d8bf4d5c4f66102c6dd36b73
N3 = 0x5ca9a30effc85f47f5889d74fd35e16705c5d1a767004fec7fdf429a205f01fd7ad876c0128ddc52caebaa0842a89996379ac286bc96ebbb71a0f8c3db212a18839f7877ebd76c3c7d8e86bf6ddb17c9c93a28defb8c58983e11304d483fd7caa19b4b261fc40a19380abae30f8d274481a432c8de488d0ea7b680ad6cf7776b

n_all = [N1, N2, N3]
ciphertext_all = [C1, C2, C3]

c_e = crt(ciphertext_all, n_all)
c = gmpy2.iroot(c_e, e)
print c

c = long(c[0])
print hex(c)[2:].strip('L').decode('hex')

