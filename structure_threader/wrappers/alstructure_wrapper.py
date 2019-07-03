#!/usr/bin/python3

# Copyright 2019 Francisco Pina Martins <f.pinamartins@gmail.com>
# This file is part of structure_threader.
# structure_threader is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# structure_threader is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with structure_threader. If not, see <http://www.gnu.org/licenses/>.

import os
import logging


try:
    import colorer.colorer as colorer
except ImportError:
    import structure_threader.colorer.colorer as colorer


def alstr_cli_generator(arg, k_val):
    """
    Generates and returns command line for running ALStructure.
    """
    output_file = os.path.join(arg.outpath, "alstr_K" + str(k_val))
    if arg.infile.endswith((".bed", ".fam", ".bim")):
        infile = arg.infile[:-4]

    cli = ["Rscript", arg.external_prog, infile, str(k_val), output_file]

    return cli, output_file