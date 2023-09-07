import matplotlib.pyplot as plt
import numpy as np

x = [1,2,3,4]
y = [1,4,9,141]

# plt.plot(x,y,"o--b")
# plt.axis([0,6,0,20])

# plt.title("Grafik Başlığı")
# plt.xlabel("x label")
# plt.ylabel("y label")
# plt.show() 
###############################################
# x = np.linspace(0,2,100)
# plt.plot(x,x,label="linear",color="Yellow")
# plt.plot(x,x**2,label="quad",color="red")
# plt.plot(x,x**3,label="cubic",color="green")
# plt.xlabel("Xlabel")
# plt.ylabel("Ylabel")
# plt.legend()
# plt.show()
###############################################
# x = np.linspace(0,2,100)
# fig,axs =  plt.subplots(3)

# axs[0].plot(x, x, color="red")
# axs[0].set_title("linear")

# axs[1].plot(x, x**2, color="green")
# axs[1].set_title("quadratic")

# axs[2].plot(x, x**3, color="yellow")
# axs[2].set_title("cubic")

# plt.tight_layout()

# plt.show() 
############################################################################
x = np.linspace(0,2,100)
fig,axs =  plt.subplots(2,2)
fig.suptitle("grafik başlığı")

axs[0,0].plot(x, x, color="red")
axs[0,1].plot(x, x**2, color="blue")
axs[1,0].plot(x, x**3, color="green")
axs[1,1].plot(x, x**4, color="yellow")
# x = np.linspace(-10,9,20)
# y = x ** 3
# z = x ** 2
# figure = plt.figure()

# axes = figure.add_axes([0,0,1,1])

# axes.plot(x,z,label="Square")
# axes.plot(x,y,label="Cube")
# axes.legend(loc=4)
plt.show() 
