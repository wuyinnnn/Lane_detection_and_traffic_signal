# Lane_detection_and_traffic_signal
nudt研一下学期进行的控制工程实验课中的无人车实验，包括预测未来行驶轨迹、车道线检测和禁止停车标志识别
该程序是在jupyter notebook中进行调试的，如果想在ros下运行，只需发布订阅话题即可
比如说预测未来行驶轨迹，就需要订阅小车发出的底盘信息
其它地方类似，后面的车道线检测和禁止停车标志识别采用的是传统的方法，没有采用机器学习，因此不需要进行训练
仅供参考