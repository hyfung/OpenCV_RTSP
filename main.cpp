#include "opencv2/opencv.hpp"

#include <iostream>

int main(int argc, const char *argv[])
{
    cv::Mat frame;

    cv::VideoCapture cap;
    cap.open(0);

    if(!cap.isOpened())
    {
        std::cout << "Failed opening capture device" << std::endl;
        return -1;
    }

    while(1)
    {

        cap.read(frame);

        cv::imshow("Frame", frame);

        if(cv::waitKey(33) >=  0)
        {
            break;
        }

    }

    return 0;
}
