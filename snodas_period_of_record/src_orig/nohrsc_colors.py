# -*- coding: utf-8 -*-
"""
Created on Fri Apr 28 10:35:03 2017

@author: Shawn M Carter, UCAR, 2017
"""

def get_colors(data_type, units):
    """Repository of graphing styles for raster colors and 
    their associated data breaks
    Acceptable values for data_type:
        (swe, percent_swe, swe_delta)
    Acceptable values for units:
        (meters, cm, mm, percent, delta_mm
    """
    # Assign color map for data type (values are RGB (0-255)/255)
    if data_type == 'swe':
        colors = [(0.7058823529, 0.7058823529, 0.7058823529),  
                  (0.8, 0.9764705882352941, 1.0), 
                  (0.6392156862745098, 0.8392156862745098, 0.9607843137254902),
                  (0.47843137254901963, 0.615686274509804, 0.8980392156862745),
                  (0.3254901960784314, 0.34901960784313724, 0.8117647058823529), 
                  (0.3058823529411765, 0.18823529411764706, 0.7137254901960784), 
                  (0.33725490196078434, 0.0784313725490196, 0.6),
                  (0.5843137254901961, 0.1411764705882353, 0.7137254901960784),
                  (0.8117647058823529, 0.27058823529411763, 0.7803921568627451), 
                  (0.8980392156862745, 0.41568627450980394, 0.7372549019607844),
                  (0.9607843137254902, 0.5764705882352941, 0.7254901960784313), 
                  (1.0, 0.7333333333333333, 0.7607843137254902), 
                  (1.0, 0.8862745098039215, 0.8666666666666667)]

    elif data_type == 'depth':
        colors = [(0.7058823529, 0.7058823529, 0.7058823529), 
                  (0.8, 0.9764705882352941, 1.0), 
                  (0.639215686275, 0.839215686275,0.960784313725),
                  (0.478431372549,0.61568627451,0.898039215686),
                  (0.325490196078,0.349019607843,0.811764705882),
                  (0.305882352941,0.188235294118,0.713725490196),
                  (0.337254901961,0.078431372549,0.6),
                  (0.58431372549,0.141176470588,0.713725490196),
                  (0.811764705882,0.270588235294,0.780392156863),
                  (0.937254901961,0.41568627451,0.780392156863),
                  (0.960784313725,0.576470588235,0.725490196078),
                  (1.0,0.733333333333,0.760784313725), 
                  (1.0,0.886274509804,0.866666666667)]


    elif data_type == 'normals':
        colors = [(0.7058823529, 0.7058823529, 0.7058823529),  
                  (0.8, 0.9764705882352941, 1.0), 
                  (0.6392156862745098, 0.8392156862745098, 0.9607843137254902), 
                  (0.47843137254901963, 0.615686274509804, 0.8980392156862745),
                  (0.3254901960784314, 0.34901960784313724, 0.8117647058823529), 
                  (0.3058823529411765, 0.18823529411764706, 0.7137254901960784),
                  (0.33725490196078434, 0.0784313725490196, 0.6),
                  (0.5843137254901961, 0.1411764705882353, 0.7137254901960784),
                  (0.8117647058823529, 0.27058823529411763, 0.7803921568627451), 
                  (0.8980392156862745, 0.41568627450980394, 0.7372549019607844),
                  (0.9607843137254902, 0.5764705882352941, 0.7254901960784313), 
                  (1.0, 0.7333333333333333, 0.7607843137254902), 
                  (1.0, 0.8862745098039215, 0.8666666666666667)]
                  
    elif data_type == 'percent_swe':
        colors = [(0.8431372549019608, 0.7568627450980392, 0.611764705882353),
                  (0.8117647058823529, 0.0, 0.29411764705882354),
                  (0.9647058823529412, 0.44313725490196076, 0.0), 
                  (1.0, 0.6627450980392157, 0.0), 
                  (1.0, 0.8470588235294118, 0.09019607843137255), 
                  (1.0, 1.0, 0.49411764705882355), 
                  (1.0, 1.0, 0.7450980392156863), 
                  (0.9019607843137255, 0.9019607843137255, 1.0),
                  (0.7450980392156863, 1.0, 1.0), 
                  (0.49411764705882355, 1.0, 1.0), 
                  (0.09019607843137255, 0.8470588235294118, 1.0), 
                  (0.0, 0.6627450980392157, 1.0), 
                  (0.0, 0.44313725490196076, 0.9647058823529412), 
                  (0.29411764705882354, 0.0, 0.9647058823529412), 
                  (0.7294117647058823, 0.611764705882353, 0.8431372549019608)]

    elif data_type == 'swe_delta':
        colors = [(0.7058823529, 0.7058823529, 0.7058823529),
                  (0.749019607843137,0.56078431372549,0.376470588235294),      
                  (0.811764705882353,0,0.294117647058823),
                  (0.964705882352941,0.443137254901961,0),
                  (1,0.847058823529412,0.0901960784313726),
                  (0.901960784313726,0.901960784313726,0.901960784313726),
                  (0.0901960784313726,0.847058823529412,1),
                  (0,0.443137254901961,0.964705882352941),
                  (0.294117647058823,0,0.964705882352941),
                  (0.749019607843137,0.376470588235294,0.749019607843137)]

    elif data_type == 'per_diff':
        colors = [(0.7058823529,0.7058823529,0.7058823529),
                  (0.749019607843137,0.56078431372549,0.376470588235294),
                  (0.811764705882353,0,0.294117647058823),
                  (0.964705882352941,0.443137254901961,0), 
                  (1,0.847058823529412,0.0901960784313726),
                  (0.901960784313726,0.901960784313726,0.901960784313726), 
                  (0.0901960784313726,0.847058823529412,1), 
                  (0,0.443137254901961,0.964705882352941),
                  (0.294117647058823,0,0.964705882352941), 
                  (0.749019607843137,0.376470588235294,0.749019607843137)]



    # Assign data breaks for the data type
    if units == 'meters':
        breaks = [0, 0.001, 0.005, 0.01, 0.025, 0.05, 
                  0.1, 0.15, 0.25, 0.5, 0.75, 1, 2]
    elif units == 'mm':
        breaks = [0,1, 5, 10, 25, 50, 100, 150, 250, 500, 750, 1000, 2000]
    elif units == 'cm':
        breaks = [0, 0.1, 0.5, 1, 2.5, 5.0, 10.0, 15.0, 25.0, 
                  0.0, 75.0, 100.0, 200.0]
    elif units == 'percent':
        breaks = [-50000, 0, 10, 25, 50, 75, 150, 250, 500, 750, 10000]
    elif units == 'delta_mm':
        breaks = [ -99998,-49998,-1.0, -0.5, -0.25, -0.1, 0.1,
                  0.25, 0.5, 1.0, 1.0e6]
    elif units == 'delta_meters':
        breaks = [-99998, -49998, -0.0010, -0.0005, -0.00025, -0.00001, 0.00001,
        0.00025,
        0.00050, 0.0010, 1.0e6]
    elif units == 'depth_mm':
        breaks = [0, 1, 2, 5, 10, 25, 50, 100, 150, 250, 750, 1000, 2000]
    else:
        raise Exception('Units must be meters, cm, or mm.')
    
    # Assign labels
    if (units == 'meters') or (units == 'cm') or (units == 'mm'):
        labels = ['0', '1 mm', '5 mm', '1 cm', '2.5 cm', '5.0 cm', 
                  '10 cm', '25 cm', '50 cm', '75 cm', '1 m', '2 m', '> 2 m']
    elif units == 'percent':
        labels = [ 'NA', '0', '10%', '25%', '50%', '75%', '150%', '250%', 
                   '500%', '750%', '>750%']
    elif (units == 'delta_mm') or (units == 'delta_meters'):
        labels = ['NA', '< -0.5"', '0.5"', '-0.25"', '-0.1"', '-0.01"', 
                  '0.01"', '0.1"', '0.25"', '0.5"', ' >0.5"']
    elif units == 'depth_mm':
        labels = ['0', '1 mm', '5 mm', '1 cm', '2.5 cm', '5.0 cm', 
                  '10 cm', '25 cm', '50 cm', '75 cm', '1 m', '2 m', '>2 m']
    
                  
    return colors, breaks, labels
