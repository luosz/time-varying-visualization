# Voreen Python script
import voreen
import voreenqt

voreen.info()
voreenqt.info()

index=range(1,24)+range(25,100)
for i in range(0, 98):
    voreen.setPropertyValue("VolumeSelector", "volumeID", i)
    # tf_filename = "../../../../_uchar/vortex/%02d.tfi" % i
    # voreen.loadTransferFunction("SingleVolumeRaycaster", "transferFunction", tf_filename)
    # print "loaded transfer function %s" % tf_filename
    tf_filename="D:/document/work/time-varying-visualization/~plot/vorts%d_optimized_parallelsearch.tfi" % index[i]
    voreen.loadTransferFunction("SingleVolumeRaycaster", "transferFunction", tf_filename)
    print("loaded transfer function %s" % tf_filename)

    voreen.repaint()
    # image_filename = "../../../../output/vortex_output/%02d.png" % i
    # voreen.snapshotCanvas(0, image_filename)
    # print "saved to image %s" % image_filename
    image_filename="D:/document/work/time-varying-visualization/~rendering2/%02d.png" % index[i]
    voreen.snapshotCanvas(0, image_filename)
    print("saved to image %s" % image_filename)

voreen.setPropertyValue("VolumeSelector", "volumeID", 0)
