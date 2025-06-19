from core.factories import sd_factory
import uos


def mount_sd_card() -> None:
    """Mounts the SD card to the /sd path."""
    sd = sd_factory()
    vfs = uos.VfsFat(sd)
    uos.mount(vfs, "/sd")


def list_files_on_sd() -> None:
    """Lists all files and directories on the SD card."""
    print(uos.listdir("/sd"))


def read_and_print_file(file_path: str) -> None:
    """Reads and prints the contents of a file."""
    try:
        with open(file_path, "r") as file:
            print(f"Reading {file_path}")
            print(file.read())
    except OSError as e:
        print(f"Error reading {file_path}: {e}")


def main() -> None:
    """Main function to execute the script."""
    mount_sd_card()
    list_files_on_sd()
    read_and_print_file("/sd/ambient_sound.csv")
    read_and_print_file("/sd/ambient_light.csv")


if __name__ == "__main__":
    main()
