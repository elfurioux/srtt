def getsubs(filename: str, linefeed: bytes) -> list[dict]:
    subs = []
    sub = {"sub": []}
    with open(file=filename,mode="rb") as fsource:
        for line in fsource.readlines():
            line = line.removesuffix(linefeed)

            if line == b'':
                subs.append(sub)
                sub = {"sub": []}
                continue

            if not "n" in sub:
                sub["n"] = line
            elif not "timing" in sub:
                sub["timing"] = line
            else:
                sub["sub"].append(line)
    return subs

def getsub(subid: int, filename: str, linefeed: bytes):
    """WARNING: function is not optimized at all. Dont use repetatively."""
    subs = getsubs(filename,linefeed)
    for k in subs:
        if int(k["n"]) == subid:
            return k
    return -1
