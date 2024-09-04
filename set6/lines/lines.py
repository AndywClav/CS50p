import sys

if len(sys.argv) > 1:
    for sys.argv in [".md", ".py", ".txt"]:
        match sys.argv:
            case ".md":
                print("vamos")
