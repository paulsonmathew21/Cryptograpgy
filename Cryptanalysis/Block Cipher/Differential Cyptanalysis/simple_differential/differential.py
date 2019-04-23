#!/usr/bin/env python
"""
Project: Differential cryptanalysis

Cipher Description:
k = (k_0,k_1)

c = s_box[m ^ k_0] ^ k_1
m = i_s_box[c ^ k_1] ^ k_0

Objective:
Perform differntial cryptanalysis of the above cipher implementation with two ct_pt pairs
"""
# S-Box 
s_box = [6, 4, 12, 5, 0, 7, 2, 14, 1, 15, 3, 13, 8, 10, 9, 11]
# Inverse S-Box
i_s_box = [4, 8, 6, 10, 1, 3, 0, 5, 12, 14, 13, 15, 2, 11, 7, 9]

def differential_analysis(m_0, m_1, c_0, c_1):
	u = m_0 ^ m_1
	print("The differential for %d and %d is: %d"%(m_0,m_1,u))
	key_samples = []
	for k_1 in range(16):
		u_0 = i_s_box[c_0 ^ k_1]
		u_1 = i_s_box[c_1 ^ k_1]
		u_temp = u_0 ^ u_1
		if u == u_temp:
			key_samples.append(k_1)
	return key_samples

# Intersection of key samples from multiple ct-pt pairs gives the actual k_1 key
key_sample_1 = differential_analysis(10, 5, 9, 6)
key_sample_2 = differential_analysis(9, 8, 7, 0)
key = [value for value in key_sample_1 if value in key_sample_2][0]
print("The value of k_1 is: %x"%key)

# Retreiving k_0 
k_0 = 10 ^ i_s_box[key ^ 9]

print("The value of k_0 is: %x"%k_0)
