#! -*- utf-8 -*- 
import sys
l = []
for arg in sys.argv[1:]:
  l.append(arg.split(':'))

def f(income):
  income = int(income)
  pension=0.08*income
  med=0.02*income
  unemployment=0.005*income
  social=0.06*income
  resid=income-pension-med-unemployment-social
 
  e=resid-3500
  if e <= 0: 
    tax=0.00
  elif 0<e<=1500: 
    tax=0.03*e
  elif 1500<e<=4500: tax=0.10*e-105
  elif 4500<e<=9000: tax=0.20*e-555
  elif 9000<e<=35000: tax=0.25*e-1005
  elif 35000<e<=55000: tax=0.30*e-2755
  elif 55000<e<=80000: tax=0.35*e-5505
  else:
    tax=0.45*e-13505

  resid2=resid-tax
  return '{:.2f}'.format(resid2)

for a, b in l:
  print('{}:{}'.format(a,f(b)))
