import os


def main():
    file_path = os.path.expanduser("~/Desktop/CyberSecurity-Notes")
    os.mkdir(file_path)

    for x in range(1,25):
        os.mkdir(file_path + "\\week" + str(x))
        for y in range(1,4):
            os.mkdir(file_path + "\\week" + str(x) + "\\day" + str(y))
main()
