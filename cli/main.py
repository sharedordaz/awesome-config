import argparse
import subprocess

def run_command(command):
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        if result.returncode == 0:
            print("Command output:")
            print(result.stdout)
        else:
            print("Command failed with error:")
            print(result.stderr)
    except Exception as e:
        print("An error occurred:", e)

def main():
    title = "Awesome-config"
    description = "\033[1;96m{title}:\033[0;1m\nEasy Configuration for the Awesome Tiling Window Manager\033[0m".format(title=title)

    parser = argparse.ArgumentParser(
            #prog=title,
            description=description
            )

    parser.add_argument ("-show", help= "Show a parameter in the config, by default displays all default options ")
    parser.add_argument ("-set", help="Change a parameter in the config")
    parser.add_argument("terminal", help="default terminal", nargs=1)

    args = parser.parse_args()

    command = " ".join(args.command)

    run_command(command)


if __name__ == "__main__":
    main()
