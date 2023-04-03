// IIRCoeffs : coefficients (b0, b1, b2, a0, a1, a2) for N_SOS_SECTIONS cascaded SOS sections
#define IIR_QXY_RES_NBITS 13 // Q2.13
#define N_SOS_SECTIONS 4
int32_t IIRCoeffs[N_SOS_SECTIONS][6] = {
	{7206, -13701, 7206, 8192, -15173, 7876},
	{8192, -15592, 8192, 8192, -15416, 7913},
	{8192, -15565, 8192, 8192, -15465, 8153},
	{8192, -15603, 8192, 8192, -15624, 8156},
};

int32_t IIRu[N_SOS_SECTIONS] = {0}, IIRv[N_SOS_SECTIONS] = {0};

