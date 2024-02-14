import argparse
import subprocess



def main():
    title = "Awesome-config"
    description = "\033[1;96m{title}:\033[0;1m\nEasy Configuration for the Awesome Tiling Window Manager\033[0m".format(title=title)

    parser = argparse.ArgumentParser(
            #prog=title,
            description=description
            )


    parser.add_argument ("-set", help="Change a parameter in the config", nargs="?" )
    parser.add_argument ("-show", help= "Show a parameter in the config, by default displays all default options",nargs="?" )
    parser.add_argument ("parameter", help="The parameter to change", nargs="?")
    parser.add_argument ("editor", help="Set a value", nargs='?')

    parser.parse_args()

    args = parser.parse_args()

    parametersList = ["terminal", "editor"]

    if args.show:
        if args.show in parametersList:
            print(args.show)
        else:
            print(args.show,"is not valid. Please enter a valid parameter ")
    elif args.set:
        print(args.set)
        if args.set in parametersList:
            if args.parameter:
                print("Setting: ",args.set, "=" ,args.parameter)
            else:
                print("Please specify " + args.set + " value")
        else:
            print(args.set,"is not valid. Please enter a valid parameter ")        
    else:
        print("Please specify a valid command\nWrite \033[0;1mawesome-config -h\033[0m for help")

    print ("NAMESPACE: ", args)

if __name__ == "__main__":
    main()
