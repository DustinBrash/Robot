#include </home/vincent/opencv/include/opencv/cv.h>
//be very careful with locations of files referenced by cv.h as this can cause an error
#include </home/vincent/opencv/include/opencv2/opencv.hpp>
//same warning here about location...
//other headers here for raspberry pi...
using namespace std;
using namespace cv;

int main()

//Now for the working part of the code...
{	

bool VideoCapture::open(int device(0));

	while (1)
	{
	//statements that call functions here and make determination (yes (1), maybe (0), no (-1))
	//order of calls: Contrast, RuleProb, RuleLogic, output (pin?) 
	};

	return 1;
//the return 1 is in the seemingly impossible case that something falls through and the loop doesnt execute
};  





