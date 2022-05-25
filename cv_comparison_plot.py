# -*- coding: utf-8 -*-
"""
Spyder Editor
"""

import numpy as np
import matplotlib.pyplot as plt
#------------------------------------------------------------------------#
# Load in Data
# Note: route of .txt files may need to be changes depending on directory
#------------------------------------------------------------------------#

data_file_1 = np.genfromtxt('/Users/elemhunt/Google Drive/Thesis Elijah /Thesis -- Drafts and Cited Referenes /DATA/Data/Laser Induced Graphene/LIG Microsupercaps/Gels/S033/_CV_0.005Vs_2C.txt')
data_file_2 = np.genfromtxt('/Users/elemhunt/Google Drive/Thesis Elijah /Thesis -- Drafts and Cited Referenes /DATA/Data/Laser Induced Graphene/LIG Microsupercaps/Gels/S033/_CV_0.01Vs_2C.txt')
data_file_3 = np.genfromtxt('/Users/elemhunt/Google Drive/Thesis Elijah /Thesis -- Drafts and Cited Referenes /DATA/Data/Laser Induced Graphene/LIG Microsupercaps/Gels/S033/_CV_0.02Vs_2C.txt')
data_file_4 = np.genfromtxt('/Users/elemhunt/Google Drive/Thesis Elijah /Thesis -- Drafts and Cited Referenes /DATA/Data/Laser Induced Graphene/LIG Microsupercaps/Gels/S033/_CV_0.05Vs_2C.txt')
# data_file_5 = np.genfromtxt('/Users/elemhunt/Google Drive/Thesis Elijah /Thesis -- Drafts and Cited Referenes /DATA/Data/Laser Induced Graphene/LIG Supercaps/Gels/S026/_CV_0.5Vs_2C.txt')

#------------------------------------------------------------------------#
# Set Columns and Data Points
#------------------------------------------------------------------------#
voltage1 = data_file_1[816:1638,2]
current1 = data_file_1[816:1638,1]
voltage2 = data_file_2[816:1638,2]
current2 = data_file_2[816:1638,1]
voltage3 = data_file_3[816:1638,2]
current3 = data_file_3[816:1638,1]
voltage4 = data_file_4[816:1638,2]
current4 = data_file_4[816:1638,1]
# voltage5 = data_file_5[816:1638,2]
# current5 = data_file_5[816:1638,1]

#------------------------------------------------------------------------#
# Plot
# Note: Legend and line color/width may need to be changed accrodingly
#------------------------------------------------------------------------#
plt.plot(voltage1,current1,'r', linewidth=2.0)
plt.plot(voltage2,current2,color='orange', linewidth=2.0)
plt.plot(voltage3,current3,'g', linewidth=2.0)
plt.plot(voltage4,current4,'b', linewidth=2.0)
# plt.plot(voltage5,current5,'m', linewidth=2.0)

plt.legend(['0.005 V/s','0.01 V/s','0.02 V/s','0.05 V/s'],loc='upper left', prop={'size': 7})
plt.title('CV Comparison of a Wired Micro-supercapacitor')
plt.xlabel('Voltage (V)')
plt.ylabel('Current (A)')

#------------------------------------------------------------------------#
# Figure Saving
# Note: Name and image size (dpi) may need to be changed
#------------------------------------------------------------------------#
plt.savefig('CV S033 Comparison', dpi = 1000)