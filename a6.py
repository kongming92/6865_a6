#assignment 6 starter code
#by Abe Davis
#
# Student Name: Charles Liu
# MIT Email: cliu2014@mit.edu

import numpy as np
from scipy import linalg

def interpolateLin(im, y, x, repeatEdge=0):
    '''same as from previous assignment'''


def applyHomography(source, out, H, bilinear=False):
    '''takes the image source, warps it by the homography H, and adds it to the composite out. If bilinear=True use bilinear interpolation, otherwise use NN. Keep in mind that we are iterating through the output image, and the transformation from output pixels to source pixels is the inverse of the one from source pixels to the output. Does not return anything.'''



def addConstraint(systm, i, constr):
    '''Adds the constraint constr to the system of equations ststm. constr is simply listOfPairs[i] from the argument to computeHomography. This function should fill in 2 rows of systm. We want the solution to our system to give us the elements of a homography that maps constr[0] to constr[1]. Does not return anything'''

def computeHomography(listOfPairs):
    '''Computes and returns the homography that warps points listOfPairs[-][0] to listOfPairs[-][1]'''


def computeTransformedBBox(imShape, H):
    '''computes and returns [[ymin, xmin],[ymax,xmax]] for the transformed version of the rectangle described in imShape. Keep in mind that when you usually compute H you want the homography that maps output pixels into source pixels, whereas here we want to transform the corners of our source image into our output coordinate system.'''

def bboxUnion(B1, B2):
    '''No, this is not a professional union for beat boxers. Though that would be awesome. Rather, you should take two bounding boxes of the form [[ymin, xmin,],[ymax, xmax]] and compute their union. Return a new bounding box of the same form. Beat boxing optional...'''


def translate(bbox):
    '''Takes a bounding box, returns a translation matrix that translates the top left corner of that bounding box to the origin. This is a very short function.'''


def stitch(im1, im2, listOfPairs):
    '''Stitch im1 and im2 into a panorama. The resulting panorama should be in the coordinate system of im2, though possibly extended to a larger image. That is, im2 should never appear distorted in the resulting panorama, only possibly translated. Returns the stitched output (which may be larger than either input image).'''


#######6.865 Only###############

def applyHomographyFast(source, out, H, bilinear=False):
    '''takes the image source, warps it by the homography H, and adds it to the composite out. This version should only iterate over the pixels inside the bounding box of source's image in out.'''


def computeNHomographies(listOfListOfPairs, refIndex):
    '''This function takes a list of N-1 listOfPairs and an index. It returns a list of N homographies corresponding to your N images. The input N-1 listOfPairs describes all of the correspondences between images I(i) and I(i+1). The index tells you which of the images should be used as a reference. The homography returned for the reference image should be the identity.'''

def compositeNImages(listOfImages, listOfH):
    '''Computes the composite image. listOfH is of the form returned by computeNHomographies. Hint: You will need to deal with bounding boxes and translations again in this function.'''

def stitchN(listOfImages, listOfListOfPairs, refIndex):
    '''Takes a list of N images, a list of N-1 listOfPairs, and the index of a reference image. The listOfListOfPairs contains correspondences between each image Ii and image I(i+1). The function should return a completed panorama'''