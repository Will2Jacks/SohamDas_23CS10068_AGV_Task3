Note: This documentation explains only those parts to which changes have been made on the existing code that has been provided.
No changes have been made to the files(and hence the functions) createFilterBank,utils,batch to Visual Words,compute DIctionary
Changes have been made only to the files extractFilterResponses,getDictionary,getHarrisPoints,getImageFeatures,getRandomPoints,getVisualWords                                         

The extract_filter_responses function takes an input image I and a filter bank as parameters.
The input image I is converted to a floating-point representation
If the input image is grayscale , it is converted to a 3-channel image by extracting the single channel(R, G or B)

The function iterates over each channel of the input image (R, G, B) separately.
The filter responses for each channel are stored separately in lists (filterresponsesRed, filterresponsesGreen, filterresponsesBlue).


The get_dictionary function creates a visual dictionary from a set of images.

For each image in imgPaths:
The image is read using OpenCV (cv.imread()) and converted to RGB format (cv.cvtColor()).
Filter Responses are extracted from the image using the extract_filter_responses() function.
Points are then selected from the filter responses based on the specified method (get_random_points() or get_harris_points()).
The selected points are then stored into pixelResponses.
