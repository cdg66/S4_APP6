// IIRCoeffs : coefficients (b0, b1, b2, a0, a1, a2) for N_SOS_SECTIONS cascaded SOS sections
#define IIR_QXY_RES_NBITS 13 // Q2.13
#define N_SOS_SECTIONS 4
int32_t IIRCoeffs[N_SOS_SECTIONS][6] = {
	{7003, -13316, 7003, 8192, -15162, 7874},
	{8192, -15592, 8192, 8192, -15426, 7915},
	{8192, -15564, 8192, 8192, -15466, 8155},
	{8192, -15604, 8192, 8192, -15628, 8159},
};

int32_t IIRu[N_SOS_SECTIONS] = {0}, IIRv[N_SOS_SECTIONS] = {0};

