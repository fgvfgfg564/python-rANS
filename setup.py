# Copyright (c) 2021-2022, InterDigital Communications, Inc
# All rights reserved.

# Redistribution and use in source and binary forms, with or without
# modification, are permitted (subject to the limitations in the disclaimer
# below) provided that the following conditions are met:

# * Redistributions of source code must retain the above copyright notice,
#   this list of conditions and the following disclaimer.
# * Redistributions in binary form must reproduce the above copyright notice,
#   this list of conditions and the following disclaimer in the documentation
#   and/or other materials provided with the distribution.
# * Neither the name of InterDigital Communications, Inc nor the names of its
#   contributors may be used to endorse or promote products derived from this
#   software without specific prior written permission.

# NO EXPRESS OR IMPLIED LICENSES TO ANY PARTY'S PATENT RIGHTS ARE GRANTED BY
# THIS LICENSE. THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND
# CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT
# NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A
# PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR
# CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
# EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
# PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS;
# OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY,
# WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR
# OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF
# ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

import os
from pathlib import Path
from pybind11.setup_helpers import Pybind11Extension, build_ext
from setuptools import setup

cwd = Path(__file__).resolve().parent

package_name = "pyans"


def get_extensions():
    ext_dirs = cwd / "cpp_exts"
    print(ext_dirs)
    ext_modules = []

    # Add rANS module
    rans_lib_dir = cwd / "third_party/ryg_rans"
    rans_ext_dir = ext_dirs / "rans"

    extra_compile_args = ["-std=c++17"]
    if os.getenv("DEBUG_BUILD", None):
        extra_compile_args += ["-O0", "-g", "-UNDEBUG"]
    else:
        extra_compile_args += ["-O3"]
    ext_modules.append(
        Pybind11Extension(
            name=f"rans",
            sources=[str(s) for s in rans_ext_dir.glob("*.cpp")],
            language="c++",
            include_dirs=[rans_lib_dir, rans_ext_dir],
            extra_compile_args=extra_compile_args,
        )
    )

    # # Add ops
    # ops_ext_dir = ext_dirs / "ops"
    # print(ops_ext_dir)
    # ext_modules.append(
    #     Pybind11Extension(
    #         name=f"{package_name}.models._CXX",
    #         sources=[str(s) for s in ops_ext_dir.glob("*.cpp")],
    #         language="c++",
    #         extra_compile_args=extra_compile_args,
    #     )
    # )

    return ext_modules


setup(
    name=package_name,
    description="A PyTorch library and evaluation platform for end-to-end compression research",
    url="https://github.com/InterDigitalInc/CompressAI",
    author="InterDigital AI Lab",
    author_email="compressai@interdigital.com",
    zip_safe=False,
    python_requires=">=3.6",
    install_requires=[
    ],
    license="BSD 3-Clause Clear License",
    ext_modules=get_extensions(),
    cmdclass={"build_ext": build_ext},
)
