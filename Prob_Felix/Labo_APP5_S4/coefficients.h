#ifndef COEFFICIENTS_H
#define COEFFICIENTS_H

#define N_SOS_SECTIONS 4
int32_t IIRCoeffs[N_SOS_SECTIONS][6] = {
	{27, -52, 27, 32, -59, 31},
	{32, -61, 32, 32, -60, 31},
	{32, -61, 32, 32, -60, 32},
	{32, -61, 32, 32, -61, 32},
};

#endif /* COEFFICIENTS_H */
