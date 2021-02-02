# 2020_FosCo
# 산림대융합프로젝트
# 과제명: 산림조사 효율성 제고를 위한 3d레이저 스캐너의 pcd 처리 시스템 개발

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


# cpp환경에서 pcl설치시 빌드

@빌드 방법(C++ 환경에서 빌드 방법)

1. 확인

 cd ~
mkdir pcl-test && cd pcl-test
 
-------------------------------------------------------------------------
2. CMakeLists.txt 파일을 작성

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
3. main.cpp 파일을 작성

 #include <iostream>

int main() {
    std::cout << "hello, world!" << std::endl;
    return (0);
}
 

--------------------------------------------------------------------------

4. 빌드

 mkdir build && cd build
cmake ..
make

-------------------------------------------------------------------------- 

5. 테스트:

 ./pcl-test
 

출력-> hello, world!

이 설치 방법은 가능한 한 호환 가능하며 Point Cloud Library를 쉽게 시작하고 실행할 수있는 방법을 제공. 이 방법에는 pcl을 설정하기 전에 추가 패키지를 사전 설치해야하는 Kinect 구성이 포함되어 있지 않음.


--------------------------------------------------------------------------

# python, colab에서 pcl 설치

-> colab, 파이썬 환경에서 pcl 구축(Fosco 소스코드.ipynb)


1. colab

colab 환경에 pcl설치와 기타 설치시 문제가 되는 모든 환경을 해결하기 위해서 각 셀마다 해결법을 제시 해놓음
순서대로 각 셀을 실행시키면 언제 어디서든 설치 및 사용 가능.
<img width="1013" alt="스크린샷 2021-02-03 오전 1 52 54" src="https://user-images.githubusercontent.com/44065090/106635159-dadee180-65c3-11eb-9148-c2fe25c0fe6f.png">

<img width="1015" alt="스크린샷 2021-02-03 오전 1 53 27" src="https://user-images.githubusercontent.com/44065090/106635334-0eba0700-65c4-11eb-996e-578046879730.png">


2. pts ? pcd ?
pts를 pcd로 바꾸는 알고리즘과 pts를 읽어 주는 알고리즘 구현

filename=".pts"
from numpy import loadtxt
from numpy import savetxt
lines = loadtxt("/content/sample_data/지면제거data.pts",skiprows=1)
size=str(lines[:,0].size)
(중략)


3. k means, DBScan, 유클라디안 군집화와 inertia

나무의 일정 구간의 데이터를 넣으면 자동으로 k means 군집화 기법을 사용하여 라벨링을 해줌, 이때 inertia 함수를 이용하여 k 값을
추정하게 되는데 이는 팔꿈치 기법이라 하여 일정 범위의 k값을 넣어서 기울기가 완만한 점을 찾아내어 k 값으로 지정하는 방식.
또한 이 결과를 2d와 3d로 표현 

* 실제 나무
<img width="409" alt="스크린샷 2021-02-03 오전 2 08 36" src="https://user-images.githubusercontent.com/44065090/106636181-03b3a680-65c5-11eb-8ea9-c74755edd472.png">


< point cloud로 변환>


* 좌표와 그래프로 표현 가능

<img width="934" alt="스크린샷 2021-02-03 오전 1 58 52" src="https://user-images.githubusercontent.com/44065090/106635436-2a251200-65c4-11eb-833f-77a7a925dfd4.png">

![K_means_2d](https://user-images.githubusercontent.com/44065090/106635935-c0593800-65c4-11eb-8e6c-27d89aada29b.png)

![20200820103948](https://user-images.githubusercontent.com/44065090/106635830-a0c20f80-65c4-11eb-8dd8-c18a5eb2b7aa.png)


<img width="323" alt="스크린샷 2021-02-03 오전 1 59 25" src="https://user-images.githubusercontent.com/44065090/106635476-38732e00-65c4-11eb-9da6-a26bfe149be1.png">


<img width="442" alt="스크린샷 2021-02-03 오전 1 59 33" src="https://user-images.githubusercontent.com/44065090/106635517-46c14a00-65c4-11eb-9c27-3ee86e74100c.png">


4. Octree, Kdtree를 사용한 수고 측정

일정구간의 나무 데이터를 군집화 시킨후 밑둥 데이터 중에 가장 높은 점을 뽑아서 그 포인트를 전체 나무 데이터에서 찾아서 그 부분 부터 kd tree 기법을 사용해 일정 범위 내의 가장 높은 포인트를 찾아가는 방식으로 구현. 이 방식은 정확도 면에서 떨어지지만 
속도적인 측면에서 이점을 지니고 있음. 정확도를 향상 시키려면 Brute Forcing  방식으로 구현이 현재로선 가장 정확함.
(이외에도 Octree 알고리즘 구현.)

<img width="700" alt="스크린샷 2021-02-03 오전 1 59 57" src="https://user-images.githubusercontent.com/44065090/106635570-593b8380-65c4-11eb-98b5-e68221e07c8d.png">

* 군집화 기법, 탐색 기법에 대한 더 자세한 사항은 문서폴더의 연구 계획서, 보고서 참조 
