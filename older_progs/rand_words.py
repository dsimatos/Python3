#! /usr/bin/env python
# -*- coding: utf8 -*-

import random

letts = ['α','β','γ','δ','ε','ζ','η','θ','ι','κ','λ','μ','ν','ξ','ο','π','ρ','σ','τ','υ','φ','χ','ψ','ω']
spc = ' '


while True:
	for i in range(2, random.randrange(13)):
		print letts[random.randrange(24)],
	print spc,
