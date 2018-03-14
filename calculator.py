#! -*- coding: utf-8 -*-
def main():
  import sys
  print(sys.argv)
  if len(sys.argv) != 2:
    print("Parameter Error")
    exit()
  try:
    e=int(sys.argv[1])-3500
  except ValueError:
    print("Parameter Error")
    exit()
  if e<=0:
    tax=0.00
  elif 0<e<=1500:
    tax=0.03*e
  elif 1500<e<=4500:
    tax=0.10*e-105
  elif 4500<e<=9000:
    tax=0.20*e-555
  elif 9000<e<=35000:
    tax=0.25*e-1005;
  elif 35000<e<=55000:
    tax=0.30*e-2775
  elif 55000<e<=80000:
    tax=0.35*e-5505
  else:
    tax=0.45*e-13505
  print('{:.2f}'.format(tax))

if __name__ == '__main__':
  main()

