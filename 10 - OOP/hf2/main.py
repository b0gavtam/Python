from szmito import *

alaplap:Alaplap = Alaplap("ASUS", "P8Z77-M PRO")
cpu:CPU = CPU("Intel", "Core i3-3225", 3.3, 4, 650)
ram:RAM = RAM("Corsair", "Vengeance", "DDR3", 8)
hdd:HDD = HDD("Samsung", "HD200HJ", 2, 7200)
gpu: GPU = GPU("NVIDIA", "GeForce GTX 750", 1, 1.02)

szmitogép:PC = PC(alaplap, cpu, ram, hdd, gpu)
print(szmitogép)