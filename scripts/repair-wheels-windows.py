import argparse
import pathlib
import shutil
import subprocess

import pupil_pthreads_win


def repair(wheel, dest_dir):
    pthreads_path = pathlib.Path(pupil_pthreads_win.dll_path)
    msvcr100_path = pathlib.Path(r"C:\WINDOWS\system32\MSVCR100.dll")

    cmd = (
        "delvewheel.exe repair -v -w {dest_dir} {wheel} "
        "--add-path {pthreads_path.parent};{msvcr100_path.parent} "
        "--add-dll {pthreads_path.name};{msvcr100_path.name}"
    )
    cmd = cmd.format(
        wheel=wheel,
        dest_dir=dest_dir,
        pthreads_path=pthreads_path,
        msvcr100_path=msvcr100_path,
    )
    print("+ " + cmd)
    out = subprocess.check_output(cmd, shell=True).decode()
    print("+ delvewheel.exe output:\n" + out)
    last_line = out.splitlines()[-1]

    # cibuildwheels expects the wheel to be in dest_dir but delvewheel does not copy the
    # wheel to dest_dir if there is nothing to repair
    if last_line.startswith("no external dependencies are needed"):
        print(f"+ Manually copying {wheel} to {dest_dir}")
        pathlib.Path(dest_dir).mkdir(exist_ok=True)
        shutil.copy2(wheel, dest_dir)
        # raise Exception("Should not happen")
    else:
        print(f"+ No need for a manual copy")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("wheel")
    parser.add_argument("dest_dir")
    args = parser.parse_args()
    repair(args.wheel, args.dest_dir)
