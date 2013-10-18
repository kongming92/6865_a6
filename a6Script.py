#script for running/testing assignment 6
#Starter code by Abe Davis
#
#
# Student Name:
# MIT Email:

import a6
import numpy as np
import glob
import imageIO as io

def getPNGsInDir(path):
    fnames = glob.glob(path+"*.png")
    pngs = list()
    for f in fnames:
        #print f
        imi = io.getImage(f)
        pngs.append(imi)
    return pngs

def getRawPNGsInDir(path):
    fnames = glob.glob(path+"*.png")
    pngs = list()
    pngnames = list()
    print path
    for f in fnames:
        print f
        imi = io.imreadGrey(f)
        pngs.append(imi)
        pngnames.append(f)
    return pngs, pngnames

def testApplyHomographyPoster():
    signH = np.array([[1.12265192e+00, 1.44940136e-01, 1.70000000e+02], [8.65164180e-03, 1.19897030e+00, 9.50000000e+01],[  2.55704864e-04, 8.06420365e-04, 1.00000000e+00]])
    green = io.getImage("green.png")
    poster = io.getImage("poster.png")
    a6.applyHomography(poster, green, signH, True)
    io.imwrite(green, "HWDueAt9pm_applyHomography.png")


def testComputeAndApplyHomographyPoster():
    green = io.getImage("green.png")
    poster = io.getImage("poster.png")

    h, w = poster.shape[0]-1, poster.shape[1]-1
    pointListPoster=[np.array([0, 0, 1]), np.array([0, w, 1]), np.array([h, w, 1]), np.array([h, 0, 1])]
    pointListT=[np.array([170, 95, 1]), np.array([171, 238, 1]), np.array([233, 235, 1]), np.array([239, 94, 1])]

    listOfPairs=zip(pointListPoster, pointListT)

    H = a6.computeHomography(listOfPairs)
    #print H
    a6.applyHomography(poster, green, H, True)
    io.imwrite(green, "HWDueAt9pm_computeHomography.png")

########

def testComputeAndApplyHomographyStata():
    im1=io.imread('stata/stata-1.png')
    im2=io.imread('stata/stata-2.png')
    pointList1=[np.array([209, 218, 1]), np.array([425, 300, 1]), np.array([209, 337, 1]), np.array([396, 336, 1])]
    pointList2=[np.array([232, 4, 1]), np.array([465, 62, 1]), np.array([247, 125, 1]), np.array([433, 102, 1])]
    listOfPairsS=zip(pointList1, pointList2)
    HS=a6.computeHomography(listOfPairsS)
    #multiply by 0.2 to better show the transition
    out=im2*0.5

    a6.applyHomography(im1, out, HS, True)
    io.imwrite(out, "stata_computeAndApplyHomography.png")

def testStitchStata():
    im1=io.imread('stata/stata-1.png')
    im2=io.imread('stata/stata-2.png')
    pointList1=[np.array([209, 218, 1]), np.array([425, 300, 1]), np.array([209, 337, 1]), np.array([396, 336, 1])]
    pointList2=[np.array([232, 4, 1]), np.array([465, 62, 1]), np.array([247, 125, 1]), np.array([433, 102, 1])]
    listOfPairs=zip(pointList1, pointList2)
    out = a6.stitch(im1, im2, listOfPairs)
    io.imwrite(out, "stata_stitch.png")

def testStitchScience():
    im1=io.imread('science/science-1.png')
    im2=io.imread('science/science-2.png')
    pointList1=[np.array([307, 15, 1], dtype=np.float64), np.array([309, 106, 1], dtype=np.float64), np.array([191, 102, 1], dtype=np.float64), np.array([189, 47, 1], dtype=np.float64)]
    pointList2=[np.array([299, 214, 1], dtype=np.float64), np.array([299, 304, 1], dtype=np.float64), np.array([182, 292, 1], dtype=np.float64), np.array([183, 236, 1], dtype=np.float64)]
    listOfPairs=zip(pointList1, pointList2)
    out = a6.stitch(im1, im2, listOfPairs)
    io.imwrite(out, "science_stitch.png")

def testComputeNHomographies():
    pointList1=[np.array([209, 218, 1]), np.array([425, 300, 1]), np.array([209, 337, 1]), np.array([396, 336, 1])]
    pointList2=[np.array([232, 4, 1]), np.array([465, 62, 1]), np.array([247, 125, 1]), np.array([433, 102, 1])]
    listOfPairs=zip(pointList1, pointList2)
    h1 = a6.computeHomography(listOfPairs)
    h2 = a6.computeNHomographies([listOfPairs], 1)
    print h1, h2

