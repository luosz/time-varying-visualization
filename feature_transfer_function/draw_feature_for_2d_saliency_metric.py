# Voreen Python script
import voreen
import voreenqt

voreen.info()
voreenqt.info()

list=["D:\\document\\work\\time-varying-visualization\\~salience\\vismale_naive_optimized_green_1000.tfi", "D:\\document\\work\\time-varying-visualization\\~salience\\vismale_naive_optimized_green_1000_1.tfi", "D:\\document\\work\\time-varying-visualization\\~salience\\vismale_naive_optimized_green_1000_2.tfi", "D:\\document\\work\\time-varying-visualization\\~salience\\vismale_naive_optimized_green_1000_3.tfi", "D:\\document\\work\\time-varying-visualization\\~salience\\vismale_naive_optimized_red_1000.tfi", "D:\\document\\work\\time-varying-visualization\\~salience\\vismale_naive_optimized_red_1000_1.tfi", "D:\\document\\work\\time-varying-visualization\\~salience\\vismale_naive_optimized_red_1000_2.tfi", "D:\\document\\work\\time-varying-visualization\\~salience\\vismale_naive_optimized_red_1000_3.tfi", "D:\\document\\work\\time-varying-visualization\\~salience\\vismale_naive.tfi", "D:\\document\\work\\time-varying-visualization\\~salience\\vismale_naive_1.tfi", "D:\\document\\work\\time-varying-visualization\\~salience\\vismale_naive_2.tfi", "D:\\document\\work\\time-varying-visualization\\~salience\\vismale_naive_3.tfi", "D:\\document\\work\\time-varying-visualization\\~salience\\vismale_strong_green.tfi", "D:\\document\\work\\time-varying-visualization\\~salience\\vismale_strong_green_1.tfi", "D:\\document\\work\\time-varying-visualization\\~salience\\vismale_strong_green_2.tfi", "D:\\document\\work\\time-varying-visualization\\~salience\\vismale_strong_green_3.tfi", "D:\\document\\work\\time-varying-visualization\\~salience\\vismale_strong_red.tfi", "D:\\document\\work\\time-varying-visualization\\~salience\\vismale_strong_red_1.tfi", "D:\\document\\work\\time-varying-visualization\\~salience\\vismale_strong_red_2.tfi", "D:\\document\\work\\time-varying-visualization\\~salience\\vismale_strong_red_3.tfi", "D:\\document\\work\\time-varying-visualization\\~salience\\vismale_weak_red.tfi", "D:\\document\\work\\time-varying-visualization\\~salience\\vismale_weak_red_1.tfi", "D:\\document\\work\\time-varying-visualization\\~salience\\vismale_weak_red_2.tfi", "D:\\document\\work\\time-varying-visualization\\~salience\\vismale_weak_red_3.tfi", "D:\\document\\work\\time-varying-visualization\\~salience\\vismale_week_green.tfi", "D:\\document\\work\\time-varying-visualization\\~salience\\vismale_week_green_1.tfi", "D:\\document\\work\\time-varying-visualization\\~salience\\vismale_week_green_2.tfi", "D:\\document\\work\\time-varying-visualization\\~salience\\vismale_week_green_3.tfi"]

for s in list:
    voreen.loadTransferFunction("SingleVolumeRaycaster", "transferFunction", s)
    print("loaded transfer function %s" % s)
    voreen.repaint()
    image_filename=s.replace(".tfi",".png")
    voreen.snapshotCanvas(0, image_filename)
    print("saved to image %s" % image_filename)
