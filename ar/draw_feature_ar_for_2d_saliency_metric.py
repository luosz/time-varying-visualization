# Voreen Python script
import voreen
import voreenqt

voreen.info()
voreenqt.info()

list=["D:\\document\\work\\time-varying-visualization\\ar\\nucleon_naive_optimized_green_1000.tfi", "D:\\document\\work\\time-varying-visualization\\ar\\nucleon_naive_optimized_green_1000_0.tfi", "D:\\document\\work\\time-varying-visualization\\ar\\nucleon_naive_optimized_green_1000_1.tfi", "D:\\document\\work\\time-varying-visualization\\ar\\nucleon_naive_optimized_green_1000_2.tfi", "D:\\document\\work\\time-varying-visualization\\ar\\nucleon_naive_optimized_green_1000_3.tfi", "D:\\document\\work\\time-varying-visualization\\ar\\nucleon_naive_optimized_red_1000.tfi", "D:\\document\\work\\time-varying-visualization\\ar\\nucleon_naive_optimized_red_1000_0.tfi", "D:\\document\\work\\time-varying-visualization\\ar\\nucleon_naive_optimized_red_1000_1.tfi", "D:\\document\\work\\time-varying-visualization\\ar\\nucleon_naive_optimized_red_1000_2.tfi", "D:\\document\\work\\time-varying-visualization\\ar\\nucleon_naive_optimized_red_1000_3.tfi", "D:\\document\\work\\time-varying-visualization\\ar\\nucleon_naive.tfi", "D:\\document\\work\\time-varying-visualization\\ar\\nucleon_naive_0.tfi", "D:\\document\\work\\time-varying-visualization\\ar\\nucleon_naive_1.tfi", "D:\\document\\work\\time-varying-visualization\\ar\\nucleon_naive_2.tfi", "D:\\document\\work\\time-varying-visualization\\ar\\nucleon_naive_3.tfi", "D:\\document\\work\\time-varying-visualization\\ar\\nucleon_strong_red.tfi", "D:\\document\\work\\time-varying-visualization\\ar\\nucleon_strong_red_0.tfi", "D:\\document\\work\\time-varying-visualization\\ar\\nucleon_strong_red_1.tfi", "D:\\document\\work\\time-varying-visualization\\ar\\nucleon_strong_red_2.tfi", "D:\\document\\work\\time-varying-visualization\\ar\\nucleon_strong_red_3.tfi", "D:\\document\\work\\time-varying-visualization\\ar\\nucleon_weak_red.tfi", "D:\\document\\work\\time-varying-visualization\\ar\\nucleon_weak_red_0.tfi", "D:\\document\\work\\time-varying-visualization\\ar\\nucleon_weak_red_1.tfi", "D:\\document\\work\\time-varying-visualization\\ar\\nucleon_weak_red_2.tfi", "D:\\document\\work\\time-varying-visualization\\ar\\nucleon_weak_red_3.tfi"]

for i in range(len(list)):
    s=list[i]
    voreen.loadTransferFunction("SingleVolumeRaycaster", "transferFunction", s)
    print("loaded transfer function %s" % s)
    if i%5<2:
        voreen.setPropertyValue("Background", "texture", "D:/document/work/time-varying-visualization/ar/tcd2.jpg")
        voreen.setPropertyValue("Background", "backgroundModeAsString", "texture")
    else:
        voreen.setPropertyValue("Background", "backgroundModeAsString", "monochrome")

    voreen.repaint()
    image_filename=s.replace(".tfi",".png")
    voreen.snapshotCanvas(0, image_filename)
    print("saved to image %s" % image_filename)
