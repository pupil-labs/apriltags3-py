#!/bin/bash -xe

# $1: {dest_dir}
# $2: {wheel}

pthreads_dll_folder=$(python -c 'import pupil_pthreads_win as pt; print(str(pt.dll_path.parent))')
delvewheel repair -w $1 $2 --add-path $pthreads_dll_folder
