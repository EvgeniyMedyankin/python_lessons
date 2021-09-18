#!/usr/bin/env python
import psutil


def main():
    # gives a single float value
    psutil.cpu_percent()
    # gives an object with many fields
    psutil.virtual_memory()
    # you can convert that object to a dictionary
    dict(psutil.virtual_memory()._asdict())
    # you can have the percentage of used RAM
    v_m_p = psutil.virtual_memory().percent
    print(v_m_p)
    # you can calculate percentage of available memory
    print(psutil.virtual_memory().available * 100 / psutil.virtual_memory().total)

    print(psutil.cpu_count())
    print(psutil.cpu_count(logical=False))


if __name__ == '__main__':
    main()
