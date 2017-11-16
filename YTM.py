#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# author : dsim
# date   : 20171106

'''
Calculation of yield to maturity (YTM)
source : http://www.investopedia.com/university/bonds/bonds3.asp
'''
import sys, decimal

def ytm(bp, cf, t):
	'''
	mv = Maturity Value = 100
	
	Inputs:
	bp = Bond Price (buy price) --> float around 100
	t  = number of periods --> int
	cf = Cash flow (coupon) --> float in the form i.ddd
	t & cf must match (if a bond is getting interest semianualy and coupon is given annualy then for 3 years we have 6 periods and cf must be given coupon/2)
	
	Output:
	i  = interest rate (the YTM Yield To Maturity we are searching) --> float in the form i.ddd
	
	For the type : bp = cf * {1 -[1/(1+i)^n]}/i + [mv/(1+i)^n] we are searching the i that makes ~equal (within 0.000001 range) the two parts
	'''
	
	bp = decimal.Decimal(bp)
	cf = decimal.Decimal(cf)
	t   = int(t)
	
	proseggisi = decimal.Decimal('0.001')
	if bp >= 100:                # if buy value is above 100
		i = cf - proseggisi      # then ytm is below coupon
		direction = -1           # and we decreased
	else:
		i = cf + proseggisi
		direction = 1
	
	difference = 1
	err = decimal.Decimal('0.000001')
	while difference > err:
		a = formula_ytm(i,cf,t)  # calculate the right part of the above (in docstring) equation
		
		if bp > a:               # 'a' must increase, so 'i' must decrease
			if direction == -1:  # if we were decreasing in previous round
				i -= proseggisi  # continue to decrease with the same amount
			else:                # but if we were increasing in previous round, we increased a lot, so
				proseggisi /= 10 # downgrade an order the decrement
				i -= proseggisi  # and decrease
				direction = -1   # and update that our movement is to decrease
		else:
			if direction == -1:
				proseggisi /= 10
				i += proseggisi
				direction = 1
			else:
				i += proseggisi
		
		difference = abs(bp - a)
		
	lektiko="YTM(" + "bond price = " + str(bp) + ", coupon = " + str(cf) + ", periods = " + str(t) + ") = "
	return(lektiko,format(i,'.4'))

def formula_ytm(i,cf,t):
	i /= 100
	return(cf * (1 - (1 / (1+i)**t)) / i + 100/(1+i)**t)

if __name__ == "__main__":
	print(ytm(sys.argv[1],sys.argv[2],sys.argv[3]))
