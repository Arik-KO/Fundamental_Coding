from pathlib import Path


for p in Path().iterdir():
    
    print(p)     # shows ls
    # print(p.absolute().parent.parent)
    # print(p.absolute())
    # print(p.absolute().parent)
    # print(p.absolute().parent.parent.parent)

if __name__ == "__main__":
    print(Path().resolve())
    # get the absolute path for this script
    print(Path(__file__).resolve())
    # get parent's absolute path of this script
    print(Path(__file__).resolve().parent)