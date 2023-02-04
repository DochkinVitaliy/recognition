
#include <opencv2/opencv.hpp>
#include <iostream>
using namespace cv;
using namespace std;
int main(int argc, char* argv[])
{
    VideoCapture cap(0); 
    if (cap.isOpened() == false) {
        return -1;
    }
    int frame_width = cap.get(CAP_PROP_FRAME_WIDTH);
    int frame_height = cap.get(CAP_PROP_FRAME_HEIGHT);

    VideoWriter ouputVideo("outcpp.avi", cv::VideoWriter::fourcc('M','J','P','G'), 10, Size(frame_width,frame_height));    
    namedWindow("My Video", WINDOW_NORMAL);
    while (true)
    {
        Mat frame;
        cap >> frame;
        if (frame.empty()){
            break;
        }
        ouputVideo.write(frame);
        imshow( "Frame", frame );
        if (waitKey(5) == 27){
            break;
        }
    }
    cap.release();
    ouputVideo.release();
    destroyAllWindows();
    return 0;
}




#include <stdio.h>
#include <opencv2/opencv.hpp>
using namespace cv;
int main(int argc, char** argv )
{
    if ( argc != 2 ){
        return -1;
    }
    Mat image;
    image = imread( argv[1], 1 );
    if ( !image.data ){
        return -1;
    }
    namedWindow("Display Image", WINDOW_AUTOSIZE );
    imshow("Display Image", image);
    waitKey(0);
    return 0;
}