def testNPanoVancouver():
    im0 = io.imread('vancouverPan/vancouver0.png')
    im1 = io.imread('vancouverPan/vancouver1.png')
    im2 = io.imread('vancouverPan/vancouver2.png')
    im3 = io.imread('vancouverPan/vancouver3.png')
    im4 = io.imread('vancouverPan/vancouver4.png')
    pointList1=[np.array([188, 52, 1], dtype=np.float64), np.array([116, 152, 1], dtype=np.float64), np.array([285, 136, 1], dtype=np.float64), np.array([254, 47, 1], dtype=np.float64)]
    pointList2=[np.array([177, 204, 1], dtype=np.float64), np.array([92, 306, 1], dtype=np.float64), np.array([273, 288, 1], dtype=np.float64), np.array([241, 200, 1], dtype=np.float64)]
    listOfPairs0=zip(pointList1, pointList2)
    pointList3=[np.array([316, 21, 1], dtype=np.float64), np.array([288, 173, 1], dtype=np.float64), np.array([178, 203, 1], dtype=np.float64), np.array([156, 82, 1], dtype=np.float64)]
    pointList4=[np.array([313, 147, 1], dtype=np.float64), np.array([291, 293, 1], dtype=np.float64), np.array([172, 324, 1], dtype=np.float64), np.array([161, 198, 1], dtype=np.float64)]
    listOfPairs1=zip(pointList3, pointList4)
    pointList5=[np.array([300, 27, 1], dtype=np.float64), np.array([175, 145, 1], dtype=np.float64), np.array([160, 198, 1], dtype=np.float64), np.array([311, 171, 1], dtype=np.float64)]
    pointList6=[np.array([283, 134, 1], dtype=np.float64), np.array([165, 254, 1], dtype=np.float64), np.array([149, 311, 1], dtype=np.float64), np.array([306, 273, 1], dtype=np.float64)]
    listOfPairs2=zip(pointList5, pointList6)
    pointList7=[np.array([177, 9, 1], dtype=np.float64), np.array([168, 156, 1], dtype=np.float64), np.array([271, 10, 1], dtype=np.float64), np.array([306, 145, 1], dtype=np.float64)]
    pointList8=[np.array([188, 166, 1], dtype=np.float64), np.array([163, 309, 1], dtype=np.float64), np.array([273, 170, 1], dtype=np.float64), np.array([311, 300, 1], dtype=np.float64)]
    listOfPairs3=zip(pointList7, pointList8)
    listOfListOfPairs = [listOfPairs0, listOfPairs1, listOfPairs2, listOfPairs3]
    listOfImages = [im0, im1, im2, im3, im4]
    refIndex = 2
    out = a6.stitchN(listOfImages, listOfListOfPairs, refIndex)
    io.imwrite(out, "vancouver_stitchNFast.png")

def testNPanoGuedelon():
    im1 = io.imread('guedelon/guedelon-1.png')
    im2 = io.imread('guedelon/guedelon-2.png')
    im3 = io.imread('guedelon/guedelon-3.png')
    im4 = io.imread('guedelon/guedelon-4.png')
    pointList1=[np.array([444, 306, 1], dtype=np.float64), np.array([198, 210, 1], dtype=np.float64), np.array([271, 198, 1], dtype=np.float64), np.array([399, 203, 1], dtype=np.float64)]
    pointList2=[np.array([434, 114, 1], dtype=np.float64), np.array([188, 44, 1], dtype=np.float64), np.array([261, 24, 1], dtype=np.float64), np.array([394, 18, 1], dtype=np.float64)]
    listOfPairs1=zip(pointList1, pointList2)
    pointList3=[np.array([419, 293, 1], dtype=np.float64), np.array([384, 234, 1], dtype=np.float64), np.array([254, 274, 1], dtype=np.float64), np.array([301, 324, 1], dtype=np.float64)]
    pointList4=[np.array([401, 142, 1], dtype=np.float64), np.array([372, 88, 1], dtype=np.float64), np.array([245, 139, 1], dtype=np.float64), np.array([292, 179, 1], dtype=np.float64)]
    listOfPairs2=zip(pointList3, pointList4)
    pointList5=[np.array([245, 139, 1], dtype=np.float64), np.array([403, 143, 1], dtype=np.float64), np.array([379, 220, 1], dtype=np.float64), np.array([273, 311, 1], dtype=np.float64)]
    pointList6=[np.array([236, 70, 1], dtype=np.float64), np.array([398, 69, 1], dtype=np.float64), np.array([371, 149, 1], dtype=np.float64), np.array([267, 238, 1], dtype=np.float64)]
    listOfPairs3=zip(pointList5, pointList6)
    listOfImages = [im1, im2, im3, im4]
    listOfListOfPairs = [listOfPairs1, listOfPairs2, listOfPairs3]
    refIndex = 2
    out = a6.stitchN(listOfImages, listOfListOfPairs, refIndex)
    io.imwrite(out, "guedelon_stitchNFast.png")

