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


The get_harris_points function takes a grayscale image and then performs HarrisEdgeDetection on it.
It also normalizes the pixel values. If the pixel values in the image exceed 1, they are normalized to the range 0-1 by dividing by 255.


The get_image_features function takes a word map and the size of the visual dictionary 
A visual image dictionary of each image is then computed using the words and a histogram is then computed
The histogram then stores the word count of each image 

The get_random_points takes the height and width of each image. The random function then generates any two random values and thus a random point is generated.
Using these random points the image is attempted to be reconstructed.

The getVisualWords function, for each pixel in the image, computes the Euclidean distance between the pixel's feature vector and each visual word in the dictionary.
It then finds the visual word in the dictionary that has the minimum distance to the pixel's feature vector.
It also assigns the index of the closest visual word to the corresponding pixel in the word map.
