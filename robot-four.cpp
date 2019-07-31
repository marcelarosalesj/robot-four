#include <opencv2/opencv.hpp>
#include <string>

using namespace std;
using namespace cv;

int main(int argc, char** argv) {
    VideoCapture cap(1);
    if(!cap.isOpened()) {
        cout << "Camera not opened" << endl;
        return -1;
    }
    
    int frame_width = cap.get(CV_CAP_PROP_FRAME_WIDTH); 
    int frame_height = cap.get(CV_CAP_PROP_FRAME_HEIGHT); 

    VideoWriter video("output.avi", CV_FOURCC('M','J','P','G'), 10, Size(frame_width,frame_height));
    
    bool stop = false;
    bool record = false;
    bool stop_record = false;
    Mat original_image;
    while(stop==false) {
        char key = waitKey(5);
        switch (key) {
            case 27: stop = true; break;	/* ESC */
            case 114: record = true; break; /* r */
            case 115: stop_record = true; break; /* s */
        }
        cap >> original_image;
        imshow("webcam", original_image);
        if(record){
            cout << "Recording" << endl;
            video.write(original_image);
        }
        if(stop_record) {
            cout << "Stop recording and exit" << endl;
            record = false;
            stop = true;
        }
    }
	cap.release();
	video.release();
    return 0;
}

