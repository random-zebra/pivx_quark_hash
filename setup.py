from distutils.core import setup, Extension

quark_hash_module = Extension('pivx_quark_hash',
                                 sources = ['quarkmodule.c',
                                            'quarkhash.c',
                                            'sha3/blake.c',
                                            'sha3/bmw.c',
                                            'sha3/groestl.c',
                                            'sha3/jh.c',
                                            'sha3/keccak.c',
                                            'sha3/skein.c'],
                               include_dirs=['.', './sha3'])

setup (name = 'pivx_quark_hash',
       version = '1.2',
       package_data = {
        '': ['*.h']
        },
       author = 'gpdionisio',
       author_email = 'gianpiero.dionisio@protonmail.ch',
       description = 'Binding for PIVX quark proof of work hashing.',
       ext_modules = [quark_hash_module],
       url = 'https://github.com/gpdionisio/pivx_quark_hash',
       download_url = 'https://github.com/gpdionisio/pivx_quark_hash/archive/v1.2.tar.gz'
       )
