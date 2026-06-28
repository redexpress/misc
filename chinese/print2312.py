def write_header(f):
    header = "区," + ",".join(str(i) for i in range(1, 95)) + "\r\n"
    f.write(header.encode("gb2312"))


# Generate gb2312_gbk.csv using GB2312 zone-position codes.
def write_gbk():
    with open("gb2312_gbk.csv", "wb") as f:
        write_header(f)

        for qu in range(1, 95):
            if qu != 1 and (qu - 1) % 10 == 0:
                f.write(b"\r\n")
                write_header(f)

            f.write(str(qu).encode("gb2312"))

            for wei in range(1, 95):
                f.write(b",")

                # Zones 10-15 and 88-94 are undefined. In Zone 55, positions 90-94 are undefined.
                if (
                    10 <= qu <= 15
                    or 88 <= qu <= 94
                    or (qu == 55 and 90 <= wei <= 94)
                ):
                    f.write(b"  ")
                else:
                    f.write(bytes((qu + 0xA0, wei + 0xA0)))

            f.write(b"\r\n")


# Convert GBK CSV to UTF-8 text.
def write_utf8():
    with open("gb2312_gbk.csv", "r", encoding="gbk", errors="replace") as src:
        text = src.read().replace(",", " ")

    with open("gb2312_utf8.txt", "w", encoding="utf-8", newline="") as dst:
        dst.write(text)


def main():
    write_gbk()
    write_utf8()


if __name__ == "__main__":
    main()