def makeStreetSign():
    sign = io.imread('highway.png')
    people = io.imread('coverphoto.png')
    h, w = people.shape[0]-1, people.shape[1]-1
    peoplecorners=[np.array([0, 0, 1]), np.array([0, w, 1]), np.array([h, w, 1]), np.array([h, 0, 1])]
    pointList1=[np.array([105, 94, 1], dtype=np.float64), np.array([110, 200, 1], dtype=np.float64), np.array([162, 200, 1], dtype=np.float64), np.array([159, 92, 1], dtype=np.float64)]
    listOfPairs = zip(peoplecorners, pointList1)
    H = a6.computeHomography(listOfPairs)
    a6.applyHomography(people, sign, H, True)
    io.imwrite(sign, "Fun.png")

def makeBostonPano():
    boston1 = io.imread('boston1/boston1-2.png')
    boston2 = io.imread('boston1/boston1-3.png')
    pointList1=[np.array([207, 215, 1], dtype=np.float64), np.array([243, 324, 1], dtype=np.float64), np.array([252, 195, 1], dtype=np.float64), np.array([274, 247, 1], dtype=np.float64)]
    pointList2=[np.array([208, 55, 1], dtype=np.float64), np.array([249, 162, 1], dtype=np.float64), np.array([256, 33, 1], dtype=np.float64), np.array([277, 90, 1], dtype=np.float64)]
    listOfPairs=zip(pointList1, pointList2)
    out = a6.stitch(boston1, boston2, listOfPairs)
    io.imwrite(out, "MyPano.png")

def makeConventionManyPano():
    conv1 = io.imread('convention/convention-1.png')
    conv2 = io.imread('convention/convention-2.png')
    conv3 = io.imread('convention/convention-3.png')
    pointList1=[np.array([298, 206, 1], dtype=np.float64), np.array([267, 320, 1], dtype=np.float64), np.array([170, 325, 1], dtype=np.float64), np.array([172, 188, 1], dtype=np.float64)]
    pointList2=[np.array([309, 70, 1], dtype=np.float64), np.array([270, 175, 1], dtype=np.float64), np.array([182, 176, 1], dtype=np.float64), np.array([179, 42, 1], dtype=np.float64)]
    listOfPairs1=zip(pointList1, pointList2)
    pointList3=[np.array([288, 173, 1], dtype=np.float64), np.array([267, 306, 1], dtype=np.float64), np.array([219, 306, 1], dtype=np.float64), np.array([217, 210, 1], dtype=np.float64)]
    pointList4=[np.array([298, 15, 1], dtype=np.float64), np.array([269, 151, 1], dtype=np.float64), np.array([225, 148, 1], dtype=np.float64), np.array([221, 55, 1], dtype=np.float64)]
    listOfPairs2=zip(pointList3, pointList4)
    listOfImages = [conv1, conv2, conv3]
    listOfListOfPairs = [listOfPairs1, listOfPairs2]
    refIndex = 1
    out = a6.stitchN(listOfImages, listOfListOfPairs, refIndex)
    io.imwrite(out, "MyPanoMany.png")


# testComputeAndApplyHomographyPoster()
# testComputeAndApplyHomographyStata()
# testStitchStata()
# testStitchScience()
# # testComputeNHomographies()
# testNPanoVancouver()
# testNPanoGuedelon()
# makeStreetSign()
# makeBostonPano()
makeConventionManyPano()
#***You can test on the first N images of a list by feeding im[:N] as the argument instead of im***

