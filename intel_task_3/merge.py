def merge(*iterables):
    val = []
    while True:
        length = len(val)
        for i in iterables:
            try:
                val.append(next(i))
            except StopIteration:
                pass
        if len(val) > length:
            val = sorted(val)
        if not val:
            return
        yield val.pop(0)
