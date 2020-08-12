# 2020_FosCo
산림대융합프로젝트
과제명: 산림조사 효율성 제고를 위한 3d레이저 스캐너의 pcd 처리 시스템 개발

@pcl 설치법
->https://readthedocs.org/projects/python-pcl-fork/downloads/pdf/rc_patches4/

@pcl docker
->https://hub.docker.com/r/youyue/pcl-docker/

@우분투 설치법 c++ 버전 pcl설치법
->
1. https://ko.a-ubuntu.com/q/c-%EC%9A%A9-ubuntu-16042-lts%EC%97%90-point-cloud-library-v18-pcl-180%EC%9D%84-%EC%84%A4%EC%B9%98%ED%95%98%EB%8A%94-%EB%B0%A9%EB%B2%95%EC%9D%80-%EB%AC%B4%EC%97%87%EC%9E%85%EB%8B%88%EA%B9%8C-%EB%8B%AB%EC%9D%80-19787
https://gist.github.com/IgniparousTempest/ce5fadbe742526d10d6bdbf15c3a3fe7
2. 오류해결법 :http://jinyongjeong.github.io/2017/01/09/pcl_install_with_qt5/

@pcl 전반적인 설명(c++, python 설치방법도 나와있음, 제일 깔끔)
->https://adioshun.gitbooks.io/pcl/content/pytncloud.html
->https://adioshun.gitbooks.io/pcl-tutorial/content/part-1/part01-chapter01/part01-chapter01-open3d-python.html

@아나콘다 파이썬 설치시 Can not import pcl, boost version error. #285 오류 해결법 
->https://github.com/strawlab/python-pcl/issues/285

@pts 파일을 pcd로 바꿔주는 코드
->https://gist.github.com/omair18/f3b85a7085b5b006c5ba919269f1db3c

@윈도우 PCL 설치법
https://neinnil.wordpress.com/2018/01/21/%EC%9C%88%EB%8F%84%EC%9A%B0%EC%A6%88%EC%97%90-pcl-%EC%84%A4%EC%B9%98%ED%95%98%EA%B8%B0/
https://codingcoding.tistory.com/408

@빌드 방법(C++)

1. 확인

 cd ~
mkdir pcl-test && cd pcl-test
 
-------------------------------------------------------------------------
2. CMakeLists.txt 파일을 작성하십시오.

 cmake_minimum_required(VERSION 2.8 FATAL_ERROR)
project(pcl-test)
find_package(PCL 1.2 REQUIRED)

include_directories(${PCL_INCLUDE_DIRS})
link_directories(${PCL_LIBRARY_DIRS})
add_definitions(${PCL_DEFINITIONS})

add_executable(pcl-test main.cpp)
target_link_libraries(pcl-test ${PCL_LIBRARIES})

SET(COMPILE_FLAGS "-std=c++11")
add_definitions(${COMPILE_FLAGS})
 
--------------------------------------------------------------------------
3. main.cpp 파일을 작성하십시오.

 #include <iostream>

int main() {
    std::cout << "hello, world!" << std::endl;
    return (0);
}
 

--------------------------------------------------------------------------

4. 엮다:

 mkdir build && cd build
cmake ..
make

-------------------------------------------------------------------------- 

5. 테스트:

 ./pcl-test
 

출력-> hello, world!

이 설치 방법은 가능한 한 호환 가능하며 Point Cloud Library를 쉽게 시작하고 실행할 수있는 방법을 제공합니다. 이 방법에는 pcl을 설정하기 전에 추가 패키지를 사전 설치해야하는 Kinect 구성이 포함되어 있지 않습니다.
