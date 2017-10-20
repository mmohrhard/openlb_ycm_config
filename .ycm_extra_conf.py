import os

flags = [
        '-x',
        'c++',
        '-Wall',
        '-std=c++14',
        '-I./src',
        '-I./tests/unit',
        '-I./src/external',
        '-I./src/zlib',
        '-I./tests/unit/gtest/include'
]


def DirectoryOfThisScript():
  return os.path.dirname( os.path.abspath( __file__ ) )

def FlagsForFile( filename, **kwargs ):
    return {
      'flags': flags,
      'include_paths_relative_to_dir': DirectoryOfThisScript()
    }
