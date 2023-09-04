import rospy
import cv2
from sensor_msgs.msg import Image
from cv_bridge import CvBridge,CvBridgeError
import os
class ImageSaver:
	def __init__(self):
		rospy.init_node('image_saver',anonymous=True)
		self.bridge=CvBridge()
		self.image_sub=rospy.Subscriber('/image_view/image_rectify',Image,self.image_callback)
		self.timer=rospy.Timer(rospy.Duration(20),self.timer_callback)
		self.counter=0
		self.image_data=None
		self.save_dir=os.path.expanduser("~/image/")
	def image_callback(self,data):
		self.image_data=data
	def timer_callback(self,event):
		if self.image_data is None:
			return
		try:
			cv_image=self.bridge.imgmsg_to_cv2(self.image_data,"bgr8")
		except CvBridgeError as e:
			pring(e)
			return
		filename="chedao_image_%04d.jpg"%self.counter
		file_path=os.path.join(self.save_dir,filename)
		cv2.imwrite(filename,cv_image)
		print("Saved image to %s"%file_path)
		self.counter+=1
		self.image_data=None
if __name__=='__main__':
	saver=ImageSaver()
	try:
		rospy.spin()
	except KeyboardInterrupt:
		print("Shutting down")
	cv2.destroyAllWindows()
