#include <stdlib.h>
#include <stdint.h>
#include <string.h>
#include <stdio.h>

#include "sha3/sph_blake.h"
#include "sha3/sph_bmw.h"
#include "sha3/sph_groestl.h"
#include "sha3/sph_jh.h"
#include "sha3/sph_keccak.h"
#include "sha3/sph_skein.h"


void quark_hash(const char* input, char* output)
{
    sph_blake512_context     ctx_blake;
    sph_bmw512_context       ctx_bmw;
    sph_groestl512_context   ctx_groestl;
    sph_skein512_context     ctx_skein;
    sph_jh512_context        ctx_jh;
    sph_keccak512_context    ctx_keccak;

    //these uint512 in the c++ source of the client are backed by an array of uint32
    uint32_t hash0[16], hash1[16], hash2[16], hash3[16], hash4[16], hash5[16], hash6[16], hash7[16], hash8[16];

    uint32_t mask[16];
    uint32_t zero[16];
    mask[0] = 8;
    zero[0] = 0;
    for(int i=1; i<16; i++) {
    		mask[i] = 0;
    		zero[i] = 0;
    }

    sph_blake512_init(&ctx_blake);
    sph_blake512 (&ctx_blake, input, 80);
    sph_blake512_close (&ctx_blake, &hash0);

    sph_bmw512_init(&ctx_bmw);
    sph_bmw512 (&ctx_bmw, &hash0, 64);
    sph_bmw512_close(&ctx_bmw, &hash1);

    if (((*hash1) & (*mask)) != (*zero)) {
    		sph_groestl512_init(&ctx_groestl);
    		sph_groestl512 (&ctx_groestl, &hash1, 64);
    		sph_groestl512_close(&ctx_groestl, &hash2);
    } else {
    		sph_skein512_init(&ctx_skein);
    	    sph_skein512 (&ctx_skein, &hash1, 64);
    	    sph_skein512_close (&ctx_skein, &hash2);
    }

    sph_groestl512_init(&ctx_groestl);
    sph_groestl512 (&ctx_groestl, &hash2, 64);
    sph_groestl512_close(&ctx_groestl, &hash3);

    sph_jh512_init(&ctx_jh);
    sph_jh512 (&ctx_jh, &hash3, 64);
    sph_jh512_close(&ctx_jh, &hash4);

    if (((*hash4) & (*mask)) != (*zero)) {
    		sph_blake512_init(&ctx_blake);
    	    sph_blake512 (&ctx_blake, &hash4, 64);
    	    sph_blake512_close (&ctx_blake, &hash5);
    } else {
    		sph_bmw512_init(&ctx_bmw);
    	    sph_bmw512 (&ctx_bmw, &hash4, 64);
    	    sph_bmw512_close(&ctx_bmw, &hash5);
    }

    sph_keccak512_init(&ctx_keccak);
    sph_keccak512 (&ctx_keccak, &hash5, 64);
    sph_keccak512_close(&ctx_keccak, &hash6);

    sph_skein512_init(&ctx_skein);
    sph_skein512 (&ctx_skein, &hash6, 64);
    sph_skein512_close (&ctx_skein, &hash7);

    if (((*hash7) & (*mask)) != (*zero)) {
    		sph_keccak512_init(&ctx_keccak);
    	    sph_keccak512 (&ctx_keccak, &hash7, 64);
    	    sph_keccak512_close(&ctx_keccak, &hash8);
    } else {
    		sph_jh512_init(&ctx_jh);
    	    sph_jh512 (&ctx_jh, &hash7, 64);
    	    sph_jh512_close(&ctx_jh, &hash8);
    }

    memcpy(output, hash8, 32);

}
