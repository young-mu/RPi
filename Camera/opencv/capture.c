#include <stdio.h>
#include <stdlib.h>
#include "opencv.hpp"

#define FILENAME "./output.jpg"

int main(int argc, const char *argv[])
{
    CvCapture *pCapture = cvCaptureFromCAM(0);
    if (pCapture == NULL) {
        fprintf(stderr, "fail to cvCreateCameraCapture\n");
        exit(1);
    }

    cvSetCaptureProperty(pCapture, CV_CAP_PROP_FRAME_WIDTH, 640);
    cvSetCaptureProperty(pCapture, CV_CAP_PROP_FRAME_HEIGHT, 480);
    cvSetCaptureProperty(pCapture, CV_CAP_PROP_BRIGHTNESS, 20);
    cvSetCaptureProperty(pCapture, CV_CAP_PROP_CONTRAST, 10);

    IplImage *pFrame = cvQueryFrame(pCapture);
    if (pFrame == NULL) {
        fprintf(stderr, "fail to cvQueryFram\n");
        exit(1);
    }

    cvSaveImage(FILENAME, pFrame);

    cvReleaseCapture(&pCapture);

    return 0;
}
