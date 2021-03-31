# yolo_scan_algorithm

# system config
* notebook : HP-Pavilion-Gaming-Laptop-16-a0xxx
* process : Intel® Core™ i7-10750H CPU @ 2.60GHz × 12
* gpu1 : NVIDIA Corporation TU116M [GeForce GTX 1660 Ti Mobile]
* gpu2 : Intel Corporation UHD Graphics
* cuda: 11.2
* cuDNN : v8.1.1
* NVIDIA-SMI 460.39
* Driver Version: 460.39
* opencv :4.4.0
* python :3.8.5
* cmake : 3.20.0
* os : Ubuntu 20.04.2 LTS x86_64

# need condition
* easy site : https://robocademy.com/2020/05/01/a-gentle-introduction-to-yolo-v4-for-object-detection-in-ubuntu-20-04/
여기서
CMake >= 3.8 (for modern CUDA support)(CPU and GPU)~~

  * open cv 4.4.0 설치 : https://webnautes.tistory.com/1433
  * nvidia 설치 : https://pstudio411.tistory.com/entry/Ubuntu-2004-Nvidia드라이버-설치하기
  * cuda 11.2 tool-kit 설치 :https://developer.nvidia.com/cuda-downloads?target_os=Linux&target_arch=x86_64&target_distro=Ubuntu&target_version=2004&target_type=debnetwork
  * cuDNN : https://developer.nvidia.com/rdp/cudnn-download
    library for linux
    guide : https://seonghyuk.tistory.com/58
    3)다운이 완료가 되면 압축을 풀어줍니다. 부터 코드 따라서 치면서 진행하면 가능, 텐서플로는 진행하지 않는다

OpenMP (for CPU)
Other Dependencies (For CPU and GPU)

mkdir start
cd start
git clone https://github.com/Profrog/yolo_scan_algorithm -b yolo_v4
make

* 여기서 에러가 뜬다면 usr/bin/ld: cannot find -lcudnn
*sudo cp cuda/include/cudnn.h /usr/local/cuda/include/
* sudo cp cuda/lib64/libcudnn* /usr/local/cuda/lib64/
* 경로가 없을경우 폴더를 만들어서 해당 코드가 돌아가게끔 한뒤 성공시킴

./darknet detector demo cfg/coco.data cfg/yolov4.cfg yolov4.weights test50.mp4 -i 0 -thresh 0.25
  









