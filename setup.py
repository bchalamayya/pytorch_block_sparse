from setuptools import setup
from torch.utils.cpp_extension import BuildExtension, CUDAExtension

import os
rootdir = os.path.dirname(os.path.realpath(__file__))

def readme():
    with open('README.md') as f:
        return f.read()

setup(name='pytorch_block_sparse',
      version='v0.1',
      description='pytorch_block_sparse is a python package for fast block sparse matrices computation.',
      long_description=readme(),
      classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: BSD 3-Clause "New" or "Revised" License',
        'Programming Language :: Python :: 3.0',
      ],
      keywords='',
      url='',
      author='',
      author_email='',
      license='MIT',
      packages=['pytorch_block_sparse'],
      install_requires=[],
      include_package_data=True,
      zip_safe=False,
      ext_modules=[
        CUDAExtension('block_sparse_native',
                      ['pytorch_block_sparse/native/block_sparse_native.cpp',
                      'pytorch_block_sparse/native/block_sparse_cutlass_kernel_back.cu',
                      'pytorch_block_sparse/native/block_sparse_cutlass_kernel.cu'],
                      extra_compile_args=['-I', '%s/pytorch_block_sparse' % rootdir]
                      ),
      ],
      cmdclass={
        'build_ext': BuildExtension
      }
      )

