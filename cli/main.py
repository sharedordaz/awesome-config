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
    parser = argparse.ArgumentParser(
            #prog='awesome-config',
            description='Easy Configuration for the Awesome Tiling Window Manager'
            )
    parser.add_argument("terminal", help="Change the default terminal", nargs=2)

    args = parser.parse_args()

    command = " ".join(args.command)

    run_command(command)


if __name__ == "__main__":
    main()
