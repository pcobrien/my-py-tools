def is_square(apositiveint):
  x = apositiveint // 2
  seen = set([x])
  while x * x != apositiveint:
    x = (x + (apositiveint // x)) // 2
    if x in seen: return False
    seen.add(x)
  return True

def plot_arr(*arg):
	import matplotlib.pyplot as plt
	from numpy import sqrt

	if is_square(int(len(arg))):
		nrows = int(sqrt(len(arg)))
		ncols = int(sqrt(len(arg)))
		fignum = 1
	else:
		nrows = len(arg)
		ncols = 1
		fignum = 1

	plt.figure()
	for i in range(len(arg)):
		plt.subplot(str(nrows)+str(ncols)+str(fignum))
		plt.imshow(arg[i].T)
		plt.colorbar()
		fignum += 1
	
	plt.show()

