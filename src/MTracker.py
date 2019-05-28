"""
			Author: Narinder Singh				Project: Cilia Segmentation			Date: 04 Mar 2019
			Course: CSCI 8360 @ UGA				Semester: Spring 2019				Module: MTracker.py

Description: This module contains methods and classes for tracking motion across frame segments.
"""

import os
from PIL import Image
import numpy as np

class MTrackerError(Exception): pass
class BadPathError(MTrackerError): pass
class BadReference(MTrackerError): pass
class BadParamsError(MTrackerError): pass

class Frame:
	"""
		This class is a greyscale image frame - a 2-D matrix.
	"""

	def __init__(self, imfile):
		"""
			Initilize the frame - @imfile is the path to the image.
		"""
		# Validate image file path
		if not os.path.isfile(imfile): raise BadPathError("Image file: " + imfile + " does not exist.")
		
		# Read the image as a numpy matrix
		img = Image.open(fpath)
		self.mat = np.asarray(img, np.int32)
	
		# Get some useful attributes from the numpy matrix
		self.shape = self.mat.shape

	def makeSegment(self, origin, size):
		"""
			Makes a @Segment object of size @size (rows x cols). @origin specifies where the origin of the segment is w.r.t to the frame's. The frame's origin is at its top left and rightwards and downwards are both positive movements. Returns a @Segment object.
		"""
		return Segment(frame, origin, shape)


class Segment:
	"""
		This class abstracts away a 2-D segment from a @Frame
	"""

	def __init__(self, frame, origin, size):
		"""
			Initilizes the Segment. @frame is the @Frame object the segment is cut from; @origin is the origin of the @Segment w.r.t the frame's and @size (rows x cols) is the size of the segment.
		"""
		nrows, ncols = size

		# Compute top-left and bottom-right pixel positons
		minr, minc = origin
		maxr, maxc = (minr + nrows -1, minc + ncols -1)

		# Make sure that the whole segment can exist within the bounds of the frame by accessing boundary pixels
		try:
			frame.mat[minr][minc]
			frame.mat[maxr][maxc]
		# Segment can't be created
		except IndexError:
			raise BadParamsError("Can't create segment with params Origin: " +  str(origin) + ", Size: ", str(size) + ".")
		# Everything looks good
		else:
			self.frame = frame
			self.origin = origin
			self.shape = shape
	
	def asNumpyMat(self):
		"""
			Return a numpy matrix of the segment.
		"""
		# Compute the bounds of the segment w.r.t the frame for slicing.
		nrows, ncols = self.size
		rmin, cmin = self.origin
		rmax, cmax = (rmin + nrows, cmin + ncols)
		return frame.mat[rmin:rmax, cmin:cmax]
		
	def computeResidual(self, other):
		"""
			Computes the sum-absolute difference between the two segments by positioning each pixel against the other.
		"""
		# Validate sizes
		if self.size != other.size: raise BadParamsError("Segment size must match.")
		diff = self.asNumpyMat() - other.asNumpyMat()
		return sum(np.absolute(diff).flat)

	def computeChanges(self, frame, movement=10, returnNewSegment=False):
		"""
			This method computes how much the contents of the segment have changed between the frame (that the segment is a segment of) and @frame. The @movement is the movement margin for the contents. @returnNewSegment parameter specifies if the new position of the segment should be returned with the change value. The idea is that if the things in a segment are smoothly moving in a video (a series of frames), they can be tracked and the computed change will be low. If however, the contents are changing, they can not be tracked and the computed change will be high.
			
			Return value: float or (float, @Segment)
		"""
		rorigin, corigin = self.origin
		
		# Minimum and maximum bounds for the origin
		rmin, cmin = rorigin - movement, corigin - movement
		rmax, cmax = rorigin + movement, corigin + movement

		# Variables to store the best resutls as we move our window
		minchange = float('inf')
		minseg = None

		# Try each segment looking for one with minimum change
		for r in xrange(rmin, rmax +1):
			for c in xrange(cmin, cmax +1):
				# See if the segment exists
				try:
					seg = frame.makeSegment((r, c), self.size)
				except IndexError:
					pass
				else:
					change = self.computeResidual(other)
					if change < minchange:
						minchange = change
						minseg = seg

		if returnNewSegment: return (minchange, minseg)
		else: return minchnage


def makeWindows(frame, size):
	"""
	
	"""
	wx, wy = size
	fx, fy = frame.shape



def computeChanges(hash, size):
	"""
	
	"""
	pass


if __name__ == '__main__':
	pass

