import argparse
import subprocess



def main():
    title = "Awesome-config"
    description = "\033[1;96m{title}:\033[0;1m\nEasy Configuration for the Awesome Tiling Window Manager\033[0m".format(title=title)

    parser = argparse.ArgumentParser(
            #prog=title,
            description=description
            )


    parser.add_argument ("-set", help="Change a parameter in the config", nargs=2 )
    parser.add_argument ("-show", help= "Show a parameter in the config, by default displays all default options",nargs=1 )
    parser.add_argument ("terminal", help="Default terminal", nargs="?")
    parser.add_argument ("editor", help="Default editor", nargs='?')

    parser.parse_args()

    args = parser.parse_args()

    parametersList = ["terminal", "editor"]

    if args.show:
        if args.show[0] in parametersList:
            print(args.show[0])
        else:
            print(args.show[0],"is not valid. Please enter a valid parameter ")
    elif args.set:
        print(args.set)
        if args.terminal:
            print("TERMINAL: ",args.terminal)

        elif args.editor:
            print(args.editor)
        else:
            print("Please specify " + args.set[0] + " value")
    else:
        print("Please specify a valid command\nWrite \033[0;1mawesome-config -h\033[0m for help")

    print ("ARGUMENTS: ", args)

if __name__ == "__main__":
    main()
